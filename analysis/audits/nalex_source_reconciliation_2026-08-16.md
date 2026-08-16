# Nalex — Source Reconciliation: Canonical Summary (6) vs Resegmented Timeline (16)

*Produced 2026-08-16. Inputs: `nalex_canonical_summary.md/.json`, `nalex_resegmented_timeline.md` (v2), `nalex_incidents.json` (v2, 16 records), `nalex_event_audit.md`, `nalex_claims_and_uncertainties.md`, `artifacts/inventories/all_incidents_inventory.md`, `artifacts/timelines/*.timeline.md`. No inference beyond what these files state.*

---

## Headline

**The canonical summary is not a summary of the 16-incident work. It is the superseded predecessor of it.**

| File | Version | Generated | Incidents |
|---|---|---|---|
| `nalex_canonical_summary.md/.json` | 1.0 | 2026-08-14 21:23 | 6 (3 Conflict + 3 Aftermath) |
| `nalex_resegmented_timeline.md` / `nalex_incidents.json` | 2 | 2026-08-15 | 16 (3 CONF + 13 AFT) |
| `nalex_event_audit.md` | — | 2026-08-15 | 105 Aftermath events → AFT-01…AFT-13 |
| `artifacts/inventories/all_incidents_inventory.md` | — | 2026-08-14 | **7** (4 Conflict + 3 Aftermath) |

Three facts establish the ordering:

1. `nalex_canonical_summary.json` carries `"timeline_version": "1.0"` and `generated_at: 2026-08-14T21:23:00+10:00`.
2. The two summary files are a byte-for-byte split of the older `artifacts/timelines/canonical_incidents.timeline.md` (same overview prose, same six events, same generated_at). They are a rename, not a new synthesis.
3. `nalex_resegmented_timeline.md` v2 contains a section titled **"What the Prior Three-Incident Framing Missed"** — an explicit, itemised critique of the summary's Aftermath framing.

So the instruction "treat the canonical summary as authoritative and flag conflicts with the 16-incident audit" inverts the actual provenance. Flagging follows.

**Also note: there are three incident lists in the folder, not two.** The Aug-14 inventory has 7 (it splits the Jun 26 afternoon hangout out as its own incident, which the summary drops). Any "6 vs 16" framing already misses this.

---

## Conflict phase — counts agree at 3, contents do not

| Canonical summary (v1) | Resegmented (v2) | Status |
|---|---|---|
| — | **CONF-01** — Relational acknowledgement dispute, Jun 26 16:04–17:06 (B021–B047) | **Absent from v1** |
| #1 Keyboard Warrior Accusation, Jun 26 23:56 (B063) | folded into **CONF-02** | v1 splits one session in two |
| #2 Retrieval Deadlock, Jun 27 00:00–02:33 (B088_B095) | folded into **CONF-02** — Jun 26 21:57 → Jun 27 02:33 (B049–B128) | " |
| #3 "It's Over" Session, Jul 4–5 00:07 (C074) | **CONF-03** — Jul 4 22:07 → Jul 5 00:53 (C047–C083) | Same session, different framing and anchor |

Three specific conflicts:

- **v1 omits the origin.** v1's Conflict phase opens at 23:56 with the keyboard-warrior voice note. v2's CONF-01 places the origin ~8 hours earlier: the afternoon acknowledgement deadlock, the 392 words of disclosure across 76 seconds sent immediately before Alex arrived, and the 37-minute window in which Naomi had no recorded opportunity to hear them. v2 calls this the *first instance* of the deadlock that then repeats twice. v1 has no record of it.
- **v1 mis-anchors the keyboard-warrior event.** v1 presents B063 as a standalone incident. v2's direct observation: B063 (23:56:48) came 1m58s after Alex's declared exit B062 (23:54:50) — a **re-entry, not an exit statement** — with rebuttal 72 seconds later. Turn rate jumps 5.1 → 25.6/hr across that point. v1 loses the hinge structure entirely.
- **Different anchor event for Jul 4–5.** v1 cites `C074`; CONF-03's source_event_ids are C047, C055, C059, C062, C065–C068, C072, C075, C080–C083. C074 is not among them. v1's outcome ("both acknowledge the structure has broken down") also differs from v2's ("Alex declared the friendship ended, C080–C081; Naomi described it as emotional blackmail, C082").

