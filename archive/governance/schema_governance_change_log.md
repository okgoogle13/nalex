# Schema Governance Change Log

**Project:** Nalex Semantic Schema  
**Change set date:** 2026-08-14  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Executed by:** Antigravity (schema governance correction pass)  
**Scope:** Documentation and schema-governance corrections only

---

## Confirmation of Source/Evidence File Integrity

- `canonical_loop_records.json` — **NOT MODIFIED** in this pass. Read-only.
- `events.jsonl` — **NOT MODIFIED** in this pass. Read-only. Not located in `data/semantic_schema/`; located at `_canonical_strong/data/event_logs/events.jsonl`.
- All raw evidence files — **NOT MODIFIED**.

No private evidence field was made more shareable in this change set. All changes to `shareable_safe` in this pass moved values from `true` to `false`.

---

## Change 1 — schema_manifest.json: Field-level privacy hardening

**Type:** Privacy hardening  
**File:** `data/semantic_schema/schema_manifest.json`

### 1a — `loop.participants`
- **Modified field:** `human_review_required`
- **Before:** `false`
- **After:** `true`
- **Reason:** Real first names of real people in a private interpersonal dispute. The prior `false` designation was inconsistent with project sensitivity. Combined with semantic labels and event excerpts in a shared artifact, participant names become identifying. Requires explicit human consent from both participants before any third-party use. Source: integrity_audit.md FLAG-02, H-03.

### 1b — `loop.semantic_loop_label`
- **Modified field:** `shareable_safe`
- **Before:** `true`
- **After:** `false`
- **Reason:** The label names the topic of a private interpersonal dispute. Although not a direct quote, it is substantive enough to identify the nature of a private conflict to a third party. `shareable_safe` is set to false pending explicit human review. `human_review_required` was already `true`. Source: integrity_audit.md FLAG-01, H-04.

### 1c — `loop.core_topic`
- **Modified field:** `shareable_safe`
- **Before:** `true`
- **After:** `false`
- **Reason:** Current value contains contested framing ("unprompted"), a characterization of events ("closed doors"), and an attributed emotional response ("resulting discomfort"). G181 contains a competing account; "unprompted" is not a neutral descriptor. `shareable_safe` set to false pending explicit human review. `human_review_required` was already `true`. Source: integrity_audit.md FLAG-03, H-05.

### 1d — `events.observation.need_or_boundary.uncertainty_note` (new entry)
- **Action:** Added as a separately classified sub-field entry (did not previously exist in manifest)
- **Values set:** `privacy_tier: "private"`, `human_review_required: true`, `viz_safe: false`, `shareable_safe: false`
- **Reason:** The `uncertainty_note` sub-field contains interpretive framing that goes beyond observation. The parent field's `shareable_safe: true` classification must not be read as applying to sub-fields. Adding a separate entry prevents `uncertainty_note` from leaking interpretive content into shareable artifacts when the parent object is rendered. Source: integrity_audit.md FLAG-04, H-06.

---

## Change 2 — schema_manifest.json: Manifest emission gate rule

**Type:** Schema governance  
**File:** `data/semantic_schema/schema_manifest.json`

- **Action:** Added top-level `_manifest_rule` key with `shareable_emission_gate` rule.
- **Rule text:** "A field must not be emitted into a shareable artifact unless BOTH conditions are met: (1) shareable_safe is true, AND (2) human_review_required is false OR an explicit recorded human approval exists for this field in this record. shareable_safe alone does not function as publishing clearance."
- **Reason:** The integrity audit identified that `shareable_safe: true` on fields that also have `human_review_required: true` creates a risk of that boolean being read as blanket clearance by a downstream consumer or agent. This rule makes the two-condition gate explicit and machine-readable at the manifest level.

---

## Change 3 — validation_report.md: Language corrections

**Type:** Language correction  
**File:** `data/semantic_schema/validation_report.md`

All corrections targeted the flagged locations from `integrity_audit.md` §5. No structural sections were added or removed. The safety verdict ("UNFIT for shareable artifact generation") was preserved unchanged.

### 3a — Line 7: "strongly aligns" (LEAK-01)
- **Before:** "strongly aligns with the schema intent and required rules"
- **After:** "No structural violations were identified in this pass … the structure appears to align with schema intent and required rules based on this review"
- **Reason:** "Strongly aligns" implied a comprehensive independent verification. This is an AI-generated self-assessment. Replaced with bounded structural-review language.

