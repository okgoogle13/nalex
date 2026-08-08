# Nalex Visualization Pipeline

## Purpose
Convert canonical Nalex analysis outputs into structured inputs for LLM-generated visual artifacts.

## Rule
Separate analysis from rendering.
- Analysis extracts and normalizes evidence.
- Rendering formats only the provided structure.
- The rendering model must not infer new themes, rewrite evidence, or add analysis.

## Canonical inputs
Prefer these sources:
- `CURRENT_STATE_CLEAN.md`
- `phase_profile.json`
- `conflict_questions_summary.json`
- `NALEX_EVIDENCE_BRIEF_headline_patterns.md`

## Flattened schema
Use a strict table or JSON/YAML structure with fields like:
- theme or pattern
- phase
- scope
- detail_label
- speaker
- metric or value
- evidence quote
- confidence
- linked theme or relation
- visual hint

## Workflow
1. Extract canonical evidence.
2. Flatten into a visualization-ready schema.
3. Choose one visual question per artifact.
4. Render with a constrained prompt.

## Best practices
- Use the simplest chart that answers the question.
- Prefer one theme, one phase question, or one relationship map per artifact.
- Keep interpretation separate unless the artifact is explicitly interpretive.
- Use component-ready records for flashcards or playbooks.
- Use explicit nodes and edges for Mermaid or other graph outputs.

## Rendering prompt rule
The rendering model should behave like a dumb layout engine.
It should only render what is provided and must not invent new structure.

### Final Verification Requirements
8. Canonical phase records are grouped using only the valid canonical phase enum.
9. Records marked `scope: "corpus"` or another template-defined non-phase scope are rendered only as defined by the schema and are not misrepresented as phase data.
10. Where a canonical phase has no applicable schema record for an artifact, it is shown as absent/not applicable only if the schema explicitly encodes that status; otherwise it is omitted and listed in the render audit.

### Validation Checklist
- every `phase` value is either a valid canonical phase or `null` when `scope` is a template-defined non-phase scope;
- every record has a valid `scope`;
- session, gap, and corpus identifiers are stored in their designated detail field;
- phase applicability or non-applicability is explicit where required by the artifact.
