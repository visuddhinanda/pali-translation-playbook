# Future AI Workflow

This document outlines a future workflow for agents that extract translation
patterns and strategies from the Pali-Chinese corpus.

## Operating Principles

- Never modify raw files in `translations/`.
- Treat every extracted rule as a hypothesis until validated against evidence.
- Preserve source provenance for every derived entry.
- Separate corpus reading, linguistic analysis, rule generation, validation, and export.
- Prefer small, reviewable knowledge entries over large opaque summaries.
- For large files, follow `docs/large-file-workflow.md`: programs may scan all data, but each LLM call should receive only a budgeted chunk.

## Workflow Overview

```text
1. Read corpus
2. Identify translation patterns
3. Generate candidate rules
4. Cluster similar rules
5. Build knowledge entries
6. Validate against corpus evidence
7. Export RAG-ready knowledge
```

## Step 1: Read Corpus

Inputs:

- `translations/index.md`
- `translations/*.jsonl`
- optional derived metadata and checksums

Agent responsibilities:

- parse JSONL strictly;
- create `corpus_id` from filename;
- attach display names and language tags from the index;
- preserve `id`, `original`, `translation`, `category`, and `path`;
- create normalized `unit_key = corpus_id + ":" + id`;
- record line numbers and basic text statistics.

Recommended outputs:

- corpus manifest;
- normalized translation unit table;
- cross-corpus alignment candidates by shared `id`;
- exact and near-duplicate source text groups.
- large-file chunk plan with a target data budget such as 20% of model context.

For initial planning, use:

```bash
python scripts/plan_chunks.py translations/3b0cb0aa-ea88-4ce5-b67d-00a3e76220cc.jsonl --max-context 128000 --budget-ratio 0.2 --format markdown
```

## Step 2: Identify Translation Patterns

Candidate signals:

- repeated source lemmas or phrases;
- repeated Chinese equivalents;
- shared IDs with divergent translations;
- parenthetical source terms in target text;
- bracketed supplements in target text;
- common Pali constructions such as absolutives, participles, compounds, passives, and formulas;
- genre-specific terminology in `category` and `path`.

For first-pass collocation discovery, do not constrain the prompt to a short list
of known expressions. The agent should ask the model to discover the most frequent
and most stable collocations in the chunk, then rank candidates with evidence.
Known expressions such as `paccayo`, `vuccati`, `nāma`, or `vā` are valid only for
second-pass validation after open discovery has produced candidates.

Useful comparison modes:

- within one corpus across many contexts;
- across corpora for the same `id`;
- across corpora for exact same `original`;
- across a textual path such as one commentary or chapter;
- across categories such as `abhidhamma`, `aṭṭhakathā`, or `ṭīkā`.

## Step 3: Generate Candidate Rules

Each candidate rule should state:

- source trigger;
- target rendering;
- supporting examples;
- possible category;
- proposed strategy;
- known limitations;
- confidence score.

Agents should avoid asserting a final rule from one example unless the source
form is highly distinctive and the entry is marked as draft.

Candidate rule prompt shape:

```yaml
task: "propose_translation_pattern"
input:
  source_examples:
    - unit_key:
      original:
      translation:
      category:
      path:
expected_output:
  pattern_candidate:
    source_pattern:
    translation_pattern:
    examples:
    conditions:
    counter_examples:
    recommended_translation:
    confidence:
```

Open collocation discovery prompt shape:

```yaml
task: "discover_collocations_open"
instruction:
  - "Do not search only for pre-listed expressions."
  - "Find recurring Pali-Chinese fixed pairings, formulaic phrases, doctrinal combinations, idioms, and repeated translation moves."
  - "Rank candidates by frequency, stability across contexts, and usefulness for future translation."
input:
  chunk_examples:
    - unit_key:
      original:
      translation:
      category:
      path:
expected_output:
  collocation_candidates:
    - source_pattern:
      translation_pattern:
      occurrence_count_in_chunk:
      examples:
      variant_translations:
      conditions:
      confidence:
```

## Step 4: Cluster Similar Rules