**Unresolved date discrepancy:** v1 says Conflict = Jun 26 – Jul 5. v2's phase table says **Jun 23 – Jul 5, 221 events**. No CONF incident covers Jun 23–25. Unexplained in both files.

---

## Aftermath phase — this is where the two sources materially disagree

| Canonical summary (v1) | Resegmented (v2) | Status |
|---|---|---|
| #4 The Reconnection, Jul 11 20:07 (G212) | **AFT-01** | Agrees |
| #5 Acknowledgement Deadlock, Jul 11 20:26 (`G173_G032`) | **AFT-01** (G173, 20:26:51) + **AFT-02** (G032, 22:30:13) | Composite ID straddles two incidents; 2h03m compressed to one timestamp |
| — | **AFT-03 … AFT-10** | **Absent from v1 — 8 incidents** |
| #6 Final Sign-off, Jul 21 19:04–21:48 (G084) | **AFT-11** + **AFT-12** + **AFT-13** | v1 treats the whole 2h44m session as one incident |

### The main gap

v1 has **zero coverage of Jul 12 and Jul 13**. Everything between Jul 11 23:55 and Jul 13 23:04 — sessions S-AM-2, S-AM-3 and all of S-AM-4 — is missing. Per the event audit that is **60 of 105 Aftermath events**. What goes with it:

1. **AFT-06 / G189 — the only substantive acknowledgement and apology from Alex in the entire corpus** ("my part to play"; names her message as "authentic, honest, guttural"), and the fact that the conflict reopened 23 minutes later (AFT-07).
2. **AFT-05 / G186** — Naomi's explicit apology demand, and the first of two Nishant prior-knowledge claims (G094).
3. **AFT-04** — the S-AM-2 attentiveness dispute ("you didn't read my messages"), including Naomi stating she has the conversation screenshotted (G100).
4. **AFT-08 / G197** and **AFT-09 / G199** — both personal disclosures, and how each was received.
5. **AFT-07 / G196** — Naomi naming her boundary declaration as the inflection point ("everything changed after I mentioned that I was going to have to maybe draw some boundaries").
6. **G108 → G067** — Naomi states a pause, then continues 17 minutes later. A behavioural fact, not a characterisation.

**Consequence, stated plainly:** any visual artifact built from v1 will represent Alex as never having acknowledged anything at any point. Per the corpus that is false. This is the single highest-cost error in using v1 as the authoritative list.

### Two smaller ID errors in v1

- **v1 #6 anchors the sign-off to G084.** Per the audit, G084 (21:48:45) is *Naomi's* last event. **Alex's final recorded event is G209 (21:20:15).** v1's prose is right in substance ("Alex signs off, Naomi continues ~28 min"); the g_id is wrong.
- **v1 #5's `G173_G032`** is a synthetic composite spanning two hours and two v2 incidents. Not usable as a schema key.

### Contradiction sets don't match

