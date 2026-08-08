# Nalex — Opus Rendering Handoff

## Precondition

A read-only Claude Code data-QA pass and deterministic local validation have
already been completed.

This does not waive your own integrity gate. Treat the supplied frozen files as
untrusted until you read and validate them in this session.

Authoritative frozen snapshot commit:

`97550f7084e264b72d6fb2cf6be01be694ed9ce9`

## Role

Act only as a constrained visualization renderer.

You are not an analyst, researcher, therapist, editor, coach, or theme
generator. Do not interpret, improve, repair, or expand the source material.

## Required files

Read these project files:

- `CURRENT_STATE_CLEAN.md`
- `index.md`
- `research_prompt_modes/visualization_pipeline.md`
- `research_prompt_modes/viz_schema_template.md`
- `research_prompt_modes/analysis_outputs/nalex_viz_schema.json`
- `visualization_input_manifest.txt`, if available

If any required file is inaccessible, incomplete, malformed, or contradictory,
state the exact file and issue, then stop. Do not claim to have read a file you
cannot access.

If Git metadata or local hashing is available, verify the commit/manifest.
Otherwise state that this verification is unavailable; do not claim it passed.

## Authority

1. `nalex_viz_schema.json` is the exclusive source of rendered content.
2. `CURRENT_STATE_CLEAN.md` is the canonical check source for project state,
   phase boundaries, and stated metrics.
3. `index.md` and `visualization_pipeline.md` define operating rules.
4. `viz_schema_template.md` defines schema fields, valid values, and literal
   rendering semantics.

If sources conflict, report literal values and locations, then stop. Never
silently reconcile or repair a conflict.

## Visualization ideation reference

A prior ideation pass has produced 12 candidate variations across 4 visual
questions, stored at:

`research_prompt_modes/analysis_outputs/nalex_viz_ideation.md`

Read this file after completing the Stage 1 integrity gate.

**This document is a non-authoritative design reference only.** It is not a
rendering specification, not a canonical data source, and not a substitute for
the authority hierarchy above. Treat it as a starting point for your own design
reasoning, not as an instruction to reproduce any variation literally.

Specifically:

- Do not treat any value, label, or metric from the ideation document as
  canonical. Canonical values come exclusively from the sources in §Authority.
- The ranked recommendations (§6 of the ideation document) reflect one prior
  pass's judgment. Apply your own Opus-level reasoning to assess whether those
  rankings hold, whether a higher-ranked alternative exists, or whether a
  documented weakness in a variation disqualifies it given the current schema
  state.
- The schema-readiness table (§5) documents which variations require new
  records. Verify the current state of `nalex_viz_schema.json` against that
  table — it may have been updated since the ideation pass.
- Data-integrity constraints in §0 of the ideation document were verified
  against the inputs at time of writing. Re-verify any constraint that affects
  your chosen variation before rendering.
- If you identify a superior design not in the ideation document, propose it
  with explicit evidence and schema-readiness assessment before rendering.

# Stage 1 — Integrity gate only

Do not design, preview, brainstorm, or create an artifact in this response.

Return:

## Access status

| File | Read | Complete | Issue |
|---|---|---|---|

## Canonical phase table

| Phase | Naomi word count | Alex word count | Source location |
|---|---:|---:|---|

Use only literal values from the canonical source. Do not estimate, calculate,
normalise, or fill missing values.

The only canonical chronological phase labels are:

- `Baseline`
- `Conflict`
- `Silence`
- `Aftermath`

## Schema audit

Validate the JSON against `viz_schema_template.md`, including:

- JSON validity and required fields;
- valid `phase`, `scope`, `detail_label`, `display_instance`, and
  `visual_hint` values;
- valid treatment of `phase: null` corpus records;
- no unsupported duplicate records;
- literal labels, quotes, values, themes, metadata, and units;
- schema consistency with canonical project values where applicable.

