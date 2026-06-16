# 翻译策略倾向

本文件记录该版本由全量扫描支持的翻译策略候选。正式条目使用 `## + yaml` 格式。

## 摘要索引

| ID | Name | Definition | Confidence | Status |
| --- | --- | --- | --- | --- |
| strategy-explanatory-literal | 解释性直译 | 保留巴利结构和关键词，同时补出语法、词源或隐含关系。 | 0.75 | machine_generated |
| strategy-pali-retention | 保留巴利原词 | 在中文译名或解释后用括号保留巴利词形。 | 0.75 | machine_generated |
| strategy-bracketed-expansion | 方括号增补 | 用方括号标出译者补足、推测或解释性成分。 | 0.7 | machine_generated |
| strategy-linebreak-decomposition | 换行拆解 | 用换行拆分多重词源、并列义项或复杂说明。 | 0.7 | machine_generated |

## 条目

## strategy-explanatory-literal

```yaml
id: strategy-explanatory-literal
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
type: strategy
name: 解释性直译
description: 保留巴利结构和关键词，同时补出语法、词源或隐含关系。
definition: 保留巴利结构和关键词，同时补出语法、词源或隐含关系。
when_used:
- 词源解释
- 语法说明
- 术语定义
- 长注释句
risks:
- 译文包含解释性增补，不能全部视为原文逐词对应。
related_entry_ids:
- syntax-etymological-explanation
- syntax-definition-vuccati-nama
evidence: []
confidence: 0.75
review_status: machine_generated
```

## strategy-pali-retention

```yaml
id: strategy-pali-retention
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
type: strategy
name: 保留巴利原词
description: 在中文译名或解释后用括号保留巴利词形。
definition: 在中文译名或解释后用括号保留巴利词形。
when_used:
- 术语未稳定
- 词源解释
- 专名或物名
- 需要可追溯性
risks:
- 降低汉语自然度，增加检索噪声。
related_entry_ids:
- style-parenthetical-pali
evidence: []
confidence: 0.75
review_status: machine_generated
```

## strategy-bracketed-expansion

```yaml
id: strategy-bracketed-expansion
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
type: strategy
name: 方括号增补
description: 用方括号标出译者补足、推测或解释性成分。
definition: 用方括号标出译者补足、推测或解释性成分。
when_used:
- 原文省略主体
- 需要补足语法关系
- 译者提示不确定内容
risks:
- 方括号内容不能直接等同于原文。
related_entry_ids:
- style-bracket-supplement
evidence: []
confidence: 0.7
review_status: machine_generated
```

## strategy-linebreak-decomposition

```yaml
id: strategy-linebreak-decomposition
version_id: 3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc
type: strategy
name: 换行拆解
description: 用换行拆分多重词源、并列义项或复杂说明。
definition: 用换行拆分多重词源、并列义项或复杂说明。
when_used:
- 多个 vā 并列
- 长词源解释
- 语法例句逐项说明
risks:
- 清洗文本时不能直接丢弃换行。
related_entry_ids:
- style-newline-decomposition
- syntax-va-alternative
evidence: []
confidence: 0.7
review_status: machine_generated
```
