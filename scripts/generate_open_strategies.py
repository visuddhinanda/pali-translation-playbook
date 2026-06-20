#!/usr/bin/env python3
"""Generate open-synthesis strategy entries from open KB candidates."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

import yaml


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            rows.append(json.loads(line))
    return rows


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False, separators=(",", ":")) + "\n")


def yaml_block(entry: dict[str, Any]) -> str:
    return "```yaml\n" + yaml.safe_dump(entry, allow_unicode=True, sort_keys=False).strip() + "\n```"


def evidence_from(entries: list[dict[str, Any]], limit: int = 8) -> list[dict[str, Any]]:
    evidence = []
    seen = set()
    for entry in entries:
        for item in entry.get("evidence", []):
            unit_key = item.get("unit_key")
            if not unit_key or unit_key in seen:
                continue
            seen.add(unit_key)
            evidence.append(item)
            if len(evidence) >= limit:
                return evidence
    return evidence


def ids(entries: list[dict[str, Any]], limit: int = 8) -> list[str]:
    return [entry["id"] for entry in entries[:limit]]


def build_strategies(version_id: str, collocations: list[dict[str, Any]], sentence_patterns: list[dict[str, Any]], style: list[dict[str, Any]]) -> list[dict[str, Any]]:
    high_frequency_collocations = sorted(collocations, key=lambda item: item.get("occurrence_count", 0), reverse=True)[:12]
    quotation_patterns = [entry for entry in sentence_patterns if entry.get("grammar_category") in {"quotation_or_citation", "gloss_or_definition", "question_or_problem"}]
    decomposition_patterns = [entry for entry in sentence_patterns if entry.get("grammar_category") in {"long_sentence", "decomposition", "supplemented_syntax"}]
    relation_patterns = [
        entry
        for entry in sentence_patterns
        if entry.get("grammar_category")
        in {"cause_or_reason", "relation_by_mode", "conditional", "relative_correlative", "correlative_comparison", "coordination", "alternative_or_variant"}
    ]
    converb_patterns = [entry for entry in sentence_patterns if entry.get("grammar_category") in {"absolutive_or_converb", "gerundive_or_obligation"}]

    definitions = [
        {
            "id": "strategy-open-frequency-first",
            "name": "高频证据优先",
            "definition": "先从全量语料中发现高频、跨 chunk 重复的搭配和句法信号，再由人工筛选为稳定规则。",
            "when_used": ["固定搭配抽取", "版本内风格画像", "RAG 候选知识生成"],
            "risks": ["高频不等于高价值，可能混入泛化词、引用缩写或格式噪声。"],
            "related_entries": high_frequency_collocations,
        },
        {
            "id": "strategy-open-explanatory-citation",
            "name": "解释与引文显化",
            "definition": "对引文、设问、词义解释和定义公式，倾向用引号、冒号、所谓、意思是、说等方式显化原文的解释结构。",
            "when_used": ["注释书解释", "词义训释", "经论引文", "设问回答"],
            "risks": ["引号内内容、译者补足和原文引文需要分层保存。"],
            "related_entries": quotation_patterns,
        },
        {
            "id": "strategy-open-decomposition",
            "name": "长句拆解与补足",
            "definition": "遇到长句、多层注释或隐含关系时，用换行、方括号、分句和补足语把结构展开。",
            "when_used": ["长复句", "多重并列", "隐含主宾语", "术语说明"],
            "risks": ["补足内容不能直接当作原文逐词对应。"],
            "related_entries": decomposition_patterns or style,
        },
        {
            "id": "strategy-open-relation-explicitation",
            "name": "关系词显化",
            "definition": "把条件、原因、方式、处所、并列、选择和对应关系转成中文关系词或语序结构。",
            "when_used": ["条件句", "原因句", "X-vasena", "yathā/tathā", "ya-/ta- 对应", "多项并列"],
            "risks": ["同一巴利形式在不同上下文中可能需要不同中文关系词。"],
            "related_entries": relation_patterns,
        },
        {
            "id": "strategy-open-verbal-relation",
            "name": "动作关系处理",
            "definition": "对绝对分词、义务式或可行性形式，按上下文处理为先后、方式、原因、应当、可知等关系。",
            "when_used": ["-tvā/-tvāna", "-tabba", "-anīya", "动作串联", "说明性指令"],
            "risks": ["形式信号只能生成候选，不能机械套用固定译法。"],
            "related_entries": converb_patterns,
        },
    ]

    strategies = []
    for item in definitions:
        related_entries = item.pop("related_entries")
        strategies.append(
            {
                "id": item["id"],
                "version_id": version_id,
                "type": "strategy",
                "name": item["name"],
                "description": item["definition"],
                "definition": item["definition"],
                "when_used": item["when_used"],
                "risks": item["risks"],
                "related_entry_ids": ids(related_entries),
                "evidence": evidence_from(related_entries),
                "confidence": 0.72 if related_entries else 0.5,
                "review_status": "machine_generated",
                "discovery_method": "open_synthesis",
            }
        )
    return [strategy for strategy in strategies if strategy["evidence"]]


def markdown_table(rows: list[dict[str, Any]]) -> str:
    lines = ["| ID | Name | Related Entries | Evidence |", "| --- | --- | ---: | ---: |"]
    for row in rows:
        lines.append(f"| {row['id']} | {row['name']} | {len(row['related_entry_ids'])} | {len(row['evidence'])} |")
    return "\n".join(lines)


def write_markdown(path: Path, strategies: list[dict[str, Any]]) -> None:
    lines = [
        "# 翻译策略倾向",
        "",
        "本文件由开放式固定搭配、开放式特殊句式和风格观察综合生成。它不以少数预设公式作为策略范围，而是把全量发现的候选归纳为可人工复核的策略假设。",
        "",
        "## 摘要索引",
        "",
        markdown_table(strategies),
        "",
        "## 条目",
        "",
    ]
    for strategy in strategies:
        lines.extend([f"## {strategy['id']}", "", yaml_block(strategy), ""])
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate open-synthesis strategy candidates.")
    parser.add_argument("--kb-dir", type=Path, required=True)
    args = parser.parse_args()

    entries = args.kb_dir / "entries"
    collocations = read_jsonl(entries / "collocations.jsonl")
    sentence_patterns = read_jsonl(entries / "sentence-patterns.jsonl")
    style_path = entries / "style-observations.jsonl"
    style = read_jsonl(style_path) if style_path.exists() else []
    version_id = args.kb_dir.name
    strategies = build_strategies(version_id, collocations, sentence_patterns, style)

    write_jsonl(entries / "strategies.jsonl", strategies)
    write_markdown(args.kb_dir / "strategies.md", strategies)
    print(json.dumps({"version_id": version_id, "strategies": len(strategies)}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