### 3b — Line 21: "Low in this pilot" (LEAK-02)
- **Before:** "Low in this pilot."
- **After:** "Assessed low in this pilot, pending human review."
- **Reason:** The flat "Low" designation without caveat could be read as definitive clearance. Added provisional qualifier.

### 3c — Line 22: "manipulative" (LEAK-03)
- **Before:** "avoiding assumptions about whether the acknowledgement was manipulative or earnest"
- **After:** "declining to characterise the acknowledgement as sincere or otherwise"
- **Reason:** "Manipulative" is not present in the coded record, is not supported by observable-move evidence, and violates `claude.md` prohibition on inferring unsupported motives. Any substitute motive attribution (e.g., "deceptive", "strategic") was also excluded. The replacement describes the coding approach without introducing a motive frame.

### 3d — Lines 29: "highly fit" / "makes excellent use" (LEAK-04)
- **Before:** "The pilot is highly fit for private testing. It accurately demonstrates the difference between `observation` and `interpretation` and makes excellent use of `evidence_integrity` flagging…"
- **After:** "The pilot appears suitable for private schema testing based on structural review. It demonstrates the separation between `observation` and `interpretation` and the `evidence_integrity` flagging is present and appears correctly applied…"
- **Reason:** Evaluative superlatives ("highly fit", "makes excellent use") imply independent verification that did not occur. Replaced with neutral, bounded wording. The Enum/Value section was similarly revised from "perfectly aligned" to "appear correctly applied".

---

## Change 4 — nalex_semantic_schema_v2.md: Null-state handling for structured optional objects

**Type:** Schema governance  
**File:** `data/semantic_schema/nalex_semantic_schema_v2.md`

- **Action:** Added new section "Null-State Handling for Structured Optional Objects" after the existing "Loop Boundary Rules" section.
- **Content added:** Defines three distinct null-states — `none` (reviewed, no relevant content found), `not_assessed` (no coding determination made), `unknown` (evidence ambiguity prevents determination) — with a table.
- **Canonical default rule added:** States that a bare `null` must not be silently converted to `none` without an explicit canonical default decision recorded by a human reviewer. If no canonical default has been established, state must be recorded as `not_assessed` until a human decision is made.
- **Reason:** The integrity audit (DIFF-02) identified that a bare `null` was normalized to `basis: "none"` during canonical record creation. The schema did not previously define the distinction between these states, leaving the conversion semantically unanchored. This section establishes the rule before further records are created.

---

## Change 5 — validation_report.md: G181 null-state convention note

**Type:** Schema governance (notation only)  
**File:** `data/semantic_schema/validation_report.md`

- **Action:** Added "Null-State Convention Note (G181 — pending schema rule review)" section to validation_report.md.
- **Content:** Notes that G181 `need_or_boundary` currently uses `basis: "none"` as the canonical convention, established prior to the null-state handling rules added in Change 4. States that the record has not been changed in this pass and that a human decision is required to confirm the mapping.
- **Reason:** `canonical_loop_records.json` was not modified (per mandate scope). The note creates a human-review prompt without altering the record, consistent with the instruction to "add a note to validation_report.md" rather than change the JSON.
- **canonical_loop_records.json:** Confirmed not modified.

---

## Unresolved Human Decisions Carried Forward

The following items remain open after this pass and require explicit human decisions before further processing. These are unchanged from integrity_audit.md §7 except where noted:

| # | Item | Blocks |
|---|---|---|
| H-01 | Audio review of G042 | Shareability |
| H-02 | Audio review of G181 — verify "coerced" wording | Shareability |
| H-03 | Confirm human_review_required: true for loop.participants is the correct disposition | Third-party sharing |
| H-04 | Review loop.semantic_loop_label for neutral phrasing; confirm or revise shareable_safe: false | Third-party sharing |
| H-05 | Review loop.core_topic — "unprompted" is contested; confirm or revise shareable_safe: false | Third-party sharing |
| H-06 | Confirm uncertainty_note sub-field entry and classification are correct | Schema governance |
| H-07 | *(Resolved in this pass — language corrections applied)* | — |
| H-08 | Verify chronological ordering of Candidate 1 events (G148, G149, G092) | Candidate extraction |
| H-09 | Audio review of G110 (speaker confidence: 0.06) | Candidate extraction |
| H-10 | Confirm G181 basis: "none" maps correctly to the new null-state "none" definition | Schema governance |

