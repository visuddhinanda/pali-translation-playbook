# 巴利语翻译知识库文档结构

本文设计一个同时适合人类阅读、人工修订、程序读取和 RAG 检索的知识库结构。核心原则是：每个 JSONL 文件代表一个独立版本，每个版本建立自己的知识库；跨版本比较作为派生分析层单独保存。

## 设计目标

- 保留每个版本的独立语言风格、用词习惯和翻译策略。
- 支持人工用 Markdown 阅读、讨论和修改。
- 支持程序用 JSONL 或 YAML 读取结构化条目。
- 支持分析语言风格、翻译用词、固定搭配、特殊句式和翻译技巧。
- 支持未来 GraphRAG、向量检索和 LLM 提示词调用。
- 不修改 `translations/` 下的原始 JSONL 文件。

## 总体目录

建议新增 `knowledge-base/` 作为派生知识库目录：

```text
knowledge-base/
  README.md
  manifest.yml

  versions/
    7ac4d13b-a43d-4409-91b5-5f2a82b916b3/
      README.md
      corpus.yml
      style-guide.md
      terminology.md
      collocations.md
      sentence-patterns.md
      strategies.md
      notes.md
      entries/
        terminology.jsonl
        collocations.jsonl
        sentence-patterns.jsonl
        strategies.jsonl
        style-observations.jsonl
        evidence.jsonl

    e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43/
      ...

  comparative/
    README.md
    version-profiles.md
    terminology-variants.md
    style-comparison.md
    pattern-comparison.md
    alignment-notes.md
    entries/
      terminology-variants.jsonl
      style-comparison.jsonl
      pattern-comparison.jsonl

  shared/
    README.md
    concepts.md
    grammar-taxonomy.yml
    strategy-taxonomy.yml
    pattern-taxonomy.yml

  exports/
    rag/
      chunks.jsonl
      graph-nodes.jsonl
      graph-edges.jsonl
```

## 顶层文件

### `knowledge-base/README.md`

人类入口，说明：

- 知识库目的；
- 每个版本的来源；
- 如何编辑；
- 如何区分版本内知识和跨版本知识；
- 审核状态说明。

### `knowledge-base/manifest.yml`

机器入口，记录所有版本：

```yaml
schema_version: "0.1"
source_directory: "translations"
versions:
  - version_id: "7ac4d13b-a43d-4409-91b5-5f2a82b916b3"
    source_file: "translations/7ac4d13b-a43d-4409-91b5-5f2a82b916b3.jsonl"
    display_name: "法护-Dhammapāla"
    source_language: "pi"
    target_language: "zh"
    kb_path: "knowledge-base/versions/7ac4d13b-a43d-4409-91b5-5f2a82b916b3"
```

## 单版本知识库结构

每个版本目录只描述该版本本身，不混入其他译者或其他版本的判断。

```text
versions/{version_id}/
  README.md
  corpus.yml
  style-guide.md
  terminology.md
  collocations.md
  sentence-patterns.md
  strategies.md
  notes.md
  entries/
    terminology.jsonl
    collocations.jsonl
    sentence-patterns.jsonl
    strategies.jsonl
    style-observations.jsonl
    evidence.jsonl
```

### `README.md`

该版本的人类说明页：

- 版本名称；
- 原始文件；
- 语言标签；
- 译者或翻译团队；
- 适合分析的文本范围；
- 已知数据问题；
- 该版本总体风格摘要。

### `corpus.yml`

版本元数据，供程序读取：

```yaml
version_id: "7ac4d13b-a43d-4409-91b5-5f2a82b916b3"
display_name: "法护-Dhammapāla"
source_file: "translations/7ac4d13b-a43d-4409-91b5-5f2a82b916b3.jsonl"
source_language: "pi"
target_language: "zh"
record_count: 19345
translator: "法护-Dhammapāla"
style_profile:
  summary: ""
  formality: null
  literalness: null
  annotation_density: null
review_status: "draft"
```

### `style-guide.md`

记录该版本的语言风格。建议分为：

- 总体风格：直译、意译、讲解式、古典汉译、现代汉语等；
- 句法风格：长句处理、短句拆分、因果关系显化；
- 术语风格：是否保留巴利语、是否使用传统佛教汉语；
- 注释风格：括号、方括号、夹注、补足主语；
- 标点风格：分号、顿号、破折号、换行；
- 风格风险：可能导致的误读或检索噪声。

对应机器条目放在 `entries/style-observations.jsonl`。

