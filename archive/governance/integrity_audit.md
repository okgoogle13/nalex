# Nalex Semantic Schema — Integrity Audit

**Audit date:** 2026-08-14  
**Auditor:** Antigravity (read-only pass)  
**Audit scope:** `data/semantic_schema/` infrastructure files only  
**Events.jsonl path confirmed:** `_canonical_strong/data/event_logs/events.jsonl` (378 events)

---

## 1. Access and Approved Mandate Basis

### File Availability

| Mandatory File | Status | Notes |
|---|---|---|
| `./claude.md` | ✅ Present | 194 lines, 16760 bytes |
| `./data/semantic_schema/canonical_loop_records.json` | ✅ Present | 187 lines, 9391 bytes |
| `./data/semantic_schema/schema_manifest.json` | ✅ Present | 147 lines, 4311 bytes |
| `./data/semantic_schema/validation_report.md` | ✅ Present | 31 lines, 2862 bytes |
| `./data/semantic_schema/tasks.md` | ✅ Present | 16 lines, 1802 bytes |
| `./data/semantic_schema/pilots/loop_house_visit_001.proposed.json` | ✅ Present | 176 lines, 8809 bytes |

**All mandatory files are present. No gaps to report.**

### Mandate Basis

`AGENTS.md` does not exist in this repository. Per explicit user authorization recorded in the audit prompt, **`./claude.md` is the approved mandate proxy for this run.** This is not treated as an error. The relevant governing rules drawn from `claude.md` for this audit are:

- Core stance: evidence-first, bounded language, observation separated from interpretation (`claude.md` §"Core stance")
- No unsupported motives, diagnoses, or predictions (`claude.md` §"Final check")
- No-git constraint: `shasum`, `wc`, `grep`, `stat` used instead of git commands (`claude.md` §"Environment constraints")
- Corpus files are read-only (`claude.md` §"Environment constraints")

---

## 2. Exact Normalization Change Log

**Comparison:** `canonical_loop_records.json` (canonical) vs `pilots/loop_house_visit_001.proposed.json` (proposed pilot)

### Structural Differences

#### DIFF-01 — Top-level wrapper object

| Location | canonical_loop_records.json | loop_house_visit_001.proposed.json |
|---|---|---|
| Root structure | Array `[{...}]` — loop fields at top level of the single record object | Object `{"loop": {...}, "events": [...]}` — explicit `loop` key wrapping header fields |

**Classification:** Lossless structural normalization. The proposed pilot introduces an explicit `loop` namespace key to separate loop-header fields from the `events` array. The canonical record merges both at the same object level inside an array. No field values differ as a result of this restructuring.

#### DIFF-02 — `need_or_boundary` in Event 2 (G181)

| Location | canonical_loop_records.json | loop_house_visit_001.proposed.json |
|---|---|---|
| `events[1].observation.need_or_boundary` | Explicit object: `{"content": null, "basis": "none", "evidence_reference": null, "uncertainty_note": null}` | `null` (bare null) |

**Classification:** Lossless structural normalization. The canonical record expanded a bare `null` into a structured null-object with all sub-fields present and nulled. No substantive data was changed; the meaning ("no boundary expressed in this event") is identical. The canonical form is more schema-conformant as it preserves the sub-field shape.

#### DIFF-03 — `interpretation` block in Event 1 (G042)

| Location | canonical_loop_records.json | loop_house_visit_001.proposed.json |
|---|---|---|
| `events[0].interpretation` | Present as `{"interpretation_tags": []}` | **Absent** (field does not exist in proposed) |

**Classification:** Lossless structural normalization. The canonical record added the `interpretation` block with an empty array to preserve the schema's structural expectation that the block exists even when no tags are present. No data was added or changed.

#### DIFF-04 — `interpretation` block in Event 2 (G181)

| Location | canonical_loop_records.json | loop_house_visit_001.proposed.json |
|---|---|---|
| `events[1].interpretation` | Present as `{"interpretation_tags": []}` | **Absent** (field does not exist in proposed) |

**Classification:** Same as DIFF-03. Lossless structural normalization.

