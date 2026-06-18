# 研究笔记

## 本轮试点范围

本版本已完成一次全量机器辅助分析。当前结果是可审阅初稿，不是人工定稿。

生成结果：

- `analysis-report.md`: 全量统计画像。
- `chunk-plan.md`: 156 个预算内 chunk。
- `entries/terminology.jsonl`: 273 个术语候选。
- `entries/collocations.jsonl`: 5 类固定搭配。
- `entries/sentence-patterns.jsonl`: 5 类句式候选。
- `entries/style-observations.jsonl`: 3 类风格观察。
- `entries/strategies.jsonl`: 4 类策略。
- `entries/evidence.jsonl`: 1876 条证据。
- `style-guide.md`: 自然语言风格报告，不含 YAML 条目块。
- `entries/reviewed-from-md.jsonl`: 287 条从 Markdown YAML 块导出的条目，不包含 `style-guide.md`。

## 后续应重点复核

- `new translate the` 等英文片段是否来自残留机器翻译或特殊格式。
- 繁简混用现象，例如部分样例中出现 `將`、`淨`、`說`。
- 方括号中的内容是否全部应归类为译者增补。
- `paccayo` 已拆分为 `后缀` 和 `缘` 两类规则，仍需人工检查边界。
- 绝对分词结构的样例需要人工筛选，不能只靠后缀正则判断。
- `terminology` 的中文词边界由脚本从括号前缀抽取，需人工校订。
- 部分括号内容不是巴利术语，可能是英文残留或说明标签。

## 大文件处理建议

后续分析大文件时不要一次性生成完整知识库。建议流程：

1. 先生成版本统计画像。
2. 按 `path` 或 `category` 分块。
3. 每次只抽取一个类别，如术语或句式。
4. 每个条目必须有证据 `unit_key`。
5. 人工确认格式后再扩大抽取范围。

详细原则已记录在 `docs/large-file-workflow.md`。

可用以下脚本先生成统计和分块计划：

```bash
python scripts/plan_chunks.py translations/3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc.jsonl --max-context 128000 --budget-ratio 0.2 --group-by path --depth 2 --format markdown
```

执行原则：

- 程序可以全量读取 JSONL。
- LLM 每次只接收不超过模型最大上下文约 20% 的数据。
- 推荐实际原文数据控制在 15%，剩余空间留给任务说明和输出。
- 每次只做一种抽取任务，例如术语、固定搭配或特殊句式。
- 二级汇总只读取 chunk-level 中间结果，不重新读取原始全文。