---

## Change 6 — canonical_loop_records.json: G181 Null-state correction

**Type:** Record correction
**File:** `data/semantic_schema/canonical_loop_records.json`

- **Action:** Updated G181 null-state basis to `not_assessed` according to new schema null-state rules.
- **JSON Path:** `events[1].observation.need_or_boundary.basis`
- **File Integrity Before:**
  - `canonical_loop_records.json`: 5988fc647b844ca7c0509e342d03c28a45f7c2fda43b627d8718fe74ce6e6fc2
  - `_canonical_strong/data/event_logs/events.jsonl`: a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548
- **File Integrity After:**
  - `canonical_loop_records.json`: e0666867d0b84822d1cd9c4c867f58ea34a06bdefdc1a24233093d2bb4ab30c7 (JSON syntax valid)
  - `_canonical_strong/data/event_logs/events.jsonl`: a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548 (Unchanged)

---

## Change [Candidate 1 Correction Pass] — Reversal of Premature Canonical Merge: loop_reassurance_001

**Date:** 2026-08-14  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Executed by:** Antigravity (Candidate 1 over-eager pilot correction workflow)  
**Type:** Canonical record reversal + proposed pilot correction

### Summary

A prior agent pass (Candidate 1 pilot workflow) prematurely merged `loop_reassurance_001` into `canonical_loop_records.json`. This record carried `coding_review_status: "proposed"` and multiple `requires_audio_review: true` flags. It was not ready for canonical admission. This pass reverses that merge and corrects the interpretive overclaiming in the proposed pilot file.

### Files Changed

| File | Change |
|---|---|
| `data/semantic_schema/canonical_loop_records.json` | `loop_reassurance_001` record removed; record count reduced from 2 → 1 |
| `data/semantic_schema/pilots/loop_reassurance_001.proposed.json` | Interpretive corrections applied (see below) |
| `data/semantic_schema/pilots/loop_reassurance_001.audit.md` | Created (new file) |

### Exact Values Changed

#### `canonical_loop_records.json`
- **Before:** Array contained 2 records: `["loop_house_visit_001", "loop_reassurance_001"]`
- **After:** Array contains 1 record: `["loop_house_visit_001"]`
- `loop_house_visit_001` is **not altered**.

#### `data/semantic_schema/pilots/loop_reassurance_001.proposed.json`

| Field / Location | Old Value | New Value | Reason |
|---|---|---|---|
| `loop.repair_response_status` | `"received"` | `"unclear"` | Sequence supports response/de-escalation; does not establish repair was received or accepted |
| `G148 observation.context_facts` | `"The speaker initially deflects fault then admits it."` | `"States 'not my fault,' then states 'it is my fault.'"` | Replaces interpretive verb ("deflects") with source-bounded paraphrase |
| `G149 observation.interaction_state_after_event` | `"repair_opening"` | `"unclear"` | Offer made; reception/outcome not established pending audio review |
| `G092 observable_moves[2] (accepts_repair)` | Present | Removed | Excerpt does not establish that a repair was received/accepted; wording ("It's all good") is consistent with several readings |
| `G092 observable_moves[3] (invites_closeness)` | Present | Removed | Supporting phrase absent from `minimal_redacted_excerpt`; rationale cited text not in the record |
| `G092 observation.context_facts` | `"The response reframes the initial conflict as teasing and diffuses the guilt."` | `"States the prior remarks were teasing ('being a bit cheeky') and states 'It's all good,' relieving pressure of the repair offer."` | Replaces outcome conclusion ("diffuses the guilt") with source-bounded description |
| `G092 observation.interaction_state_after_event` | `"connected"` | `"unclear"` | Interpretive relational-outcome claim not derivable from excerpt alone |

### Why Canonical Admission Requires Integrity Review

Canonical status in this schema carries a different weight from proposed status:
- Canonical records are the basis for future visualization, artifact generation, and inter-loop analysis
- A record with `coding_review_status: "proposed"` and `requires_audio_review: true` across all events cannot have its codes treated as verified
- Accepting a `received` repair status when no excerpt shows the repair being received sets a precedent that undermines the schema's observation/interpretation separation
- `invites_closeness` was coded from a rationale citing text not present in the record — this is a category error that canonical admission would have embedded as fact

