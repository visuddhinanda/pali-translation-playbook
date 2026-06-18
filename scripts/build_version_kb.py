#!/usr/bin/env python3
"""Build a derived knowledge-base draft for one translation version.

The output is machine-assisted and evidence-linked. It is intended for human
review, not as a final linguistic authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml

from plan_chunks import estimate_tokens, group_key, plan_chunks


PALI_CHARS = "A-Za-zāīūṅñṭḍṇḷṃṁĀĪŪṄÑṬḌṆḶṂ"
PALI_WORD_RE = re.compile(rf"[{PALI_CHARS}][{PALI_CHARS}0-9.-]{{1,64}}")
PAREN_PALI_RE = re.compile(rf"([一-龥A-Za-zāīūṅñṭḍṇḷṃṁĀĪŪṄÑṬḌṆḶṂ、/·？?]{{0,16}})[（(]\s*([{PALI_CHARS}][{PALI_CHARS}0-9 .-]{{1,64}})\s*[）)]")
ABSOLUTIVE_RE = re.compile(rf"\b[{PALI_CHARS}]+(?:tvā|tvāna)\b")
STOP_PALI_TERMS = {
    "new",
    "translate",
    "the",
    "and",
    "or",
    "person",
    "new translate",
    "translate the",
}


def slug(value: str) -> str:
    normalized = value.lower().strip()
    normalized = normalized.replace("ā", "a").replace("ī", "i").replace("ū", "u")
    normalized = normalized.replace("ṅ", "n").replace("ñ", "n").replace("ṭ", "t")
    normalized = normalized.replace("ḍ", "d").replace("ṇ", "n").replace("ḷ", "l")
    normalized = normalized.replace("ṃ", "m").replace("ṁ", "m")
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    return normalized.strip("-") or "item"


def short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]


def truncate(text: str, limit: int = 260) -> str:
    text = text.replace("\r\n", "\n")
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def evidence_source_quote(text: str, support_ids: list[str] | None = None, limit: int = 260) -> str:
    text = text.replace("\r\n", "\n")
    if len(text) <= limit:
        return text
    support_ids = support_ids or []
    if any("absolutive" in support_id for support_id in support_ids):
        signal_patterns = [rf"\b[{PALI_CHARS}]+(?:tvā|tvāna)\b"]
    elif any("paccayo" in support_id or "paccaya" in support_id for support_id in support_ids):
        signal_patterns = [r"\b\w*paccay\w*\b"]
    elif any("vuccati" in support_id for support_id in support_ids):
        signal_patterns = [r"\bvuccati\b"]
    elif any("nama" in support_id for support_id in support_ids):
        signal_patterns = [r"\bnāma\b"]
    elif any("va-alternative" in support_id for support_id in support_ids):
        signal_patterns = [r"\svā\s"]
    else:
        signal_patterns = [
            rf"\b[{PALI_CHARS}]+(?:tvā|tvāna)\b",
            r"\b\w*paccay\w*\b",
            r"\bvuccati\b",
            r"\bnāma\b",
            r"\svā\s",
        ]
    signal_patterns.extend([
        r"\b\w*paccay\w*\b",
        r"\bvuccati\b",
        r"\bnāma\b",
        r"\svā\s",
        rf"\b[{PALI_CHARS}]+(?:tvā|tvāna)\b",
    ])
    for pattern in signal_patterns:
        match = re.search(pattern, text)
        if match:
            half = limit // 2
            start = max(0, match.start() - half)
            end = min(len(text), start + limit)
            start = max(0, end - limit)
            prefix = "…" if start > 0 else ""
            suffix = "…" if end < len(text) else ""
            return prefix + text[start:end].strip() + suffix
    return truncate(text, limit)


def clean_chinese_label(prefix: str) -> str:
    label = prefix.strip(" ，、：:“”\"'[]【】（）()；;。")
    label = re.sub(rf"[{PALI_CHARS}0-9 .-]+", "", label)
    label = label.strip(" ，、：:“”\"'[]【】（）()；;。")
    for marker in ["而成为", "成为", "故为", "名为", "所谓", "即", "因此为", "而为"]:
        if marker in label:
            label = label.rsplit(marker, 1)[-1]
    for prefix_marker in ["将", "將", "把", "以", "用", "在", "和", "与", "给", "对", "为", "是", "那些", "不过"]:
        if label.startswith(prefix_marker):
            label = label[len(prefix_marker) :]
    label = label.strip(" 的之，、：:“”\"'[]【】（）()；;。")
    if not label or len(label) > 8:
        return "(needs_human_label)"
    return label


def json_dump(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def read_version_metadata(source_file: Path) -> dict[str, str]:
    version_id = source_file.stem
    metadata = {
        "version_id": version_id,
        "display_name": version_id,
        "target_language": "zh",
        "source_language": "pi",
        "source_file": str(source_file),
    }
    index_path = source_file.parent / "index.md"
    if not index_path.exists():
        return metadata

    current_id = None
    for raw_line in index_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if line.startswith("# "):
            current_id = line[2:].strip()
            continue
        if current_id != version_id:
            continue
        if line.startswith("- 版本名称："):
            metadata["display_name"] = line.split("：", 1)[1].strip()
        elif line.startswith("- 语言："):
            metadata["target_language"] = line.split("：", 1)[1].strip()
    return metadata


def load_records(source_file: Path) -> list[dict[str, Any]]:
    version_id = source_file.stem
    records = []
    with source_file.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            record = json.loads(line)
            payload = {
                "unit_key": f"{version_id}:{record.get('id', '')}",
                "line": line_no,
                "id": record.get("id"),
                "original": record.get("original"),
                "translation": record.get("translation"),
                "category": record.get("category"),
                "path": record.get("path"),
            }
            record["_line"] = line_no
            record["_unit_key"] = f"{version_id}:{record.get('id', '')}"
            record["_estimated_tokens"] = estimate_tokens(json.dumps(payload, ensure_ascii=False))
            records.append(record)
    return records


def unit_ref(record: dict[str, Any], support_ids: list[str] | None = None) -> dict[str, Any]:
    return {
        "unit_id": record["id"],
        "unit_key": record["_unit_key"],
        "line": record["_line"],
        "source_quote": evidence_source_quote(record["original"], support_ids),
        "target_quote": truncate(record["translation"]),
    }


def add_evidence(
    evidence_rows: list[dict[str, Any]],
    supports: list[str],
    record: dict[str, Any],
    observation: str,
    evidence_type: str,
) -> str:
    evidence_id = f"ev-{len(evidence_rows) + 1:06d}"
    evidence_rows.append(
        {
            "evidence_id": evidence_id,
            "type": evidence_type,
            "unit_id": record["id"],
            "unit_key": record["_unit_key"],
            "line": record["_line"],
            "source_quote": evidence_source_quote(record["original"], supports),
            "target_quote": truncate(record["translation"]),
            "observation": observation,
            "supports": supports,
            "confidence": 0.65,
            "review_status": "machine_generated",
        }
    )
    return evidence_id


def top_items(counter: Counter[str], limit: int = 20) -> list[dict[str, Any]]:
    return [{"value": key, "count": count} for key, count in counter.most_common(limit)]


def build_profile(records: list[dict[str, Any]]) -> dict[str, Any]:
    source_lengths = [len(record["original"]) for record in records]
    target_lengths = [len(record["translation"]) for record in records]
    category_counter = Counter(group_key(record, "category", 3) for record in records)
    path_counter = Counter(group_key(record, "path", 2) for record in records)
    chinese_markers = Counter()
    marker_list = ["以", "被", "即", "应", "这里", "或", "义", "因此", "由于", "称为", "所谓", "其中", "名为", "故为", "根据", "如是", "后缀"]
    for record in records:
        translation = record["translation"]
        for marker in marker_list:
            if marker in translation:
                chinese_markers[marker] += 1

    source_signals = {
        "paccayo": lambda text: bool(re.search(r"\bpaccayo\b", text)),
        "vuccati": lambda text: "vuccati" in text,
        "nāma": lambda text: bool(re.search(r"\bnāma\b", text)),
        "vā": lambda text: bool(re.search(r"\svā\s", text)),
        "absolutive_tvā": lambda text: bool(ABSOLUTIVE_RE.search(text)),
        "ti_or_iti": lambda text: bool(re.search(r"\b(?:iti|ti)\b", text)),
    }
    target_signals = {
        "parenthetical_pali": lambda text: bool(PAREN_PALI_RE.search(text)),
        "square_bracket_supplement": lambda text: "[" in text or "]" in text or "［" in text or "］" in text,
        "newline": lambda text: "\n" in text,
    }

    return {
        "record_count": len(records),
        "unique_id_count": len({record["id"] for record in records}),
        "empty_category_or_path": [unit_ref(record) for record in records if not record["category"] or not record["path"]],
        "source_length": {
            "average": round(statistics.mean(source_lengths), 2),
            "median": statistics.median(source_lengths),
            "max": max(source_lengths),
        },
        "target_length": {
            "average": round(statistics.mean(target_lengths), 2),
            "median": statistics.median(target_lengths),
            "max": max(target_lengths),
        },
        "top_categories": top_items(category_counter, 20),
        "top_paths": top_items(path_counter, 20),
        "source_signals": {name: sum(fn(record["original"]) for record in records) for name, fn in source_signals.items()},
        "target_signals": {name: sum(fn(record["translation"]) for record in records) for name, fn in target_signals.items()},
        "chinese_markers": top_items(chinese_markers, 30),
    }


def collect_terminology(records: list[dict[str, Any]], evidence_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        for chinese_raw, pali_raw in PAREN_PALI_RE.findall(record["translation"]):
            pali = " ".join(pali_raw.lower().split())
            if pali in STOP_PALI_TERMS:
                continue
            chinese = clean_chinese_label(chinese_raw)
            grouped[(pali, chinese)].append(record)

    entries = []
    for (pali, chinese), term_records in sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0])):
        entry_id = f"term-{slug(pali)}-{slug(chinese)}-{short_hash(pali + '|' + chinese)}"
        evidence_ids = [
            add_evidence(
                evidence_rows,
                [entry_id],
                record,
                f"译文括号保留巴利词 `{pali}`，前置中文片段为 `{chinese}`。",
                "terminology",
            )
            for record in term_records
        ]
        categories = Counter(group_key(record, "category", 3) for record in term_records)
        entries.append(
            {
                "id": entry_id,
                "version_id": term_records[0]["_unit_key"].split(":", 1)[0],
                "type": "terminology",
                "pali": pali,
                "chinese": chinese,
                "term_category": "parenthetical_pali_candidate",
                "occurrence_count": len(term_records),
                "top_categories": top_items(categories, 5),
                "evidence_ids": evidence_ids,
                "evidence_sample": [unit_ref(record) for record in term_records[:5]],
                "confidence": 0.55 if chinese == "(needs_human_label)" else 0.7,
                "review_status": "machine_generated",
                "notes": ["由译文括号中的巴利词自动抽取，需要人工确认中文词边界。"],
            }
        )
    return entries


def has_any(text: str, markers: list[str]) -> bool:
    return any(marker in text for marker in markers)


def pattern_records(records: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    return {
        "collocation-paccayo-suffix": [
            record
            for record in records
            if re.search(r"\bpaccayo\b", record["original"]) and "后缀" in record["translation"]
        ],
        "collocation-paccayo-condition": [
            record
            for record in records
            if re.search(r"\bpaccayo\b", record["original"])
            and "缘" in record["translation"]
            and "后缀" not in record["translation"]
        ],
        "collocation-vuccati-definition": [
            record
            for record in records
            if "vuccati" in record["original"]
            and has_any(record["translation"], ["称为", "所谓", "被称为", "所说", "为"])
        ],
        "collocation-nama-naming": [
            record
            for record in records
            if re.search(r"\bnāma\b", record["original"])
            and has_any(record["translation"], ["名为", "所谓", "即", "称为", "是说", "就是"])
        ],
        "collocation-va-alternative": [
            record
            for record in records
            if re.search(r"\svā\s", record["original"])
            and ("或" in record["translation"] or "或者" in record["translation"] or "\n" in record["translation"])
        ],
        "pattern-absolutive-tva": [record for record in records if ABSOLUTIVE_RE.search(record["original"])],
        "pattern-bracket-supplement": [record for record in records if "[" in record["translation"] or "]" in record["translation"] or "［" in record["translation"] or "］" in record["translation"]],
        "pattern-newline-decomposition": [record for record in records if "\n" in record["translation"]],
        "pattern-parenthetical-pali-retention": [record for record in records if PAREN_PALI_RE.search(record["translation"])],
    }


def collect_collocations(records: list[dict[str, Any]], evidence_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    definitions = {
        "collocation-paccayo-suffix": {
            "source_pattern": "X paccayo",
            "translation_pattern": "X为后缀 / X 是后缀",
            "function": "词源或语法派生说明",
            "recommended_translation": ["X为后缀", "X 是后缀"],
        },
        "collocation-paccayo-condition": {
            "source_pattern": "X-paccayena paccayo / X paccayo",
            "translation_pattern": "以X缘为缘 / X为缘",
            "function": "阿毗达摩缘法或条件关系说明",
            "recommended_translation": ["以X缘为缘", "X为缘"],
        },
        "collocation-vuccati-definition": {
            "source_pattern": "X vuccati",
            "translation_pattern": "称为 / 所谓 / 被称为 / 所说 / 为",
            "function": "定义、命名或术语解释",
            "recommended_translation": ["称为", "所谓", "被称为", "所说", "为"],
        },
        "collocation-nama-naming": {
            "source_pattern": "X nāma",
            "translation_pattern": "名为 / 所谓 / 即 / 是说 / 就是",
            "function": "命名、分类或定义",
            "recommended_translation": ["名为", "所谓", "即", "是说", "就是"],
        },
        "collocation-va-alternative": {
            "source_pattern": "X vā Y",
            "translation_pattern": "X，或Y / 换行并列",
            "function": "并列解释或替代词源",
            "recommended_translation": ["或", "或者", "换行并列"],
        },
    }
    grouped = pattern_records(records)
    entries = []
    for entry_id, meta in definitions.items():
        matched = grouped[entry_id]
        if not matched:
            continue
        evidence_ids = [
            add_evidence(evidence_rows, [entry_id], record, f"匹配固定搭配 `{meta['source_pattern']}`。", "collocation")
            for record in matched
        ]
        entries.append(
            {
                "id": entry_id,
                "version_id": records[0]["_unit_key"].split(":", 1)[0],
                "type": "collocation",
                **meta,
                "occurrence_count": len(matched),
                "evidence_ids": evidence_ids,
                "evidence_sample": [unit_ref(record, [entry_id]) for record in matched[:8]],
                "confidence": 0.75 if matched else 0.0,
                "review_status": "machine_generated",
            }
        )
    return entries


def collect_sentence_patterns(records: list[dict[str, Any]], evidence_rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    grouped = pattern_records(records)
    definitions = {
        "syntax-etymological-explanation": {
            "grammar_category": "etymological_explanation",
            "source_pattern": "root/word + meaning + derived form + paccayo",
            "translation_pattern": "词根义 + 派生解释 + 后缀说明",
            "technique": "将巴利词源分析拆成中文解释单元，并保留关键巴利形式。",
            "source_ids": ["collocation-paccayo-suffix"],
        },
        "syntax-paccaya-condition-formula": {
            "grammar_category": "conditional_relation_formula",
            "source_pattern": "X-paccayena paccayo / X paccayo",
            "translation_pattern": "以X缘为缘 / X为缘",
            "technique": "在阿毗达摩或因缘说明中，将 paccaya/paccayo 译为缘，并显化为条件关系。",
            "source_ids": ["collocation-paccayo-condition"],
        },
        "syntax-definition-vuccati-nama": {
            "grammar_category": "definition_formula",
            "source_pattern": "X vuccati / X nāma",
            "translation_pattern": "称为 / 所谓 / 名为 / 即",
            "technique": "把巴利定义公式转成中文命名或说明句。",
            "source_ids": ["collocation-vuccati-definition", "collocation-nama-naming"],
        },
        "syntax-va-alternative": {
            "grammar_category": "alternative_explanation",
            "source_pattern": "X vā Y",
            "translation_pattern": "X，或Y / 换行并列",
            "technique": "用“或”显化并列解释关系，必要时换行拆分。",
            "source_ids": ["collocation-va-alternative"],
        },
        "syntax-absolutive-tva-candidate": {
            "grammar_category": "absolutive_construction_candidate",
            "source_pattern": "verb-tvā / verb-tvāna",
            "translation_pattern": "候选集合，未确认固定译法",
            "technique": "仅按 -tvā/-tvāna 形式自动检测；该条目用于人工筛选，不作为翻译规则。",
            "source_ids": ["pattern-absolutive-tva"],
        },
    }
    entries = []
    for entry_id, meta in definitions.items():
        matched = []
        source_ids = meta["source_ids"]
        for source_id in source_ids:
            matched.extend(grouped[source_id])
        seen = set()
        unique_matched = []
        for record in matched:
            if record["_unit_key"] not in seen:
                seen.add(record["_unit_key"])
                unique_matched.append(record)
        if not unique_matched:
            continue
        evidence_ids = [
            add_evidence(evidence_rows, [entry_id], record, f"匹配句式 `{meta['source_pattern']}`。", "sentence_pattern")
            for record in unique_matched
        ]
        public_meta = {key: value for key, value in meta.items() if key != "source_ids"}
        entries.append(
            {
                "id": entry_id,
                "version_id": records[0]["_unit_key"].split(":", 1)[0],
                "type": "sentence_pattern",
                **public_meta,
                "occurrence_count": len(unique_matched),
                "evidence_ids": evidence_ids,
                "evidence_sample": [unit_ref(record, [entry_id]) for record in unique_matched[:8]],
                "confidence": 0.55 if "candidate" in entry_id else 0.7,
                "review_status": "needs_review" if "candidate" in entry_id else "machine_generated",
            }
        )
    return entries


def collect_style_and_strategy(records: list[dict[str, Any]], evidence_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    grouped = pattern_records(records)
    version_id = records[0]["_unit_key"].split(":", 1)[0]
    style_defs = [
        ("style-parenthetical-pali", "pali_retention", "译文经常用括号保留巴利词形。", "pattern-parenthetical-pali-retention"),
        ("style-bracket-supplement", "translator_supplement", "译文使用方括号补出隐含或解释性内容。", "pattern-bracket-supplement"),
        ("style-newline-decomposition", "line_break_decomposition", "译文使用换行拆分并列解释或复杂词源分析。", "pattern-newline-decomposition"),
    ]
    style_entries = []
    for entry_id, dimension, observation, source_id in style_defs:
        matched = grouped[source_id]
        evidence_ids = [
            add_evidence(evidence_rows, [entry_id], record, observation, "style_observation")
            for record in matched
        ]
        style_entries.append(
            {
                "id": entry_id,
                "version_id": version_id,
                "type": "style_observation",
                "dimension": dimension,
                "observation": observation,
                "occurrence_count": len(matched),
                "evidence_ids": evidence_ids,
                "evidence_sample": [unit_ref(record, [entry_id]) for record in matched[:8]],
                "confidence": 0.75,
                "review_status": "machine_generated",
            }
        )

    strategy_entries = [
        {
            "id": "strategy-explanatory-literal",
            "version_id": version_id,
            "type": "strategy",
            "name": "解释性直译",
            "definition": "保留巴利结构和关键词，同时补出语法、词源或隐含关系。",
            "when_used": ["词源解释", "语法说明", "术语定义", "长注释句"],
            "related_entry_ids": ["syntax-etymological-explanation", "syntax-definition-vuccati-nama"],
            "risks": ["译文包含解释性增补，不能全部视为原文逐词对应。"],
            "confidence": 0.75,
            "review_status": "machine_generated",
        },
        {
            "id": "strategy-pali-retention",
            "version_id": version_id,
            "type": "strategy",
            "name": "保留巴利原词",
            "definition": "在中文译名或解释后用括号保留巴利词形。",
            "when_used": ["术语未稳定", "词源解释", "专名或物名", "需要可追溯性"],
            "related_entry_ids": ["style-parenthetical-pali"],
            "risks": ["降低汉语自然度，增加检索噪声。"],
            "confidence": 0.75,
            "review_status": "machine_generated",
        },
        {
            "id": "strategy-bracketed-expansion",
            "version_id": version_id,
            "type": "strategy",
            "name": "方括号增补",
            "definition": "用方括号标出译者补足、推测或解释性成分。",
            "when_used": ["原文省略主体", "需要补足语法关系", "译者提示不确定内容"],
            "related_entry_ids": ["style-bracket-supplement"],
            "risks": ["方括号内容不能直接等同于原文。"],
            "confidence": 0.7,
            "review_status": "machine_generated",
        },
        {
            "id": "strategy-linebreak-decomposition",
            "version_id": version_id,
            "type": "strategy",
            "name": "换行拆解",
            "definition": "用换行拆分多重词源、并列义项或复杂说明。",
            "when_used": ["多个 vā 并列", "长词源解释", "语法例句逐项说明"],
            "related_entry_ids": ["style-newline-decomposition", "syntax-va-alternative"],
            "risks": ["清洗文本时不能直接丢弃换行。"],
            "confidence": 0.7,
            "review_status": "machine_generated",
        },
    ]
    return style_entries, strategy_entries


def attach_strategy_evidence(
    strategy_entries: list[dict[str, Any]],
    evidence_sources: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    source_by_id = {entry["id"]: entry for entry in evidence_sources}
    attached = []
    for strategy in strategy_entries:
        related_ids = [entry_id for entry_id in strategy["related_entry_ids"] if entry_id in source_by_id]
        evidence_ids = []
        evidence_sample = []
        for entry_id in related_ids:
            source = source_by_id[entry_id]
            evidence_ids.extend(source.get("evidence_ids", [])[:3])
            evidence_sample.extend(source.get("evidence_sample", [])[:3])
        if not evidence_sample:
            continue
        strategy = dict(strategy)
        strategy["related_entry_ids"] = related_ids
        strategy["evidence_ids"] = evidence_ids
        strategy["evidence_sample"] = evidence_sample[:8]
        attached.append(strategy)
    return attached


def markdown_table(rows: list[dict[str, Any]], columns: list[tuple[str, str]]) -> str:
    lines = ["| " + " | ".join(header for header, _ in columns) + " |"]
    lines.append("| " + " | ".join("---" for _ in columns) + " |")
    for row in rows:
        values = [str(row.get(key, "")).replace("\n", "<br>") for _, key in columns]
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def yaml_block(entry: dict[str, Any]) -> str:
    return "```yaml\n" + yaml.safe_dump(entry, allow_unicode=True, sort_keys=False).strip() + "\n```"


def md_entry(entry: dict[str, Any], title: str | None = None, note: str | None = None) -> str:
    heading = title or entry["id"]
    lines = [f"## {heading}", "", yaml_block(entry)]
    if note:
        lines.extend(["", note])
    return "\n".join(lines)


def terminology_md_entry(item: dict[str, Any]) -> dict[str, Any]:
    chinese = None if item["chinese"] == "(needs_human_label)" else item["chinese"]
    return {
        "id": item["id"],
        "version_id": item["version_id"],
        "type": item["type"],
        "name": f"{item['pali']} -> {chinese or 'needs human label'}",
        "description": "从译文括号中保留的巴利词形自动抽取的术语候选，中文词边界需人工复核。",
        "pali": item["pali"],
        "chinese": chinese,
        "term_category": item["term_category"],
        "occurrence_count": item["occurrence_count"],
        "top_categories": item["top_categories"],
        "evidence": item["evidence_sample"],
        "evidence_ids": item["evidence_ids"],
        "confidence": item["confidence"],
        "review_status": item["review_status"],
        "notes": item["notes"],
    }


def collocation_md_entry(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item["id"],
        "version_id": item["version_id"],
        "type": item["type"],
        "name": item["source_pattern"],
        "description": f"{item['function']}。该版本中出现 {item['occurrence_count']} 次。",
        "source_pattern": item["source_pattern"],
        "translation_pattern": item["translation_pattern"],
        "function": item["function"],
        "recommended_translation": item["recommended_translation"],
        "occurrence_count": item["occurrence_count"],
        "evidence": item["evidence_sample"],
        "evidence_ids": item["evidence_ids"],
        "confidence": item["confidence"],
        "review_status": item["review_status"],
    }


def sentence_pattern_md_entry(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item["id"],
        "version_id": item["version_id"],
        "type": item["type"],
        "name": item["grammar_category"],
        "description": item["technique"],
        "grammar_category": item["grammar_category"],
        "source_pattern": item["source_pattern"],
        "translation_pattern": item["translation_pattern"],
        "technique": item["technique"],
        "occurrence_count": item["occurrence_count"],
        "evidence": item["evidence_sample"],
        "evidence_ids": item["evidence_ids"],
        "confidence": item["confidence"],
        "review_status": item["review_status"],
    }


def style_md_entry(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item["id"],
        "version_id": item["version_id"],
        "type": item["type"],
        "name": item["dimension"],
        "description": item["observation"],
        "dimension": item["dimension"],
        "observation": item["observation"],
        "occurrence_count": item["occurrence_count"],
        "evidence": item["evidence_sample"],
        "evidence_ids": item["evidence_ids"],
        "confidence": item["confidence"],
        "review_status": item["review_status"],
    }


def strategy_md_entry(item: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": item["id"],
        "version_id": item["version_id"],
        "type": item["type"],
        "name": item["name"],
        "description": item["definition"],
        "definition": item["definition"],
        "when_used": item["when_used"],
        "risks": item["risks"],
        "related_entry_ids": item["related_entry_ids"],
        "evidence": item.get("evidence_sample", []),
        "evidence_ids": item.get("evidence_ids", []),
        "confidence": item["confidence"],
        "review_status": item["review_status"],
    }


def write_markdown_files(
    kb_dir: Path,
    source_file: Path,
    metadata: dict[str, str],
    profile: dict[str, Any],
    chunk_plan: list[dict[str, Any]],
    terminology: list[dict[str, Any]],
    collocations: list[dict[str, Any]],
    sentence_patterns: list[dict[str, Any]],
    style_entries: list[dict[str, Any]],
    strategy_entries: list[dict[str, Any]],
) -> None:
    version_id = source_file.stem
    version_name = metadata["display_name"]
    top_terms = sorted(terminology, key=lambda item: (-item["occurrence_count"], item["pali"]))[:50]
    chunk_summary = {
        "chunk_count": len(chunk_plan),
        "max_estimated_tokens": max((chunk["estimated_tokens"] for chunk in chunk_plan), default=0),
        "largest_chunk_id": max(chunk_plan, key=lambda chunk: chunk["estimated_tokens"])["chunk_id"] if chunk_plan else None,
    }
    target_signals = profile["target_signals"]
    source_signals = profile["source_signals"]
    record_count = profile["record_count"]
    source_average = profile["source_length"]["average"]
    target_average = profile["target_length"]["average"]
    parenthetical_count = target_signals.get("parenthetical_pali", 0)
    bracket_count = target_signals.get("square_bracket_supplement", 0)
    newline_count = target_signals.get("newline", 0)
    tvā_count = source_signals.get("absolutive_tvā", 0)

    (kb_dir / "analysis-report.md").write_text(
        "\n".join(
            [
                "# 全量分析报告",
                "",
                f"- version id: `{version_id}`",
                f"- source file: `{source_file}`",
                f"- records: `{profile['record_count']}`",
                f"- unique ids: `{profile['unique_id_count']}`",
                f"- source average length: `{profile['source_length']['average']}`",
                f"- target average length: `{profile['target_length']['average']}`",
                f"- chunk count: `{chunk_summary['chunk_count']}`",
                f"- max chunk tokens: `{chunk_summary['max_estimated_tokens']}`",
                "",
                "## Source Signals",
                "",
                markdown_table(
                    [{"signal": key, "count": value} for key, value in profile["source_signals"].items()],
                    [("Signal", "signal"), ("Count", "count")],
                ),
                "",
                "## Target Signals",
                "",
                markdown_table(
                    [{"signal": key, "count": value} for key, value in profile["target_signals"].items()],
                    [("Signal", "signal"), ("Count", "count")],
                ),
                "",
                "## Top Categories",
                "",
                markdown_table(profile["top_categories"], [("Category", "value"), ("Count", "count")]),
                "",
                "## Top Paths",
                "",
                markdown_table(profile["top_paths"], [("Path", "value"), ("Count", "count")]),
                "",
                "## Chinese Marker Counts",
                "",
                markdown_table(profile["chinese_markers"], [("Marker", "value"), ("Count", "count")]),
                "",
                "## Empty Metadata Records",
                "",
                markdown_table(profile["empty_category_or_path"], [("Unit", "unit_key"), ("Line", "line")])
                if profile["empty_category_or_path"]
                else "None.",
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "chunk-plan.md").write_text(
        "\n".join(
            [
                "# Chunk Plan",
                "",
                "Generated with `scripts/build_version_kb.py` using a 128k context and 20% data budget.",
                "",
                markdown_table(
                    chunk_plan,
                    [
                        ("Chunk", "chunk_id"),
                        ("Group", "group_key"),
                        ("Records", "record_count"),
                        ("Tokens", "estimated_tokens"),
                        ("Start", "start_line"),
                        ("End", "end_line"),
                    ],
                ),
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "terminology.md").write_text(
        "\n".join(
            [
                "# 翻译用词",
                "",
                "本文件由全量扫描生成，记录译文括号中保留巴利词形的术语候选。正式条目使用 `## + yaml` 格式；中文词边界为机器抽取，需要人工复核。",
                "",
                f"- candidate terms: `{len(terminology)}`",
                "- edit rule: 修改 YAML 块，不要只改摘要文字。",
                "",
                "## 摘要索引",
                "",
                markdown_table(
                    [
                        {
                            "pali": item["pali"],
                            "chinese": item["chinese"],
                            "count": item["occurrence_count"],
                            "confidence": item["confidence"],
                            "sample": item["evidence_sample"][0]["unit_key"] if item["evidence_sample"] else "",
                        }
                        for item in top_terms
                    ],
                    [("Pali", "pali"), ("Chinese", "chinese"), ("Count", "count"), ("Confidence", "confidence"), ("Sample", "sample")],
                ),
                "",
                "## 条目",
                "",
                "\n\n".join(
                    md_entry(terminology_md_entry(item), title=item["id"])
                    for item in sorted(terminology, key=lambda item: (-item["occurrence_count"], item["pali"], item["chinese"]))
                ),
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "collocations.md").write_text(
        "\n".join(
            [
                "# 固定搭配与公式表达",
                "",
                "本文件记录全量扫描得到的固定搭配候选。正式条目使用 `## + yaml` 格式。",
                "",
                "## 摘要索引",
                "",
                markdown_table(
                    [
                        {
                            "id": item["id"],
                            "source": item["source_pattern"],
                            "target": item["translation_pattern"],
                            "count": item["occurrence_count"],
                        }
                        for item in collocations
                    ],
                    [("ID", "id"), ("Source Pattern", "source"), ("Translation Pattern", "target"), ("Count", "count")],
                ),
                "",
                "## 条目",
                "",
                "\n\n".join(md_entry(collocation_md_entry(item), title=item["id"]) for item in collocations),
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "sentence-patterns.md").write_text(
        "\n".join(
            [
                "# 特殊句式翻译技巧",
                "",
                "本文件记录全量扫描得到的句式候选。正式条目使用 `## + yaml` 格式。`needs_review` 表示仅由形式信号检测，需人工确认。",
                "",
                "## 摘要索引",
                "",
                markdown_table(
                    [
                        {
                            "id": item["id"],
                            "category": item["grammar_category"],
                            "source": item["source_pattern"],
                            "target": item["translation_pattern"],
                            "count": item["occurrence_count"],
                            "status": item["review_status"],
                        }
                        for item in sentence_patterns
                    ],
                    [("ID", "id"), ("Category", "category"), ("Source", "source"), ("Target", "target"), ("Count", "count"), ("Status", "status")],
                ),
                "",
                "## 条目",
                "",
                "\n\n".join(md_entry(sentence_pattern_md_entry(item), title=item["id"]) for item in sentence_patterns),
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "style-guide.md").write_text(
        "\n".join(
            [
                "# 语言风格画像",
                "",
                "本文是供人工阅读和修订的自然语言风格报告。机器可读的风格条目保存在 `entries/style-observations.jsonl`，不要从本文解析结构化数据。",
                "",
                "## 总体判断",
                "",
                f"`{version_name}` 版本整体呈现解释性、讨论型、学习型翻译风格。译文经常不仅给出中文结果，还保留术语线索、补出语法关系，并在必要处显示译者对原文结构的理解过程。这个版本适合研究“学习共同体如何处理巴利注释文本”，也适合作为 LLM 识别翻译决策、术语保留和解释性增补的语料。",
                "",
                f"从全量 `{record_count}` 条记录看，该版本巴利原文平均长度为 `{source_average}` 个字符，中文译文平均长度为 `{target_average}` 个字符。长度关系只能说明整体压缩或扩展趋势，不能直接判断翻译质量；真正有分析价值的是术语保留、方括号补足、换行拆解、定义公式和并列解释等可证据化信号。",
                "",
                "## 可量化信号",
                "",
                markdown_table(
                    [
                        {"dimension": item["dimension"], "observation": item["observation"], "count": item["occurrence_count"]}
                        for item in style_entries
                    ],
                    [("Dimension", "dimension"), ("Observation", "observation"), ("Count", "count")],
                ),
                "",
                "## 巴利词形保留",
                "",
                f"全量扫描发现 `{parenthetical_count}` 条译文含有括号中的巴利形式，并抽取出 `{len(terminology)}` 个术语候选。这类处理常见于三种情况：",
                "",
                "第一，译者给出中文解释后保留巴利原词，便于读者回查原文。",
                "",
                "第二，译者在语法术语、教理术语、专名、地名、物名或不易定译的词上保留巴利形式，降低误读风险。",
                "",
                "第三，译者在讨论型译文中把巴利词作为解释对象，而不是完全转化为中文译名。",
                "",
                "这种风格对术语抽取很有价值，但也带来一个问题：括号前面的中文不一定都是稳定译词，有时只是解释性短语。因此 `terminology.md` 中的中文词边界需要人工复核。",
                "",
                "## 方括号补足",
                "",
                f"该版本有 `{bracket_count}` 条译文含方括号。方括号通常表示译者补足、解释、不确定判断或语法成分显化。",
                "",
                "方括号内容不能简单等同于巴利原文的直接译文。建立知识库时，应把这类内容视为 translator supplement，即“译者增补信息”。对于 RAG 或 LLM 提示词，这类内容很有价值，因为它揭示了译者如何补足隐含结构；但在严格对齐时，应与正文译文分层保存。",
                "",
                "## 换行拆解",
                "",
                f"该版本有 `{newline_count}` 条译文含换行。换行多用于拆分复杂解释，尤其是词源说明、多个 `vā` 并列解释、长句中的义项分解或讨论式补注。这种换行不是纯排版噪声，而可能表示译者对并列解释层次的理解。",
                "",
                "因此，后续清洗数据时不要无条件删除换行。更好的做法是保留原始换行，同时在派生字段中提供 normalized text。对于句式分析，换行可以作为识别“并列解释”“词源分解”“多义项列举”的信号。",
                "",
                "## 解释性连接词",
                "",
                "该版本常用解释性连接词来显化巴利原文关系。高频中文标记包括“以”“被”“即”“应”“这里”“或”“义”“因此”“由于”“称为”“所谓”“名为”“故为”等。",
                "",
                "这些词反映出该版本的翻译目标并非完全自然化，而是倾向于把注释关系说清楚。例如 `vuccati` 常译为“称为、所谓、被称为、所说、为”；`nāma` 常译为“名为、所谓、即、是说、就是”；`paccayo` 在当前证据中主要落入阿毗达摩缘法或条件关系语境，译为“缘、为缘”。这种区分对翻译规则抽取非常重要，不能只按巴利词面合并。",
                "",
                "## 术语风格",
                "",
                "该版本在教理和阿毗达摩语境中倾向使用传统佛教汉语术语，例如“所缘缘”“因缘”“眼识界”等。同时，在尚未稳定汉译或带有词源说明的词上，译者会保留巴利原词。整体策略可以概括为：教理术语尽量术语化，词源分析尽量可追溯。",
                "",
                f"这种风格适合建立版本内术语表，但不宜直接推出跨版本标准译法。不同版本可能更偏流畅汉语、传统佛典译语或现代解释语；本版本的术语记录应先作为 `{version_name}` 版本用词习惯保存。",
                "",
                "## 句法风格",
                "",
                "译者经常把巴利句法关系转成显性的中文关系词。例如工具格、原因关系、处所关系、定义关系、并列解释等，常通过“以、由于、在、即、所谓、或”等表达。该版本尤其适合分析注释书中的定义句、词源句和并列解释句。",
                "",
                f"不过，形式信号不能直接等同于翻译规则。例如 `-tvā/-tvāna` 绝对分词候选有 `{tvā_count}` 条，但很多译文未必明确译成“之后、先、以……方式”。因此这类条目目前只能作为候选集合，需要人工筛选后再总结具体翻译技巧。",
                "",
                "## 风险与使用建议",
                "",
                "- 括号和方括号内容应与正文译文分层处理。",
                "- 换行可能表示语义层级，不应在清洗时无条件删除。",
                "- 自动抽取的中文词边界需要人工校订。",
                "- 不要只根据巴利词面建立规则，应同时检查中文译法和上下文语境。",
                "- `style-guide.md` 是人工阅读文件；机器读取应使用 `entries/style-observations.jsonl`。",
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "style-prompt.md").write_text(
        "\n".join(
            [
                "# 翻译风格提示词",
                "",
                f"用途：将本文件作为大模型翻译巴利语到中文时的风格约束，使输出尽量接近 `{version_name}` 版本。",
                "范围：适用于注释书、语法书、词源解释、阿毗达摩和教理说明类文本。",
                "注意：本文件是给 LLM 使用的操作性提示词，不是研究报告。研究说明见 `style-guide.md`。",
                "",
                "## 角色与目标",
                "",
                "你是一名巴利语到中文的学习型、解释型译者。翻译目标不是只生成流畅中文，而是尽量保留原文的术语、句法关系、词源分析和注释结构，使读者能看出巴利原文如何被理解。",
                "",
                "输出应接近以下风格：",
                "",
                "- 解释性强；",
                "- 保留重要巴利词形；",
                "- 显化定义、因果、处所、工具、并列等关系；",
                "- 对隐含成分可用方括号补足；",
                "- 对复杂词源或并列解释可换行拆分；",
                "- 教理术语尽量使用稳定佛教汉语。",
                "",
                "## 总体翻译原则",
                "",
                "1. 优先准确表达巴利原文结构，不要过度文学化。",
                "2. 对术语、词源、语法分析要保持可追溯性。",
                "3. 如果中文直译不自然，可以适度解释，但不要隐藏原文结构。",
                "4. 对原文未明说但中文需要补出的内容，用方括号表示。",
                "5. 如果一个巴利词在不同语境中有不同译法，按语境处理，不要机械统一。",
                "",
                "## 巴利词形保留",
                "",
                "重要术语、语法标签、词源分析对象、专名、地名、物名或不易定译的词，可以保留巴利原词。",
                "",
                "推荐格式：",
                "",
                "```text",
                "中文译名(巴利词)",
                "```",
                "",
                "示例风格：",
                "",
                "```text",
                "勤学者(vedeha)",
                "第三变格(tatiyāvibhatti)",
                "茧丝(koseyya)",
                "```",
                "",
                "## 方括号补足",
                "",
                "当中文需要补出原文隐含的主体、对象、关系、语境或译者说明时，使用方括号。",
                "",
                "推荐用法：",
                "",
                "```text",
                "[很多人]也说...",
                "通往[涅槃]的...",
                "[额外]有[字母]...",
                "```",
                "",
                "方括号表示补足或解释，不表示原文逐词直译。",
                "",
                "## 换行拆分",
                "",
                "遇到多重词源解释、多个 `vā` 并列解释、长串义项、语法例句或复杂注释，可以用换行拆分。换行用于显示解释层次，不只是排版。",
                "",
                "## 常见公式处理",
                "",
                "### `vuccati`",
                "",
                "根据语境译为：`称为`、`所谓`、`被称为`、`所说`、`为`。",
                "",
                "### `nāma`",
                "",
                "根据语境译为：`名为`、`所谓`、`即`、`是说`、`就是`。",
                "",
                "### `vā`",
                "",
                "通常显化为 `或`、`或者`。如果是多个并列解释，也可以用换行拆分。",
                "",
                "### `paccayo / paccaya`",
                "",
                "必须按语境区分：",
                "",
                "```text",
                "词源或语法派生语境：后缀",
                "阿毗达摩缘法或条件关系语境：缘 / 为缘 / 以X缘为缘",
                "```",
                "",
                "## 教理与阿毗达摩术语",
                "",
                "在教理、阿毗达摩、心识、缘法、界、处等语境中，优先使用传统佛教汉语术语。",
                "",
                "示例：",
                "",
                "```text",
                "ārammaṇapaccaya -> 所缘缘",
                "cakkhuviññāṇadhātu -> 眼识界",
                "hetupaccaya -> 因缘",
                "```",
                "",
                "## 句法关系显化",
                "",
                "巴利语中的格关系、因果关系、处所关系、工具关系、定义关系、并列关系，在中文中应尽量显化。常用中文关系词包括：`以`、`由于`、`在`、`即`、`所谓`、`称为`、`或`、`因此`、`故为`。",
                "",
                "## 绝对分词与分词结构",
                "",
                "遇到 `-tvā`、`-tvāna` 等形式时，不要机械套用固定译法。根据上下文判断为：`...之后`、`先...再...`、`以...方式`、`由于...`、`在...之后`。如果中文不需要显式译出，也可以自然处理，但要保留动作关系。",
                "",
                "## 输出风格限制",
                "",
                "避免：",
                "",
                "- 过度文学化；",
                "- 删除巴利术语线索；",
                "- 把所有解释压缩成一句流畅中文；",
                "- 把方括号补足混同为原文直译；",
                "- 机械统一多义词译法；",
                "- 忽略注释书中的定义、词源和并列解释结构。",
                "",
                "优先：清楚、可追溯、解释性、术语一致、结构透明。",
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "strategies.md").write_text(
        "\n".join(
            [
                "# 翻译策略倾向",
                "",
                "本文件记录该版本由全量扫描支持的翻译策略候选。正式条目使用 `## + yaml` 格式。",
                "",
                "## 摘要索引",
                "",
                markdown_table(
                    [
                        {
                            "id": item["id"],
                            "name": item["name"],
                            "definition": item["definition"],
                            "confidence": item["confidence"],
                            "status": item["review_status"],
                        }
                        for item in strategy_entries
                    ],
                    [("ID", "id"), ("Name", "name"), ("Definition", "definition"), ("Confidence", "confidence"), ("Status", "status")],
                ),
                "",
                "## 条目",
                "",
                "\n\n".join(md_entry(strategy_md_entry(item), title=item["id"]) for item in strategy_entries),
                "",
            ]
        ),
        encoding="utf-8",
    )


def update_manifest(manifest_path: Path, metadata: dict[str, str], kb_dir: Path, status: str = "machine_generated_full_draft") -> None:
    if manifest_path.exists():
        manifest = yaml.safe_load(manifest_path.read_text(encoding="utf-8")) or {}
    else:
        manifest = {
            "schema_version": "0.1",
            "source_directory": "translations",
            "notes": ["Derived knowledge base. Raw JSONL files are not modified."],
            "versions": [],
        }

    versions = manifest.setdefault("versions", [])
    entry = {
        "version_id": metadata["version_id"],
        "source_file": metadata["source_file"],
        "display_name": metadata["display_name"],
        "source_language": metadata["source_language"],
        "target_language": metadata["target_language"],
        "kb_path": str(kb_dir),
        "status": status,
    }
    replaced = False
    for index, existing in enumerate(versions):
        if existing.get("version_id") == metadata["version_id"]:
            versions[index] = entry
            replaced = True
            break
    if not replaced:
        versions.append(entry)

    manifest_path.write_text(yaml.safe_dump(manifest, allow_unicode=True, sort_keys=False), encoding="utf-8")


def write_version_metadata_files(
    kb_dir: Path,
    source_file: Path,
    metadata: dict[str, str],
    profile: dict[str, Any],
    chunk_plan: list[dict[str, Any]],
    terminology: list[dict[str, Any]],
    collocations: list[dict[str, Any]],
    sentence_patterns: list[dict[str, Any]],
    style_entries: list[dict[str, Any]],
    strategy_entries: list[dict[str, Any]],
    evidence_rows: list[dict[str, Any]],
) -> None:
    version_id = metadata["version_id"]
    version_name = metadata["display_name"]
    empty_records = profile["empty_category_or_path"]
    style_summary = "解释性、讨论型，常保留巴利词形、补足隐含关系并拆分复杂说明。"

    corpus = {
        "version_id": version_id,
        "display_name": version_name,
        "source_file": metadata["source_file"],
        "source_language": metadata["source_language"],
        "target_language": metadata["target_language"],
        "record_count": profile["record_count"],
        "translator": version_name,
        "review_status": "machine_generated_full_draft",
        "raw_schema": {"fields": ["id", "original", "translation", "category", "path"]},
        "observed_quality": {
            "valid_jsonl": True,
            "unique_ids_within_version": profile["record_count"] == profile["unique_id_count"],
            "empty_category_path_records": [
                {"line": item["line"], "unit_id": item["unit_id"]}
                for item in empty_records
            ],
        },
        "style_profile": {
            "summary": style_summary,
            "literalness": "medium",
            "explanatory_density": "high",
            "pali_retention": "high" if profile["target_signals"].get("parenthetical_pali", 0) > 500 else "medium",
            "bracketed_supplements": "high" if profile["target_signals"].get("square_bracket_supplement", 0) > 500 else "medium",
            "line_break_usage": "high" if profile["target_signals"].get("newline", 0) > 1000 else "medium",
        },
        "statistics": {
            "multiline_translation_count": profile["target_signals"].get("newline", 0),
            "parenthetical_pali_candidate_count": profile["target_signals"].get("parenthetical_pali", 0),
            "bracketed_translation_count": profile["target_signals"].get("square_bracket_supplement", 0),
            "average_source_length_chars": profile["source_length"]["average"],
            "average_target_length_chars": profile["target_length"]["average"],
        },
        "derived_outputs": {
            "chunk_count": len(chunk_plan),
            "terminology_entries": len(terminology),
            "collocation_entries": len(collocations),
            "sentence_pattern_entries": len(sentence_patterns),
            "style_observation_entries": len(style_entries),
            "strategy_entries": len(strategy_entries),
            "evidence_rows": len(evidence_rows),
            "style_markdown_format": "natural_language",
            "style_prompt": "style-prompt.md",
            "generated_by": "scripts/build_version_kb.py",
        },
    }
    (kb_dir / "corpus.yml").write_text(yaml.safe_dump(corpus, allow_unicode=True, sort_keys=False), encoding="utf-8")

    data_notes = [
        "- 本版本 JSONL 全部可解析。",
        f"- `id` 在本文件内{'唯一' if corpus['observed_quality']['unique_ids_within_version'] else '存在重复'}。",
    ]
    if empty_records:
        data_notes.append("- 存在 `category` 或 `path` 为空的记录，详见 `corpus.yml`。")
    else:
        data_notes.append("- 未发现 `category` 或 `path` 为空的记录。")

    (kb_dir / "README.md").write_text(
        "\n".join(
            [
                f"# {version_name} 版本知识库",
                "",
                "## 基本信息",
                "",
                f"- version id: `{version_id}`",
                f"- version name: `{version_name}`",
                f"- source file: `{metadata['source_file']}`",
                f"- source language: `{metadata['source_language']}`",
                f"- target language: `{metadata['target_language']}`",
                f"- records: `{profile['record_count']}`",
                "",
                "## 当前状态",
                "",
                "本版本已经按大文件工作流完成一次全量机器辅助分析。结果是可审阅初稿，不是人工定稿。",
                "",
                "主要输出：",
                "",
                "- `analysis-report.md`: 全量统计画像。",
                "- `chunk-plan.md`: 按上下文预算生成的分块计划。",
                "- `profile.json`: 机器可读统计画像。",
                "- `entries/*.jsonl`: 机器可读知识条目和证据。",
                "- `style-guide.md`: 给人类阅读的自然语言风格报告。",
                "- `style-prompt.md`: 给大模型翻译时使用的风格提示词。",
                "",
                "初步观察：",
                "",
                f"- 该版本包含 `{profile['record_count']}` 条翻译单元，生成 `{len(chunk_plan)}` 个预算内 chunk。",
                f"- 抽取 `{len(terminology)}` 个术语候选、`{len(collocations)}` 类固定搭配、`{len(sentence_patterns)}` 类句式候选。",
                f"- 生成 `{len(evidence_rows)}` 条证据记录，知识条目均保留可追溯 `unit_key`。",
                "- 该版本适合作为讨论型、学习型翻译风格样本，但术语边界仍需人工复核。",
                "",
                "## 数据注意事项",
                "",
                *data_notes,
                "- 当前条目由脚本全量扫描生成，需要人工复核。",
                "- `terminology` 条目的中文词边界为机器抽取，尤其需要人工校订。",
                "",
                "## 文件说明",
                "",
                "- `corpus.yml`: 版本元数据。",
                "- `style-guide.md`: 语言风格画像。",
                "- `style-prompt.md`: LLM 翻译风格提示词。",
                "- `terminology.md`: 术语和翻译用词。",
                "- `collocations.md`: 固定搭配和公式表达。",
                "- `sentence-patterns.md`: 特殊句式处理。",
                "- `strategies.md`: 翻译策略倾向。",
                "- `notes.md`: 研究笔记和待复核问题。",
                "- `entries/`: 程序读取的 JSONL 条目。",
                "",
            ]
        ),
        encoding="utf-8",
    )

    (kb_dir / "notes.md").write_text(
        "\n".join(
            [
                "# 研究笔记",
                "",
                "## 本轮处理范围",
                "",
                "本版本按大文件工作流处理：先统计画像，再按 `path` 分块，随后抽取术语、固定搭配、句式、风格和策略候选。",
                "",
                "生成结果：",
                "",
                f"- `chunk-plan.md`: `{len(chunk_plan)}` 个预算内 chunk。",
                f"- `entries/terminology.jsonl`: `{len(terminology)}` 个术语候选。",
                f"- `entries/collocations.jsonl`: `{len(collocations)}` 类固定搭配。",
                f"- `entries/sentence-patterns.jsonl`: `{len(sentence_patterns)}` 类句式候选。",
                f"- `entries/style-observations.jsonl`: `{len(style_entries)}` 类风格观察。",
                f"- `entries/strategies.jsonl`: `{len(strategy_entries)}` 类策略。",
                f"- `entries/evidence.jsonl`: `{len(evidence_rows)}` 条证据。",
                "- `style-guide.md`: 自然语言风格报告，不含 YAML 条目块。",
                "- `entries/reviewed-from-md.jsonl`: 从 Markdown YAML 块导出的机器可读条目。",
                "",
                "## 后续应重点复核",
                "",
                "- `terminology` 的中文词边界由脚本从括号前缀抽取，需人工校订。",
                "- 括号内容不一定都是稳定术语，可能是语法说明、专名、英文或临时注释。",
                "- 方括号、脚注和讨论性补充应与正文译文分层处理。",
                "- `vā`、`nāma`、`vuccati` 等公式条目需继续检查上下文，避免只按词面归类。",
                "- 绝对分词结构目前是候选集合，不能直接当作确认规则使用。",
                "- 后续扩展应每次只审一个类别，例如术语、固定搭配或特殊句式。",
                "",
                "## 大文件处理原则",
                "",
                "详细原则见 `docs/large-file-workflow.md`。执行时 LLM 每次接收的数据量应控制在模型最大上下文约 20% 以内；实际原文数据建议控制在 15%，其余空间留给任务说明和输出。",
                "",
            ]
        ),
        encoding="utf-8",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Build a machine-generated version KB draft.")
    parser.add_argument("source_file", type=Path)
    parser.add_argument("--kb-dir", type=Path, required=True)
    parser.add_argument("--max-context", type=int, default=128000)
    parser.add_argument("--budget-ratio", type=float, default=0.20)
    args = parser.parse_args()

    records = load_records(args.source_file)
    metadata = read_version_metadata(args.source_file)
    entries_dir = args.kb_dir / "entries"
    entries_dir.mkdir(parents=True, exist_ok=True)

    profile = build_profile(records)
    data_budget = int(args.max_context * args.budget_ratio)
    chunk_plan = plan_chunks(records, "path", 2, data_budget)
    evidence_rows: list[dict[str, Any]] = []

    terminology = collect_terminology(records, evidence_rows)
    collocations = collect_collocations(records, evidence_rows)
    sentence_patterns = collect_sentence_patterns(records, evidence_rows)
    style_entries, strategy_entries = collect_style_and_strategy(records, evidence_rows)
    strategy_entries = attach_strategy_evidence(strategy_entries, [*collocations, *sentence_patterns, *style_entries])

    json_dump(args.kb_dir / "profile.json", profile)
    write_jsonl(entries_dir / "chunk-plan.jsonl", chunk_plan)
    write_jsonl(entries_dir / "terminology.jsonl", terminology)
    write_jsonl(entries_dir / "collocations.jsonl", collocations)
    write_jsonl(entries_dir / "sentence-patterns.jsonl", sentence_patterns)
    write_jsonl(entries_dir / "style-observations.jsonl", style_entries)
    write_jsonl(entries_dir / "strategies.jsonl", strategy_entries)
    write_jsonl(entries_dir / "evidence.jsonl", evidence_rows)
    write_markdown_files(
        args.kb_dir,
        args.source_file,
        metadata,
        profile,
        chunk_plan,
        terminology,
        collocations,
        sentence_patterns,
        style_entries,
        strategy_entries,
    )
    write_version_metadata_files(
        args.kb_dir,
        args.source_file,
        metadata,
        profile,
        chunk_plan,
        terminology,
        collocations,
        sentence_patterns,
        style_entries,
        strategy_entries,
        evidence_rows,
    )
    update_manifest(args.kb_dir.parent.parent / "manifest.yml", metadata, args.kb_dir)

    print(json.dumps(
        {
            "version_id": args.source_file.stem,
            "records": len(records),
            "chunks": len(chunk_plan),
            "terminology_entries": len(terminology),
            "collocation_entries": len(collocations),
            "sentence_pattern_entries": len(sentence_patterns),
            "style_entries": len(style_entries),
            "strategy_entries": len(strategy_entries),
            "evidence_rows": len(evidence_rows),
        },
        ensure_ascii=False,
        indent=2,
    ))


if __name__ == "__main__":
    main()
