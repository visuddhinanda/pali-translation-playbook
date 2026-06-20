# 云台教理组 版本知识库

## 基本信息

- version id: `74ebf4c5-c243-4948-955d-6c277e29276a`
- version name: `云台教理组`
- source file: `translations/74ebf4c5-c243-4948-955d-6c277e29276a.jsonl`
- source language: `pi`
- target language: `zh`
- records: `6686`

## 当前状态

本版本已经按大文件工作流完成一次全量机器辅助分析。结果是可审阅初稿，不是人工定稿。

主要输出：

- `analysis-report.md`: 全量统计画像。
- `chunk-plan.md`: 按上下文预算生成的分块计划。
- `profile.json`: 机器可读统计画像。
- `entries/*.jsonl`: 机器可读知识条目和证据。
- `style-guide.md`: 给人类阅读的自然语言风格报告。
- `style-prompt.md`: 给大模型翻译时使用的风格提示词。

初步观察：

- 该版本包含 `6686` 条翻译单元，生成 `150` 个预算内 chunk。
- 抽取 `712` 个术语候选、`200` 个开放式固定搭配候选、`18` 类开放式句式候选。
- 生成 `5856` 条证据记录，知识条目均保留可追溯 `unit_key`。
- 该版本适合作为讨论型、学习型翻译风格样本，但术语边界仍需人工复核。

## 数据注意事项

- 本版本 JSONL 全部可解析。
- `id` 在本文件内唯一。
- 未发现 `category` 或 `path` 为空的记录。
- 当前条目由脚本全量扫描生成，需要人工复核。
- `terminology` 条目的中文词边界为机器抽取，尤其需要人工校订。

## 文件说明

- `corpus.yml`: 版本元数据。
- `style-guide.md`: 语言风格画像。
- `style-prompt.md`: LLM 翻译风格提示词。
- `terminology.md`: 术语和翻译用词。
- `collocations.md`: 固定搭配和公式表达。
- `sentence-patterns.md`: 特殊句式处理。
- `strategies.md`: 翻译策略倾向。
- `notes.md`: 研究笔记和待复核问题。
- `entries/`: 程序读取的 JSONL 条目。
