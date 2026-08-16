# Audit: loop_reassurance_001 (Proposed Pilot)

**File under review:** `./data/semantic_schema/pilots/loop_reassurance_001.proposed.json`  
**Audit date:** 2026-08-14 (updated 2026-08-14, boundary and vocabulary correction pass)  
**Auditor:** Antigravity (schema correction workflow — Candidate 1 over-eager pilot correction; boundary and context audit; vocabulary correction pass)  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)

---

> **EXPLICIT FINDING:**
> This is a proposed private pilot. It is context-dependent, private, and
> not eligible for canonical admission. It is not suitable for shareable
> artifact generation.

---

## 1. Actual Timestamp Order

| Source Event | Timestamp (UTC)         | Speaker (attributed) | Speaker conf | Source Order in Record |
|---|---|---|---|---|
| G147         | 2026-04-01 23:59:40     | Alex                 | 0.29 (low)   | External dependency only — not a loop member |
| G148         | 2026-04-02 00:17:15     | Naomi                | 0.37 (low)   | 1 |
| G149         | 2026-04-02 00:17:46     | Naomi                | 0.45 (medium)| 2 |
| G092         | 2026-04-02 00:19:08     | Alex                 | 0.53 (medium)| 3 |

**Gap notes:**
- G147 → G148: **17 minutes 35 seconds**. G147 is an external context dependency, not a loop member. The boundary rationale has been updated to reflect this.
- G148 → G149: 31 seconds (contiguous).
- G149 → G092: 82 seconds (response).

---

## 2. Source Quality Limitations

| Event | Source Quality                 | Key Limitation |
|---|---|---|
| G147  | `voice_transcript` (inferred)  | Speaker confidence **0.29** — the lowest of the four events. If speaker attribution to Alex cannot be confirmed by audio, the G147→G092 semantic link breaks. Source review required before this dependency can be relied upon. |
| G148  | `transcript_with_known_errors` | Speaker confidence **0.37** (low). Transcript restoration (`txt_restored_20260802`) applied; original wording unverified against audio. Full source text includes "You could have asked for more. I don't know. I didn't know. I don't know things. And I didn't mean to." — these phrases are absent from the `minimal_redacted_excerpt`. Tone (e.g. whether fault admission is contrite or contemptuous) cannot be determined from text alone. |
| G149  | `voice_transcript`             | Speaker confidence 0.45 (medium). Automated transcript. Tone of offer (sincere vs. exasperated) not captured. Minor omission in excerpt ("Walk over.") — does not affect coding. |
| G092  | `voice_transcript`             | Speaker confidence 0.53 (medium). Transcribed by `faster-whisper/medium`, a lower model tier than G147/G148/G149 (all `large-v3`). Full source text includes "If you want to come say hey, you're more than welcome to. You can also get your bike." — partly absent from `minimal_redacted_excerpt`. |

All three loop events (G148, G149, G092) have `requires_audio_review: true`. G147 (external dependency) also requires audio review.

---

## 3. G147 External Context Dependency

G147 source text (from `events.jsonl`):
> "I'm just going to hit you with a little bit of bog guilt here and remind you that you did kind of toast my last little bit of rocks."

G092 references "teasing" and "giving you some shit" — these phrases describe a prior act. G147 is the only candidate source event for that referent in the available record.

**G147 is documented as an external context dependency** (`external_context_dependencies` array in the loop object), not as a loop member. It is not added to `loop_start_event_id`, is not included in `events[]`, and is not listed in `intervening_events_note.excluded_event_ids`.

**Dependency is required for interpretation:** The `responds_to_concern_with_explanation_of_intent` code on G092 seq 1 describes Alex explaining the intent behind prior remarks. Without G147, the referent of "teasing" and "giving some shit" in G092 cannot be source-traced. The code is retained but carries this external dependency as a documented condition.

**Speaker confidence caveat:** G147's speaker confidence is 0.29. If audio review does not confirm the Alex attribution, the semantic link between G147 and G092's self-description cannot be established, and G092 seq 1's coding rationale loses its anchor.

---

## 4. Excerpt-to-Code Alignment Table (Current State)

### G148 — Speaker: Naomi (conf: 0.37, low)

| Seq | Code | Excerpt Support | Finding |
|---|---|---|---|
| 1 | `uses_heightened_or_confrontational_language` | "Fucking not my fault" (in excerpt and source) | **Supported** |
| 2 | *(removed)* | See vocabulary note below | **Removed — no valid vocabulary code** |

**Vocabulary note — G148 seq 2 (removed):**

The source statement "Actually, it is my fault" is a statement of causal responsibility for an event. The prior code `acknowledges_impact_of_action` is defined as "Validates how an action *affected the other person*." A fault admission is not impact validation. The existing vocabulary also does not include `apologises` as a fit, since "it is my fault" is not a general apology.

No existing controlled-vocabulary code in `nalex_semantic_schema_v2.md` accurately covers this move. The following code is proposed for human vocabulary decision before this sequence can be recoded:

> **Proposed code (pending human decision):**  
> `states_causal_responsibility` — States that one is at fault for or caused a specific event or outcome. Distinct from `acknowledges_impact_of_action` (which validates effect on other person) and from `apologises` (which is a general expression of regret). Source basis: "Actually, it is my fault."

This proposal must not be added to `nalex_semantic_schema_v2.md` without explicit human approval. The sequence remains absent from `observable_moves` until the decision is made.