### Summary Table

| # | Field Path | Change Type | Classification |
|---|---|---|---|
| DIFF-01 | Root structure | Proposed uses `loop` wrapper key; canonical merges at root | Lossless structural normalization |
| DIFF-02 | `events[1].observation.need_or_boundary` | Null → explicit null-object with typed sub-fields | Lossless structural normalization |
| DIFF-03 | `events[0].interpretation` | Absent → `{"interpretation_tags": []}` | Lossless structural normalization |
| DIFF-04 | `events[1].interpretation` | Absent → `{"interpretation_tags": []}` | Lossless structural normalization |

**No field renames, enum changes, deleted substantive fields, changed values, or potentially substantive changes were identified.**

---

## 3. Schema and Enum Compliance

### Enum Values Present in the Pilot

| Field Path | Value Used | Assessment |
|---|---|---|
| `events[0].observation.direct_response_status` | `not_applicable` | ✅ Valid |
| `events[1].observation.direct_response_status` | `partly_addresses_prior_concern` | ✅ Valid |
| `events[0].coding_metadata.coded_by` | `ai_proposed_pending_human_review` | ✅ Valid |
| `events[1].coding_metadata.coded_by` | `ai_proposed_pending_human_review` | ✅ Valid |
| `events[0].coding_metadata.coding_review_status` | `proposed` | ✅ Valid |
| `events[1].coding_metadata.coding_review_status` | `proposed` | ✅ Valid |
| `events[0].artifact_controls.display_mode` | `private_only` | ✅ Valid |
| `events[1].artifact_controls.display_mode` | `private_only` | ✅ Valid |
| `events[0].observation.need_or_boundary.basis` | `constrained_paraphrase` | ✅ Valid |
| `events[1].observation.need_or_boundary.basis` | `none` (canonical) / null (proposed) | ✅ Equivalent |
| `loop.loop_outcome` | `response_provided` | ✅ Valid |
| `loop.repair_response_status` | `unclear` | ✅ Valid |
| `loop.boundary_confidence` | `medium` | ✅ Valid |

### Observable Move Codes

| Code | Event | Assessment |
|---|---|---|
| `states_explicit_concern_or_boundary` | G042 | ✅ Controlled vocabulary, observational |
| `uses_heightened_or_confrontational_language` | G042 | ✅ Controlled vocabulary, observational |
| `contests_stated_account` | G181 | ✅ Controlled vocabulary, observational |
| `responds_to_concern_with_explanation_of_intent` | G181 | ✅ Controlled vocabulary, observational |
| `acknowledges_impact_of_action` | G181 | ✅ Controlled vocabulary, observational |

No codes asserting motive, diagnosis, or psychological state were used. No unknown, invalid, or legacy enum values identified anywhere in the schema tree.

---

## 4. Privacy and Visualization-Safety Audit

### Fields Marked `viz_safe: true` or `shareable_safe: true`

| Field | viz_safe | shareable_safe | Assessment |
|---|---|---|---|
| `loop.interaction_loop_id` | true | true | ✅ Synthetic ID only. No content risk. |
| `loop.semantic_loop_label` | true | true | ⚠️ FLAG-01 |
| `loop.participants` | true | true | ⚠️ FLAG-02 |
| `loop.core_topic` | true | true | ⚠️ FLAG-03 |
| `loop.loop_start_event_id` | true | true | ✅ Reference ID only. |
| `loop.loop_end_event_id` | true | true | ✅ Reference ID only. |
| `loop.loop_outcome` | true | true | ✅ Neutral enum. Safe. |
| `loop.repair_response_status` | true | true | ✅ Neutral enum (`unclear`). Safe. |
| `loop.boundary_confidence` | true | true | ✅ Analytic confidence metric. Safe. |
| `events.observation.observable_moves` | true | true | ✅ Controlled-vocabulary codes only. Safe. |
| `events.observation.need_or_boundary` | true | true | ⚠️ FLAG-04 |
| `events.coding_metadata.coding_review_status` | true | true | ✅ Status tracker enum. Safe. |
| `events.artifact_controls.privacy_level` | true | true | ✅ Driver field, not content. Safe. |

