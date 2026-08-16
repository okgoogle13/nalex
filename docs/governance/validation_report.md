# Validation Report

## Access Check Result
All required files were successfully accessed, adhering to the modified requirement (`claude.md` was used as the mandate proxy instead of `AGENTS.md`).

## Schema Compliance Result
- **Overall**: No structural violations were identified in this pass of `loop_house_visit_001.proposed.json`; the structure appears to align with schema intent and required rules based on this review, however minor structural normalizations were required.
- **Normalizations applied**: 
  - In Event 2, `need_or_boundary` was `null`. This was normalized to an explicit empty object `{ "content": null, "basis": "none", "evidence_reference": null, "uncertainty_note": null }` to comply with the structured schema rules.
  - Added an empty `interpretation` block (e.g. `"interpretation_tags": []`) to Event 1 and Event 2 since the schema defines the property structurally, even if optional tags are omitted.

## Field Drift or Naming Issues
- The pilot JSON correctly implements the v2 schema names. No unknown fields, legacy metric carryovers, or drifted naming conventions were found.

## Enum/Value Issues
- **`events.observation.direct_response_status`**: Enums used (`not_applicable`, `partly_addresses_prior_concern`) are present in the schema values and appear correctly applied.
- **`events.coding_metadata.coded_by`**: Set to `ai_proposed_pending_human_review`, matching the allowed enum.
- No invalid enum values were identified anywhere in the schema tree in this pass.

## Interpretive Leakage Risks
- **Risk Assessment**: Assessed low in this pilot, pending human review. The `observable_moves` coding relies heavily on `states_explicit_concern_or_boundary`, `uses_heightened_or_confrontational_language`, and `responds_to_concern_with_explanation_of_intent`, which do not in themselves assert hidden motives.
- **Integrity Note**: Event 2 (`G181`) contains an acknowledgement (`rejection's not nice`), which the coder isolated from intent and noted the ambiguity, declining to characterise the acknowledgement as sincere or otherwise — consistent with the schema's observation/interpretation separation requirement.

## Privacy/Display-Control Risks
- **Risk Assessment**: High if rendered automatically.
- **Artifact Controls**: The pilot correctly tags `events.artifact_controls.privacy_level` as `private_evidence` and `display_mode` as `private_only` for both events due to swearing (e.g., "fucking music") and voice transcript ambiguity.

## Fitness
- **Private Schema Testing**: The pilot appears suitable for private schema testing based on structural review. It demonstrates the separation between `observation` and `interpretation` and the `evidence_integrity` flagging is present and appears correctly applied without defaulting back to word-count or latency metrics.
- **Shareable Artifact Generation**: The pilot is currently **UNFIT** for shareable artifact generation. It must not be rendered into a shared visualization view until `requires_audio_review` is manually cleared and `privacy_level` is shifted to `shareable_paraphrase`.

## Null-State Convention Note (G181 — pending schema rule review)
The G181 `need_or_boundary` object currently uses `basis: "none"` as the canonical convention for the null-state of this structured optional object (i.e., no boundary was expressed in this event). This usage was established prior to the null-state handling rules added to `nalex_semantic_schema_v2.md` in schema governance change set 2026-08-14. The record's use of `basis: "none"` has not been changed in this pass. A human decision is required to confirm whether `basis: "none"` maps to `none` (reviewed — no relevant content found) under the new rules, and whether any other sub-fields require state updates. See `schema_governance_change_log.md` Change 5.
