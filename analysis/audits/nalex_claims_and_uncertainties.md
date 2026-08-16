# Nalex Timeline — Claims Requiring Review and Remaining Uncertainties
*Produced 2026-08-15. For use alongside `nalex_resegmented_timeline.md` (v2) and `nalex_incidents.json` (v2).*

---

## Section 1: Factual Claims Requiring Manual Source Review

The following 12 claims appear in the revised timeline. Each is sourced, but each relies on something other than a direct verbatim event from `events.jsonl` — specifically: participant account, editorial inference from `CURRENT_STATE_CLEAN.md`, or external annotation layer. They are not errors; they are correctly attributed in the timeline. This list exists to document what a downstream user should independently verify before treating them as established.

| # | Claim | Where Used | Current Source | What Independent Verification Looks Like | Risk Level |
|---|---|---|---|---|---|
| 1 | Alex sent 392 words across B044/B045/B046 in 76 seconds | CONF-01, CONF-02 | CURRENT_STATE_CLEAN.md §8.4 (word count) + timestamps B044/B046 (76s computed) | Count words in B044/B045/B046 transcripts; subtract B044 timestamp from B046 timestamp | Low — timestamps are in `events.jsonl`; word count is the only external figure |
| 2 | Naomi's last turn before Alex's arrival-window monologue was B039 at 16:27:42 (37 min 14s gap) | CONF-01 | Timestamps of B039 and B044 from `events.jsonl` | Confirm B039 is the last Naomi turn before B044 by scanning `events.jsonl` chronologically | Low — direct timestamp computation |
| 3 | Exchange rate before B063: 5.1 turns/hr; after B063: 25.6 turns/hr | CONF-02 | CURRENT_STATE_CLEAN.md §8.1 table | Recount turns and duration in `events.jsonl` for S7 (Jun 26 21:57 – Jun 27 02:33), split at B063 | Low — computable from `events.jsonl` |
| 4 | Alex's Conflict-phase sign-offs held in 2 of 11 instances | CONF-02 | CURRENT_STATE_CLEAN.md §8.2 table | Identify all 11 sign-offs in Conflict-phase events; check whether each was breached within-session | Moderate — requires identifying all sign-off events by content, not tag |
| 5 | B063's "keyboard warrior" premise assessed as "factually false on the record" | CONF-02 | CURRENT_STATE_CLEAN.md §8.4 (analytical assessment) | This is an editorial conclusion, not a raw fact. Reviewers should read §8.4 and assess independently based on B046 timestamp and B066 rebuttal | Moderate — well-sourced but editorial; citable as CURRENT_STATE_CLEAN.md §8.4's conclusion |
| 6 | C066–C068 annotated as genuine_unanswered = true | CONF-03 | `conflict_questions_annotated.json` (Rev 6, delivered 2026-08-05) | Open `conflict_questions_annotated.json`, locate C066–C068, check `genuine_unanswered` field | Low — annotation layer is canonical (CURRENT_STATE_CLEAN.md §6 Rev 6) |
| 7 | G212's speaker is Naomi (confirmed by manual listening) | AFT-01 | CURRENT_STATE_CLEAN.md §3 ("Originally Unknown; manual listening confirmed Naomi") | Re-listen to the G212 audio file if available | Low — CURRENT_STATE_CLEAN.md §3 is explicit; no Unknown labels remain |
| 8 | Naomi's post-exit word count in Aftermath: 2,585 words across 11 tail turns | AFT-13 (and generally) | CURRENT_STATE_CLEAN.md §13.3 | Identify all post-exit Naomi turns in `events.jsonl` (turns where Alex has exited in-session); count words | Moderate — requires identifying in-session exits, which requires reading turn structure |
| 9 | AFT-06 "did not survive the session it occurred in" | AFT-06 | CURRENT_STATE_CLEAN.md §13.4 (editorial characterisation) | Read AFT-07 onwards; confirm conflict reopened within 23 min of G191 | Low — directly verifiable by reading AFT-07 source events |
| 10 | Naomi's claim about prior knowledge via Nishant (G094, G211) | AFT-05, AFT-13 | Participant account only | No corpus event independently corroborates this. Would require external evidence (Nishant interview, etc.) not present in corpus | High — participant claim flagged throughout; no corroboration path within corpus |
| 11 | CURRENT_STATE_CLEAN.md §13.3's label `alex_topic_contingent_availability` | AFT-12 | CURRENT_STATE_CLEAN.md §13.3 (analytical label) | This is a structural characterisation, not a self-description. Reviewers should note that Alex does not name this pattern himself; the label is analyst-assigned | Moderate — clearly marked [inference] in timeline; risk is misreading it as participant admission |
| 12 | CURRENT_STATE_CLEAN.md §13.1's Flooding Hypothesis (exit-as-regulation) | AFT-09 | CURRENT_STATE_CLEAN.md §9.1 (analytical hypothesis) | This is explicitly a hypothesis, not an established motive. Alex's own stated reason in G199 is ADHD/dyslexia + feeling overwhelmed. The Flooding Hypothesis is an analyst's frame for that stated reason | Moderate — clearly marked [inference]; risk is same as #11 |

---

## Section 2: Remaining Uncertainties and Missing Opposing-Channel Audio

### 2.1 Missing Alex-side audio in S-AM-2 and S-AM-3

**What is missing**: All 8 events in S-AM-2 (G030–G100) and S-AM-3 (G186–G188) are Naomi audio. Alex's replies in these sessions are not in the corpus.