### Flags

**FLAG-01 — `loop.semantic_loop_label` marked `shareable_safe: true`**

Current value: `"House Visit Boundary and Intent"`  
Risk: Names the topic of a private interpersonal dispute. While not directly quoting either participant, it is substantive enough to identify the nature of a private conflict to a third party.  
Assessment: Potentially shareable-unsafe without context stripping. The manifest requires `human_review_required: true`, which partially mitigates this, but the `shareable_safe: true` designation may be premature. The label should be reviewed before any third-party distribution. **Not a blocker for private use.**

**FLAG-02 — `loop.participants` marked `shareable_safe: true` with `human_review_required: false`**

Current value: `["Naomi", "Alex"]`  
Risk: Real first names of real people in a private interpersonal dispute. The manifest does not require human review for this field before shareable designation applies.  
Assessment: **Privacy concern.** First names combined with a semantic label and event excerpts in a shared artifact become identifying. The `human_review_required: false` designation is inconsistent with the sensitivity of this project. This field should not appear in any artifact destined for a third party without explicit consent from both participants.  
Recommended action (human decision required): Set `human_review_required: true` for `loop.participants`.

**FLAG-03 — `loop.core_topic` marked `shareable_safe: true`**

Current value: `"Unprompted house visit, closed doors, and resulting discomfort"`  
Risk: Contains a contextual claim about another person's behavior ("unprompted"), a characterization of events ("closed doors"), and an attributed emotional response ("resulting discomfort"). G181 contains a competing account of these events, making "unprompted" a contested framing rather than a neutral descriptor.  
Assessment: Interpretive leakage risk if rendered before review. The manifest's own note acknowledges the risk ("Must not contain triggering specifics without review") but the boolean `shareable_safe: true` could be read as blanket clearance by a downstream consumer. Recommended action: Default `shareable_safe` to `false` for all fields where `human_review_required: true`, flipping only after review completes.

**FLAG-04 — `events.observation.need_or_boundary` marked `shareable_safe: true` — sub-field gap**

The `uncertainty_note` sub-field within `need_or_boundary` contains: `"Paraphrased from stated grievances; boundary is articulated retrospectively rather than as a forward-looking rule."` This is interpretive framing that goes beyond observation. The field-level `shareable_safe: true` classification in `schema_manifest.json` applies to `events.observation.need_or_boundary` as a category but `uncertainty_note` is not separately enumerated and has no independent privacy classification.  
Assessment: If `need_or_boundary` is rendered as a unit (including sub-fields), `uncertainty_note` could leak interpretive framing. Recommended action: Add `uncertainty_note` as a separately classified sub-field in `schema_manifest.json` marked `shareable_safe: false`.

### Fields Correctly Marked Private (No Flags)

- `events.source.minimal_redacted_excerpt` — correctly private; contains raw statements including profanity and vulnerability
- `events.evidence_integrity.requires_audio_review` — correctly private; must block shareable generation when `true`
- `loop.boundary_rationale` — correctly private; analyst reasoning notes
- `loop.intervening_events_note` — correctly private; analyst reasoning about excluded events
- `events.interpretation.interpretation_tags` — correctly private; high interpretive leakage risk acknowledged

---

## 5. Interpretive-Leakage Audit

**Source:** `validation_report.md`

### Flagged Language

**LEAK-01 — Line 7: "strongly aligns"**

> "The `loop_house_visit_001.proposed.json` structure **strongly aligns** with the schema intent and required rules"

Classification: **Unsupported certainty.** "Strongly aligns" implies a comprehensive verification pass was completed. This report is itself AI-generated. Bounded alternative: "no structural violations were identified in this pass" or "appears to align with schema intent based on this review."

**LEAK-02 — Line 21: "Low in this pilot" (flat risk designation)**

> "**Risk Assessment**: Low in this pilot."

Classification: **Unsupported certainty.** The flat "Low" designation without caveat that this is an AI assessment pending human review may be read as a definitive clearance. Bounded alternative: "assessed low, pending human review."