---

### G149 — Speaker: Naomi (conf: 0.45, medium)

| Seq | Code | Excerpt Support | Finding |
|---|---|---|---|
| 1 | `offers_specific_repair_step` | "I could go over there or something... how can I help?" (in excerpt and source) | **Supported** |

---

### G092 — Speaker: Alex (conf: 0.53, medium)

| Seq | Code | Excerpt Support | Finding |
|---|---|---|---|
| 1 | `responds_to_concern_with_explanation_of_intent` | "I'm kind of teasing... being a bit cheeky" (in excerpt and source) | **Supported — with documented external dependency on G147** |

**Previously removed codes — status:**

| Code | Status | Reason |
|---|---|---|
| `accepts_repair` | Removed (prior pass). Removal stands. | "It's all good" and "don't feel like you have to" are consistent with multiple readings; no excerpt language establishes that a repair from G149 was received or acknowledged. |
| `invites_closeness` | Removed (prior pass). **Pending human source-review gate.** | The phrase "If you want to come say hey, you're more than welcome to" is confirmed present in the G092 full source text (`events.jsonl`) but is absent from the current `minimal_redacted_excerpt`. This code may be reconsidered **only after**: (a) human source review verifies the wording, (b) human determines the code is necessary for this pilot, and (c) the excerpt is extended to include the phrase. Do not reinstate from rationale alone. |

---

## 5. Boundary Verdict

**Verdict: Viable only with G147 recorded as an explicit external context dependency.**

- G148 → G149 → G092 is chronologically ordered and not interrupted by other events in the source log.
- The three-event sequence is not self-contained for interpretation. G092's only code (`responds_to_concern_with_explanation_of_intent`) refers to a prior act described as "teasing" — G147 is the only available source referent.
- G147 is 17 minutes 35 seconds before G148. It is not a loop member.
- `boundary_confidence` has been lowered from `medium` to `low` reflecting: (1) the external dependency on G147 at low speaker confidence, and (2) the low speaker confidence on G148 with restored transcript.

---

## 6. Private-Canonical Readiness

**Not ready for private-canonical admission.**

| Condition | Status |
|---|---|
| Boundary adequately documented | ✅ G147 documented as external dependency with gap and confidence caveats |
| Every remaining code is excerpt-supported | ✅ Yes (G148 seq 1, G149 seq 1, G092 seq 1) — with G092 carrying the G147 external dependency |
| G148 seq 2 resolved | ⚠️ Removed pending vocabulary decision (human action required) |
| `invites_closeness` resolved | ⚠️ Removed pending human source-review gate |
| All `requires_audio_review: true` events resolved | ❌ All three loop events + G147 require audio review |
| Speaker confidence adequate | ❌ G147 (0.29) and G148 (0.37) both low |
| `coding_review_status` upgraded from `proposed` | ❌ All events remain at `proposed` |

---

## 7. Excluded Interpretations and Vocabulary Decisions

- **`repair_response_status: received`** (prior pass) — Changed to `unclear`. De-escalatory wording was provided; no excerpt establishes the repair was received or accepted.
- **`interaction_state_after_event: connected` (G092)** (prior pass) — Changed to `unclear`. Interpretive relational-outcome claim not derivable from excerpt.
- **`interaction_state_after_event: repair_opening` (G149)** (prior pass) — Changed to `unclear`. Offer was made; reception not established pending audio.
- **`acknowledges_impact_of_action` (G148 seq 2)** (this pass) — Removed. Code definition does not match the observable move (fault admission ≠ impact validation). No substitute code exists; vocabulary proposal recorded above.
- **`accepts_repair` (G092)** (prior pass) — Removed. No excerpt support.
- **`invites_closeness` (G092)** (prior pass, confirmed this pass) — Absent from excerpt; present in full source. Pending human source-review gate; not reinstated.
- **`context_facts` wording** (prior pass) — Replaced with source-bounded language throughout.

---

## 8. Unresolved Questions Requiring Human Decision

- [ ] **H-01** Audio review of G148: tone of fault admission, verification of restored transcript wording, confirmation of speaker attribution (conf 0.37).
- [ ] **H-02** Audio review of G149: tone of offer.
- [ ] **H-03** Audio review of G092: confirmation of full text including "If you want to come say hey, you're more than welcome to" and speaker attribution.
- [ ] **H-04** Audio review and speaker confirmation of G147 (external dependency, conf 0.29). If attribution to Alex cannot be confirmed, the G147→G092 semantic link cannot be established and G092 seq 1's coding rationale loses its source anchor.
- [ ] **H-05** Vocabulary decision: approve or reject proposed code `states_causal_responsibility` for G148. If approved, add to `nalex_semantic_schema_v2.md` and recode G148 seq 2.
- [ ] **H-06** `invites_closeness` gate: after audio review of G092, decide whether to extend the `minimal_redacted_excerpt` to include the "come say hey" phrase and reinstate the code.
- [ ] **H-07** G148 excerpt completeness: decide whether omitted phrases ("You could have asked for more. I don't know. I didn't know. I don't know things. And I didn't mean to.") require additional coding.
- [ ] **H-08** Model tier note for G092 (`faster-whisper/medium` vs. `large-v3` for other events): decide whether to add a `source_quality_note` to the G092 event record.
- [ ] **H-09** Canonical admission gate: after all audio reviews are complete and above decisions are resolved, explicit human approval required to move any event from `coding_review_status: proposed`.
