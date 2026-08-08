# Nalex Visualization Schema Template

## Recommended record shape

```json
{
  "theme": "string",
  "phase": "Baseline | Conflict | Silence | Aftermath | null",
  "scope": "phase | session | gap | corpus",
  "detail_label": "string | null",
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
  "visual_hint": "timeline | bar | heatmap | network | cards | table",
  "forward_looking_evaluation": "string"
}
```

## Notes
- `phase` must be `null` only for valid non-phase records (e.g. `scope: "corpus"`).
- `detail_label` must contain the exact literal identifier (e.g. "Aftermath_Session_1") when applicable, otherwise `null`.
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
  "scope": "phase",
  "detail_label": null,
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
  "visual_hint": "timeline",
  "forward_looking_evaluation": "Reframing this initiation drive into a mutually agreed check-in cadence could prevent burnout."
}
```

### Conflict question record
```json
{
  "theme": "retrieval_vs_proof_deadlock",
  "phase": "Conflict",
  "scope": "phase",
  "detail_label": null,
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
  "visual_hint": "network",
  "forward_looking_evaluation": "Separating genuine requests for information from defensive boundary setting is required to break the deadlock."
}
```
