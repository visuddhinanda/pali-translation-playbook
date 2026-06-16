# Data Model Inference

This document describes the schema inferred from the JSONL files in `translations/`.
It documents the current raw data shape only; it does not prescribe edits to the
raw corpus.

## Repository Snapshot

The repository currently contains six JSONL translation corpora and one index:

| Corpus file | Index name | Language | Records |
| --- | --- | --- | ---: |
| `7ac4d13b-a43d-4409-91b5-5f2a82b916b3.jsonl` | 法护-Dhammapāla | `zh` | 19,345 |
| `e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43.jsonl` | 初译·高级班内部讨论 | `zh-Hans` | 13,006 |
| `5310999c-0b0c-4bb0-9bb9-9cdd176e9ef0.jsonl` | 法句义注中译组——一校 | `zh` | 8,650 |
| `74ebf4c5-c243-4948-955d-6c277e29276a.jsonl` | 云台教理组 | `zh` | 6,686 |
| `331447b6-39bb-4b49-ac10-6206db93a050.jsonl` | 钱玮 | `zh` | 6,350 |
| `3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc.jsonl` | 胜嗣Jinadāyāda | `zh` | 2,659 |

Total raw records inspected: 56,696.

## Raw JSONL Schema

Every valid record has the following fields:

```json
{
  "id": "23-618-162-172",
  "original": "Apica, maraṇāsannakāle ...",
  "translation": "特别是在临死之时...",
  "category": ["añña", "leḍī sayādo", "abhidhamma"],
  "path": ["paramatthadīpanī", "Paramatthadīpanī"]
}
```

| Field | Type | Required in raw data | Meaning |
| --- | --- | --- | --- |
| `id` | string | yes | Segment identifier. Observed form is four numeric parts joined by hyphens, for example `23-618-162-172`. |
| `original` | string | yes | Pali source text. |
| `translation` | string | yes | Chinese translation text. |
| `category` | array of strings | yes | Hierarchical classification such as collection, genre, nikāya, text family, or commentary class. |
| `path` | array of strings | yes | Hierarchical textual path, usually including source file/work title and local section labels. |

## Field Observations

### `id`

- All inspected IDs match the pattern `number-number-number-number`.
- IDs are unique inside each JSONL file.
- IDs are not globally unique across all files. At least 7,874 IDs occur in more than one corpus file.
- Recommendation: never use `id` alone as a primary key. Use `corpus_id + id`.

### `original`

- Contains Pali text, including diacritics.
- Some records include braces around cited lemmas, for example `{Bodhimūle}ti`.
- Some records include embedded references, brackets, and punctuation from source editions.
- Segment length varies widely: short discourse markers and long commentary passages both occur.

### `translation`

- Contains Chinese text with occasional embedded Pali, Sanskrit, or English-like technical notation.
- Many translations include translator notes in parentheses or square brackets.
- Some translations contain escaped newlines, producing multi-line rendered text after JSON parsing.
- Translation style differs by corpus: some are compact, some explanatory, some preserve Pali terms in parentheses.

### `category`

- Always present as an array, but one record has an empty array.
- Observed depth ranges from 0 to 8.
- It is useful for broad filtering, but the levels are not fully normalized across corpora.
- Example values include `sutta`, `aṭṭhakathā`, `ṭīkā`, `abhidhamma`, `khuddakanikāya`, and `visuddhimagga`.

### `path`

- Always present as an array, but one record has an empty array.
- Observed depth ranges from 0 to 8.
- Usually more directly useful than `category` for locating textual context.
- Levels mix machine-like slugs, edition titles, chapter names, and local section numbers.

## Data Quality Notes

Positive findings:

- All inspected lines are valid JSON.
- The field set is consistent across all records.
- Type usage is consistent across all records.
- The corpus is already segment-aligned enough to support pattern extraction.

Known consistency issues:

- One record in `3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc.jsonl` has empty `category` and `path`.
- `id` is locally unique but not globally unique.
- `category` and `path` hierarchy depths vary.
- Translations include inline notes, bracketed supplements, parenthetical Pali terms, and line breaks without separate annotation fields.
- Some source texts repeat across records and corpora, including generic formulae such as `Evaṃ sabbattha.`.
- Different corpora can translate the same `id` differently, which is valuable evidence for translation strategy analysis.

## Current Data Assumptions

- Each JSONL file represents one translation source or channel.
- The filename UUID is the safest current `corpus_id`.
- The repository index provides human-readable corpus names and target language tags.
- The source language is Pali for all records unless future metadata states otherwise.
- Raw records should remain immutable; all normalization and annotation should be stored as derived documentation or generated artifacts.

## Implications for Knowledge Extraction

The corpus should be treated as parallel evidence, not as a translation memory. Repeated IDs and repeated source texts are useful because they expose translator variation. Future extraction should compare:

- same `corpus_id`, neighboring `path` context;
- same `id`, different corpora;
- same or similar `original`, different translations;
- same technical term across genres;
- same grammatical construction across translators.

