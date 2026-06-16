#!/usr/bin/env python3
"""Plan LLM-sized chunks for a translation JSONL file.

This script only reads raw translation data. It does not modify files under
translations/.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any


def estimate_tokens(text: str) -> int:
    """Conservative token estimate for mixed Pali/Chinese JSON text."""
    ascii_chars = sum(1 for char in text if ord(char) < 128)
    non_ascii_chars = len(text) - ascii_chars
    return max(1, ascii_chars // 4 + non_ascii_chars)


def record_payload(record: dict[str, Any], version_id: str, line_no: int) -> str:
    payload = {
        "unit_key": f"{version_id}:{record.get('id', '')}",
        "line": line_no,
        "id": record.get("id"),
        "original": record.get("original"),
        "translation": record.get("translation"),
        "category": record.get("category"),
        "path": record.get("path"),
    }
    return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))


def group_key(record: dict[str, Any], mode: str, depth: int) -> str:
    values = record.get(mode)
    if not isinstance(values, list) or not values:
        return "(empty)"
    return " > ".join(str(value) for value in values[:depth])


def split_group(records: list[dict[str, Any]], budget: int) -> list[list[dict[str, Any]]]:
    chunks: list[list[dict[str, Any]]] = []
    current: list[dict[str, Any]] = []
    current_tokens = 0

    for record in records:
        tokens = record["_estimated_tokens"]
        if current and current_tokens + tokens > budget:
            chunks.append(current)
            current = []
            current_tokens = 0
        current.append(record)
        current_tokens += tokens

    if current:
        chunks.append(current)
    return chunks


def load_records(path: Path) -> list[dict[str, Any]]:
    version_id = path.stem
    records = []
    with path.open(encoding="utf-8") as handle:
        for line_no, line in enumerate(handle, 1):
            record = json.loads(line)
            payload = record_payload(record, version_id, line_no)
            record["_line"] = line_no
            record["_unit_key"] = f"{version_id}:{record.get('id', '')}"
            record["_estimated_tokens"] = estimate_tokens(payload)
            records.append(record)
    return records


def build_profile(records: list[dict[str, Any]]) -> dict[str, Any]:
    category_counter = Counter()
    path_counter = Counter()
    signal_counter = Counter()
    total_tokens = 0

    signals = {
        "paccayo": "paccayo",
        "vuccati": "vuccati",
        "nama": "nāma",
        "iti_ti": "ti",
        "va": " vā ",
        "parentheses_in_translation": "(",
        "brackets_in_translation": "[",
        "newline_in_translation": "\n",
    }

    for record in records:
        total_tokens += record["_estimated_tokens"]
        category_counter[group_key(record, "category", 3)] += 1
        path_counter[group_key(record, "path", 2)] += 1
        original = record.get("original", "")
        translation = record.get("translation", "")
        for signal, needle in signals.items():
            haystack = translation if "translation" in signal else original
            if needle in haystack:
                signal_counter[signal] += 1

    return {
        "record_count": len(records),
        "estimated_total_tokens": total_tokens,
        "top_categories": category_counter.most_common(10),
        "top_paths": path_counter.most_common(10),
        "signals": dict(signal_counter),
    }


def plan_chunks(records: list[dict[str, Any]], mode: str, depth: int, budget: int) -> list[dict[str, Any]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for record in records:
        grouped[group_key(record, mode, depth)].append(record)

    plan = []
    chunk_index = 1
    for key, group_records in sorted(grouped.items()):
        for chunk_records in split_group(group_records, budget):
            token_count = sum(record["_estimated_tokens"] for record in chunk_records)
            plan.append(
                {
                    "chunk_id": f"chunk-{chunk_index:04d}",
                    "group_mode": mode,
                    "group_key": key,
                    "record_count": len(chunk_records),
                    "estimated_tokens": token_count,
                    "start_line": chunk_records[0]["_line"],
                    "end_line": chunk_records[-1]["_line"],
                    "unit_keys": [record["_unit_key"] for record in chunk_records[:5]],
                    "unit_key_sample_note": "first five unit keys only",
                }
            )
            chunk_index += 1
    return plan


def main() -> None:
    parser = argparse.ArgumentParser(description="Plan context-safe LLM chunks for a JSONL version.")
    parser.add_argument("file", type=Path, help="Path to a translations/*.jsonl file.")
    parser.add_argument("--max-context", type=int, default=128000, help="Model maximum context in tokens.")
    parser.add_argument("--budget-ratio", type=float, default=0.20, help="Fraction of max context for data.")
    parser.add_argument("--group-by", choices=["path", "category"], default="path")
    parser.add_argument("--depth", type=int, default=2, help="Prefix depth for path/category grouping.")
    parser.add_argument("--format", choices=["json", "markdown"], default="json")
    args = parser.parse_args()

    budget = max(1, int(args.max_context * args.budget_ratio))
    records = load_records(args.file)
    output = {
        "version_id": args.file.stem,
        "source_file": str(args.file),
        "max_context": args.max_context,
        "budget_ratio": args.budget_ratio,
        "data_budget_tokens": budget,
        "profile": build_profile(records),
        "chunks": plan_chunks(records, args.group_by, args.depth, budget),
    }

    if args.format == "json":
        print(json.dumps(output, ensure_ascii=False, indent=2))
        return

    print(f"# Chunk Plan: {args.file.stem}")
    print()
    print(f"- source file: `{args.file}`")
    print(f"- max context: `{args.max_context}`")
    print(f"- data budget tokens: `{budget}`")
    print(f"- record count: `{output['profile']['record_count']}`")
    print(f"- estimated total tokens: `{output['profile']['estimated_total_tokens']}`")
    print(f"- chunk count: `{len(output['chunks'])}`")
    print()
    print("| chunk_id | group | records | est_tokens | lines |")
    print("| --- | --- | ---: | ---: | --- |")
    for chunk in output["chunks"]:
        lines = f"{chunk['start_line']}-{chunk['end_line']}"
        print(
            f"| `{chunk['chunk_id']}` | {chunk['group_key']} | "
            f"{chunk['record_count']} | {chunk['estimated_tokens']} | {lines} |"
        )


if __name__ == "__main__":
    main()