Clustering should reduce duplicate or overlapping candidate rules.

Cluster dimensions:

- same source lemma;
- same Pali construction;
- same Chinese rendering;
- same doctrinal concept;
- same strategy label;
- same genre or textual family;
- shared counter-example behavior.

Cluster outputs:

- canonical pattern ID;
- merged description;
- representative examples;
- variant renderings;
- conflict notes;
- review priority.

Important distinction:

- Cluster exact terminology variants together only when concept identity is clear.
- Keep grammatical patterns separate from doctrinal terminology unless evidence shows a stable interaction.

## Step 5: Build Knowledge Entries

Knowledge entries should use the schemas in:

- `docs/pattern-framework.md`
- `docs/strategy-framework.md`
- `docs/corpus-specification.md`

Recommended entry types:

- `pattern_entry`
- `strategy_entry`
- `terminology_entry`
- `concept_entry`
- `evidence_entry`
- `alignment_entry`

Every knowledge entry should include:

- stable ID;
- human-readable name;
- concise description;
- category tags;
- evidence unit keys;
- confidence;
- review status;
- source and target snippets;
- conditions and risks.

## Step 6: Validate Against Corpus Evidence

Validation tasks:

- confirm every example exists in the raw corpus;
- confirm source and target quotes match the cited unit;
- search for counter-examples;
- compare same `id` across corpora;
- test whether the pattern holds outside its original genre;
- mark conflicts and variant translations.

Suggested validation statuses:

- `unvalidated`
- `evidence_checked`
- `counter_examples_checked`
- `human_reviewed`
- `accepted`
- `deprecated`

Evidence thresholds:

| Status | Minimum expectation |
| --- | --- |
| `unvalidated` | Machine-generated candidate only. |
| `evidence_checked` | Positive examples verified in raw corpus. |
| `counter_examples_checked` | Search performed for likely contradictions. |
| `human_reviewed` | Reviewed by a competent Pali-Chinese reader. |
| `accepted` | Stable enough for translator guidance and RAG retrieval. |

## Step 7: Export RAG-Ready Knowledge

RAG exports should be optimized for retrieval and reasoning, not only keyword
matching.

Recommended chunk types:

```yaml
rag_chunk:
  chunk_id:
  chunk_type: "pattern_entry"
  title:
  summary:
  searchable_text:
  source_language: "pi"
  target_language: "zh"
  tags:
  evidence_unit_keys:
  related_ids:
  confidence:
  review_status:
  provenance:
    source_files:
    generated_by:
    generated_at:
```

Retrieval fields:

- source Pali trigger;
- normalized Pali form;
- Chinese equivalent;
- strategy labels;
- grammar labels;
- doctrinal concept labels;
- textual genre;
- examples;
- counter-examples.

## Recommended Agent Roles

Future automation can be split into specialized agents:

| Agent | Responsibility |
| --- | --- |
| Corpus Reader | Parse JSONL, build normalized unit records, detect alignments. |
| Linguistic Annotator | Identify terms, morphology, compounds, and constructions. |
| Pattern Miner | Propose reusable translation patterns from evidence groups. |
| Strategy Analyst | Assign decision-level strategy labels and risks. |
| Validator | Check examples, search counter-examples, score confidence. |
| Knowledge Curator | Merge duplicates, write final entries, manage review status. |
| RAG Exporter | Produce chunked JSON/Markdown optimized for retrieval. |

## Human Review Loop

Machine extraction should feed a human review workflow:

1. Agent proposes candidate pattern.
2. Agent attaches positive and negative evidence.
3. Human reviewer accepts, edits, splits, merges, or rejects.
4. Accepted entries become part of the playbook.
5. Rejected entries remain available as audit history if useful.

## Near-Term Implementation Recommendation

Before building complex extraction code, create small derived artifacts:

- corpus manifest from `translations/index.md`;
- normalized unit sample;
- alignment report for repeated `id` values;
- first manually reviewed pattern entries;
- first manually reviewed strategy entries.

This keeps the project research-first while preparing clean interfaces for
GraphRAG, vector search, and prompt-time retrieval.
