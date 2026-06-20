# 研究笔记

## 本轮处理范围

本版本按大文件工作流处理：先统计画像，再按 `path` 分块，随后抽取术语、固定搭配、句式、风格和策略候选。

生成结果：

- `chunk-plan.md`: `150` 个预算内 chunk。
- `entries/terminology.jsonl`: `712` 个术语候选。
- `entries/collocations.jsonl`: `200` 个开放式固定搭配候选。
- `entries/sentence-patterns.jsonl`: `18` 类开放式句式候选。
- `entries/style-observations.jsonl`: `3` 类风格观察。
- `entries/strategies.jsonl`: `4` 类策略。
- `entries/evidence.jsonl`: `5856` 条证据。
- `style-guide.md`: 自然语言风格报告，不含 YAML 条目块。
- `entries/reviewed-from-md.jsonl`: 从 Markdown YAML 块导出的机器可读条目。

## 后续应重点复核

- 固定搭配和特殊句式均使用 open 默认发现流程；未在提示词或抽取入口限定为少数预设结果。

- `terminology` 的中文词边界由脚本从括号前缀抽取，需人工校订。
- 括号内容不一定都是稳定术语，可能是语法说明、专名、英文或临时注释。
- 方括号、脚注和讨论性补充应与正文译文分层处理。
- `vā`、`nāma`、`vuccati` 等公式条目需继续检查上下文，避免只按词面归类。
- 绝对分词结构目前是候选集合，不能直接当作确认规则使用。
- 后续扩展应每次只审一个类别，例如术语、固定搭配或特殊句式。

## 大文件处理原则

详细原则见 `docs/large-file-workflow.md`。执行时 LLM 每次接收的数据量应控制在模型最大上下文约 20% 以内；实际原文数据建议控制在 15%，其余空间留给任务说明和输出。
