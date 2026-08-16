# Visualization Readiness Contract

This policy dictates the gating requirements before any visualization or artifact generation can occur.

## Core Rules

1. **Approved Inputs Only:** Visualization ideation and rendering may begin *only* from approved, explicitly bounded inputs (the projection layer). 
2. **No Direct Raw Renders:** Raw evidence (`events.jsonl`) cannot be rendered directly into artifacts.
3. **Proposed is Not Viz-Ready:** `private_proposed` records (e.g., pilots pending review) are not viz-ready and must not be used for artifact creation.
4. **Canonical is Not Renderable:** `canonical_private` records contain sensitive rationales, full unredacted quotes, and analyst uncertainty. They are not automatically renderable.
5. **Projection Layer Mandate:** A projection layer must exist between semantic records and any artifact. All rendering must pull from this projection layer, which enforces privacy, redacts names, and filters non-shareable fields.
6. **Reflective Artifact Requirements:** Reflective artifacts require specific structures: `evidence_samples`, `source_limits`, `observation_summary`, `reflection_prompts`, and `counterevidence_or_limits`. They cannot be generated from mechanical metric-centric schemas.
7. **Speaker Confidence is Non-Gating:** Raw `speaker_conf` is uninterpreted metadata and must not be treated as a validated probability or as a standalone eligibility threshold for rendering.