**LEAK-03 — Line 22: "manipulative" introduced as a framing**

> "the coder correctly isolated from intent and noted the ambiguity, avoiding assumptions about whether the acknowledgement was **manipulative** or earnest."

Classification: **Interpretive leakage.** The word "manipulative" is not present in the coded record, is not supported by observable-move evidence, and violates the `claude.md` prohibition on inferring unsupported motives (`claude.md` §"Core stance"). The audit introduces a motive frame that the record itself deliberately withheld. The description of coding approach should not introduce motive frames absent from the source data.

**LEAK-04 — Line 29: "highly fit" / "makes excellent use"**

> "The pilot is **highly fit** for private testing. It accurately demonstrates the difference between `observation` and `interpretation` and **makes excellent use** of `evidence_integrity` flagging..."

Classification: **Unsupported certainty / self-endorsement.** An AI-generated validation report should not use evaluative superlatives about an AI-generated pilot record. This implies independent verification that did not occur. Bounded alternatives: "appears suitable for private testing based on structural review" and "the `evidence_integrity` flagging is present and appears correctly applied."

**LEAK-05 — Line 30: "UNFIT" for shareable generation**

> "The pilot is currently **UNFIT** for shareable artifact generation."

Classification: **Appropriate. No flag.** This is a safety-strengthening statement correctly tracking that `requires_audio_review: true` blocks shareability.

### Summary

| ID | Location | Issue | Classification |
|---|---|---|---|
| LEAK-01 | validation_report.md L7 | "strongly aligns" — implies complete verification | Unsupported certainty |
| LEAK-02 | validation_report.md L21 | "Low" without AI caveat | Unsupported certainty |
| LEAK-03 | validation_report.md L22 | "manipulative" not present in source, motive inference | Interpretive leakage |
| LEAK-04 | validation_report.md L29 | "highly fit", "makes excellent use" — self-endorsing superlatives | Unsupported certainty |
| LEAK-05 | validation_report.md L30 | "UNFIT" — correct safety designation | No flag |

---

## 6. Candidate-Loop Existence Check

**Source:** `tasks.md`  
**Events.jsonl confirmed path:** `_canonical_strong/data/event_logs/events.jsonl` (378 events)  
**Method:** `grep -c '"eid": "<ID>"'` — reports count per event ID; all returned 1

### Candidate 1: Guilt and Reassurance

| Event ID | Claimed Speaker | Exists in events.jsonl |
|---|---|---|
| G148 | Naomi | ✅ Confirmed |
| G149 | Naomi | ✅ Confirmed |
| G092 | Alex | ✅ Confirmed |

**Ordering concern (not resolved here):** The candidate lists events G148, G149, G092. G092 has a lower numeric suffix than G148/G149, which may indicate it predates the other two chronologically. Whether this ordering is intentional (e.g., G092 is a delayed response) or a sequencing error cannot be determined without timestamp verification. See H-08.

**Prerequisite flagged in tasks.md:** `txt_restored_20260802` flag; audio review required before extraction.

### Candidate 2: Pingas/Money Dispute

| Event ID | Claimed Speaker | Exists in events.jsonl |
|---|---|---|
| G106 | Alex | ✅ Confirmed |
| G110 | Naomi | ✅ Confirmed |
| G155 | Alex | ✅ Confirmed |

**Prerequisite flagged in tasks.md:** Very low speaker confidence on G110 (0.06); audio review required before extraction.

### Pilot Events (cross-reference)

| Event ID | Role | Exists |
|---|---|---|
| G042 | Loop start (Naomi) | ✅ Confirmed |
| G180 | Excluded intervening | ✅ Confirmed |
| G181 | Loop end (Alex) | ✅ Confirmed |

**All candidate and pilot event IDs exist in `events.jsonl`. No ghost IDs detected.** This audit does not assess semantic validity of candidate loops, does not extract candidate data, and does not claim the candidate loops are valid.

---

## 7. Required Human Source-Review Decisions

