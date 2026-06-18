# 大文件处理与上下文预算

本文记录大 JSONL 文件进入 LLM 分析前的处理原则。目标是避免一次输入过多导致细节丢失，同时保留全量语料的统计视角和证据链。

## 核心原则

不要把完整 JSONL 文件直接发送给 LLM。正确流程是：

```text
程序全量扫描
  -> 生成统计画像和候选片段
  -> LLM 在预算内分块分析
  -> 产出 chunk-level 中间条目
  -> 合并、去重、冲突记录
  -> 形成 version-level 知识库
```

程序可以读取完整文件；LLM 只接收控制在上下文预算内的数据。

## 上下文预算

如果模型最大上下文是 `N` tokens，每次发给 LLM 的原始数据建议不超过：

```text
data_budget = N * 0.20
```

更稳妥的生产设置：

```text
raw_data_budget = N * 0.15
instruction_and_output_budget = N * 0.05
```

例如：

| 模型最大上下文 | 单次数据上限 20% | 推荐原文数据 15% |
| ---: | ---: | ---: |
| 32k | 6.4k | 4.8k |
| 64k | 12.8k | 9.6k |
| 128k | 25.6k | 19.2k |
| 200k | 40k | 30k |

## 分块顺序

优先按语言学意义分块，不优先机械按行数切分。

推荐顺序：

1. 按 `version_id` 分开，每个 JSONL 版本单独建库。
2. 按 `path` 前缀分块，保留同一文本或章节上下文。
3. 按 `category` 前缀分块，保留同一文类或藏经层级。
4. 按任务分块，每次只分析一种知识类型。
5. 按信号过滤，例如只分析含 `paccayo`、`vuccati`、`nāma`、`vā` 的记录。
6. 若仍超预算，再按行号范围切小块。

注意：第 5 条只适用于复核某个已知信号或验证既有规则，不适用于首次抽取固定搭配。固定搭配的首次发现必须使用开放式分析，不能在提示词中预先限定 `paccayo`、`vuccati`、`nāma`、`vā` 等少数搭配，否则输出会退化为“已知规则复查”，无法发现该版本真正高频或有特色的搭配。

## 单次 LLM 任务粒度

每次只做一种任务：

- 语言风格画像；
- 术语抽取；
- 固定搭配抽取；
- 特殊句式抽取；
- 翻译策略归纳；
- 证据复核；
- 冲突和变体合并。

不要在同一个大 chunk 中同时要求完整分析风格、术语、搭配、句式和策略。

## 固定搭配抽取规则

固定搭配抽取分为两个阶段，不能混用。

第一阶段是开放式发现。LLM 接收预算内 chunk 后，应从该 chunk 中自行寻找重复出现或高度相似的 Pali 片段、汉译表达、公式句、术语组合、注释书套语和特殊译法。提示词只能说明“寻找高频固定搭配和可复用翻译模式”，不能列出希望模型寻找的具体搭配。输出应按出现频次、跨上下文稳定性、译法一致性和语言学价值排序，并为每个候选提供 `unit_key` 证据。

第二阶段才是定向复核。只有当开放式阶段已经产生候选后，才能针对某个候选搭配继续追问，例如检查 `paccayo` 是否分为“后缀”和“缘”，或检查 `vā` 是否稳定译为“或/或者/换行并列”。定向复核不得替代开放式发现。

如果一个 10,000 行以上的版本只抽出与小版本相同数量的固定搭配，应视为抽取方法异常，而不是语料确实没有更多搭配。此时应记录为 `needs_open_discovery_rerun`，并重新按 chunk 做开放式搭配发现。

开放式固定搭配抽取的输出建议至少包含：

```yaml
id:
source_pattern:
translation_pattern:
collocation_type:
occurrence_count_in_chunk:
evidence:
  - unit_key:
    source_quote:
    target_quote:
variant_translations:
conditions:
notes:
confidence:
review_status: machine_generated
```

## 中间结果要求

每个 chunk 的输出必须是结构化中间结果，并且每个结论都带证据：

```json
{
  "type": "terminology",
  "version_id": "VERSION_ID",
  "pali": "ārammaṇapaccaya",
  "chinese": "所缘缘",
  "evidence": [
    {
      "unit_key": "VERSION_ID:44-219-20-28",
      "source_quote": "Ārammaṇapaccayoti",
      "target_quote": "“所缘缘”"
    }
  ],
  "confidence": 0.8,
  "review_status": "machine_generated"
}
```

没有 `unit_key` 的结论只能进入研究笔记，不能进入正式知识条目。

## 汇总与合并

分块分析后，不再把原始全文重新发送给 LLM。二级汇总只读取 chunk-level 中间结果：

```text
chunk entries
  -> merge same source pattern
  -> merge same terminology
  -> collect evidence
  -> record variant translations
  -> produce version-level Markdown and JSONL
```

如果出现不同译法，不要强行统一：

```yaml
pali: "paccayo"
variants:
  - chinese: "后缀"
    condition: "词源或语法派生说明"
    evidence: []
  - chinese: "缘"
    condition: "阿毗达摩缘法语境"
    evidence: []
```

## 大文件试运行建议

对任一大版本，先做三步：

1. 用脚本生成统计画像和 chunk 计划。
2. 选择一个低风险任务，例如 `terminology` 或 `collocations`。
3. 只处理 1 到 3 个 chunk，人工确认条目格式后再扩大范围。

这可以避免模型上下文过大、抽取目标过宽、证据链丢失三个常见问题。
