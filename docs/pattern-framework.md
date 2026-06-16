# Translation Pattern Framework

Translation patterns capture reusable Pali-to-Chinese correspondences grounded in
corpus evidence. A pattern is smaller than a general strategy and larger than a
single translation memory pair.

## Purpose

Patterns should answer:

- What source form or construction recurs?
- How is it usually rendered in Chinese?
- Under what conditions does that rendering work?
- What evidence supports the rule?
- When should the rule not be applied?

## Pattern Categories

Recommended initial categories:

- `terminology`
- `syntax`
- `compounds`
- `participles`
- `absolutive_constructions`
- `passive_voice`
- `honorific_expressions`
- `doctrinal_vocabulary`
- `discourse_markers`
- `idiomatic_translation`
- `commentarial_gloss`
- `etymological_explanation`
- `enumeration`
- `quotation_formula`

## Pattern Schema

```yaml
id:
name:
category:
description:

source_pattern:
  language: "pi"
  form:
  normalized_form:
  grammar:
  lexical_triggers:
  structural_template:

translation_pattern:
  language: "zh"
  form:
  normalized_form:
  style:
  transformation:

examples:
  - unit_key:
    source_quote:
    target_quote:
    note:

conditions:
  - 

counter_examples:
  - unit_key:
    source_quote:
    target_quote:
    reason:

recommended_translation:

confidence:
review_status:
related_patterns:
related_strategies:
notes:
```

## Field Definitions

| Field | Meaning |
| --- | --- |
| `id` | Stable pattern ID, preferably human-readable. |
| `name` | Short descriptive label. |
| `category` | One category or a small controlled list. |
| `description` | Research note explaining the pattern. |
| `source_pattern` | Pali trigger: word, phrase, morphology, syntax, or discourse function. |
| `translation_pattern` | Chinese rendering behavior or transformation. |
| `examples` | Positive corpus evidence. |
| `conditions` | Constraints required for valid use. |
| `counter_examples` | Evidence that limits or contradicts the rule. |
| `recommended_translation` | Default recommendation for new translation work. |
| `confidence` | Numeric score or label based on evidence and review. |
| `review_status` | Workflow state such as `draft`, `machine_generated`, or `human_reviewed`. |
| `related_patterns` | Links to narrower, broader, or alternative patterns. |
| `related_strategies` | Links to strategy entries explaining translator decisions. |

## Example: Discourse Marker

```yaml
id: "pattern-discourse-tena-vuttam"
name: "Tena vuttaṃ as citation transition"
category: "discourse_markers"
description: >
  The formula "Tena vuttaṃ" introduces a quoted or summarized statement. Some
  Chinese translations render its discourse function rather than its literal
  instrumental structure.

source_pattern:
  language: "pi"
  form: "Tena vuttaṃ"
  normalized_form: "tena vuttaṃ"
  grammar: "instrumental pronoun + past participle"
  lexical_triggers: ["tena", "vuttaṃ"]
  structural_template: "Tena vuttaṃ [quote or explanation]"

translation_pattern:
  language: "zh"
  form: "根据以上所述"
  normalized_form: "according to what was stated above"
  style: "semantic discourse rendering"
  transformation: "renders connective function, not word-by-word grammar"

examples:
  - unit_key: "e5bc5c97-a6fb-4ccb-b7df-be6dcfee9c43:1-290-2-5"
    source_quote: "Tena vuttaṃ–"
    target_quote: "根据以上所述——"
    note: "Explicitly marks discourse continuation."

conditions:
  - "Use when the phrase introduces a cited verse, explanation, or conclusion."
  - "Prefer functional rendering when literal '因此被说' sounds unnatural."

counter_examples: []

recommended_translation: "根据以上所述；因此说；故说"
confidence: 0.75
review_status: "draft"
related_patterns: []
related_strategies:
  - "strategy-semantic-translation"
notes:
  - "Needs more evidence across corpora before becoming accepted."
```

## Example: Doctrinal Term

```yaml
id: "pattern-term-sabbannutanana"
name: "sabbaññutañāṇa as 一切知智"
category: "doctrinal_vocabulary"
description: >
  The doctrinal compound "sabbaññutañāṇa" is often preserved as a technical
  term in Chinese, sometimes with the Pali form in parentheses.

source_pattern:
  language: "pi"
  form: "sabbaññutañāṇa"
  normalized_form: "sabbaññutañāṇa"
  grammar: "compound noun"
  lexical_triggers: ["sabbaññutañāṇa"]
  structural_template: null

translation_pattern:
  language: "zh"
  form: "一切知智"
  normalized_form: "omniscience knowledge"
  style: "doctrinal terminology"
  transformation: "technical equivalent, optionally with source term retained"

examples:
  - unit_key: "331447b6-39bb-4b49-ac10-6206db93a050:1-348-17-29"
    source_quote: "sabbaññutañāṇampi"
    target_quote: "一切知智(sabbaññutañāṇa)"
    note: "Chinese term plus Pali in parentheses."

conditions:
  - "Use in doctrinal or commentarial contexts."
  - "Retain Pali in parentheses when terminological precision is important."

counter_examples: []

recommended_translation: "一切知智"
confidence: 0.8
review_status: "draft"
related_patterns: []
related_strategies:
  - "strategy-doctrinal-translation"
notes: []
```

## Confidence Guidelines

Use a transparent confidence scale:

| Score | Meaning |
| --- | --- |
| `0.9-1.0` | Strong evidence across corpora, human reviewed. |
| `0.7-0.89` | Repeated evidence, plausible rule, needs more review. |
| `0.5-0.69` | Candidate pattern from limited evidence. |
| `<0.5` | Weak hypothesis or exploratory note. |

Confidence should consider:

- number of supporting examples;
- number of corpora represented;
- genre diversity;
- counter-examples;
- consistency of source form;
- consistency of target rendering;
- human review status.

## Extraction Guidance

Good pattern candidates include:

- repeated Pali terms with stable Chinese equivalents;
- grammatical constructions translated through recurring Chinese structures;
- formulas translated by discourse function;
- bracketed translator supplements that reveal implicit syntax;
- divergent renderings of the same unit across translators;
- commentarial explanations of roots, compounds, or etymology.

Avoid making a pattern when:

- only one example exists and it is not linguistically distinctive;
- the target text is a free paraphrase without clear source alignment;
- the source span is too broad to be reusable;
- the proposed rule is actually a general translation strategy.

