# Nalex Project Index

This index describes the canonical artifacts for Nalex in August 2026 and how agents should use them. This project allows both analysis (describe, compare, interpret) and intervention modeling (prescribe, coach, draft responses, generate repair scripts).

---

## 1. Canonical Analysis Document

- File: `CURRENT_STATE_CLEAN.md`
- Role:
  - Single source of truth for:
    - Phase definitions and boundaries.
    - Primary findings (volume gap, latency, unanswered questions, initiation).
    - Verified corrections, purge description, and artifact status.
    - Phase-wise numeric backbone (baseline comparison audit).
    - Aftermath window summary (July 5+).
    - Conflict question-structure summary.
    - `NALex_PHASE_PROFILE` JSON bundle for Baseline, Conflict, Aftermath (now in `phase_profile.json`).
  - All downstream agents should read this before interpreting the dataset.

Usage notes:
- Do not contradict this document’s phase windows, counts, or corrections.
- When in doubt about a metric, recompute from `events.jsonl` using the definitions in this file.

---

## 2. Interpretive Summaries

- File: `NALEX_EVIDENCE_BRIEF_headline_patterns.md`
- Role:
  - Digestible "why this matters" synthesis and framing aid.
  - Provides quick access to high-value interpretations like effort/closure asymmetry and flat-output correction.
  - Explicitly separates measured evidence from hypotheses.
- Note: This is a legitimate reference file for agents to use for quick framing, while `CURRENT_STATE_CLEAN.md` remains the ledger and canonical source of truth.

---

## 3. Core Data Artifact

- File: `events.jsonl`
- Role:
  - Canonical event stream.
  - Source for all recomputed metrics and profiles.
- Invariants:
  - Join keys: always use `sha256`, never `eid`.
  - Timestamps: fully standardized to strict `YYYY-MM-DD HH:MM:SS` format.
  - Phases:
    - Baseline: 2026-04-01 to 2026-06-22
    - Conflict: 2026-06-23 to 2026-07-05
    - Silence: 2026-07-06 to 2026-07-10
    - Aftermath (canonical): 2026-07-11 to 2026-07-21

---

## 4. Supporting Metrics Artifacts

These are derived from `events.jsonl` and must be treated as read-only summaries.

- `baseline_comparison_audit.json`
- `aftermath_stats.json`
- `gap_stats_out.json`
- `phase_profile.json`

---

## 5. Conflict Question Analysis

- Sources: `conflict_questions.txt`, `conflict_questions_annotated.json`, `conflict_questions_summary.json`
- Role:
  - `conflict_questions.txt` is the raw list of question-bearing turns.
  - `conflict_questions_annotated.json` and `conflict_questions_summary.json` contain the definitive message-level annotation layer and summary stats.
- Note: `conflict_questions_annotated.csv` and `conflict_questions_tags.csv` are maintained as secondary exports, but the JSON files are the primary canonical source.

---

## 6. Conflict Case Studies

- The June 26–27 conflict deep dive is **consolidated into `CURRENT_STATE_CLEAN.md` §8** (Rev 5). Read it there.
- The standalone source file now lives at `_archive/keyboard_warrior_conflict_analysis.md` and is archive-only — do not use it as active source data.

---

## 7. Directory Structure

### 7.1 Canonical / active (usable as source data)

*   **Root `.md`**: `CURRENT_STATE_CLEAN.md`, `NALEX_EVIDENCE_BRIEF_headline_patterns.md`, `index.md`, `claude.md`, `AGENTS.md`.
*   **Root data**: `events.jsonl` (canonical event stream) and the four derived summaries in §4.
*   **Root scripts**: `recompute_harness.py` (metric validation) and `refactor_questions_v2.py` (live annotation generator).
*   `research_prompt_modes/`: the canonical 2-pass + repair-layer + visualization-pipeline prompt architecture and its outputs (§10), including the required visualization stack `visualization_pipeline.md`, `viz_schema_template.md`, and `nalex_gemini_viz_corrective_prompt.md` (§11).
*   `_canonical_strong/`: triaged, single-copy source set for visualization builds — resolves duplicate copies of viz inputs found elsewhere in the repo (§13).

### 7.2 Archive-only (never use as source data)

*   `_archive/`: superseded docs, legacy handover files, older JSON extracts (including the pre-Rev-5 aftermath/prequel dumps), old scripts, and retired prompts. Kept for history only.

### 7.3 Special-purpose (not evidence)

*   `visualisations/`: rendered presentation artifacts (`nalex_playbook_dark_m3.html`, `nalex_patterns_flashcards.html`) plus the viz-pipeline planning docs that feed them (`nalex_viz_ideation.md`, `nalex_viz_canonical_render_spec.md`, `visualization_input_manifest.txt`). For review and demo only — outputs, not sources.
*   `_provenance/`: upstream provenance index over the raw audio pool. Covers purged files by design.
*   `_backup/`: pre-repair backups for forensic recovery only.

