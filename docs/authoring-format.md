# 知识库人工编辑格式规范

本文规定知识库最终采用的人工编辑格式。目标是让人类容易阅读和修改，同时让程序可以稳定提取为 JSONL/YAML/RAG chunk。

## 最终决策

采用：

```text
Markdown section + fenced YAML block
```

也就是：

- `##` 标题用于人类阅读、定位和折叠。
- 每个知识条目必须包含一个 ` ```yaml ` 结构块。
- YAML 结构块是该条目的机器可读主数据。
- 标题下方可以有自由说明文字，但程序只依赖 YAML 块。
- Markdown 表格只作为摘要索引，不作为主编辑格式。
- `entries/*.jsonl` 是机器导出结果，可以由 Markdown 中的 YAML 块生成。

例外：`style-guide.md` 可以是自然语言研究报告，不强制包含 YAML 块。对应机器数据应保存在 `entries/style-observations.jsonl`。

## 为什么不使用表格作为主格式

表格适合快速浏览，但不适合作为主数据：

- 难以表达多条证据。
- 难以表达条件、风险、变体译法、复核状态。
- 人工编辑长文本容易破坏表格。
- 程序解析 Markdown 表格比解析 YAML 更脆弱。

因此表格只用于：

- `analysis-report.md` 中的统计摘要；
- `terminology.md` 开头的候选列表摘要；
- 自动生成的索引；
- 人类快速浏览，不作为权威数据源。

## 为什么不使用纯标题叙述作为主格式

纯 `##` 标题和段落适合阅读，但机器抽取不稳定：

- 字段边界不明确。
- 证据难以可靠解析。
- 不同编辑者容易写出不同格式。
- 后续导出 JSONL/RAG chunk 需要大量启发式解析。

因此 `##` 标题用于组织，YAML 块用于结构化。

## 标准条目格式

每个条目使用如下格式：

````markdown
## collocation-paccayo-suffix

```yaml
id: "collocation-paccayo-suffix"
version_id: "3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc"
type: "collocation"
name: "paccayo 后缀公式"
source_pattern: "X paccayo"
translation_pattern: "X为后缀 / X 是后缀"
description: "该版本在词源或语法派生说明中常将 paccayo 译为后缀。"
conditions:
  - "词源解释"
  - "语法派生说明"
risks:
  - "阿毗达摩语境中的 paccaya 可能应译为 缘，而非 后缀。"
recommended_translation:
  - "X为后缀"
  - "X 是后缀"
evidence:
  - unit_key: "3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc:9-95-6-16"
    source_quote: "eru paccayo"
    target_quote: "eru为后缀"
confidence: 0.75
review_status: "machine_generated"
tags:
  - "etymology"
  - "grammar"
```

人工说明：

这里可以写解释、讨论、疑问或待复核意见。程序默认不解析这一段。
````

## 文件级格式

每个可人工维护的知识文件建议这样组织：

```text
terminology.md
  # 翻译用词
  ## 摘要
  ## 待复核问题
  ## term-...
     yaml block
  ## term-...
     yaml block

collocations.md
  # 固定搭配
  ## 摘要
  ## collocation-...
     yaml block

sentence-patterns.md
  # 特殊句式
  ## 摘要
  ## syntax-...
     yaml block
```

## 必填字段

所有条目必填：

```yaml
id:
version_id:
type:
name:
description:
evidence:
confidence:
review_status:
```

所有 `evidence` 至少包含：

```yaml
unit_key:
source_quote:
target_quote:
```

## 推荐字段

术语条目：

```yaml
pali:
chinese:
term_category:
usage_conditions:
variant_translations:
```

固定搭配条目：

```yaml
source_pattern:
translation_pattern:
conditions:
counter_examples:
recommended_translation:
```

句式条目：

```yaml
grammar_category:
source_pattern:
translation_pattern:
technique:
conditions:
risks:
```

策略条目：

```yaml
definition:
when_used:
signals:
risks:
related_patterns:
```

## 生成关系

推荐数据流：

```text
human-editable Markdown
  -> parse fenced YAML blocks
  -> entries/*.jsonl
  -> RAG chunks / graph nodes / graph edges
```

机器生成初稿时可以先生成 `entries/*.jsonl` 和摘要表格，但进入人工校订阶段后，应把重要条目转换为上述 Markdown YAML block 格式。

可用脚本：

```bash
python scripts/markdown_yaml_to_jsonl.py \
  knowledge-base/versions/VERSION_ID/collocations.md \
  knowledge-base/versions/VERSION_ID/sentence-patterns.md \
  --output knowledge-base/versions/VERSION_ID/entries/reviewed.jsonl
```

该脚本只读取 fenced `yaml` 块。普通说明文字和摘要表格不会进入 JSONL。

## 编辑规则

- 人工修改应优先修改 YAML 块。
- 不要只改表格摘要，因为表格可以重新生成。
- 不要删除 `unit_key`，否则条目失去证据回链。
- 如果不确定，设置 `review_status: "needs_review"`。
- 如果中文词边界不确定，使用 `chinese: null` 并在 `notes` 中说明。
- 如果同一 Pali 有多个译法，使用 `variant_translations`，不要强行合并。
