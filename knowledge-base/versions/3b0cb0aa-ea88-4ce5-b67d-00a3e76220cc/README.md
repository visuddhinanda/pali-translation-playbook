# 胜嗣Jinadāyāda 版本知识库

## 基本信息

- version id: `3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc`
- version name: `胜嗣Jinadāyāda`
- source file: `translations/3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc.jsonl`
- source language: `pi`
- target language: `zh`
- records: `2659`

## 试点结论

这个版本适合作为“学习型/分析型翻译”的样本。译文经常保留巴利词形、补出隐含关系，并用括号或方括号标记解释性信息。

初步观察：

- 译文平均长度短于原文，但在词源解释和语法说明段落中会明显扩展。
- 约 26.7% 的译文含括号，常用于保留巴利词或解释术语。
- 约 14.7% 的译文含换行，常用于拆分并列解释或词源分析。
- 译文中常见“即”“被”“应”“因此”“由于”“称为”“所谓”等解释性连接词。
- 该版本对语法、词源、术语的显性化程度较高。

## 数据注意事项

- 本版本 JSONL 全部可解析。
- `id` 在本文件内唯一。
- 第 1686 行 `id=148-1-1-6` 的 `category` 和 `path` 为空。
- 本试点只建立少量人工可审阅条目，不代表完整抽取。

## 文件说明

- `corpus.yml`: 版本元数据。
- `style-guide.md`: 语言风格画像。
- `terminology.md`: 术语和翻译用词。
- `collocations.md`: 固定搭配和公式表达。
- `sentence-patterns.md`: 特殊句式处理。
- `strategies.md`: 翻译策略倾向。
- `notes.md`: 研究笔记和待复核问题。
- `entries/`: 程序读取的 JSONL 条目。