The integrity review gate exists to catch exactly this class of error before it propagates into rendered artifacts.

### File Integrity Before and After

| File | Before Hash (SHA-256) | After Hash (SHA-256) |
|---|---|---|
| `canonical_loop_records.json` | `99d6c06f23c15e8374563f4b1d6c51e7de201baf036ce788ac44d7440f5772aa` | `a4cb1a42c6fa0b39e862918b36c60e537bafe408bf7fb6f6f1a40e76aa933819` |
| `pilots/loop_reassurance_001.proposed.json` | `e61a70febef74e5bc4dc653567f4f56f53570c5d8caec7c111dd6ea646b5761e` | `49812f6c4dbc041926b19c3cf40dc0ac8c1cb1a2a77c8f870001bd464628a70b` |
| `_canonical_strong/data/event_logs/events.jsonl` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` |

**Confirmation: `events.jsonl` was not changed. Before and after hashes are identical.**

### Remaining Review Gates

- [ ] Audio review of G148, G149, G092 required before any coding can move from `proposed`
- [ ] G147 (reference event for G092 "teasing" context) must be examined to confirm loop boundary
- [ ] `invites_closeness` may be reinstated only if the supporting excerpt is added to `minimal_redacted_excerpt` and audio is reviewed
- [ ] `loop_reassurance_001` may be re-admitted to canonical only after all `requires_audio_review` flags are resolved and a human reviewer explicitly approves coding_review_status upgrade

---

## Change [Boundary Governance + Vocabulary Correction Pass] — loop_reassurance_001 Proposed Pilot

**Date:** 2026-08-14  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Executed by:** Antigravity (narrowly scoped schema correction — boundary, vocabulary, and source-quality fields)  
**Change type:** Boundary governance · Vocabulary correction · Source-quality protection

### Files Changed

| File | Change type |
|---|---|
| `data/semantic_schema/pilots/loop_reassurance_001.proposed.json` | Boundary governance + vocabulary correction |
| `data/semantic_schema/pilots/loop_reassurance_001.audit.md` | Updated to reflect all corrections |

`canonical_loop_records.json` — **not modified**  
`_canonical_strong/data/event_logs/events.jsonl` — **not modified**  
`nalex_semantic_schema_v2.md` — **not modified** (no new code was approved; vocabulary proposal is pending human decision only)

### Fields Changed — `loop_reassurance_001.proposed.json`

| Field | Old Value | New Value | Change type |
|---|---|---|---|
| `loop.boundary_confidence` | `"medium"` | `"low"` | Boundary governance |
| `loop.boundary_rationale` | Single sentence describing "chronologically contiguous" exchange | Factual multi-sentence description naming G148/G149 contiguity, G092 as response, G147 as external context dependency with 17m35s gap | Boundary governance |
| `loop.intervening_events_note.reason` | "No intervening events." | Clarified that G147 is not an intervening event but an external dependency documented separately | Boundary governance |
| `loop.intervening_events_note.effect_on_boundary_confidence` | "None." | States G147 dependency reduces confidence to low | Boundary governance |
| `loop.external_context_dependencies` | Field absent | Added array with G147 entry: `referenced_by_later_event`, `required_for_interpretation: true`, source quality caveat (conf 0.29) | Boundary governance |
| `loop.source_limitations` | Brief note on G148 restoration | Expanded to name all four events requiring audio review and both low-confidence speaker attributions | Source-quality protection |
| `G148 observable_moves[seq 2]` (`acknowledges_impact_of_action`) | Present | **Removed.** Code definition (validates impact on other person) does not match observable move (statement of causal responsibility). No substitute code exists in vocabulary. | Vocabulary correction |
| `G148 observation._coding_note_seq2_removed` | Field absent | Added explanatory note documenting removal reason and pending vocabulary proposal | Vocabulary correction |
| `G092 evidence_integrity.unverified_or_ambiguous_claims` | "Context of original 'teasing' refers to unincluded prior event (presumably G147)" | Updated to name G147 as a documented external dependency and state the speaker-confidence risk | Boundary governance |
| `G092 coding_metadata.review_notes` | Brief note | Extended with `invites_closeness` pending gate: phrase confirmed in source, absent from excerpt, reinstatement requires human source review and excerpt extension | Boundary governance / vocabulary protection |

### Vocabulary Decision — G148 seq 2

**Decision: Removed. No substitute code applied.**

- `acknowledges_impact_of_action` was incorrectly applied to "Actually, it is my fault" — a statement of causal responsibility, not impact validation.
- `apologises` does not fit — no expression of regret is present.
- No existing code in `nalex_semantic_schema_v2.md` covers a direct fault admission.
- A new code `states_causal_responsibility` has been **proposed** in the audit file. It is not added to the vocabulary until a human approves it.
- `nalex_semantic_schema_v2.md` was **not modified**.

### Boundary Governance Rationale

`boundary_confidence` was lowered from `medium` to `low` because:
1. G092's only coded move requires G147 as a referent, and G147 is 17 minutes 35 seconds before G148 — not "chronologically contiguous" with the loop.
2. G147's speaker confidence is 0.29 (low); if attribution cannot be confirmed by audio, the dependency cannot be relied upon.
3. G148's speaker confidence is 0.37 (low) with restored transcript — the loop's start event carries compound source uncertainty.

### File Integrity

| File | Before Hash (SHA-256) | After Hash (SHA-256) |
|---|---|---|
| `pilots/loop_reassurance_001.proposed.json` | `49812f6c4dbc041926b19c3cf40dc0ac8c1cb1a2a77c8f870001bd464628a70b` | `ac8f5af1afd82c24e76f51e4f8e0f618fb76fe6eb7b364ce2b7f8a867b309732` |
| `canonical_loop_records.json` | `a4cb1a42c6fa0b39e862918b36c60e537bafe408bf7fb6f6f1a40e76aa933819` | `a4cb1a42c6fa0b39e862918b36c60e537bafe408bf7fb6f6f1a40e76aa933819` |
| `_canonical_strong/data/event_logs/events.jsonl` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` |

