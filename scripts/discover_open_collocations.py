#!/usr/bin/env python3
"""Open-ended collocation discovery for one translation version.

This script intentionally does not seed the extraction with known expressions such
as paccayo/vuccati/nāma/vā. It ranks repeated source-side forms and estimates
target-side renderings from the observed Chinese translations.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import yaml


PALI_CHARS = "A-Za-zāīūṅñṭḍṇḷṃṁĀĪŪṄÑṬḌṆḶṂ"
PALI_WORD_RE = re.compile(rf"[{PALI_CHARS}][{PALI_CHARS}0-9-]*")
CHINESE_RE = re.compile(r"[\u3400-\u9fff]+")
GENERIC_PALI_STOP = {
    "atha",
    "ca",
    "ce",
    "eva",
    "evaṃ",
    "hi",
    "idha",
    "iti",
    "kho",
    "na",
    "no",
    "pana",
    "so",
    "sā",
    "taṃ",
    "tassa",
    "tattha",
    "tato",
    "te",
    "ti",
    "vā",
}
GENERIC_PALI_UNIGRAM_STOP = GENERIC_PALI_STOP | {
    "attho",
    "attano",
    "dhammā",
    "ettha",
    "hoti",
    "hotī",
    "hutvā",
    "katvā",
    "tasmā",
    "tesaṃ",
    "tathā",
    "yasmā",
    "yathā",
    "vuttaṃ",
}
GENERIC_CHINESE_FRAGMENTS = {
    "一个",
    "一种",
    "这个",
    "那个",
    "如此",
    "这里",
    "其中",
    "因为",
    "所以",
    "因此",
    "或者",
    "以及",
    "已经",
    "应当",
}


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


def truncate(text: str, limit: int = 220) -> str:
    text = text.replace("\r\n", "\n").strip()
    if len(text) <= limit:
        return text
    return text[: limit - 1] + "…"


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def normalize_source(text: str) -> str:
    text = normalize_space(text)
    text = re.sub(r"^[0-9]+[.．]\s*", "", text)
    return text


def source_words(text: str) -> list[str]:
    return [word.lower() for word in PALI_WORD_RE.findall(text)]


def load_records(source_file: Path) -> list[dict[str, Any]]:
    version_id = source_file.stem
    records = []
    with source_file.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            record = json.loads(line)
            record["_line"] = line_no
            record["_unit_key"] = f"{version_id}:{record['id']}"
            record["_source_norm"] = normalize_source(record["original"])
            record["_words"] = source_words(record["original"])
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


def ngrams(words: list[str], n: int) -> set[tuple[str, ...]]:
    grams = set()
    for index in range(len(words) - n + 1):
        gram = tuple(words[index : index + n])
        if all(word in GENERIC_PALI_STOP for word in gram):
            continue
        if n == 1 and (gram[0] in GENERIC_PALI_UNIGRAM_STOP or len(gram[0]) < 5):
            continue
        if n > 1 and any(len(word) <= 1 for word in gram):
            continue
        grams.add(gram)
    return grams


def chinese_text(text: str) -> str:
    return "".join(CHINESE_RE.findall(text))


def target_phrases(records: list[dict[str, Any]], limit: int = 5) -> list[str]:
    phrase_counter: Counter[str] = Counter()
    document_counter: Counter[str] = Counter()
    for record in records:
        text = chinese_text(record["translation"])
        seen = set()
        for size in range(2, 9):
            for index in range(0, max(0, len(text) - size + 1)):
                phrase = text[index : index + size]
                if phrase in GENERIC_CHINESE_FRAGMENTS:
                    continue
                if len(set(phrase)) == 1:
                    continue
                seen.add(phrase)
        for phrase in seen:
            document_counter[phrase] += 1
            phrase_counter[phrase] += 1

    scored = []
    minimum = 2 if len(records) < 8 else max(2, math.ceil(len(records) * 0.15))
    for phrase, count in phrase_counter.items():
        doc_count = document_counter[phrase]
        if doc_count < minimum:
            continue
        scored.append((doc_count * len(phrase), doc_count, len(phrase), phrase))
    scored.sort(reverse=True)

    selected: list[str] = []
    for _, _, _, phrase in scored:
        if any(phrase in existing or existing in phrase for existing in selected):
            continue
        selected.append(phrase)
        if len(selected) >= limit:
            break
    return selected


def target_variants(records: list[dict[str, Any]], limit: int = 5) -> list[str]:
    variants = []
    seen = set()
    for record in records:
        value = truncate(normalize_space(record["translation"]), 80)
        if value in seen:
            continue
        seen.add(value)
        variants.append(value)
        if len(variants) >= limit:
            break
    return variants


def candidate_type(source_pattern: str, kind: str) -> str:
    word_count = len(source_pattern.split())
    if kind == "exact_source":
        return "repeated_formula"
    if "‘‘" in source_pattern or "ti" in source_pattern.split() or source_pattern.endswith("–"):
        return "quotation_or_explanation_formula"
    if word_count == 1:
        return "lexical_collocation"
    if word_count >= 4:
        return "phrase_formula"
    return "source_phrase_collocation"


def evidence_sample(records: list[dict[str, Any]], source_pattern: str, limit: int = 8) -> list[dict[str, Any]]:
    examples = []
    pattern_words = set(source_pattern.lower().split())
    for record in records[: limit * 3]:
        source = record["original"]
        if pattern_words:
            words = source_words(source)
            hit_index = next((index for index, word in enumerate(words) if word in pattern_words), None)
            if hit_index is not None:
                source_quote = truncate(source)
            else:
                source_quote = truncate(source)
        else:
            source_quote = truncate(source)
        examples.append(
            {
                "unit_id": record["id"],
                "unit_key": record["_unit_key"],
                "line": record["_line"],
                "source_quote": source_quote,
                "target_quote": truncate(record["translation"]),
            }
        )
        if len(examples) >= limit:
            break
    return examples


def build_candidate(
    version_id: str,
    kind: str,
    source_pattern: str,
    records: list[dict[str, Any]],
    line_to_chunk: dict[int, str],
) -> dict[str, Any]:
    chunks = Counter(line_to_chunk.get(record["_line"], "unknown") for record in records)
    phrases = target_phrases(records)
    variants = target_variants(records)
    translation_pattern = " / ".join(phrases[:3]) if phrases else " / ".join(variants[:3])
    candidate_id = f"open-collocation-{slug(source_pattern)}-{short_hash(source_pattern)}"
    occurrence_count = len(records)
    chunk_count = len(chunks)
    confidence = min(0.9, 0.45 + min(0.25, occurrence_count / 80) + min(0.2, chunk_count / 20))
    return {
        "id": candidate_id,
        "version_id": version_id,
        "type": "collocation",
        "source_pattern": source_pattern,
        "translation_pattern": translation_pattern,
        "collocation_type": candidate_type(source_pattern, kind),
        "occurrence_count": occurrence_count,
        "chunk_count": chunk_count,
        "top_chunks": [{"chunk_id": key, "count": value} for key, value in chunks.most_common(8)],
        "evidence": evidence_sample(records, source_pattern),
        "variant_translations": variants,
        "conditions": ["由开放式全量重复模式发现；需人工判断是否为真正翻译搭配。"],
        "notes": [
            "未用预设搭配清单筛选。",
            "translation_pattern 由目标译文中的高频中文片段自动估计，可能需要人工改写。",
        ],
        "confidence": round(confidence, 2),
        "review_status": "machine_generated",
        "discovery_method": kind,
    }


def discover_candidates(records: list[dict[str, Any]], chunks: list[dict[str, Any]], limit: int) -> list[dict[str, Any]]:
    version_id = records[0]["_unit_key"].split(":", 1)[0]
    line_to_chunk = chunk_id_by_line(chunks)
    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)

    for record in records:
        source_norm = record["_source_norm"]
        if 5 <= len(source_norm) <= 180:
            grouped[("exact_source", source_norm)].append(record)

        words = record["_words"]
        for size in range(1, 7):
            for gram in ngrams(words, size):
                source_pattern = " ".join(gram)
                grouped[(f"source_ngram_{size}", source_pattern)].append(record)

    raw_candidates = []
    for (kind, source_pattern), matched in grouped.items():
        unique = {record["_unit_key"]: record for record in matched}
        matched_records = sorted(unique.values(), key=lambda record: record["_line"])
        occurrence_count = len(matched_records)
        if kind == "exact_source":
            if occurrence_count < 3:
                continue
        elif kind == "source_ngram_1":
            if occurrence_count < 20:
                continue
        else:
            if occurrence_count < 4:
                continue
        chunk_count = len({line_to_chunk.get(record["_line"], "unknown") for record in matched_records})
        source_len = len(source_pattern.split())
        score = occurrence_count * (1 + min(source_len, 5) * 0.35) * (1 + min(chunk_count, 10) * 0.08)
        if kind == "source_ngram_1":
            score *= 0.22
        elif kind == "exact_source":
            score *= 1.4
        raw_candidates.append((score, kind, source_pattern, matched_records))

    raw_candidates.sort(reverse=True, key=lambda item: (item[0], len(item[2])))
    selected: list[tuple[str, str, set[str]]] = []
    candidates = []
    unigram_count = 0
    for _, kind, source_pattern, matched_records in raw_candidates:
        if kind == "source_ngram_1" and unigram_count >= max(15, limit // 5):
            continue
        record_set = {record["_unit_key"] for record in matched_records}
        skip = False
        for selected_kind, selected_pattern, selected_records in selected:
            intersection = len(record_set & selected_records)
            union = len(record_set | selected_records)
            overlap = intersection / union if union else 0
            if overlap >= 0.88 and (source_pattern in selected_pattern or selected_pattern in source_pattern):
                skip = True
                break
            if kind != "exact_source" and selected_kind == "exact_source" and overlap >= 0.70:
                skip = True
                break
        if skip:
            continue
        selected.append((kind, source_pattern, record_set))
        if kind == "source_ngram_1":
            unigram_count += 1
        candidates.append(build_candidate(version_id, kind, source_pattern, matched_records, line_to_chunk))
        if len(candidates) >= limit:
            break
    return candidates


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def markdown_table(rows: list[dict[str, Any]]) -> str:
    lines = [
        "| ID | Source Pattern | Translation Pattern | Count | Chunks | Type |",
        "| --- | --- | --- | ---: | ---: | --- |",
    ]
    for row in rows:
        lines.append(
            "| "
            + " | ".join(
                [
                    row["id"],
                    row["source_pattern"].replace("|", "\\|"),
                    row["translation_pattern"].replace("|", "\\|").replace("\n", "<br>"),
                    str(row["occurrence_count"]),
                    str(row["chunk_count"]),
                    row["collocation_type"],
                ]
            )
            + " |"
        )
    return "\n".join(lines)


def yaml_block(entry: dict[str, Any]) -> str:
    return "```yaml\n" + yaml.safe_dump(entry, allow_unicode=True, sort_keys=False).strip() + "\n```"


def write_markdown(path: Path, candidates: list[dict[str, Any]], source_file: Path, chunk_count: int) -> None:
    lines = [
        "# 开放式固定搭配全量候选",
        "",
        "本文件按开放式发现生成：不预设具体搭配清单，而是从全量语料中寻找重复出现的 Pali 片段、公式句和稳定译法。结果是机器候选，供人工筛选、合并和改写。",
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
    parser = argparse.ArgumentParser(description="Discover open-ended collocation candidates.")
    parser.add_argument("source_file", type=Path)
    parser.add_argument("--chunk-plan", type=Path, required=True)
    parser.add_argument("--kb-dir", type=Path, required=True)
    parser.add_argument("--limit", type=int, default=200)
    args = parser.parse_args()

    records = load_records(args.source_file)
    chunks = load_chunks(args.chunk_plan)
    candidates = discover_candidates(records, chunks, args.limit)

    entries_dir = args.kb_dir / "entries"
    entries_dir.mkdir(parents=True, exist_ok=True)
    write_jsonl(entries_dir / "collocations-open.jsonl", candidates)
    write_markdown(args.kb_dir / "collocations-open.md", candidates, args.source_file, len(chunks))
    print(
        json.dumps(
            {
                "version_id": args.source_file.stem,
                "records": len(records),
                "chunks": len(chunks),
                "candidates": len(candidates),
                "output_markdown": str(args.kb_dir / "collocations-open.md"),
                "output_jsonl": str(entries_dir / "collocations-open.jsonl"),
            },
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