### `terminology.md`

记录该版本的翻译用词。适合人类维护表格：

```markdown
| Pali | 译法 | 类型 | 使用条件 | 例证 | 备注 |
| --- | --- | --- | --- | --- | --- |
| sabbaññutañāṇa | 一切知智 | 教理术语 | 佛智语境 | corpus:id | 可保留巴利夹注 |
```

对应机器条目放在 `entries/terminology.jsonl`。

### `collocations.md`

记录固定搭配、惯用语和公式句：

- `Tena vuttaṃ` 之类引文公式；
- `evaṃ ...` 结构；
- 常见注释书解释公式；
- 巴利复合词的固定汉译搭配；
- 佛教术语组合，如心、所、蕴、处、界相关搭配。

对应机器条目放在 `entries/collocations.jsonl`。

### `sentence-patterns.md`

记录特殊句式和语法结构的翻译技巧：

- 绝对分词结构；
- 现在分词、过去分词；
- 被动表达；
- 复合词展开；
- 工具格、属格、处格的关系翻译；
- 省略主语或宾语的补足；
- 长串同位语；
- 注释书词源解释句式。

对应机器条目放在 `entries/sentence-patterns.jsonl`。

### `strategies.md`

记录该版本的翻译策略偏好：

- 直译；
- 意译；
- 解释性翻译；
- 教理术语优先；
- 增补；
- 省略；
- 语序重排；
- 保留巴利原词；
- 用现代汉语解释传统术语。

对应机器条目放在 `entries/strategies.jsonl`。

### `notes.md`

保存人工研究笔记：

- 尚未结构化的观察；
- 争议译法；
- 需要复核的条目；
- 与其他版本不同但暂未进入比较层的发现。

## 机器可读条目格式

所有 `entries/*.jsonl` 建议使用“一行一个知识条目”。每个条目必须能追溯到原始语料。

### 通用字段

```json
{
  "id": "term-000001",
  "version_id": "7ac4d13b-a43d-4409-91b5-5f2a82b916b3",
  "type": "terminology",
  "name": "sabbaññutañāṇa -> 一切知智",
  "description": "该版本将 sabbaññutañāṇa 译为一切知智。",
  "tags": ["doctrinal_vocabulary", "abhidhamma"],
  "evidence": [
    {
      "unit_id": "1-348-17-29",
      "unit_key": "7ac4d13b-a43d-4409-91b5-5f2a82b916b3:1-348-17-29",
      "source_quote": "sabbaññutañāṇampi",
      "target_quote": "一切知智"
    }
  ],
  "confidence": 0.8,
  "review_status": "draft",
  "notes": []
}
```

### 术语条目

```json
{
  "id": "term-sabbannutanana",
  "type": "terminology",
  "version_id": "331447b6-39bb-4b49-ac10-6206db93a050",
  "pali": "sabbaññutañāṇa",
  "chinese": "一切知智",
  "term_category": "doctrinal_vocabulary",
  "usage_conditions": ["佛智语境", "注释书语境"],
  "variant_translations": [],
  "evidence": [],
  "confidence": 0.8,
  "review_status": "draft"
}
```

### 固定搭配条目

```json
{
  "id": "collocation-tena-vuttam",
  "type": "collocation",
  "version_id": "e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43",
  "source_pattern": "Tena vuttaṃ",
  "translation_pattern": "根据以上所述",
  "function": "引出前文所述或后文引文",
  "recommended_translation": ["根据以上所述", "因此说", "故说"],
  "evidence": [],
  "confidence": 0.75,
  "review_status": "draft"
}
```

### 特殊句式条目

```json
{
  "id": "syntax-absolutive-001",
  "type": "sentence_pattern",
  "version_id": "VERSION_ID",
  "grammar_category": "absolutive_construction",
  "source_pattern": "verb-tvA / verb-ya absolutive",
  "translation_pattern": "先...然后... / ...之后...",
  "technique": "将巴利前行动作转为汉语时间或条件关系",
  "conditions": [],
  "risks": [],
  "evidence": [],
  "confidence": 0.6,
  "review_status": "draft"
}
```

### 风格观察条目

```json
{
  "id": "style-annotation-density-001",
  "type": "style_observation",
  "version_id": "VERSION_ID",
  "dimension": "annotation_density",
  "observation": "该版本经常使用括号保留巴利原词。",
  "signals": ["target_contains_pali_parentheses"],
  "evidence": [],
  "confidence": 0.7,
  "review_status": "draft"
}
```

