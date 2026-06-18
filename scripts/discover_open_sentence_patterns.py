#!/usr/bin/env python3
"""Open-ended sentence-pattern discovery for one translation version.

The extractor uses broad syntactic signals instead of a hand-picked list of
known translation formulas. Output is evidence-linked machine candidates for
human linguistic review.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


PALI_CHARS = "A-Za-zāīūṅñṭḍṇḷṃṁĀĪŪṄÑṬḌṆḶṂ"
PALI_WORD_RE = re.compile(rf"[{PALI_CHARS}][{PALI_CHARS}0-9-]*")


def short_hash(value: str) -> str:
    return hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]


def slug(value: str) -> str:
    normalized = value.lower().strip()
    for old, new in {
        "ā": "a",
        "ī": "i",
        "ū": "u",
        "ṅ": "n",
        "ñ": "n",
        "ṭ": "t",
        "ḍ": "d",
        "ṇ": "n",
        "ḷ": "l",
        "ṃ": "m",
        "ṁ": "m",
    }.items():
        normalized = normalized.replace(old, new)
    normalized = re.sub(r"[^a-z0-9]+", "-", normalized)
    return normalized.strip("-")[:80] or "item"


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def truncate(text: str, limit: int = 260) -> str:
    text = text.replace("\r\n", "\n").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def words(text: str) -> list[str]:
    return [word.lower() for word in PALI_WORD_RE.findall(text)]


def load_records(source_file: Path) -> list[dict[str, Any]]:
    version_id = source_file.stem
    records = []
    with source_file.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            record = json.loads(line)
            record["_line"] = line_no
            record["_unit_key"] = f"{version_id}:{record['id']}"
            record["_words"] = words(record["original"])
            records.append(record)
    return records


def load_chunks(chunk_file: Path) -> list[dict[str, Any]]:
    chunks = []
    with chunk_file.open(encoding="utf-8") as handle:
        for line in handle:
            chunks.append(json.loads(line))
    return chunks


def chunk_id_by_line(chunks: list[dict[str, Any]]) -> dict[int, str]:
    mapping = {}
    for chunk in chunks:
        for line_no in range(chunk["start_line"], chunk["end_line"] + 1):
            mapping[line_no] = chunk["chunk_id"]
    return mapping


def has_word(record: dict[str, Any], candidates: set[str]) -> bool:
    return any(word in candidates for word in record["_words"])


def has_regex(text: str, pattern: str) -> bool:
    return bool(re.search(pattern, text, flags=re.IGNORECASE))


def target_markers(text: str) -> list[str]:
    markers = [
        "若",
        "如果",
        "当",
        "时",
        "则",
        "因此",
        "由于",
        "因为",
        "所以",
        "为了",
        "以",
        "依",
        "通过",
        "根据",
        "关于",
        "在此",
        "此中",
        "其中",
        "如",
        "譬如",
        "同样",
        "或者",
        "或",
        "和",
        "与",
        "不",
        "没有",
        "不能",
        "无",
        "应",
        "应当",
        "当知",
        "可知",
        "称为",
        "名为",
        "所谓",
        "意思是",
        "是指",
        "说",
        "？",
        "?",
    ]
    return [marker for marker in markers if marker in text]


def target_pattern(records: list[dict[str, Any]]) -> str:
    counter = Counter()
    for record in records:
        counter.update(target_markers(record["translation"]))
    values = [marker for marker, _ in counter.most_common(6)]
    return " / ".join(values) if values else "候选集合，需人工归纳译法"


def syntax_signals(record: dict[str, Any]) -> list[tuple[str, str, str, str]]:
    source = normalize_space(record["original"])
    word_set = set(record["_words"])
    signals: list[tuple[str, str, str, str]] = []

    def add(key: str, category: str, source_pattern: str, technique: str) -> None:
        signals.append((key, category, source_pattern, technique))

    if "‘‘" in source or "’’" in source or '"' in source:
        add("quoted_text_ti", "quotation_or_citation", "quoted text + ti / iti", "将引文或被解释词显化为中文引号、冒号或引用句。")
    if has_word(record, {"sace", "ce", "yadi"}):
        add("conditional_clause", "conditional", "sace / ce / yadi + clause", "把条件从句译为若、如果、当……时等条件关系。")
    if has_word(record, {"kathaṃ", "kiṃ", "kasmā", "kuto", "kattha", "kadā"}):
        add("question_explanation", "question_or_problem", "interrogative + explanatory answer", "把问句或设问译为何、为什么、若问等解释性结构。")
    if {"yathā", "tathā"} <= word_set:
        add("yatha_tatha_correlative", "correlative_comparison", "yathā ... tathā ...", "把如是对应结构译为如……同样/也……。")
    if word_set & {"yo", "yaṃ", "ye", "yassa", "yasmiṃ"} and word_set & {"so", "taṃ", "te", "tassa", "tasmiṃ"}:
        add("relative_correlative", "relative_correlative", "ya-/yo- relative + ta-/so- correlative", "把关系从句转成汉语的所、凡、若、此/彼对应关系。")
    if has_word(record, {"na", "no", "natthi", "mā"}):
        add("negative_clause", "negation", "na / no / natthi / mā + predicate", "把否定结构译为不、没有、不能、无等。")
    if any(word.endswith(("tvā", "tvāna")) for word in record["_words"]):
        add("absolutive_sequence", "absolutive_or_converb", "verb-tvā / verb-tvāna", "把先行动作、方式、原因或条件关系译成后、而、以、通过等。")
    if any(word.endswith(("tabba", "tabbaṃ", "tabbo", "tabbā", "anīya", "anīyaṃ")) for word in record["_words"]):
        add("gerundive_obligation", "gerundive_or_obligation", "-tabba / -anīya forms", "把应做、可做、当知、应被理解等义务或可能性显化。")
    if has_word(record, {"vasena"}):
        add("vasena_relation", "relation_by_mode", "X-vasena", "把方式、依据、范围译为以、依、由于、按照……方式。")
    if has_word(record, {"kāraṇā", "hetu", "hetunā", "paccayā"}):
        add("cause_reason_relation", "cause_or_reason", "kāraṇā / hetu / hetunā / paccayā", "把原因、条件或依据译为因为、由于、以……为缘。")
    if has_word(record, {"viya", "iva", "seyyathāpi"}):
        add("simile_comparison", "simile", "viya / iva / seyyathāpi", "把譬喻关系译为如、譬如、犹如、像。")
    if has_word(record, {"ettha", "tattha", "idha"}):
        add("locative_topic", "locative_topic", "ettha / tattha / idha", "把处所或论题入口译为在此、此中、其中、这里。")
    if word_set & {"vā"} and source.count(" vā") >= 2:
        add("alternative_series", "alternative_or_variant", "X vā Y vā", "把多项替代或并列解释译为或、或者、换行列举。")
    if word_set & {"ca"} and source.count(" ca") >= 2:
        add("coordinated_series", "coordination", "X ca Y ca", "把多项并列译为和、与、以及，或用顿号/换行列举。")
    if has_regex(source, rf"\b[{PALI_CHARS}]+ti\b") or " ti " in f" {source.lower()} ":
        add("iti_gloss", "gloss_or_definition", "X-ti / X ti + explanation", "把被解释词、引文或定义对象显化为冒号、引号、所谓、意思是。")
    if len(source) >= 180 or source.count(",") + source.count("，") >= 3:
        add("long_sentence_decomposition", "long_sentence", "long multi-clause sentence", "把长句拆为分号、句号、方括号补足或换行结构。")
    if "[" in record["translation"] or "［" in record["translation"]:
        add("bracketed_supplement_syntax", "supplemented_syntax", "implicit source relation + bracketed target supplement", "用方括号补出主语、宾语、语境、逻辑关系或术语说明。")
    if "\n" in record["translation"]:
        add("newline_decomposition_syntax", "decomposition", "complex source + target line breaks", "用换行拆解并列、长句、偈颂或注释层次。")
    return signals


def evidence_sample(records: list[dict[str, Any]], limit: int = 8) -> list[dict[str, Any]]:
    return [
        {
            "unit_id": record["id"],
            "unit_key": record["_unit_key"],
            "line": record["_line"],
            "source_quote": truncate(record["original"]),
            "target_quote": truncate(record["translation"]),
        }
        for record in records[:limit]
    ]


def variant_translations(records: list[dict[str, Any]], limit: int = 6) -> list[str]:
    seen = set()
    variants = []
    for record in records:
        value = truncate(normalize_space(record["translation"]), 100)
        if value in seen:
            continue
        seen.add(value)
        variants.append(value)
        if len(variants) >= limit:
            break
    return variants


def discover(records: list[dict[str, Any]], chunks: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    version_id = records[0]["_unit_key"].split(":", 1)[0]
    line_to_chunk = chunk_id_by_line(chunks)
    grouped: dict[str, dict[str, Any]] = {}

    for record in records:
        for key, category, source_pattern, technique in syntax_signals(record):
            if key not in grouped:
                grouped[key] = {
                    "category": category,
                    "source_pattern": source_pattern,
                    "technique": technique,
                    "records": [],
                }
            grouped[key]["records"].append(record)

    candidates = []
    for key, item in grouped.items():
        matched = sorted(item["records"], key=lambda record: record["_line"])
        if len(matched) < 10:
            continue
        chunks_seen = Counter(line_to_chunk.get(record["_line"], "unknown") for record in matched)
        candidate = {
            "id": f"open-syntax-{slug(key)}-{short_hash(key)}",
            "version_id": version_id,
            "type": "sentence_pattern",
            "name": item["category"],
            "description": item["technique"],
            "grammar_category": item["category"],
            "source_pattern": item["source_pattern"],
            "translation_pattern": target_pattern(matched),
            "technique": item["technique"],
            "occurrence_count": len(matched),
            "chunk_count": len(chunks_seen),
            "top_chunks": [{"chunk_id": chunk_id, "count": count} for chunk_id, count in chunks_seen.most_common(8)],
            "evidence": evidence_sample(matched),
            "variant_translations": variant_translations(matched),
            "conditions": ["由开放式句法信号全量发现；需人工判断是否可提升为翻译规则。"],
            "counter_examples": [],
            "confidence": round(min(0.88, 0.45 + min(0.25, len(matched) / 600) + min(0.18, len(chunks_seen) / 80)), 2),
            "review_status": "machine_generated",
            "discovery_method": "open_syntactic_signal",
        }
        candidates.append(candidate)

    candidates.sort(key=lambda item: (-item["occurrence_count"], item["grammar_category"]))
    return candidates[:limit]


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def yaml_block(entry: dict[str, Any]) -> str:
    return "```yaml\n" + yaml.safe_dump(entry, allow_unicode=True, sort_keys=False).strip() + "\n```"


def markdown_table(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| ID | Category | Source Pattern | Translation Pattern | Count | Chunks |",
        "| --- | --- | --- | --- | ---: | ---: |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["id"],
                    row["grammar_category"],
                    row["source_pattern"].replace("|", "\\|"),
                    row["translation_pattern"].replace("|", "\\|").replace("\n", "<br>"),
                    str(row["occurrence_count"]),
                    str(row["chunk_count"]),
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def write_markdown(path: Path, candidates: list[dict[str, Any]], source_file: Path, chunk_count: int) -> None:
    lines = [
        "# 开放式特殊句式翻译技巧候选",
        "",
        "本文件按开放式句法信号生成：不限定某几个既有规则，而是从全量语料中寻找可复用的句法处理方式。结果是机器候选，供人工筛选、合并和改写。",
        "",
        f"- source file: `{source_file}`",
        f"- chunk count: `{chunk_count}`",
        f"- candidate count: `{len(candidates)}`",
        "- review status: `machine_generated`",
        "",
        "## 摘要索引",
        "",
        markdown_table(candidates),
        "",
        "## 条目",
        "",
    ]
    for candidate in candidates:
        lines.extend([f"## {candidate['id']}", "", yaml_block(candidate), ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Discover open-ended sentence pattern candidates.")
    parser.add_argument("source_file", type=Path)
    parser.add_argument("--chunk-plan", type=Path, required=True)
    parser.add_argument("--kb-dir", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=120)
    args = parser.parse_args()

    records = load_records(args.source_file)
    chunks = load_chunks(args.chunk_plan)
    candidates = discover(records, chunks, args.limit)

    entries_dir = args.kb_dir / "entries"
    entries_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(entries_dir / "sentence-patterns-open.jsonl", candidates)
    write_markdown(args.kb_dir / "sentence-patterns-open.md", candidates, args.source_file, len(chunks))
    print(
        json.dumps(
            {
                "version_id": args.source_file.stem,
                "records": len(records),
                "chunks": len(chunks),
                "candidates": len(candidates),
                "output_markdown": str(args.kb_dir / "sentence-patterns-open.md"),
                "output_jsonl": str(entries_dir / "sentence-patterns-open.jsonl"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