**`canonical_loop_records.json` was not modified. `events.jsonl` was not modified. Hashes confirm.**

### Remaining Human Source-Review Gates

- [ ] Audio review of G148 (tone, speaker confirmation, transcript restoration verification)
- [ ] Audio review of G149 (tone of offer)
- [ ] Audio review of G092 (speaker confirmation, full text verification including "come say hey" phrase)
- [ ] Audio review and speaker confirmation of G147 (conf 0.29; external dependency link at risk if attribution fails)
- [x] Human vocabulary decision: approve or reject proposed code `states_causal_responsibility` for G148 seq 2 — **APPROVED by user 2026-08-14. Applied in Change [Vocabulary Addition] below.**
- [ ] Human decision on `invites_closeness` reinstatement after audio review and excerpt extension
- [ ] Explicit human approval required at canonical admission gate

---

## Change [Vocabulary Addition] — nalex_semantic_schema_v2.md: Add `states_causal_responsibility`

**Date:** 2026-08-14  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Executed by:** Antigravity (vocabulary addition pass — user-approved single code)  
**Change type:** Controlled-vocabulary addition (observation layer)  
**Approval source:** Explicit user approval, 2026-08-14  
**Source proposal:** `data/semantic_schema/proposals/causal_responsibility_code_review.md`

### Code Added

**Name:** `states_causal_responsibility`  
**Layer:** Observation layer (`observable_moves`) only  
**Definition:** Speaker explicitly states that they caused or were at fault for a specific event or outcome.

### Inclusion Boundary

- Explicit first-person fault or causation statement present in the text.
- A specific event or outcome is established either in the same minimally sufficient excerpt or in a directly adjacent, explicitly referenced source event.
- If adjacent source context establishes the event/outcome, the supporting source_event_id must be recorded in `evidence_reference`.

### Exclusion Boundary

- Regret without a causal/fault claim: use `apologises` if supported.
- Validation of another person's experience: use `acknowledges_impact_of_action` if supported.
- Explanation of intent without a causal/fault claim.
- Future remedy proposal without causal/fault claim.
- Global self-criticism, vague guilt, sarcasm, hypotheticals, or unsupported inference.

### Adjacent-Evidence Traceability Rule

Where the specific event or outcome named by the fault claim is established not in the coded excerpt itself but in a directly adjacent and explicitly referenced source event, that source event's ID must be recorded in `evidence_reference` for the coded move. This preserves full traceability without requiring the excerpt to repeat material already captured in the adjacent record.

### Coding Rule (Misuse Prevention)

Do not infer sincerity, factual accuracy, remorse, accountability quality, motivation, relational impact, or repair outcome from this code. The code records only that an explicit fault or causation statement appears in the source text. Where literal meaning depends materially on tone, preserve the source caveat and set `requires_audio_review: true`.

