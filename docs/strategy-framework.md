# Translation Strategy Framework

Translation strategies describe decision-level approaches used by translators.
They explain why a pattern may be literal, explanatory, reordered, expanded, or
adapted to doctrinal convention.

## Strategy Schema

```yaml
id:
name:
definition:
when_used:
examples:
  - unit_key:
    source_quote:
    target_quote:
    explanation:
risks:
signals:
related_patterns:
confidence:
review_status:
```

## Strategy Catalog

### Literal Translation

```yaml
id: "strategy-literal-translation"
name: "Literal translation"
definition: "Preserves the visible lexical and syntactic structure of the Pali as much as Chinese allows."
when_used:
  - "The Pali structure is simple and maps naturally into Chinese."
  - "Technical precision is more important than fluency."
  - "The translator wants readers to see the source structure."
risks:
  - "Can produce unnatural Chinese."
  - "Can obscure implied relations if Pali syntax is compressed."
  - "Can mislead when idioms are translated word by word."
signals:
  - "Close word order."
  - "Minimal added explanation."
  - "Frequent preservation of source terms."
```

### Semantic Translation

```yaml
id: "strategy-semantic-translation"
name: "Semantic translation"
definition: "Renders the meaning or discourse function of the Pali rather than its surface form."
when_used:
  - "A literal rendering would be awkward or misleading."
  - "The Pali phrase functions as a discourse marker, idiom, or formula."
  - "Chinese readability is important."
risks:
  - "May hide grammatical features useful for study."
  - "May flatten doctrinal nuance."
  - "May over-interpret ambiguous source text."
signals:
  - "Chinese target is natural but not word-for-word."
  - "Connectives and formulae are rendered functionally."
```

### Explanatory Translation

```yaml
id: "strategy-explanatory-translation"
name: "Explanatory translation"
definition: "Adds explicit information to clarify grammar, reference, doctrine, or context."
when_used:
  - "The source relies on implicit context."
  - "A compound or doctrinal term needs unpacking."
  - "The target audience includes learners or researchers."
risks:
  - "Can mix translation with commentary."
  - "Can make later alignment harder."
  - "Can introduce interpretation not present in the source."
signals:
  - "Bracketed supplements."
  - "Parenthetical Pali or explanatory glosses."
  - "Target text significantly longer than source-equivalent literal rendering."
```

### Doctrinal Translation

```yaml
id: "strategy-doctrinal-translation"
name: "Doctrinal translation"
definition: "Uses established Buddhist Chinese terminology to preserve doctrinal precision."
when_used:
  - "The Pali term has a recognized Buddhist Chinese equivalent."
  - "The passage discusses Abhidhamma, commentarial doctrine, or technical categories."
  - "Consistency across the knowledge base matters."
risks:
  - "Classical terms may be opaque to modern readers."
  - "Different Buddhist traditions may prefer different equivalents."
  - "Doctrinal equivalence can be asserted too early."
signals:
  - "Stable technical terms such as 一切知智."
  - "Pali retained in parentheses."
  - "Concept-level consistency across passages."
```

### Context-Driven Translation

```yaml
id: "strategy-context-driven-translation"
name: "Context-driven translation"
definition: "Chooses the target rendering based on local textual, doctrinal, or narrative context."
when_used:
  - "A Pali term has several valid Chinese equivalents."
  - "The same form behaves differently across genres."
  - "Nearby context resolves an otherwise ambiguous relation."
risks:
  - "Requires strong contextual evidence."
  - "Can reduce term consistency."
  - "Can be hard for automated systems to reproduce."
signals:
  - "Different renderings for the same lemma across contexts."
  - "Use of surrounding path/category metadata in notes."
```

### Omission

```yaml
id: "strategy-omission"
name: "Omission"
definition: "Leaves a source element untranslated when it is redundant, formulaic, or unnatural in Chinese."
when_used:
  - "The omitted element is discourse padding."
  - "Chinese grammar already implies the relation."
  - "A repeated formula would distract from readability."
risks:
  - "Can lose doctrinal or grammatical detail."
  - "Can make source-target alignment incomplete."
  - "Can hide repeated rhetorical structures."
signals:
  - "No target equivalent for a visible source token."
  - "Short target text for a longer source segment."
```

### Expansion

```yaml
id: "strategy-expansion"
name: "Expansion"
definition: "Adds target-language material to make implicit Pali relations explicit."
when_used:
  - "Pali compounds require unpacking."
  - "Ellipsis must be resolved for Chinese readers."
  - "Doctrinal categories need explanatory wording."
risks:
  - "Can over-specify ambiguity."
  - "Can blur the boundary between translation and annotation."
  - "Can make extracted examples noisy."
signals:
  - "Bracketed additions."
  - "Chinese target is much longer than expected."
  - "Explicit subjects, objects, or causal links added."
```

### Reordering

```yaml
id: "strategy-reordering"
name: "Reordering"
definition: "Changes source order to produce grammatical or idiomatic Chinese."
when_used:
  - "Pali modifiers or clauses precede/follow in a way that is unnatural in Chinese."
  - "Long compounds need head-final or head-initial adjustment."
  - "Cause, condition, or result must be made clear."
risks:
  - "Can make phrase-level alignment harder."
  - "Can accidentally change emphasis."
  - "Can obscure rhetorical order."
signals:
  - "Target order differs from source order."
  - "Chinese groups modifiers around a different head."
```

## Relationship Between Strategies and Patterns

A strategy is not itself a reusable source-target rule. A strategy explains a
translator decision that may appear in many patterns.

Examples:

- A `discourse_markers` pattern may use `semantic_translation`.
- A `doctrinal_vocabulary` pattern may use `doctrinal_translation`.
- A `compounds` pattern may use `expansion` and `reordering`.
- A `passive_voice` pattern may use `semantic_translation` if Chinese avoids explicit passive marking.

## Annotation Guidance

Annotate strategy at the smallest useful span:

- unit-level when the whole sentence is paraphrased;
- phrase-level when only one construction is expanded or reordered;
- term-level when a doctrinal equivalent is selected.

A strategy annotation should include evidence, not only a label. For example:

```yaml
strategy_annotation:
  strategy_id: "strategy-expansion"
  unit_key: "corpus:unit"
  source_span: "pajānaṃ sattānaṃ pati"
  target_span: "作为有情（pajā）的主人（pati）"
  rationale: "The compound relation is unpacked with an explicit explanatory phrase."
  confidence: 0.8
```

