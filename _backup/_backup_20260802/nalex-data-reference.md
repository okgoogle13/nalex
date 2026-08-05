# Nalex — dataset reference

Reference notes for the structural data extracted from the Naomi & Alex Signal transcripts. This is a description of what the files contain, not a set of instructions. Coaching behaviour is governed by the project instructions.

**Extracted:** 2026-07-23 (amended 2026-07-24)
**Method:** mechanical extraction only — no interpretation, no tone judgements, no assessment of who was right
**Location:** `~/Projects/Nalex/`

---

## Speakers

| Speaker | Pronouns | In the transcript |
|---|---|---|
| **Naomi** | she / her | Provided the transcript. Messages labelled `"s": "Naomi"` |
| **Alex** | he / him | The other party. Messages labelled `"s": "Alex"` |

Only these two send messages. "Nishant", "Ned", "Freya", and "Fisher" appear as third parties referenced in conversation. That's a fact about *this transcript* only — it says nothing about anyone's role in the wider situation.

**Communication styles, as they appear structurally in the data:**

- **Naomi tends to:** send long, dense messages; focus on "reality", truth, and explicitly defining misinterpretation; prefer direct but non-confrontational in-person conversations; struggle to flex her style when the other person is overwhelmed.
- **Alex tends to:** rely heavily on audio and voice notes; view himself as straightforward while communicating with a naturally flirty kindness; struggle to accept that two people can experience the same interaction differently; use pressure `?` messages; end interactions unilaterally when frustrated.

---

## Source material

**Original transcript:** `compact_signal_transcript_for_claude.md`
Three Signal conversations spanning ~12 days, 218 events total.

| ID | Date | Duration | Events | Format |
|---|---|---|---|---|
| **A** | June 23, 2026 | ~3h05m (00:45–03:50) | 26 | Text only |
| **B** | June 26–27, 2026 | ~15h (11:30–02:34+1d) | 117 | Text + audio |
| **C** | July 4–5, 2026 | ~12.5h (12:29–00:53+1d) | 75 | Text + audio |

---

## Data files

1. **`events.final.jsonl`** — 430 chronological events, schema `{cid, eid, t, s, kind, gap, txt}`
2. **`claims.json`** — 564 extracted spans, typed `factual_assertion` / `commitment_or_plan` / `subjective_feeling`
3. **`contradictions.json`** — 3 pairs of structurally inconsistent claims
4. **`timeline_stats.json`** — durations, gaps, speaker message counts
5. **`reference_links.json`** — 13 instances of speakers referring back to past conversations
6. **`threads.json`** — 15 thematic threads
7. **`quote_index.json`** — 13 instances of speakers quoting or paraphrasing past statements
8. **`speaker_stats.json`** — event counts (121 Alex, 93 Naomi, 1 Unknown, 3 System)
9. **`nalex-data-reference.md`** — human-readable version of the above

---

## Structural flags

Eight features the extraction flagged as notable. They are pointers to places in the data, offered without conclusions attached.

**1 — Communication style incompatibility.** The data maps a mismatch between Naomi's need for explicit reality and truth-naming, and Alex's comfort with fluid ambiguity and flirtatious kindness.

**2 — Mutual expressions of friendship and grief.** Alongside conflict, both speakers voice a desire for connection and express grief at the breakdown.

**3 — The unnamed prior conversation.** In Conversation A, Naomi references "a conversation we had" that Alex claims not to recognise. It recurs as an anchor for later misunderstanding.

**4 — Who started what.** Alex's account of who initiated the sexual-tension topic changes within the same conversation. *(Contradiction 1.)*

**5 — "Not wanting to sound conceited."** Alex uses this to explain why he didn't speak more directly. Naomi contests the framing.

**6 — Unanswered questions.** Naomi asserts Alex hasn't answered her questions (the "it's not fair" incident, the "Monday night" claim). Alex asks "what are your questions?". Both loop.

**7 — How the friendship ends.** Alex ends it unilaterally and explicitly at C080–C081.

**8 — Question-mark pressure messages.** Alex sends standalone `?` or `??` messages after delays in Naomi responding.
