# Corrective Prompt for Gemini 3.1 Pro

Fix the pipeline.

1. Source only canonical inputs:
- `CURRENT_STATE_CLEAN.md`
- `phase_profile.json`
- `conflict_questions_summary.json`
- `NALEX_EVIDENCE_BRIEF_headline_patterns.md`

2. Flatten first.
Convert source material into strict JSON/YAML/table records with only:
- theme/pattern
- phase
- speaker
- metric/value
- evidence quote
- confidence
- linked theme/relation

3. Separate evidence from interpretation.
- Keep metrics and short evidence spans in the payload.
- Remove long narrative analysis from render inputs.
- Only include interpretation if the artifact is explicitly an interpretive visual.

4. Render second.
Use a dumb layout-engine prompt:
- do not infer new themes
- do not add analysis
- do not rewrite evidence
- only render what is provided

Rules:
- One visual question per artifact.
- Use the simplest chart that answers it.
- Prefer timeline, bar/heatmap, or node-link only when directly justified.
- For flashcards/playbooks, use component-ready records, not prose.
- For Mermaid/graph outputs, provide explicit nodes, edges, and labels.

Do not ask the model to decide the presentation. Define the schema first, then render it exactly.
