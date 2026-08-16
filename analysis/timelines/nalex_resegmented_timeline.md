# Nalex Incident Timeline — Revised and Audited
*Version 2. Produced 2026-08-15.*
*Sources: `events.jsonl` (378 events), `CURRENT_STATE_CLEAN.md` (Rev 6), `conflict_questions_annotated.json`.*

## Reading Rules

- **Direct observation**: verbatim quote or measurable fact from `events.jsonl`. Includes timestamps, word counts, gap calculations derived from timestamps.
- **Naomi's account** / **Alex's account**: one participant's stated claim. Not independently verified unless separately noted.
- **[inference]**: analyst's most parsimonious structural reading. Alternatives noted where live.
- All accounts are kept separate where Naomi's and Alex's differ.
- Every incident has at least one source_event_id.
- Participant claims are not promoted to independently verified facts.

## Attribution Conventions

| Prior phrasing | Revised phrasing | Reason |
|---|---|---|
| "Nishant accusation" | "Naomi's claim about prior knowledge via Nishant" | Claim is participant account only; no corroborating corpus event |
| "Alex's final word" | "Alex's final recorded event" | "Final word" implies rhetorical finality not established by record |
| "emotional blackmail" | "Naomi describes the interaction as emotional blackmail" | Participant characterisation, not an independently verified description |
| "forced me to be vulnerable" | "Naomi says she was forced into vulnerability" | Participant claim |
| "friendship register available" | "warm reciprocal exchange" | Evaluative framing; replaced with descriptive |
| suicide attempt described without attribution | "Alex refers to a past suicide attempt" | Participant claim; corpus cannot verify the biographical fact |

---

## Phase Overview

| Phase | Window | Events | Sessions | Source |
|---|---|---|---|---|
| Baseline | Apr 1 – Jun 22 | 52 | 10 | CURRENT_STATE_CLEAN.md §1 |
| Conflict | Jun 23 – Jul 5 | 221 | 10 | CURRENT_STATE_CLEAN.md §1 |
| Silence | Jul 6 – Jul 10 | 0 | — | CURRENT_STATE_CLEAN.md §1 |
| Aftermath | Jul 11 – Jul 21 | 105 | 5 | CURRENT_STATE_CLEAN.md §1; session count recomputed from `events.jsonl` using 60-min gap rule |

Channel caveat (CURRENT_STATE_CLEAN.md §7.2D): All 105 Aftermath events are `kind=audio`. The Conflict phase contains 69 `kind=text` events; none survive into July. Naomi's turns in S-AM-2 and S-AM-3 respond to apparent Alex input not in the corpus (e.g., G030: *"So you didn't read my messages is what you're telling me right now"*; G188: *"Why are you still responding to me then"*). All Aftermath asymmetry figures are upper bounds within the audio channel only.

---

## CONFLICT PHASE — Three Incidents

---

### CONF-01 — Relational Acknowledgement Dispute (afternoon, Jun 26)

| Field | Value | Source |
|---|---|---|
| incident_id | CONF-01 | — |
| phase | Conflict | timestamp |
| session | S5 | CURRENT_STATE_CLEAN.md §8.0 |
| date_time_start | 2026-06-26 16:04 | B022 |
| date_time_end | 2026-06-26 17:06 | B047 |
| source_event_ids | B021, B022, B023, B026, B028, B039, B044, B045, B046, B047 | `events.jsonl` |
| participants | Naomi, Alex | — |
| confidence | High | — |
| ordering_status | Confirmed. Precedes CONF-02 by ~5 hours (B047 → B049). | timestamp difference |

**Neutral description**: During an afternoon visit, Naomi asked Alex to acknowledge an unspoken past conversation. Alex responded that he could not acknowledge a conversation she would not name. He then sent 392 words of disclosure (B044: 307w, B045: 55w, B046: 30w) across 76 seconds of recording time immediately before arriving at her apartment. Naomi had been out of the exchange for 37 minutes (B039, 16:27:42, to B044, 17:04:56) and had no recorded window to hear the messages before he arrived.

