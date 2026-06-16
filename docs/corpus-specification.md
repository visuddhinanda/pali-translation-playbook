# Normalized Corpus Specification

This specification proposes a normalized model for future corpus processing,
annotation, and retrieval. It is a derived model; it does not require changing
the raw JSONL files in `translations/`.

## Design Goals

- Preserve raw translation data exactly as received.
- Make corpus identity explicit.
- Separate source segments, translations, annotations, and extraction evidence.
- Support both human research and LLM/RAG workflows.
- Keep enough provenance to trace every knowledge entry back to corpus evidence.

## Layered Model

```text
Layer 1: Parallel Corpus
  Immutable raw translation records and normalized read models.

Layer 2: Translation Patterns
  Reusable correspondences between Pali forms and Chinese rendering choices.

Layer 3: Translation Strategies
  Higher-level translator decisions explaining why a rendering pattern is used.
```

## Entity: Corpus

A corpus represents one JSONL source/channel.

```yaml
corpus:
  corpus_id: "7ac4d13b-a43d-4409-91b5-5f2a82b916b3"
  source_file: "translations/7ac4d13b-a43d-4409-91b5-5f2a82b916b3.jsonl"
  display_name: "法护-Dhammapāla"
  source_language: "pi"
  target_language: "zh"
  translator: "法护-Dhammapāla"
  source_channel: null
  license: null
  record_count: 19345
  notes: []
```

Recommended fields:

| Field | Required | Description |
| --- | --- | --- |
| `corpus_id` | yes | Stable ID. Use the JSONL filename UUID without extension. |
| `source_file` | yes | Relative path to raw JSONL. |
| `display_name` | yes | Name from `translations/index.md`. |
| `source_language` | yes | Usually `pi`. |
| `target_language` | yes | `zh`, `zh-Hans`, or more specific language tag. |
| `translator` | recommended | Translator, group, or channel name when known. |
| `source_channel` | optional | Publication, class, edition, or workflow source. |
| `license` | optional | Corpus license if available. |
| `record_count` | derived | Count from raw JSONL. |
| `notes` | optional | Curatorial notes and caveats. |

## Entity: Translation Unit

A translation unit is one aligned Pali-Chinese segment in one corpus.

```yaml
translation_unit:
  unit_key: "7ac4d13b-a43d-4409-91b5-5f2a82b916b3:23-618-162-172"
  corpus_id: "7ac4d13b-a43d-4409-91b5-5f2a82b916b3"
  unit_id: "23-618-162-172"
  source_text:
    language: "pi"
    text: "Apica, maraṇāsannakāle ..."
  target_text:
    language: "zh"
    text: "特别是在临死之时..."
  context:
    category_path: ["añña", "leḍī sayādo", "abhidhamma"]
    textual_path: ["paramatthadīpanī", "Paramatthadīpanī"]
    previous_unit_key: null
    next_unit_key: null
  metadata:
    raw_line_number: 1
    source_length_chars: 109
    target_length_chars: 42
    has_translator_notes: true
    has_line_breaks: false
```

Recommended key policy:

- `unit_id` preserves the raw `id`.
- `unit_key = corpus_id + ":" + unit_id`.
- Cross-corpus alignment should use `unit_id` as an alignment candidate, not as a primary key.

## Entity: Cross-Corpus Alignment

Use this entity when the same segment appears in multiple corpora.

```yaml
alignment:
  alignment_id: "unit-id:23-618-162-172"
  alignment_type: "shared_unit_id"
  source_unit_id: "23-618-162-172"
  unit_keys:
    - "7ac4d13b-a43d-4409-91b5-5f2a82b916b3:23-618-162-172"
    - "e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:23-618-162-172"
  confidence: 0.9
  notes:
    - "Shared raw ID. Confirm source text before using as strict alignment."
```

Possible `alignment_type` values:

- `shared_unit_id`
- `exact_source_text`
- `near_duplicate_source_text`
- `manual_alignment`
- `same_textual_path`

## Entity: Linguistic Annotation

Annotations should be stored outside the raw corpus.

```yaml
annotation:
  annotation_id: "ann-000001"
  unit_key: "corpus:unit"
  span:
    source_start: null
    source_end: null
    target_start: null
    target_end: null
  type: "terminology"
  label: "sabbaññutañāṇa"
  value:
    source_form: "sabbaññutañāṇa"
    target_form: "一切知智"
    normalized_concept: "omniscience-knowledge"
  evidence:
    pattern_ids: []
    strategy_ids: []
  annotator:
    kind: "human"
    name: null
  confidence: 0.85
  notes: []
```

Supported annotation types:

| Type | Purpose |
| --- | --- |
| `terminology` | Maps Pali terms to Chinese renderings and concept IDs. |
| `grammar` | Marks grammatical constructions such as absolutives, participles, compounds, or passives. |
| `idiom` | Captures idiomatic or formulaic expressions. |
| `sentence_pattern` | Captures larger syntactic templates. |
| `translation_strategy` | Links a unit or span to a strategy such as expansion or reordering. |
| `note` | Stores philological, doctrinal, or editorial comments. |

## Entity: Evidence

Evidence connects derived knowledge to raw corpus observations.

```yaml
evidence:
  evidence_id: "ev-000001"
  unit_key: "corpus:unit"
  source_quote: "Tena vuttaṃ"
  target_quote: "根据以上所述"
  observation: "Discourse marker translated semantically rather than literally."
  supports:
    - "pattern:discourse-tena-vuttam"
    - "strategy:semantic-translation"
  confidence: 0.8
```

## RAG-Oriented Chunking

Recommended retrieval units:

- `translation_unit`: fine-grained lookup for exact evidence.
- `aligned_unit_group`: compare translations for the same unit across corpora.
- `pattern_entry`: reusable translation rule with examples.
- `strategy_entry`: decision-level guidance with risks.
- `concept_entry`: doctrinal or terminological concept card.

Each RAG chunk should include:

- stable ID;
- title;
- category tags;
- source language and target language;
- short summary;
- normalized searchable text;
- evidence unit keys;
- confidence and review status.

## Versioning

Derived artifacts should record:

- raw corpus snapshot date;
- source file checksums when available;
- extraction method;
- model or annotator identity;
- review status.

Recommended review states:

- `draft`
- `machine_generated`
- `human_reviewed`
- `accepted`
- `deprecated`