### Placement in Schema

Inserted in the Factual Controlled Vocabulary list after `apologises` and before `accepts_repair`, consistent with the existing structural style of observation-layer move codes.

### No Event or Pilot Recoded in This Pass

`pilots/loop_reassurance_001.proposed.json` was **not modified** in this pass. G148 seq 2 remains absent from `observable_moves` pending audio review (H-01 in the pilot audit) and explicit human approval at the pilot coding gate (H-09). The code is now available for use; application to the pilot requires a separate approved pass after audio review.

`canonical_loop_records.json` was **not modified**.  
`_canonical_strong/data/event_logs/events.jsonl` was **not modified**.

### File Integrity

| File | Before Hash (SHA-256) | After Hash (SHA-256) |
|---|---|---|
| `nalex_semantic_schema_v2.md` | `cf6ed6504714f9303b10f78510c24b6f8d322cd4994d7ad82962957a39989666` | `8aa8be8ccf20b7726b81f2d1836c24d2856fc5cfec557d172b0c6a81f2220123` |
| `schema_governance_change_log.md` | `4ef5cb5fc0311c9936d5ba29bb2d86ae02e021f9635ae5ab692ab89886a41fe3` | `e00c3cd4c156a2cb6fb6e9fa01b1904f1c93ae5075d0014f45b894697a3e34d0` |
| `canonical_loop_records.json` | `a4cb1a42c6fa0b39e862918b36c60e537bafe408bf7fb6f6f1a40e76aa933819` | `a4cb1a42c6fa0b39e862918b36c60e537bafe408bf7fb6f6f1a40e76aa933819` (unchanged) |
| `_canonical_strong/data/event_logs/events.jsonl` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` (unchanged) |

---

## Change [Vocabulary Spec Refinement] — nalex_semantic_schema_v2.md: `states_causal_responsibility` entry expanded

**Date:** 2026-08-14  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Executed by:** Antigravity (spec-refinement pass — same approved code, extended entry)  
**Change type:** Controlled-vocabulary spec refinement (observation layer)  
**Approval source:** Explicit user approval, 2026-08-14 (same approval as Change [Vocabulary Addition])  
**Source recommendation:** `data/semantic_schema/proposals/causal_responsibility_code_review.md`

### Context

The code `states_causal_responsibility` was added to `nalex_semantic_schema_v2.md` in the immediately preceding pass (Change [Vocabulary Addition]). The current pass applies a more detailed spec provided in the same user-approved instruction. The code name, definition, layer placement, and core boundaries are unchanged. Two elements were added to the schema entry:

1. **Exclusion clause extended** — Added explicit exclusion of "ambiguous statements where literal meaning cannot be established from the available source." The prior entry covered sarcasm and hypotheticals but did not name source-ambiguity cases explicitly.
2. **Co-occurrence rule added** — Added: "Co-occurring apology, impact acknowledgement, intent explanation, or repair offer must each be independently excerpt-supported and coded separately." This was implied by the schema's general evidence-integrity rules but was not stated within the code entry itself. Adding it in-entry prevents the code from being used as a proxy admission for adjacent moves.

### What Was Not Changed

- Code name: unchanged (`states_causal_responsibility`)
- Definition: unchanged
- Layer: unchanged (observation layer, `observable_moves`, only)
- Adjacent-evidence traceability rule: unchanged (when adjacent evidence establishes the event/outcome, the supporting source_event_id must be recorded in `evidence_reference`)
- Non-inference safeguards: unchanged and extended (motive, emotional state, manipulation now named explicitly alongside sincerity, remorse, accountability quality, relational impact, repair success)

### No Pilot, Canonical Record, Raw Evidence, Manifest, or Visualization File Changed

`pilots/loop_reassurance_001.proposed.json` — **not modified**  
`canonical_loop_records.json` — **not modified**  
`_canonical_strong/data/event_logs/events.jsonl` — **not modified**  
`schema_manifest.json` — **not modified**  
No visualization file was modified.

### Verification: Code Appears Exactly Once in Schema

`states_causal_responsibility` appears at exactly one location in `nalex_semantic_schema_v2.md` (Factual Controlled Vocabulary list, after `apologises`, before `accepts_repair`).

### File Integrity

| File | Before Hash (SHA-256) | After Hash (SHA-256) |
|---|---|---|
| `nalex_semantic_schema_v2.md` | `8aa8be8ccf20b7726b81f2d1836c24d2856fc5cfec557d172b0c6a81f2220123` | *(recorded below after write)* |
| `schema_governance_change_log.md` | `9dac1a8b5f8371eda80dd179954688ff455c193ecb7f023e35a4efd350a5fe02` | *(recorded below after write)* |
| `pilots/loop_reassurance_001.proposed.json` | `ac8f5af1afd82c24e76f51e4f8e0f618fb76fe6eb7b364ce2b7f8a867b309732` | `ac8f5af1afd82c24e76f51e4f8e0f618fb76fe6eb7b364ce2b7f8a867b309732` (unchanged) |
| `canonical_loop_records.json` | `a4cb1a42c6fa0b39e862918b36c60e537bafe408bf7fb6f6f1a40e76aa933819` | `a4cb1a42c6fa0b39e862918b36c60e537bafe408bf7fb6f6f1a40e76aa933819` (unchanged) |
| `_canonical_strong/data/event_logs/events.jsonl` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` | `a1fb572fdecd7b7ae1dda02bf9e2f177ee10979476e87b91577102a0113cb548` (unchanged) |


