# Project State and Layer Contract

## Objective
This document defines the working layers of the Nalex repository, what files belong in each tier, the flow of data between layers, and the current status of existing files. This structure ensures a safe, evidence-first approach that separates raw facts from private analysis and public rendering.

## 1. raw_evidence
- **Definition:** The immutable source of truth containing transcription data and raw excerpts.
- **Files:** `_canonical_strong/data/event_logs/events.jsonl`
- **Flow:** Read-only. May be ingested by downstream layers but must not be modified or reinterpreted directly during analysis.
- **Forbidden:** No artifact or projection generation reads directly from here for rendering. No editing.

## 2. proposed_private_records
- **Definition:** Newly coded semantic records or pilots that have not passed full integrity or human review.
- **Files:** Files in `./data/semantic_schema/proposals/` and `./data/semantic_schema/pilots/` (e.g., `loop_reassurance_001.proposed.json`).
- **Flow:** Must pass review gates (audio review, privacy clearance, vocabulary alignment) before merging into canonical records.
- **Forbidden:** Not viz-ready. Cannot be rendered into artifacts.

## 3. canonical_private_records
- **Definition:** Verified, approved semantic records (the system of record for analysis).
- **Files:** `./data/semantic_schema/canonical_loop_records.json`
- **Flow:** Feeds into the projection layer.
- **Forbidden:** Not automatically renderable. Contains private rationales, unredacted names, and vulnerability that must not appear in shareable artifacts.

## 4. schema_and_governance
- **Definition:** The rules, definitions, contracts, and audit trails governing the semantic structure.
- **Files:** `nalex_semantic_schema_v2.md`, `schema_manifest.json`, `schema_governance_change_log.md`, `integrity_audit.md`, and contracts.
- **Flow:** Informs the structure of pilots and canonical records.
- **Forbidden:** No evidence data is stored here.

## 5. viz_ready_projections
- **Definition:** Stripped, de-identified structural representations derived from canonical records, safe for visualization.
- **Files:** Expected in `./data/semantic_schema/projections/`. (e.g. `nalex_viz_projection_contract.json`)
- **Flow:** Created from `canonical_private_records`. Feeds into `viz` artifact rendering.
- **Forbidden:** Must exclude raw names, unreviewed private rationale, full source excerpts, and private uncertainty notes.

## 6. reflective_schema
- **Definition:** Specialized data shapes built for constructive, bounded reflection and artifact bundling.
- **Files:** Expected in `./data/semantic_schema/reflective/`. (e.g. `nalex_reflective_schema_contract.json`)
- **Flow:** Provides the content-structure for reflective artifacts based on safely projected data.
- **Forbidden:** No diagnostic inferences or uncited claims.

## 7. artifact_outputs
- **Definition:** The final rendered output files (e.g., HTML views, SVGs).
- **Files:** `./visualisations/` (legacy), `./artifacts/viz/`, `./artifacts/reflective/`, `./artifacts/archive/`.
- **Flow:** End of pipeline. Reads only from projections/reflective schemas.
- **Forbidden:** Artifacts do not generate new analytical claims or feed back into canonical records.

## Current File Status
- **events.jsonl:** Stable, read-only (`raw_evidence`).
- **canonical_loop_records.json:** Active, holds one approved record (`loop_house_visit_001`) (`canonical_private_records`).
- **loop_reassurance_001.proposed.json:** Pending review (`proposed_private_records`).
- **nalex_viz_schema.json (in visualisations/schemas):** Legacy schema. It is metric-centric, evidence-thin, and unsuitable for reflective artifact creation. Retained strictly for legacy visualization backward compatibility. Do not destructively rewrite it.