**Direct observations**:
- B022 (Naomi, 16:04): *"I thought it was a bit weird that you wouldn't acknowledge what conversation I was talking about."*
- B023 (Alex, 16:09): *"How can I acknowledge a conversation that you won't tell me what it is? So, enlighten me."*
- B021 (Alex, 16:04): *"we talked about this in person because you're right, we should not do it over text or even voice message."* [Alex's own rule, stated by Alex.]
- B044 (Alex, 17:04:56): 307-word sexual-tension disclosure by voice note.
- B046 (Alex, 17:06:12): *"I am turning onto High Street... could you let me in the garage?"* — 76 seconds after B044 (computed: 17:06:12 − 17:04:56 = 76s).
- B047: incoming call record; Alex arrives 17:08.
- B039 (Naomi, 16:27:42): last Naomi turn before Alex's monologue. Gap to B044: 37 min 14s (computed from timestamps).

**Attributed accounts**:
- *Naomi's account (later: G182, G055, G194)*: She had not heard the voice messages before he arrived. She restates this at minimum four times in the corpus; CURRENT_STATE_CLEAN.md §8.4 confirms the timing claim is "specific, checkable, and correct" given the timestamp record.
- *Alex's account (B063, G099)*: He read her in-person quietness as concealment and avoidance.

**[inference]**: The "acknowledge this / name it first" deadlock here is structurally identical to B088–B106 (eight hours later) and G032/G173 (Aftermath, Jul 11). This is the first instance. See CURRENT_STATE_CLEAN.md §8.7a.

**significance_tags**: `acknowledgement-deadlock`, `voice-note-channel-timing`, `first-instance-retrieval-deadlock`, `directness-loop`

**Outcome**: Unresolved. Alex left. Naomi's first question sent at 21:57 (B049).

---

### CONF-02 — "Keyboard Warrior" Trigger and Overnight Escalation

| Field | Value | Source |
|---|---|---|
| incident_id | CONF-02 | — |
| phase | Conflict | timestamp |
| session | S7 | CURRENT_STATE_CLEAN.md §8.0 |
| date_time_start | 2026-06-26 21:57 | B049 |
| date_time_end | 2026-06-27 02:33 | B128 (paraphrase) |
| source_event_ids | B049, B055, B056, B062, B063, B066, B069, B072, B074, B085, B087, B088, B091, B092, B095, B107, B122, B127, B128 | `events.jsonl`; B122/B127/B128 untranscribable (CURRENT_STATE_CLEAN.md §3) |
| participants | Naomi, Alex | — |
| confidence | High (pre-01:28); paraphrase only for B122/B127/B128 | CURRENT_STATE_CLEAN.md §3 |
| ordering_status | Confirmed. | — |

**Neutral description**: Naomi's first question about the disclosure (B049, 21:57) opened an exchange that escalated over ~4.5 hours. Alex's "keyboard warrior" comment (B063, 23:56) was delivered 1m58s after a declared exit (B062, 23:54) — making it a re-entry, not an exit statement. A direct rebuttal arrived 72 seconds later (B066, 23:58). Exchange rate jumped from 5.1 turns/hr before B063 to 25.6 turns/hr after (computed from CURRENT_STATE_CLEAN.md §8.1 table). Neither party's questions were ever enumerated as a list. Alex's Conflict-phase sign-offs held in 2 of 11 instances (CURRENT_STATE_CLEAN.md §8.2). Late-night content from Naomi (B122/B127/B128, 01:28–01:45) is untranscribable.

**Direct observations**:
- B049 (Naomi, 21:57): *"Why did you ever, like, even mention the sexual tension then? I'm so confused."*
- B062 (Alex, 23:54): Declared exit. B063 follows 1m58s later.
- B063 (Alex, 23:56): Keyboard warrior comment. [Re-entry after B062. Timestamp gap computed: 23:56:48 − 23:54:50 = 1m58s per CURRENT_STATE_CLEAN.md §8.2.]
- B066 (Naomi, 23:58): *"I clearly wasn't okay... I needed to listen to your fucking voice messages, which you didn't give me a chance to listen to."* [72 seconds after B063; CURRENT_STATE_CLEAN.md §8.4 labels this the contemporaneous rebuttal.]
- B069 (Naomi): *"you literally haven't answered a single fucking one of my questions."*
- B088 (Alex): *"What are your fucking questions?"* [See CURRENT_STATE_CLEAN.md §8.3 on the retrieval deadlock.]
- B092 (Alex): *"if I was such a trans chaser, then why the fuck didn't we hook up?"*
- B095 (Naomi): *"Now I hate you."*
- B107 (Alex): *"I will not be responding to any more messages."* [Breached within 9 minutes; CURRENT_STATE_CLEAN.md §8.2.]

**Attributed accounts**:
- *Naomi's account*: She responded at her first available opportunity after hearing the voice messages; "keyboard warrior" framing mischaracterises ordinary voice-note channel latency. Direct rebuttal at B066.
- *Alex's account*: Naomi was avoidant in person and then delivered heavy emotional material by voice note the moment he drove away.
- *[inference]*: CURRENT_STATE_CLEAN.md §8.4 assesses Alex's charge as "factually false on the record" given the B046/B047 timestamps. The rebuttal at B066 is contemporaneous and specific. Both characterisations are internally consistent from each party's vantage point; the timing record supports Naomi's account of latency.

**significance_tags**: `keyboard-warrior-hinge`, `5x-escalation`, `retrieval-deadlock`, `mutual-character-attack`, `alex-exits-not-held`

**Outcome**: Cessation without agreement. B122/B127/B128 content cited from CURRENT_STATE_CLEAN.md §8.5 only — no verbatim transcript exists.

---

### CONF-03 — Boundary and Flirtation Clarification Session (Jul 4–5)

| Field | Value | Source |
|---|---|---|
| incident_id | CONF-03 | — |
| phase | Conflict | timestamp |
| session | S9/S10 | CURRENT_STATE_CLEAN.md §13.2 |
| date_time_start | 2026-07-04 22:07 | C047 |
| date_time_end | 2026-07-05 00:53 | C083 |
| source_event_ids | C047, C055, C059, C062, C065, C066, C067, C068, C072, C075, C080, C081, C082, C083 | `events.jsonl` |
| participants | Naomi, Alex | — |
| confidence | High | — |
| ordering_status | Confirmed. Last Conflict session before Silence. | timestamp |

**Neutral description**: Six days after the overnight escalation, Alex re-initiated contact. The conversation moved from logistics to the underlying dispute. Alex asked three specific clarifying questions (C066–C068) about what Naomi experienced as flirtation. Naomi said she would give specific examples but was busy. Alex declared the friendship ended (C080–C081). Naomi described this as emotional blackmail (C082). No agreed terms.

**Direct observations**:
- C047 (Alex, 22:07): *"I'm not eager to discuss it, but it clearly needs to be discussed... I don't want to lose you as a friend."* [conflict_questions_annotated.json annotation: intent = repair]
- C066 (Alex, 23:36): *"May I ask you what things I did to make you feel like I was flirting with you more so than anyone else?"* [conflict_questions_annotated.json: genuine_unanswered = true]
- C072 (Naomi, 23:44): *"this is so fucking dumb that we're doing this over voice again... I hate this."*
- C080 (Alex, 00:46): *"I think I am done with this friendship myself."*
- C081 (Alex, 00:46): *"just in case that was not direct enough for you, that was me ending the friendship."*
- C082 (Naomi, 00:49): *"It's not fair for you to do this emotional... blackmail, basically."* [Naomi describes the interaction as emotional blackmail.]
- C083 (Alex, 00:53): *"I've not really insulted you. I've not sworn at you. I've not called you a fuckwit."*

**Attributed accounts**:
- *Alex's account*: Attempted repair; met with unavailability; ended the friendship when platonic basis seemed uncertain.
- *Naomi's account*: Describes the termination as emotional blackmail (C082), not a legitimate exit.
- *[inference]*: C066–C068 (genuine, unanswered per annotation layer) establish the factual questions that the Aftermath sessions will attempt and fail to revisit.

**significance_tags**: `repair-attempt`, `boundary-clarification`, `friendship-termination-declared`, `retrieval-deadlock`, `directness-loop`

**Outcome**: Friendship declared ended. 6.8-day silence follows (CURRENT_STATE_CLEAN.md §3: silence broken Jul 11 20:07:12).

---

## SILENCE — Jul 6–10 (0 events)

No events in `events.jsonl` for Jul 6–10 inclusive. Silence broken at 2026-07-11 20:07:12 (G212, Naomi; speaker confirmed by manual listening, CURRENT_STATE_CLEAN.md §3).

---

## AFTERMATH PHASE — 13 Episodes

### Session Summary

| Session | Start | End | Events | Gap before (computed) |
|---|---|---|---|---|
| S-AM-1 | Jul 11 20:07:12 | Jul 11 22:53:24 | 40 | 6.8 days since C083 |
| S-AM-2 | Jul 11 23:55:57 | Jul 12 00:04:10 | 4 | 62.6 min after G070 |
| S-AM-3 | Jul 12 01:10:23 | Jul 12 01:31:53 | 4 | 66.2 min after G100 |
| S-AM-4 | Jul 13 19:31:56 | Jul 13 23:04:44 | 28 | ~42 hr after G188 |
| S-AM-5 | Jul 21 19:04:12 | Jul 21 21:48:45 | 29 | ~7.8 days after G200 |

---

### AFT-01 — Reconnection After Silence

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-01 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-1 | gap computation |
| event_type | Reconnection / conditional friendship offer | — |
| date_time_start | 2026-07-11 20:07:12 | G212 |
| date_time_end | 2026-07-11 20:27:26 | G019 |
| source_event_ids | G212, G170, G171, G172, G173, G174, G019 | `events.jsonl` |
| participants | Naomi (opens), Alex | — |
| confidence | High | — |
| ordering_status | First Aftermath episode. | — |

**Neutral description**: After 6.8 days of no contact following Alex's friendship termination (C081), Naomi sent the first Aftermath message (G212, 20:07:12). Exchanges were logistical and low-key for the first ~19 minutes. At 20:26, Alex named acknowledgement as a condition for resuming the friendship. This demand arrived on Alex's third turn (G173).

**Direct observations**:
- G212 (Naomi, 20:07:12, 7.3s): *"Sorry, I've been asleep all day. Whatever you want to do, dude."* [Speaker confirmed by manual listening, CURRENT_STATE_CLEAN.md §3.]
- G170 (Alex, 20:15): *"I would have came past earlier, but I've started drinking."*
- G171 (Alex, 20:16): Offer to buy her glass.
- G172 (Naomi, 20:21): Financial anxiety aside; off-conflict topic. [Subsumed; not a conflict turn.]
- G173 (Alex, 20:26): *"I wouldn't mind having my friend back just think some uh acknowledgement would be good is all."*
- G174 (Alex, 20:27): *"But I also don't wish to end in another argument."*
- G019 (Alex, 20:27): *"So if this is going to create another argument just just forget it and move on."*

**Attributed accounts**:
- *Alex's account (G173–G019)*: Wants friendship back; requires acknowledgement first; fears re-escalation.
- *Naomi's account (G032, later in S-AM-1)*: She did not know what she was being asked to acknowledge.

**significance_tags**: `naomi-opens-aftermath`, `6.8-day-silence-broken`, `alex-acknowledgement-demand`, `low-key-opening`

**Outcome**: Transitions to AFT-02 within the same session. No acknowledged break between AFT-01 and AFT-02.

---

### AFT-02 — Acknowledgement Deadlock (First Contact Session)

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-02 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-1 | gap computation |
| event_type | Accountability dispute / retrieval deadlock | — |
| date_time_start | 2026-07-11 20:30:43 | G097 |
| date_time_end | 2026-07-11 22:30:13 | G032 |
| source_event_ids | G097, G175, G096, G080, G028, G066, G176, G020, G040, G089, G085, G016, G177, G037, G065, G064, G032 | `events.jsonl` |
| participants | Naomi, Alex | — |
| confidence | High | — |
| ordering_status | Follows AFT-01 continuously within S-AM-1. | — |

**Correction from prior draft**: G096 (Alex, 20:48:49, *"What does this have to do with the price of fish though?"*) was absent from the prior source_event_ids list. Now included as subsumed. This was the only event missing from the prior timeline's accounting.

**Neutral description**: Alex's acknowledgement request (AFT-01) was met by Naomi with a deflection toward a third-party topic (a call from Nishant). For approximately two hours, Alex requested clarity; Naomi answered briefly and vaguely. Alex escalated to requiring preliminary acknowledgement before any in-person conversation (G064). Naomi asked what she was supposed to acknowledge (G032). Multiple off-conflict tangents intervene (Jamie logistics, ATO concern, Nemo 2.0 aside) and are subsumed.

**Direct observations**:
- G175 (Alex, 20:31): *"I've had radio silence and it's been a little bit hurtful, but I've endured worse."*
- G096 (Alex, 20:48): *"What does this have to do with the price of fish though?"* [Alex dismissing Nishant tangent.]
- G080 (Alex, 20:58): *"The anxiety of not knowing is going to kill me."*
- G176 (Alex, 21:54): *"You're still being very vague, and I would like just the smallest amount of clarity."*
- G064 (Alex, 22:29): *"Dude you haven't acknowledged a single thing like if you want me to come around and talk about it there needs to be like a preliminary fucking conversation."*
- G032 (Naomi, 22:30): *"What am I acknowledging? If you want to do this over the phone, let's do it. Let's go!"*

**Attributed accounts**:
- *Alex's account*: Needs acknowledgement before risking an in-person confrontation again.
- *Naomi's account*: Does not know what she is being asked to acknowledge.
- *[inference]*: Structurally identical to CONF-01's deadlock (B022/B023), 15 days earlier. Per CURRENT_STATE_CLEAN.md §8.7a, the acknowledgement demand is mutual across the corpus (Naomi: 4 Aftermath instances; Alex: 4 Aftermath instances).

**significance_tags**: `acknowledgement-deadlock`, `retrieval-deadlock-recurrence`, `alex-anxiety-stated`, `alex-in-person-condition`

**Outcome**: No acknowledgement given. Session continues to AFT-03 without break.

---

### AFT-03 — Conflicting Accounts of Jun 26

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-03 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-1 | gap computation |
| event_type | Delayed processing / account dispute | — |
| date_time_start | 2026-07-11 22:30:45 | G046 |
| date_time_end | 2026-07-11 22:53:24 | G070 |
| source_event_ids | G046, G178, G179, G031, G099, G045, G042, G180, G181, G062, G112, G182, G183, G055, G184, G070 | `events.jsonl` |
| participants | Naomi, Alex | — |
| confidence | High | — |
| ordering_status | Immediately follows AFT-02 within S-AM-1. | — |

**Neutral description**: Both parties gave their respective accounts of the June 26 events. Naomi stated she had not heard the voice messages before Alex arrived (G182 — third corpus instance of this statement). Alex stated he experienced her in-person silence as avoidance (G099). Both disputed the other's characterisation. Alex exited (G183). Naomi continued for three post-exit turns, including the first mention of the dinner debt (G184).

**Direct observations**:
- G099 (Alex, 22:36): *"last time I came over to have the conversation face-to-face you just stared at the ground... And then the second I left you started up over comments like over text."*
- G042 (Naomi, 22:40): *"that's not fair. That's not what happened. You're mischaracterizing that situation."*
- G182 (Naomi, 22:46): *"I didn't even listen to your voice messages that you sent before, right before you arrived."* [Third corpus instance; see B066, G055 for prior instances.]
- G112 (Alex, 22:45): *"you called me a chaser when I turned you down... You kind of gaslit me the whole night."*
- G180 (Naomi, 22:43): *"it's one thing to call someone a coward, it's another thing to pathologize someone and call them a narcissist."*
- G183 (Alex, 22:48): *"All right, Nelly. Have a good one. I'll speak to you another time."* [Alex Exit 1 in Aftermath.]
- G184 (Naomi, 22:49, post-exit): *"You owe me for dinner for that night."* [Dinner debt — first mention.]
- G070 (Naomi, 22:53, post-exit): *"the fact that after the fact you got angry at me for... asking you questions at all is ridiculous. It's like borderline abusive, dude."* [Naomi describes Alex's anger at her questions as borderline abusive.]

**Attributed accounts**:
- *Naomi's account*: She was not avoidant — she was uninformed. Describes Alex's subsequent anger at her questions as "borderline abusive" (G070).
- *Alex's account*: Her silence was concealment; the chaser accusation amounted to gaslighting (G112).
- *[inference]*: This is the third corpus instance of Naomi's voice-message timing claim. CURRENT_STATE_CLEAN.md §8.4 assesses the timing record as supporting her account.

**significance_tags**: `voice-message-timing-dispute`, `mischaracterisation-dispute`, `alex-exit-1-of-4`, `post-exit-continuation`, `dinner-debt-first-mention`

**Outcome**: Alex exits (G183). S-AM-1 closes at 22:53:24. Gap of 62.6 min to S-AM-2.

---

### AFT-04 — Attentiveness Dispute

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-04 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-2 | gap computation |
| event_type | Good-faith dispute / attentiveness challenge | — |
| date_time_start | 2026-07-11 23:55:57 | G030 |
| date_time_end | 2026-07-12 00:04:10 | G100 |
| source_event_ids | G030, G185, G075, G100 | `events.jsonl` |
| participants | Naomi (audio only; Alex's replies absent from corpus) | — |
| confidence | Moderate. Naomi's audio confirmed. Alex's side of exchange unknown. | CURRENT_STATE_CLEAN.md §7.2D |
| ordering_status | Second Aftermath session. S-AM-2. | — |

**Neutral description**: S-AM-2 opens 62.6 minutes after S-AM-1 closes. All four events are Naomi audio. G030's framing (*"So you didn't read my messages is what you're telling me right now"*) implies Alex replied in a channel not captured in this corpus. Core dispute: whether Alex read and engaged with her messages when first sent.

**Direct observations**:
- G030 (Naomi, 23:55): *"So you didn't read my messages is what you're telling me right now."*
- G185 (Naomi, 23:56): *"it's not obvious that you're actually listening to anything I'm saying or reading anything I'm saying."*
- G075 (Naomi, 00:02): *"You literally didn't listen or read a single thing or respond to a single question."*
- G100 (Naomi, 00:04): *"Signal does allow you to take screenshots because I have the whole fucking conversation screenshotted."*

**Attributed accounts**:
- *Naomi's account*: Alex did not read or engage with her messages when first sent; this failure is ongoing. She states she has screenshots.
- *Alex's account*: Not audible. His replies implied by G030's and G188's framing but absent from the corpus.
- *[inference]*: The dispute extends the "you didn't listen" thread from CONF-02 (B069, B107). Missing Alex-side audio is the principal limitation on this episode's interpretation.

**significance_tags**: `attentiveness-dispute`, `what-was-known-dispute`, `naomi-only-session`, `missing-alex-replies`, `screenshot-evidence`

**Outcome**: No resolution recorded. S-AM-2 closes 00:04:10. Gap of 66.2 min to S-AM-3.

---

### AFT-05 — Explicit Apology Demand and Claim About Prior Knowledge via Nishant

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-05 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-3 | gap computation |
| event_type | Accountability dispute / apology-format demand | — |
| date_time_start | 2026-07-12 01:10:23 | G186 |
| date_time_end | 2026-07-12 01:31:53 | G188 |
| source_event_ids | G186, G094, G187, G188 | `events.jsonl` |
| participants | Naomi (audio only; Alex's replies implied by G188 framing) | — |
| confidence | Moderate. Naomi's audio confirmed. Alex's side unknown. | CURRENT_STATE_CLEAN.md §7.2D |
| ordering_status | Third Aftermath session. ~42-hour gap follows before S-AM-4. | — |

**Neutral description**: S-AM-3 contains four Naomi audio events. G186 is the most explicit statement in the corpus of what Naomi states she needed from Alex. G094 contains Naomi's claim that Alex had prior knowledge of her feelings via Nishant before raising them with her. G188 implies Alex was still replying when Naomi sent this turn. G187 contains Naomi's account of having been compelled into vulnerability.

**Direct observations**:
- G186 (Naomi, 01:10): *"You haven't even apologized one single time for one single thing. In fact, not one single authentic apology."* / *"It's a type of emotional blackmail."* [Naomi describes the situation as emotional blackmail.] / *"I still want to be your friend. I'll be patient."*
- G094 (Naomi, 01:15): *"it's not cool that you went to Nashant and spoke to Nashant about the situation and you were told what was going on, and you knew what was going on, and then you acted dumb."* [Naomi's claim about prior knowledge via Nishant. No corroborating corpus event establishes what Nishant told Alex or when.]
- G187 (Naomi, 01:22): *"you kept pushing the point. Like you forced it out of me. You forced me to be vulnerable when I didn't want to be... you just wanted to reject me. That's all."* [Naomi says she was forced into vulnerability.]
- G188 (Naomi, 01:31): *"Why are you still responding to me then?... I'll keep waiting for you, dude... you to be better than this."*

**Attributed accounts**:
- *Naomi's account (all four events)*: Alex gave no authentic apology; prior knowledge of her feelings was available to him via Nishant and he used it strategically; she says she was forced into vulnerability she had been willing to let go of; she describes the situation as emotional blackmail.
- *Alex's account*: Not audible. G188 implies he was still sending replies.
- *[inference]*: G186 functions as the closest specification in the corpus of what Naomi states she needed: at minimum one authentic apology and acknowledgement of named harms. This is not the same as a demand for agreement.

**Claim status note**: Naomi's claim about prior knowledge via Nishant (G094) is a participant account. No corpus event independently establishes what Nishant communicated to Alex or when. This claim recurs at G211 (Jul 21).

**significance_tags**: `apology-demand-explicit`, `acknowledgement-absence-stated`, `naomi-claim-nishant-prior-knowledge`, `naomi-says-forced-into-vulnerability`, `naomi-only-session`

**Outcome**: Naomi states she will wait. S-AM-3 ends 01:31:53. ~42-hour gap before S-AM-4.

---

### AFT-06 — Mutual Acknowledgement and Apology Exchange

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-06 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-4 | gap computation |
| event_type | Mutual acknowledgement / bilateral apology / personal disclosure | — |
| date_time_start | 2026-07-13 19:31:56 | G053 |
| date_time_end | 2026-07-13 20:09:52 | G191 |
| source_event_ids | G053, G189, G190, G006, G010, G102, G090, G191 | `events.jsonl` |
| participants | Naomi (opens), Alex | — |
| confidence | High | — |
| ordering_status | S-AM-4 opening sub-episode. | — |

**Neutral description**: Naomi opened S-AM-4 expressing that Alex's withdrawal was emotionally immature, while simultaneously apologising for her own behaviour and offering continued friendship. Alex responded with what he described as his first authentic message from her, apologised for "his part to play," disclosed personal context about cutting people from his life including his brother (G006), and expressed understanding of rejection (G010). He exited while driving (G191, 20:09:52). This is the only recorded mutual acknowledgement event in the corpus.

**Direct observations**:
- G053 (Naomi, 19:31): *"I am sorry for... my behaviour that has caused you sadness and despair."*
- G189 (Alex, 19:42): *"that is the first honest... authentic, honest, guttural message I've got from you... And obviously, I'm sorry for my part to play in this. I just wanted some fucking acknowledgement, and you've gone above and beyond. Thank you."*
- G006 (Alex, 19:44): Personal disclosure — cutting people from his life including his brother.
- G010 (Alex, 19:45): *"I understand where it comes from... Rejection sucks, especially..."*
- G191 (Alex, 20:09): *"And I'm gone."* [Exit while driving.]

**Attributed accounts**:
- *Alex's stated account (G189)*: Her message was authentic rather than reactive. His acknowledgement is conditional on that framing. His apology ("my part to play") does not name specific harms.
- *Naomi's account (G029, Jul 21)*: *"This is the first moment you've even really acknowledged that I've said anything."* She describes this as the only such moment even at the end of the corpus.
- *[inference]*: CURRENT_STATE_CLEAN.md §13.4 states this event "did not survive the session it occurred in." The session continues with the conflict reopened at AFT-07. Alex's apology is non-specific.

**significance_tags**: `mutual-acknowledgement-single-instance`, `alex-apology-given`, `naomi-apology-given`, `alex-personal-disclosure`

**Outcome**: Both parties apologised and acknowledged. Alex exits while driving. 23-min pause follows before AFT-07.

---

### AFT-07 — Conflict Reopened; Apology Negotiation

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-07 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-4 | gap computation |
| event_type | Conflict reopening / apology negotiation | — |
| date_time_start | 2026-07-13 20:32:56 | G192 |
| date_time_end | 2026-07-13 21:13:53 | G196 |
| source_event_ids | G192, G193, G194, G034, G195, G196 | `events.jsonl` |
| participants | Naomi, Alex | — |
| confidence | High | — |
| ordering_status | Follows AFT-06 within S-AM-4. 23-min pause between G191 and G192 (computed). | — |

**Neutral description**: After a 23-minute gap (Alex driving), Naomi returned to the substantive dispute. She challenged Alex's "sponge" self-description (G193). Naomi restated the voice-message timing account (G194 — fourth corpus instance). Both parties discussed what the apology should be for (G034, G195). Naomi identified the boundary declaration as the point where things deteriorated (G196).

**Direct observations**:
- G193 (Alex, 20:33): *"I am a sponge. I will reciprocate the emotions around me because I don't have my own."*
- G194 (Naomi, 20:35): *"I hadn't even listened to your voice messages. As I've said many times, like, there's, like, three two-minute voice messages you sent right before you arrived."* [Fourth corpus instance; first at B066, then G182, then G055.]
- G034 (Naomi, 20:42): *"Well, what am I apologizing for like I'm apologizing... if my behavior has done that then I'm sorry... just as I would hope that..."*
- G195 (Naomi, 20:57): *"it's not about a list. It's not about things I did wrong. Um, it's about what hurt you... you acting like you didn't know when you did know, that hurt me a lot."*
- G196 (Naomi, 21:13): *"From my perspective, it seemed like everything changed after I mentioned that I was going to have to maybe draw some boundaries."*

**Attributed accounts**:
- *Naomi's account (G195, G196)*: The hurt was Alex appearing to feign ignorance of her feelings; the boundary declaration was the inflection point that changed his behaviour. G034 is apology negotiation (what specifically to apologise for), not a refusal.
- *Alex's account (G193)*: He reflects and reciprocates others' emotions; his earlier tone matched what he was receiving.
- *[inference]*: G034's framing ("what am I apologising for") is a request for specificity, not a denial of wrongdoing. This reading is consistent with CURRENT_STATE_CLEAN.md §13.4's description of apology negotiation.

**significance_tags**: `conflict-reopened-within-session`, `voice-message-timing-fourth-instance`, `apology-negotiation`, `boundary-as-inflection-point`, `sponge-disclosure`

**Outcome**: No resolution. Transitions into AFT-08 without break.

---

### AFT-08 — Past Suicide Attempt Reference; Harm Identification; Partial De-escalation

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-08 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-4 | gap computation |
| event_type | Personal disclosure / harm identification / partial de-escalation | — |
| date_time_start | 2026-07-13 21:25:24 | G197 |
| date_time_end | 2026-07-13 21:49:21 | G108 |
| source_event_ids | G197, G087, G021, G017, G047, G026, G108 | `events.jsonl` |
| participants | Naomi, Alex | — |
| confidence | High | — |
| ordering_status | Follows AFT-07 within S-AM-4. | — |

**Neutral description**: Alex refers to a past suicide attempt as context for his stated imperviousness to hurt from this conflict (G197). Naomi reads this as another attempt to hurt her (G087) and identifies the narcissist accusation as qualitatively more harmful than the coward accusation (G021). Naomi self-corrects mid-attack (G017). She states she has said her piece and will try not to message again (G108). She does not hold to this — AFT-09 follows 17 minutes later.

**Direct observations**:
- G197 (Alex, 21:25): *"none of it really hurt me because... there's nothing that can really be done or said to me at this point that is going to hurt me... i've already been through fucking far worse shit than this like attempted suicide."* [Alex refers to a past suicide attempt. This is Alex's stated account; the biographical fact cannot be independently verified from the corpus.]
- G087 (Naomi, 21:38): *"Exactly what you're doing. That's exactly what you're doing. You literally just trying to hurt me."*
- G021 (Naomi, 21:39): *"calling someone a coward is one thing, saying someone is a narcissist... Like, that's a different thing. Those are different ballparks."*
- G017 (Naomi, 21:43): *"You are kind of dumb. I mean, fuck, sorry. That's being mean."* [Self-correction within same turn.]
- G108 (Naomi, 21:49): *"I've said my piece... I will do my very best to not message you again unless a thought comes up."*

**Attributed accounts**:
- *Alex's account (G197)*: The conflict did not hurt him; he has endured worse. He refers to a past suicide attempt as the basis for this claim.
- *Naomi's account (G087, G021)*: G197 reads as an attempt to hurt her; the narcissist accusation is in a different category from the coward accusation.
- *[inference]*: CURRENT_STATE_CLEAN.md §13.3 labels G197 as `alex_defended_invulnerability` — "a protective frame, not a report." This is an analytical interpretation, not an established fact.

**significance_tags**: `alex-personal-disclosure`, `invulnerability-claim`, `alex-defended-invulnerability`, `naomi-names-specific-harms`, `naomi-states-pause-not-held`

**Outcome**: Naomi states she has said her piece (G108). Does not hold — AFT-09 follows at 22:06 (17.2 min later per gap computation).

---

### AFT-09 — Renewed Accusation; Neurodivergence Disclosure; Exit

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-09 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-4 | gap computation |
| event_type | Renewed accusation / personal disclosure / exit-as-regulation | — |
| date_time_start | 2026-07-13 22:06:35 | G067 |
| date_time_end | 2026-07-13 22:18:56 | G088 |
| source_event_ids | G067, G198, G199, G088 | `events.jsonl` |
| participants | Naomi, Alex | — |
| confidence | High | — |
| ordering_status | Follows AFT-08 within S-AM-4. 17.2-min gap from G108 to G067. | — |

**Neutral description**: Despite G108's stated pause, Naomi sent further turns. She stated that her earlier remark about everyone being out to hurt her was a hint about cumulative harm (G067). She stated Alex should have scrolled up rather than requiring her to repeat herself (G198). Alex cited ADHD and dyslexia as reasons scrolling was difficult, stated he was getting overwhelmed, and put his phone on silent (G199 — Exit 2 in S-AM-4). Naomi challenged the applicability of ADHD as an excuse (G088).

**Direct observations**:
- G067 (Naomi, 22:06): *"Me saying everyone's out to hurt me was actually just a subtle hint to you that you're just piling on where other people have in the past."*
- G198 (Naomi, 22:11): *"I shouldn't have to repeat myself. I shouldn't have to post screenshots... all you had to do was scroll up in the conversation and look."*
- G199 (Alex, 22:12): *"I'm just going to stop you there for a second. I'm an illiterate ADHD fucking head case... Sometimes scrolling up and reading something when you're doing six other things at once is not that easy... I'm getting worked up, so I'm actually going to put my phone on silent."* [Alex Exit 2 in S-AM-4.]
- G088 (Naomi, 22:18): *"You don't have a problem reading any of the other..."* [Disputes ADHD applicability.]

**Attributed accounts**:
- *Naomi's account (G198)*: Scrolling up is minimal labour; documented facts should not require repetition.
- *Alex's account (G199)*: Scrolling while occupied is genuinely difficult with ADHD and dyslexia; he is overwhelmed and exits.
- *[inference]*: CURRENT_STATE_CLEAN.md §9.1 (Flooding Hypothesis) frames Alex's exits as nervous-system regulation rather than strategic avoidance. This is an analytical interpretation, not an established motive.

**significance_tags**: `alex-neurodivergence-disclosure`, `retrieval-deadlock-recurrence`, `alex-exit-2-of-4`, `naomi-continues-after-stated-pause`

**Outcome**: Alex exits (G199). Naomi sends one further turn (G088). One more post-exit turn follows (AFT-10, 45.8 min later).

---

### AFT-10 — Post-exit Communication Style Complaint; Session Close

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-10 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-4 | gap computation |
| event_type | Post-exit continuation / communication style complaint | — |
| date_time_start | 2026-07-13 23:04:44 | G200 |
| date_time_end | 2026-07-13 23:04:44 | G200 |
| source_event_ids | G200 | `events.jsonl` |
| participants | Naomi (post-exit; Alex has exited at G199, 22:12) | — |
| confidence | High | — |
| ordering_status | Closes S-AM-4. 45.8-min gap from G088 to G200 (computed). 7.8-day silence follows. | — |

**Neutral description**: 45.8 minutes after G088 (and 52 minutes after Alex's exit at G199), Naomi sent one final turn in S-AM-4. She objected to what she described as backhanded inferences in Alex's communication, including a comparison to her father.

**Direct observations**:
- G200 (Naomi, 23:04): *"I have to say that I don't very much like the way you've been speaking to me tonight. A lot of your comments are underlaid with backhanded inferences, like, I'm not your dad... He never did that."*

**Attributed accounts**:
- *Naomi's account (G200)*: Alex's communication style contained objectionable backhanded inferences, including an implied comparison to her father.
- *[inference]*: This is the third post-exit turn Naomi sends in S-AM-4 (after G088 and G200). Alex's side is not available after G199.

**significance_tags**: `post-exit-continuation`, `communication-style-complaint`, `session-close`

**Outcome**: S-AM-4 closes at 23:04:44. Longest inter-session gap in Aftermath follows: ~7.8 days before S-AM-5.

---

### AFT-11 — Warm Reciprocal Exchange (S-AM-5 Opening)

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-11 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-5 | gap computation |
| event_type | context_episode | — |
| significance | contrast_before_escalation | — |
| date_time_start | 2026-07-21 19:04:12 | G201 |
| date_time_end | 2026-07-21 21:13:03 | G061 |
| source_event_ids | G201, G073, G050, G202, G091, G203, G204, G023, G205, G039, G079, G107, G063, G206, G072, G003, G069, G103, G061 | `events.jsonl` |
| participants | Naomi (opens), Alex | — |
| duration | 128.9 min (computed: G061 21:13:03 − G201 19:04:12) | timestamp difference |
| confidence | High | — |
| ordering_status | S-AM-5 opening sub-episode. Retained as context_episode to account for the abrupt shift in AFT-12. | — |

**Neutral description**: After a 7.8-day gap following S-AM-4, Naomi opened S-AM-5 with a message about gambling winnings and new synthesisers. Alex responded and proposed dropping off a synthesiser-related item. Both parties engaged in approximately 129 minutes of warm reciprocal exchange across gambling, synthesisers, logistics, and cultural in-jokes. Neither party introduced conflict content. This episode is retained as a context episode because it directly precedes AFT-12's 6-minute escalation and is necessary to interpret the abruptness of that shift.

**Direct observations**:
- G201 (Naomi, 19:04): Gambling wins and new synthesisers.
- G050 (Alex, 19:25): *"How much did you win this week?"*
- G202 (Alex, 19:26): Synthesiser/cork drop-off offer.
- G091 (Naomi, 19:33): *"I grant you permission. I bequeath upon you the permiss of her lady, Naomi."* [Playful mock-formal.]
- G206 (Alex, 20:53): Cultural in-joke exchange opens.
- G061 (Alex, 21:13): *"I'm fucking starving. I haven't had dinner yet."* [Last warm-exchange turn before G207.]

**Attributed accounts**:
- *[inference]*: CURRENT_STATE_CLEAN.md §13.3 labels this pattern `alex_topic_contingent_availability`: warm reciprocal exchange is available; conflict-adjacent topics trigger withdrawal. This is an analytical characterisation, not a stated intent.

**significance_tags**: `context_episode`, `contrast_before_escalation`, `warm-reciprocal-exchange`, `naomi-opens-session-5`

**Outcome**: Transitions to AFT-12 when Naomi raises the dinner debt at 21:14:31 (G207). Elapsed since G061: 1m28s.

---

### AFT-12 — Dinner Debt Trigger; Conflict Fatigue; Alex's Final Recorded Event

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-12 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-5 | gap computation |
| event_type | Topic-contingent withdrawal / final exit | — |
| date_time_start | 2026-07-21 21:14:31 | G207 |
| date_time_end | 2026-07-21 21:20:15 | G209 |
| source_event_ids | G207, G022, G078, G059, G208, G209 | `events.jsonl` |
| participants | Naomi, Alex | — |
| elapsed_to_exit | 5 min 44 sec (computed: G209 21:20:15 − G207 21:14:31) | timestamp difference |
| confidence | High | — |
| ordering_status | Follows AFT-11 within S-AM-5. | — |

**Correction from prior draft**: G078 (Naomi, 21:17:30) was absent from the prior source_event_ids list. Now added as primary.

**Neutral description**: Naomi raised the dinner debt she had first mentioned at G184 (Jul 11). Alex immediately categorised this as re-opening the larger conflict (G022). Naomi disputed this characterisation (G078, G208). Alex stated the purpose of raising it was unclear (G059) and issued his final recorded event in the corpus (G209). Elapsed time from dinner-debt mention to Alex's exit: 5 min 44 sec (computed).

**Direct observations**:
- G207 (Naomi, 21:14): *"You owe me dinner from the last time I saw you I haven't forgotten."*
- G022 (Alex, 21:16): *"Are you starting this up again? Is that what I'm hearing?"*
- G078 (Naomi, 21:17): *"Why do you disagree with me about you saying that you would pay for dinner that night? I don't understand."*
- G059 (Alex, 21:19): *"Why even bring it up is what I'm saying. What is this gonna achieve?"*
- G208 (Naomi, 21:19): *"What do you mean, bringing up dinner? Am I not allowed to talk about dinner?... I wasn't bringing it up. You brought it up, apparently."*
- G209 (Alex, 21:20): *"Okay, and on that note, I will see you another time."* [Alex's final recorded event in the corpus.]

**Attributed accounts**:
- *Alex's account (G022, G059)*: Raising the dinner debt was re-opening the larger conflict; no productive purpose served.
- *Naomi's account (G078, G208)*: Dinner was a separate practical matter; she was not intending to raise the main dispute. She states Alex categorised the topic and brought it up.
- *[inference]*: CURRENT_STATE_CLEAN.md §9.3 frames Alex's response as conflict fatigue. CURRENT_STATE_CLEAN.md §13.3 labels the pattern `alex_topic_contingent_availability`. Both are analytical characterisations.

**significance_tags**: `dinner-debt-trigger`, `alex-final-recorded-event`, `conflict-fatigue`, `topic-contingent-withdrawal`

**Outcome**: Alex's final recorded event at 21:20:15. Naomi continues for 28 min / 6 turns / 765 words (AFT-13). Corpus ends at 21:48:45.

---

### AFT-13 — Final Accountability Protest; No Closure; Corpus End

| Field | Value | Source |
|---|---|---|
| incident_id | AFT-13 | — |
| phase | Aftermath | timestamp |
| session_id | S-AM-5 | gap computation |
| event_type | Post-exit continuation / accountability demand / corpus end | — |
| date_time_start | 2026-07-21 21:20:55 | G058 |
| date_time_end | 2026-07-21 21:48:45 | G084 |
| source_event_ids | G058, G029, G210, G211, G012, G084 | `events.jsonl` |
| participants | Naomi (post-exit; Alex's final recorded event was G209, 21:20:15) | — |
| post_exit_duration | 28 min 30 sec (computed: G084 21:48:45 − G209 21:20:15) | timestamp difference |
| words | 765 (CURRENT_STATE_CLEAN.md §13.3) | — |
| confidence | High for Naomi's audio. Naomi's claim about prior knowledge via Nishant is participant account only. | — |
| ordering_status | Final episode in corpus. | — |

**Neutral description**: After Alex's final recorded event (G209, 21:20:15), Naomi continued for 28 minutes across 6 turns. Core content: she stated no substantive conversation had taken place (G058); named AFT-06 as the only instance of Alex acknowledging what she had said (G029); appealed to the record as uncontestable (G210); restated her claim about prior knowledge via Nishant (G211); named the irony of Alex's repeated "I'm not having this conversation" exits (G012, G084). The corpus ends with G084.

**Direct observations**:
- G058 (Naomi, 21:20, 40 sec after G209): *"We haven't even had one single conversation about it yet."*
- G029 (Naomi, 21:35): *"you haven't taken any amount of responsibility, or you haven't even acknowledged it. This is the first moment you've even really acknowledged that I've said anything. You just go silent, you don't even respond. You've not said sorry."*
- G210 (Naomi, 21:38): *"Do you disagree that that's not... the canonical truth? Because it actually is. You can't argue with the record."*
- G211 (Naomi, 21:42): *"on the Saturday night prior to the Tuesday, you went into Nishant's house and asked Nishant what was going on and Nishant told you."* [Naomi's claim about prior knowledge via Nishant; second corpus instance, first at G094. No corroborating event.]
- G012 (Naomi, 21:45): *"Can't say not having this conversation again and again and again when you haven't even had the conversation one time."*
- G084 (Naomi, 21:48:45): *"The irony of the line of, um, I'm not having this conversation is that you've been saying I'm not having this conversation the moment since you left my house on that Friday."* [Last event in corpus.]

**Attributed accounts**:
- *Naomi's account (G029)*: AFT-06 (G189, Jul 13) was the only time Alex acknowledged what she said. She notes it but frames it as the exception proving the absence.
- *Naomi's account (G210–G211)*: Nishant told Alex what was happening before Alex raised it with her; she frames this as an established fact ("canonical truth"). No corroborating corpus event.
- *Alex's account*: Not available. Alex has exited at G209.
- *[inference]*: CURRENT_STATE_CLEAN.md §13.4: *"The Aftermath has no closure event. No mutual ending, no repair turn, no agreed terms."* Tagged `dyad_no_closure_event`. Corpus ends mid-protest; what followed after 21:48:45 is unknown.

**Claim status note**: Naomi's claim about prior knowledge via Nishant (G211) is a participant account. She frames it as factual ("canonical truth," "you can't argue with the record") but no corpus event independently establishes this claim. See also G094 (AFT-05) for the first instance.

**significance_tags**: `no-closure-event`, `post-exit-continuation`, `corpus-end`, `naomi-last-word`, `dyad-no-closure-event`

**Outcome**: Corpus ends. No Alex response. No agreed close. CURRENT_STATE_CLEAN.md §3: last event is G084, 21 July 21:48:45.

---

## Coverage Table — All 13 Candidate Aftermath Episodes

| # | Candidate Episode | Evidenced? | Incident(s) | Notes |
|---|---|---|---|---|
| 1 | Reconnection after silence | Yes | AFT-01 | G212 (Jul 11 20:07:12); 6.8-day silence confirmed |
| 2 | Explanation of original conflict / delayed processing | Yes | AFT-03, AFT-07 | Voice-message timing account appears 4x: B066, G182, G055, G194 |
| 3 | Reopening of unresolved conflict | Yes | AFT-07 | Within S-AM-4; 23-min gap after mutual acknowledgement (AFT-06) |
| 4 | Acknowledgement / accountability dispute | Yes | AFT-02, AFT-05, AFT-06, AFT-13 | Recurring across all 5 sessions; AFT-06 is partial resolution |
| 5 | Dispute over what was known, ignored, or understood | Yes | AFT-04 | S-AM-2; attentiveness challenge; Nishant knowledge claim at AFT-05/AFT-13 |
| 6 | Reality, flirtation, and boundary clarification | Partial | AFT-11 | Warm reciprocal exchange present; no explicit flirtation re-negotiation in Aftermath sessions |
| 7 | Alex's account of feeling hurt or invalidated | Partial | AFT-02 (G175), AFT-03 (G099) | "Radio silence... a little bit hurtful" (G175); "punching bag" phrasing in CONF-02 (Conflict) not Aftermath |
| 8 | Apology-format negotiation | Yes | AFT-05, AFT-06, AFT-07 | G186 (demand stated); G189 (non-specific apology delivered); G034 (what to apologise for) |
| 9 | Trauma or sensitivity disclosure | Yes | AFT-08, AFT-09 | G197 (Alex refers to a past suicide attempt); G199 (ADHD/dyslexia disclosure) |
| 10 | Response to that disclosure | Partial | AFT-08, AFT-09 | Naomi reads G197 as attempt to hurt her (G087); disputes ADHD applicability to scrolling (G088); does not engage with disclosures as disclosures |
| 11 | Renewed accusations or defensive escalation | Yes | AFT-09, AFT-12 | G067/G198 in S-AM-4; G022/G059/G208 in S-AM-5 |
| 12 | Requests to pause, take space, or stop | Partial | AFT-08, AFT-09, AFT-12 | G108 (Naomi states pause — not held); G199 (Alex exit-as-regulation); G209 (Alex final recorded event) |
| 13 | Final accountability exchange and sign-off Jul 21 | Yes | AFT-13 | G029, G012, G084; no mutual sign-off; Naomi continues 28 min post-exit |

Episodes 6, 7, 10, and 12: present but partial. No candidate episode is entirely absent from the corpus.

---

## What the Prior Three-Incident Framing Missed

The prior Aftermath framing (reconnection / acknowledgement dispute / corpus end) collapsed or omitted:

1. **Two distinct Naomi-only sessions** (S-AM-2 / S-AM-3) — losing the S-AM-2 attentiveness dispute (AFT-04) and S-AM-3's explicit apology-format demand and claim about prior knowledge via Nishant (AFT-05).
2. **The single mutual acknowledgement event** (AFT-06, G189) — subsumed into the surrounding dispute, obscuring that it occurred and that the conflict reopened 23 minutes later.
3. **Both personal disclosures** (G197: Alex refers to a past suicide attempt; G199: ADHD/dyslexia) entirely.
4. **The warm reciprocal exchange** (AFT-11, 129 min) as a structurally distinct sub-episode — necessary to interpret the 5m44s collapse at AFT-12.
5. **The 7.8-day gap** between S-AM-4 and S-AM-5 as a structural break.
6. **The distinction** between Naomi's stated pause at G108 ("I've said my piece") and her actual continuation 17 minutes later (G067) — a behavioural fact.