## Change [Preparation Pass] — Project folder preparation and layer contract definition

**Date:** 2026-08-14  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Executed by:** Antigravity (Preparation agent pass)  
**Type:** Structural, policy, and contract-level changes

### Changes Made:
- **Created folders:** `./data/semantic_schema/projections/`, `./data/semantic_schema/reflective/`, `./data/semantic_schema/audits/`, `./artifacts/archive/`, `./artifacts/reflective/`, `./artifacts/viz/`
- **Created `project_state_and_layer_contract.md`**: Defined the 7-layer structure (raw evidence to artifact outputs).
- **Created `viz_readiness_contract.md`**: Defined explicit visualization readiness policies (projections required, raw/proposed are unrenderable).
- **Created `reflective/nalex_reflective_schema_contract.json`**: Defined the target shape for reflective schemas.
- **Created `projections/nalex_viz_projection_contract.json`**: Defined the target shape for viz-safe projections.
- **Created `pre_viz_blockers.md`**: Assessed and listed current blockers preventing artifact generation.
- **Created `legacy_artifact_status.md`**: Reclassified legacy HTML artifacts as archive-only and recommended fresh templates.
- Legacy `nalex_viz_schema.json` was inspected and reclassified as retained for legacy use only, not edited.

### Governance Confirmations:
- **No raw evidence semantics were reinterpreted.**
- **No pilot or canonical content was silently upgraded.**
- **Legacy files were reclassified but not edited.**

## Change [Audio Review Pass] — Formal resolution of pilot blockers

**Date:** 2026-08-14
**Authority basis:** Manual audio review by human analyst

### Changes Made:
- **G042 Audio Review:** Verified tone as distressed and frustrated; transcript excerpt confirmed accurate. `requires_audio_review` flag cleared in canonical records.
- **G181 Audio Review:** Verified speaker intent; `coerced` confirmed but contextually meant as a caring friend attempting to get her out of the house. Acknowledgment of rejection confirmed as misunderstanding of her boundary. `requires_audio_review` flag cleared in canonical records.
- **Governance confirmation:** G181 null-state mapping officially recorded and verified as `not_assessed` (basis "none").
- **Pipeline Status:** `loop_house_visit_001` projection eligibility updated to `true` and reflective schema rendering status updated to `ready`.

---

## Change [Calibration Correction Pass] — source_confidence_calibration_review.md

**Date:** 2026-08-14  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Executed by:** Antigravity (source-confidence calibration correction pass)  
**Change type:** Calibration assumption correction

### Summary
- **Calibration recommendation corrected:** The assumption that `speaker_conf` measures technical probability of speaker identity, transcript accuracy, or intent was unsupported and has been removed.
- **Raw `speaker_conf` semantics are not established:** The precise technical meaning of this field is undocumented in accessible materials.
- **Numerical confidence mapping withdrawn:** The proposed quartile-based Low/Medium/High mapping was withdrawn as a governance recommendation. It is retained only as an exploratory corpus distribution.
- **No core schema changes:** No schema (`nalex_semantic_schema_v2.md`), pilot, canonical record, or raw evidence file was altered in this pass.
