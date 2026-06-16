#!/usr/bin/env python3
"""Extract fenced YAML knowledge entries from Markdown into JSONL."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

import yaml


YAML_BLOCK_RE = re.compile(r"```ya?ml\n(.*?)\n```", re.DOTALL)
REQUIRED_FIELDS = ("id", "version_id", "type")


def extract_entries(markdown: str, source_file: Path) -> list[dict[str, Any]]:
    entries = []
    for index, match in enumerate(YAML_BLOCK_RE.finditer(markdown), 1):
        data = yaml.safe_load(match.group(1))
        if data is None:
            continue
        if not isinstance(data, dict):
            raise ValueError(f"{source_file}: YAML block {index} is not a mapping")
        missing = [field for field in REQUIRED_FIELDS if field not in data]
        if missing:
            raise ValueError(f"{source_file}: YAML block {index} missing fields: {', '.join(missing)}")
        data.setdefault("_source_markdown", str(source_file))
        data.setdefault("_source_block", index)
        entries.append(data)
    return entries


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Markdown fenced YAML entries to JSONL.")
    parser.add_argument("markdown_files", nargs="+", type=Path)
    parser.add_argument("--output", "-o", type=Path, required=True)
    args = parser.parse_args()

    all_entries = []
    for markdown_file in args.markdown_files:
        markdown = markdown_file.read_text(encoding="utf-8")
        all_entries.extend(extract_entries(markdown, markdown_file))

    args.output.parent.mkdir(parents=True, exist_ok=True)
    with args.output.open("w", encoding="utf-8") as handle:
        for entry in all_entries:
            handle.write(json.dumps(entry, ensure_ascii=False, separators=(",", ":")) + "\n")

    print(json.dumps({"output": str(args.output), "entries": len(all_entries)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