## 跨版本比较层

`comparative/` 不替代单版本知识库。它只记录版本之间的差异和共性。

```text
comparative/
  README.md
  version-profiles.md
  terminology-variants.md
  style-comparison.md
  pattern-comparison.md
  alignment-notes.md
  entries/
    terminology-variants.jsonl
    style-comparison.jsonl
    pattern-comparison.jsonl
```

### `version-profiles.md`

总结各版本的总体画像：

```markdown
| version_id | 名称 | 风格倾向 | 术语倾向 | 注释密度 | 适合用途 |
| --- | --- | --- | --- | --- | --- |
| ... | 法护-Dhammapāla | 教理精确 | 保留术语 | 中 | 教理术语分析 |
```

### `terminology-variants.md`

比较同一 Pali 词在不同版本中的译法：

```markdown
| Pali | 版本 | 译法 | 风格判断 | 例证 |
| --- | --- | --- | --- | --- |
| sabbaññutañāṇa | 钱玮 | 一切知智 | 术语化 | unit_key |
| sabbaññutañāṇa | 其他版本 | ... | ... | unit_key |
```

### `style-comparison.md`

比较版本之间的语言风格：

- 哪个版本更直译；
- 哪个版本更解释性；
- 哪个版本更常保留巴利原词；
- 哪个版本更偏现代汉语；
- 哪个版本更偏传统佛教汉语。

### `pattern-comparison.md`

比较特殊结构的译法：

- 同一个绝对分词结构，不同版本如何处理；
- 同一个复合词，不同版本是否展开；
- 同一个被动句，不同版本是否显化被动；
- 同一个注释书公式，不同版本是否采用固定汉语表达。

## 共享分类层

`shared/` 保存跨版本通用的分类体系，不保存某个版本的具体翻译结论。

```text
shared/
  concepts.md
  grammar-taxonomy.yml
  strategy-taxonomy.yml
  pattern-taxonomy.yml
```

### `grammar-taxonomy.yml`

```yaml
grammar_categories:
  - id: "absolutive_construction"
    name_zh: "绝对分词结构"
    pali_signals: ["-tvā", "-tvāna", "-ya"]
  - id: "compound"
    name_zh: "复合词"
    pali_signals: []
  - id: "passive_voice"
    name_zh: "被动表达"
    pali_signals: ["-īyati", "-yati"]
```

### `strategy-taxonomy.yml`

```yaml
strategies:
  - id: "literal"
    name_zh: "直译"
  - id: "semantic"
    name_zh: "意译"
  - id: "expansion"
    name_zh: "增补"
  - id: "reordering"
    name_zh: "语序重排"
```

## 推荐工作流

### 第一阶段：每个版本独立建库

1. 读取一个 JSONL 版本。
2. 建立该版本的 `corpus.yml`。
3. 抽样分析语言风格，写入 `style-guide.md`。
4. 抽取高频术语，写入 `terminology.md` 和 `entries/terminology.jsonl`。
5. 抽取固定搭配，写入 `collocations.md`。
6. 抽取特殊句式，写入 `sentence-patterns.md`。
7. 总结该版本策略偏好，写入 `strategies.md`。

### 第二阶段：跨版本比较

1. 按相同 `unit_id` 对齐不同版本。
2. 比较同一 Pali 原文的不同汉译。
3. 提取术语差异。
4. 提取风格差异。
5. 提取句式处理差异。
6. 把比较结果写入 `comparative/`，不要覆盖单版本结论。

### 第三阶段：RAG 导出

1. 将单版本条目导出为 RAG chunk。
2. 将跨版本比较条目导出为 comparison chunk。
3. 为每个 chunk 保留 `version_id`、`unit_key`、`type`、`tags` 和 `review_status`。
4. 构建图谱节点：版本、术语、句式、策略、证据。
5. 构建图谱边：版本使用术语、句式采用策略、证据支持模式。

## 关键建模建议

- 每个版本必须有独立知识库，不要过早合并成一个“标准译法”。
- `version_id` 是所有知识条目的必填字段。
- `unit_key = version_id + ":" + unit_id` 是证据引用的最小稳定单位。
- 人类编辑 Markdown，程序读取 `entries/*.jsonl` 和 `*.yml`。
- 单版本知识库回答“这个版本怎样翻译”。
- 跨版本比较层回答“不同版本之间有什么差异”。
- 共享分类层只提供标签体系，不替代具体证据。

