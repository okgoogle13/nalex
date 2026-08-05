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