The following items cannot be resolved by automated or AI review and require explicit human decisions before further processing:

| # | Item | File | Location | Blocks |
|---|---|---|---|---|
| H-01 | Audio review of G042 — verify redacted excerpt matches spoken wording | `canonical_loop_records.json` | `events[0].evidence_integrity.requires_audio_review: true` | Shareability |
| H-02 | Audio review of G181 — verify "coerced" wording; confirm scope of "rejection" acknowledgment | `canonical_loop_records.json` | `events[1].evidence_integrity.requires_audio_review: true` | Shareability |
| H-03 | Decide whether first names are safe for any shareable artifact; set `human_review_required: true` for `loop.participants` | `schema_manifest.json` | `loop.participants` | Third-party sharing |
| H-04 | Review `loop.semantic_loop_label` for neutral phrasing before any shared artifact | `schema_manifest.json` / `canonical_loop_records.json` | `loop.semantic_loop_label` | Third-party sharing |
| H-05 | Review `loop.core_topic` — "unprompted" is contested framing given G181's competing account | `schema_manifest.json` / `canonical_loop_records.json` | `loop.core_topic` | Third-party sharing |
| H-06 | Add `uncertainty_note` as separately classified sub-field in schema_manifest.json (`shareable_safe: false`) | `schema_manifest.json` | Missing sub-field entry | Schema governance |
| H-07 | Revise validation_report.md language: remove LEAK-01 through LEAK-04 superlatives and motive frame | `validation_report.md` | Lines 7, 21–22, 29 | Documentation quality |
| H-08 | Verify chronological ordering of Candidate 1 events (G148, G149, G092) against timestamps in events.jsonl | `tasks.md` / `events.jsonl` | Candidate 1 event sequence | Candidate extraction |
| H-09 | Audio review of G110 (speaker confidence: 0.06) before Candidate 2 extraction | `tasks.md` | Candidate 2 prerequisite note | Candidate extraction |
| H-10 | Decide whether `shareable_safe: true` on fields requiring human review should be gated until that review completes | `schema_manifest.json` | Multiple fields | Schema governance |

---

## 8. Verdict: Retain, Revise, or Rerun

### `canonical_loop_records.json` → **RETAIN**

All four structural differences from the proposed pilot are lossless normalizations. No substantive data was changed, added, or deleted. All privacy controls are correctly set to `private_evidence` / `private_only`. All `requires_audio_review` flags are correctly set to `true`. Suitable for private schema testing as-is. No shareable artifact may be generated until H-01 and H-02 are cleared.

### `pilots/loop_house_visit_001.proposed.json` → **RETAIN as source reference**

The proposed pilot is the correct source for the normalization comparison. Its structural omissions (bare `null`, absent `interpretation` blocks) were correctly normalized in the canonical record. It should not be treated as the working copy; `canonical_loop_records.json` is authoritative.

### `schema_manifest.json` → **REVISE (minor, schema governance)**

Three fields warrant revision before any shareable artifact generation:
- `loop.participants` — set `human_review_required: true` (FLAG-02, H-03)
- `loop.core_topic` — gate `shareable_safe` until review completes (FLAG-03, H-05)
- `events.observation.need_or_boundary` — add `uncertainty_note` sub-field with `shareable_safe: false` (FLAG-04, H-06)

Not blocking for private use.

### `validation_report.md` → **REVISE (language only)**

The report is structurally sound and the safety verdict ("UNFIT for shareable artifact generation") is correct and must be preserved. However, LEAK-01 through LEAK-04 introduce unsupported certainty and one motive frame ("manipulative") not present in the source data. These must be revised to bounded language before this document is treated as authoritative. The report must not be cited as an independent verification — it is an AI-generated self-assessment.

### `tasks.md` → **RETAIN**

Both candidate loops exist in `events.jsonl`. Prerequisite audio reviews are correctly documented. Chronological ordering of Candidate 1 (H-08) requires human verification before extraction proceeds.

---

*This audit is read-only and proposes no changes to any source or evidence file. All findings requiring action are listed in §7. No record in this audit is marked shareable or approved.*