For each failure, state artifact key, record identity/index, field, literal
value, violated rule, and source location.

End with exactly one line:

`INTEGRITY GATE: PASS — ready for rendering on explicit instruction.`

or:

`INTEGRITY GATE: FAIL — rendering prohibited.`

If the gate fails, stop.

# Stage 2 — Render only on my next explicit instruction

After a Stage 1 pass, wait for my separate instruction to render.

Create one self-contained responsive HTML artifact:

`nalex_visualization.html`

## Design reasoning (before committing to a variation)

Before rendering, state:

1. Which variation from the ideation document (or a new proposal) you are
   selecting and why, in terms of evidence strength, schema readiness, and
   information gain over the already-published headline.
2. Any ideation-document ranking you are disagreeing with, and the specific
   reason grounded in the current schema or canonical source state.
3. Any new records that must be added to `nalex_viz_schema.json` before
   rendering can proceed honestly, per the schema-readiness table in §5 of
   the ideation document.
4. Which data-integrity constraints from §0 of the ideation document apply
   to your chosen variation and how you will surface them on the artifact face.

Do not proceed to render until this reasoning is stated. If the schema is
missing required records, stop and report what is needed rather than
substituting approximations.

## Rendering boundary

Render exclusively from:

`research_prompt_modes/analysis_outputs/nalex_viz_schema.json`

Use literal schema content only, including:

- values, labels, quotes, themes, metadata, units;
- `phase`, `scope`, `detail_label`, `display_instance`, and `visual_hint`;
- `forward_looking_evaluation` only where it literally exists in the schema.

Use `phase` only for canonical chronological grouping.

Respect `scope` and `detail_label` exactly:

- Phase records belong to their literal canonical phase.
- Session and gap records retain their literal detail label and must not become
  new canonical phases.
- Corpus records with `phase: null` must not be displayed as phase data.
- `display_instance` identifies intentional repeated display records only; it
  must not duplicate, aggregate, or alter a metric.

## Prohibitions

Do not:

- Invent, repair, infer, calculate, convert, aggregate, normalise, rank, or
  fill data.
- Add percentages, averages, totals, differences, ratios, trends, or claims.
- Paraphrase, shorten, correct, merge, or interpret labels, quotes, or themes.
- Add coaching, therapeutic, psychological, causal, or explanatory framing.
- Use canonical-source content to fill a schema omission.
- Show absent/inapplicable metrics as zero unless that exact zero record exists
  in the schema.
- Replace a template-approved `visual_hint` with another visual encoding.
- Reproduce any value from `nalex_viz_ideation.md` directly — render only
  from `nalex_viz_schema.json`.

## Artifact constraints

- Inline CSS and only necessary inline JavaScript.
- No external URLs, libraries, APIs, data fetching, fonts, or data files.
- No hidden derived calculations.
- Accessible contrast, semantic structure, and responsive mobile/desktop layout.
- Readable literal source values and labels.
- Include this exact method note:

  `This artifact renders the supplied schema without deriving new metrics.`

Use existing project templates for style reference only — not as a content source.

## Pre-delivery audit

Before presenting the artifact, verify:

1. Every displayed value, label, quote, theme, and evaluation exists literally
   in the schema.
2. Every visual follows its exact template-defined `visual_hint`.
3. Every record follows its literal `phase`, `scope`, `detail_label`, and
   `display_instance`.
4. No metric was derived, replaced, inferred, converted, or zero-filled.
5. Corpus records are not displayed as chronological phase data.
6. Session/gap labels are not displayed as extra canonical phases.
7. No unsupported analysis or interpretation appears.
8. Rendered canonical phase counts agree with the Stage 1 audit where those
   counts are explicitly available in the schema.

Return only:

1. `nalex_visualization.html`;
2. a concise render audit;
3. limitations or omitted/unrenderable schema fields.

Do not claim the artifact is complete if any verification fails.
