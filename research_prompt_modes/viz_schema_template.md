# Nalex Visualization Schema Template

## Recommended record shape

```json
{
  "theme": "string",
  "phase": "Baseline | Conflict | Silence | Aftermath",
  "speaker": "Naomi | Alex | both | mixed",
  "metric": {
    "name": "string",
    "value": "number|string",
    "unit": "string"
  },
  "evidence_quote": "string",
  "confidence": "low | medium | high",
  "linked_theme": "string|null",
  "relation_type": "supports | contrasts | repeats | escalates | repairs | diverges",
  "visual_hint": "timeline | bar | heatmap | network | cards | table"
}
```

## Notes
- Keep each record small and auditable.
- Prefer one visual question per artifact.
- Do not mix long narrative interpretation into the rendering payload.
- Add interpretation only when the artifact is explicitly meant to visualize interpretation.

## Examples

### Phase asymmetry record
```json
{
  "theme": "unilateral_initiation",
  "phase": "Aftermath",
  "speaker": "Naomi",
  "metric": {
    "name": "sessions_initiated",
    "value": 5,
    "unit": "count"
  },
  "evidence_quote": "Naomi initiates all Aftermath sessions.",
  "confidence": "high",
  "linked_theme": "emotional_overfunctioning",
  "relation_type": "supports",
  "visual_hint": "timeline"
}
```

### Conflict question record
```json
{
  "theme": "retrieval_vs_proof_deadlock",
  "phase": "Conflict",
  "speaker": "both",
  "metric": {
    "name": "genuine_unanswered_questions",
    "value": 12,
    "unit": "count"
  },
  "evidence_quote": "Questions function as rhetorical crossfire rather than information-seeking.",
  "confidence": "high",
  "linked_theme": "question_inversion",
  "relation_type": "escalates",
  "visual_hint": "network"
}
```