**Evidence that he was replying**: 
- G030 (23:55): *"So you didn't read my messages is what you're telling me right now"* — presupposes a received message.
- G188 (01:31): *"Why are you still responding to me then?"* — presupposes ongoing replies.

**Effect on the timeline**: 
- AFT-04 and AFT-05 are classified Moderate confidence because Alex's side of those exchanges is unknown.
- Alex's replies, if captured, could change the interpretation of what he was or was not conceding in those sessions.
- CURRENT_STATE_CLEAN.md §7.2D: "Phase-level Aftermath asymmetries are therefore channel-specific, not whole-of-contact."

**Resolution path**: Locate Alex's text-channel records for Jul 11 23:55–Jul 12 01:31 if they exist outside the audio corpus.

---

### 2.2 Untranscribable events B122, B127, B128

**What is missing**: Three events in the late-night barrage of CONF-02 (Jun 27 01:28–01:45) appear in screenshots but have no underlying `.aac` file. They are untranscribable.

**What is known** (from CURRENT_STATE_CLEAN.md §8.5, paraphrase): B122 — Naomi accuses Alex of only using her to "smoke gear"; B127 — Naomi tells Alex to "suffer the worst fucking misery of your life"; B128 — Naomi mocks his internal monologue.

**Effect on the timeline**: CONF-02 relies on CURRENT_STATE_CLEAN.md §8.5 for these three events. The paraphrase is from the document's own characterisation, not a verbatim transcript.

**Resolution path**: None within current corpus. The audio files do not exist.

---

### 2.3 The Nishant prior-knowledge claim

**What is claimed** (Naomi's account, G094 and G211): Alex attended Nishant's home on the Saturday before the Tuesday conflict and was told about Naomi's feelings. He then feigned ignorance when raising the topic with her.

**What the corpus shows**: G028 (Alex, S-AM-1): *"You asked me if Nishant had called me and I said no."* — Alex denies Nishant contact in a general sense, not specifically on the Saturday claimed.

**What the corpus does not show**: No event independently establishes (a) whether the Saturday meeting occurred; (b) what Nishant said; (c) whether Alex had prior knowledge; (d) whether Nishant was later asked.

**Effect on the timeline**: This claim appears at G094 (AFT-05) and G211 (AFT-13). Both are marked as participant account only. The claim cannot be confirmed or refuted from `events.jsonl` alone.

**Resolution path**: External to the corpus. Would require Nishant's account or other corroborating evidence.

---

### 2.4 B004 and C021: null transcripts

**What is missing**: B004 and C021 are audio events marked `[unclear/no clear speech detected]` (CURRENT_STATE_CLEAN.md §3). Content is unknown.

**Effect on the timeline**: Neither falls in the Aftermath. B004 is in the Conflict phase; impact on Conflict narrative is unknown without content. C021 similarly.

**Resolution path**: Manual re-listening to audio files if they exist and audio quality has improved.

---

### 2.5 Conflict-phase text events: sha256 join hole

**What is missing**: 77 of 378 events carry no `sha256` (CURRENT_STATE_CLEAN.md §7.2F). All 77 are in the Conflict phase. EID-based joins for Conflict events may be unreliable.

**Effect on the timeline**: All Aftermath events (105/105) resolve on `sha256` (confirmed in CURRENT_STATE_CLEAN.md §7.1). The Conflict incidents (CONF-01–CONF-03) rely on EID-based identification. Downstream joins to Conflict events should verify on content, not EID alone.

**Resolution path**: For Conflict events, verify quotes and content directly from `events.jsonl` rather than relying solely on EID.

---

### 2.6 EID renumbering caveat

**What occurred**: EIDs were renumbered in August 2026. CURRENT_STATE_CLEAN.md §3: *"Join artifacts to `events.jsonl` on `sha256`, never on `eid`."*

**Effect on the timeline**: All EIDs used in this timeline (e.g., G212, G189, B063) were sourced from the current `events.jsonl` and verified by content. However, any artifact predating the August renumbering that references the same event may use a different EID.

**Resolution path**: Always cross-reference by `sha256` or verbatim quote when joining to external artifacts.

---

### 2.7 Conflict-phase approximate timestamps

**What is uncertain**: 36 Conflict events carry approximate (`~`) or minute-only timestamps (CURRENT_STATE_CLEAN.md §7.2E). This affects computed latencies and gap times in CONF-01–CONF-03.

**Effect on the timeline**: The 37-minute gap in CONF-01 (B039 to B044) and the 76-second delivery window (B044 to B046) are computed from events that carry exact timestamps. These particular calculations are not affected. CONF-02's exchange-rate figures (§8.1) exclude `~`-prefixed rows per CURRENT_STATE_CLEAN.md §7.2E.

**Resolution path**: For any new latency or gap computation in the Conflict phase, exclude `~`-prefixed timestamps or report both results.

---

### 2.8 What happened after Jul 21 21:48:45

**What is unknown**: The corpus ends with G084. CURRENT_STATE_CLEAN.md §3: *"Nothing in the 12 days to 2 August."* Whether the dyad had further contact after that point, whether any resolution occurred, and whether Alex ever read AFT-13's content are all unknown.

**Effect on the timeline**: AFT-13's characterisation as "no closure" is accurate within the corpus boundary. It cannot be stated whether closure occurred or did not occur outside that boundary.

**Resolution path**: None within current corpus. Any statement about post-corpus events would require additional data sources.