- v1 JSON carries **one** contradiction: `B063_vs_B044` (keyboard-warrior premise).
- v2's CONF/AFT records carry the same premise plus the mischaracterisation dispute (AFT-03) and the baby-photos/paintings dispute (G181).
- `nalex_claims_and_uncertainties.md` adds eight open uncertainties that v1 carries none of — notably **missing Alex-side audio in S-AM-2 and S-AM-3** (Naomi's turns there respond to input not in the corpus), untranscribable B122/B127/B128, and the Nishant claim having no corroborating corpus event.

---

## Separate issue: one older artifact contains a materially wrong event reading

`artifacts/timelines/all_critical_incidents.timeline.md` (v3.0, Aug 14 19:46) describes **G042** and **G181** as a physical house visit on 2026-07-11 — "Alex brings Naomi to his house, puts on music, closes the door, and shows photos" — tagged `boundary_crossing_triggered_distress`.

Per the Aug-15 event audit, both are audio events inside S-AM-1:

- G042 (Jul 11 **22:40:44**, Naomi) — "that's not fair. That's not what happened. You're mischaracterizing that situation."
- G181 (Jul 11 **22:43:31**, Alex) — baby-photos vs paintings clarification, subsumed in AFT-03.

They are the parties *disputing a past visit*, not a visit occurring on Jul 11. The same misreading propagates into `all_loops_significant_events.timeline.md`. Neither is part of the 6-vs-16 question, but both sit in the folder and would corrupt anything built from them. Recommend quarantining both to `_archive/` regardless of which incident list you pick.

---

## Summary of every conflict flagged

| # | Conflict | Severity |
|---|---|---|
| 1 | v1 is dated earlier than, and explicitly superseded by, v2 | Blocking |
| 2 | v1 omits 8 Aftermath incidents (AFT-03…AFT-10) and 60 of 105 Aftermath events | Blocking |
| 3 | v1's omission removes the corpus's only mutual acknowledgement (AFT-06/G189) | Blocking |
| 4 | v1 omits CONF-01, the first instance of the deadlock | High |
| 5 | Three incident lists exist (6 / 7 / 16), not two | High |
| 6 | v1 #6 anchored to G084; Alex's final event is G209 | Medium |
| 7 | v1 #5 uses composite `G173_G032` spanning two v2 incidents | Medium |
| 8 | v1 cites C074 for Jul 4–5; not in CONF-03's source events | Medium |
| 9 | Conflict phase start: Jun 26 (v1) vs Jun 23 (v2 phase table) | Low, unexplained |
| 10 | `all_critical_incidents.timeline.md` misreads G042/G181 as a physical visit | High, separate |
| 11 | No event-level audit exists for the 221 Conflict events; CONF-01…03 not audited to AFT standard | Low, known gap |

---

## What I need from you

Your standing instruction is "canonical summary is authoritative; flag conflicts." I've flagged them, and on the evidence I don't think that instruction should stand. Three options:

**A — Make v2 authoritative (recommended).** `nalex_incidents.json` (16 records, full schema: source_event_ids, speaker_accounts, key_quotes, confidence, ordering_status, outcome) becomes the artifact source. Regenerate the canonical summary as a genuine rollup of CONF-01…03 + AFT-01…13. Cost: one regeneration pass.

**B — Keep a 6-incident presentation layer, re-derived from v2.** Useful if 6 is the right granularity for mobile artifacts. Fix the IDs and timestamps, and add at least one incident covering Jul 12–13 so the acknowledgement event isn't invisible. Cost: same pass, plus a defensible rollup rule.

**C — Keep v1 as-is.** Your stated default. You accept that artifacts will show no acknowledgement from Alex at any point, and will omit both disclosures, the apology negotiation, and 60 of 105 Aftermath events.

Also, independent of A/B/C: confirm whether to quarantine `all_critical_incidents.timeline.md` and `all_loops_significant_events.timeline.md`.

---

## Sources

All local, under `Projects/Nalex/`:

- `_canonical_strong/analysis/conflict_analysis/nalex_canonical_summary.md` / `.json`
- `_canonical_strong/analysis/conflict_analysis/nalex_resegmented_timeline.md`
- `_canonical_strong/analysis/conflict_analysis/nalex_incidents.json`
- `_canonical_strong/analysis/conflict_analysis/nalex_event_audit.md`
- `_canonical_strong/analysis/conflict_analysis/nalex_claims_and_uncertainties.md`
- `artifacts/inventories/all_incidents_inventory.md`
- `artifacts/timelines/canonical_incidents.timeline.md`, `all_critical_incidents.timeline.md`, `all_loops_significant_events.timeline.md`
