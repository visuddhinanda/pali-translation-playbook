# 研究笔记

## 本轮处理范围

本版本按大文件工作流处理：先统计画像，再按 `path` 分块，随后抽取术语、固定搭配、句式、风格和策略候选。

重要修正：当前 `collocations.md` 的固定搭配结果来自脚本内置的少数公式信号，属于定向扫描，不是开放式搭配发现。对于 13,006 条记录的版本来说，只得到 4 类固定搭配明显不足，应标记为 `needs_open_discovery_rerun`。下一轮应让 LLM 在每个 chunk 中开放式寻找最高频、最稳定、最有翻译价值的固定搭配，再由人工筛选和修正。

生成结果：

- `chunk-plan.md`: `191` 个预算内 chunk。
- `entries/terminology.jsonl`: `4039` 个术语候选。
- `entries/collocations.jsonl`: `4` 类固定搭配。
- `entries/sentence-patterns.jsonl`: `4` 类句式候选。
- `entries/style-observations.jsonl`: `3` 类风格观察。
- `entries/strategies.jsonl`: `4` 类策略。
- `entries/evidence.jsonl`: `16861` 条证据。
- `style-guide.md`: 自然语言风格报告，不含 YAML 条目块。
- `entries/reviewed-from-md.jsonl`: 从 Markdown YAML 块导出的机器可读条目。
- `collocations-open-test.md`: 开放式固定搭配测试结果，覆盖 3 个 chunk，证明当前 4 类固定搭配结果抽取不足。
- `collocations-open.md`: 全量开放式固定搭配候选，覆盖 191 个 chunk，生成 200 条机器候选。
- `entries/collocations-open.jsonl`: 与 `collocations-open.md` 对应的机器可读候选。
- `entries/collocations-open-from-md.jsonl`: 从 `collocations-open.md` 的 YAML 块重新导出的候选，用于验证人类可编辑 Markdown 能回写机器格式。
- `sentence-patterns-open.md`: 全量开放式特殊句式候选，覆盖 191 个 chunk，生成 18 类机器候选。
- `entries/sentence-patterns-open.jsonl`: 与 `sentence-patterns-open.md` 对应的机器可读候选。
- `entries/sentence-patterns-open-from-md.jsonl`: 从 `sentence-patterns-open.md` 的 YAML 块重新导出的候选，用于验证人类可编辑 Markdown 能回写机器格式。

## 后续应重点复核

- `terminology` 的中文词边界由脚本从括号前缀抽取，需人工校订。
- 括号内容不一定都是稳定术语，可能是语法说明、专名、英文或临时注释。
- 方括号、脚注和讨论性补充应与正文译文分层处理。
- `collocations.md` 需要按开放式固定搭配发现流程重跑；不要只查 `paccayo`、`vuccati`、`nāma`、`vā` 等预设搭配。
- `collocations-open.md` 已经完成全量开放式候选生成，但仍是机器候选；需要人工删除泛化单词、合并重叠公式、改写 `translation_pattern`。
- `sentence-patterns-open.md` 已完成全量开放式句法信号候选生成；当前粒度偏宏观，需要人工拆分更细规则，例如将 `quoted text + ti` 区分为引文、词义解释、标题说明等。
- `vā`、`nāma`、`vuccati` 等公式条目需继续检查上下文，避免只按词面归类。
- 绝对分词结构目前是候选集合，不能直接当作确认规则使用。
- 后续扩展应每次只审一个类别，例如术语、固定搭配或特殊句式。

## 大文件处理原则

详细原则见 `docs/large-file-workflow.md`。执行时 LLM 每次接收的数据量应控制在模型最大上下文约 20% 以内；实际原文数据建议控制在 15%，其余空间留给任务说明和输出。