---

## 8. Project Rules (For All Agents)

### 8.1 Instruction precedence

1. **Task-specific handoff prompts** override everything else for the current task.
2. **`claude.md`** governs Nalex project analysis behavior, file routing, and the evidence-first project workflow. This is the default for all work in this repository.
3. **`AGENTS.md`** governs the broader general coaching / default relationship mode, and applies **only when explicitly invoked**.

Where `claude.md` and `AGENTS.md` conflict, `claude.md` wins for project analysis tasks.

### 8.2 Required

- Center structural patterns (volume and latency asymmetries, question and answer patterns).
- Respect phase definitions and the data purge constraints.
- Separate observation from interpretation; keep analysis distinct from visualization rendering (§11).
- Use only active files as source data. Archive-only artifacts (§7.2) must not be treated as evidence.

---

## 9. Quick Reference: Phase Labels

- **Baseline** (`baseline_chronic_asymmetry`): higher Naomi volume/questions, slower responses, shared initiation.
- **Conflict** (`conflict_question_inversion`): higher interrogative load, inversion of who gets ignored, dense crossfire.
- **Aftermath** (`aftermath_unilateral_initiation`): Naomi initiates all sessions, increased volume/responsiveness, Alex constrained.

---

## 10. Research Prompts Architecture

- Directory: `research_prompt_modes/`
- Role: Defines the core analytical passes and intervention protocols for the LLM.
- Structure (2-Pass + 1-Layer + Viz Pipeline):
  - `shared_system_prompt.md`: Base system prompt containing canonical constraints.
  - `pass_a_micro_session_audit.md`: (Pass 1) Micro-session audit.
  - `pass_b_macro_participant_profile.md`: (Pass 2) Macro participant profile.
  - `layer_c_repair_protocol.md`: (Layer C) Two-Lane Repair Protocol.
  - `visualization_pipeline.md`: Strict evidence-to-visualization workflow.
  - `viz_schema_template.md`: Flattened schema template for rendering inputs.
  - `nalex_gemini_viz_corrective_prompt.md`: Reusable corrective prompt for Gemini visualization planning.
- Outputs:
  - Located in `research_prompt_modes/analysis_outputs/` (`pass_a_output.md`, `pass_b_output.md`, `layer_c_output.md`).

---

## 11. Visualization Rule

**Visualization inputs must be flattened into a strict schema before rendering.** This is not optional scratch work — it is a required, three-file pipeline in `research_prompt_modes/`, and all three files must be read before producing a visualization:

- `visualization_pipeline.md`: the workflow itself — extract evidence from canonical sources, flatten it, then render. Defines the analysis/rendering separation.
- `viz_schema_template.md`: the flattened schema every visualization input must conform to before rendering (theme/pattern, phase, speaker, metric/value, evidence quote, confidence, linked theme/relation, visual hint).
- `nalex_gemini_viz_corrective_prompt.md`: the corrective prompt to hand a rendering model (e.g. Gemini) so it behaves as a "dumb layout engine" — no inferred themes, no rewritten evidence, no added analysis.

Use canonical sources (§1–§5) to extract evidence, convert into the schema in `viz_schema_template.md`, then render per `visualization_pipeline.md`. Rendering models must not infer new themes, rewrite evidence, or add analysis.

---

## 12. Archive Rule

Move legacy, superseded, or one-off artifacts to `_archive/`.
Keep `_backup/` for recovery only and `_provenance/` for forensic lineage.

---

## 13. Canonical Triage Set (`_canonical_strong/`)

Several visualization-pipeline inputs existed as duplicate copies across the repo (e.g. one in `visualisations/`, another in `research_prompt_modes/` or `research_prompt_modes/analysis_outputs/`). On 2026-08-09 these were triaged and the winning copy of each was placed in `_canonical_strong/` with a provenance note (`CANONICAL TRIAGE NOTE` comment/header/JSON key) recording the original path and why it was kept. Underlying content is unchanged from the source copy — only provenance metadata and, for JSON, unicode-escape normalization were added.

- `_canonical_strong/nalex_mobile_v1_playful.html`: base layout/interaction shell for new visualization builds (strongest mobile-first M3 Expressive dark-mode realization; schema-locked rendering with prefixed `INTERPRETATION` tags).
- `_canonical_strong/viz_schema_template.md`: the §11 schema contract — identical to `research_prompt_modes/viz_schema_template.md` plus the triage note.
- `_canonical_strong/nalex_viz_schema.json`: flattened record set with `forward_looking_evaluation` populated on every record — the primary source of ready-to-use, forward-focused coaching text for rendering.

**Rule:** when building or refining a visualization artifact, read the `_canonical_strong/` copy of each file, not the duplicates in `visualisations/` or `research_prompt_modes/`. Treat non-`_canonical_strong/` copies of these three files as superseded — do not edit them; edit `_canonical_strong/` and, if needed, re-run triage to fold changes back.
