# Nalex Project: Current State — August 2026

**This is the single source of truth for the dataset and its findings.** Ignore all previous `HANDOVER_TO_CLAUDE` docs, which contain conflicting or stale instructions.

## 1. What the Corpus Contains

The canonical timeline is **`events.jsonl`** (378 events). It covers April to July 2026.
It is divided into three structural phases:

1. **Baseline Phase** (April 1 – June 22): 160 events. This period shows near-parity volume between Naomi and Alex (4,885 words to 4,228 words). It establishes their normal communication baseline.
2. **Phase 1: Conflict** (Conversations A/B/C, June 23 – July 5): 218 events. The primary conflict block. 
3. **Phase 2: Aftermath** (July 11 – July 21): 114 events. Characterized by intermittent contact, long silences, and a significant shift in Naomi's message volume.

**What is EXCLUDED (The Purge):**
- **Dec–March Audio**: 30 events from December 2025 to March 2026 were completely removed from `events.jsonl` and all downstream JSON artifacts. These were discovered to be Naomi talking to third parties (Jake and Pauly), not Alex. Alex sent zero detectable messages during this period.
- **Jake & Holly**: Audio mathematically resembling Alex's summer fingerprint but manually identified as Jake and Holly was purged.
- *Any previous LLM instruction claiming a "speaker profile reversal" in the winter months (Directive 3) is invalid and must be ignored. The reversal was an artifact of third-party contamination.*

## 2. The Three Stable Findings

Across every pipeline re-run, fingerprint rebuild, and artifact correction, these three findings have remained robust. Use these as the structural ground-truth for behavioral coaching:

1. **The July Volume Gap (2.5×):** In the Aftermath, Naomi sent roughly 7,500 words across 65 messages compared to Alex's ~3,000 words across 49 messages. This volume gap is specific to the post-fight aftermath, not a standing feature of their friendship (which was at parity in April–June).
2. **Alex Replies Faster, Naomi Writes Longer:** Alex's median reply latency is faster (122s vs 140s), but his messages are shorter (median 26 words vs 67). After the conflict, Naomi's message length roughly doubled, while Alex's stayed the same.
3. **Unanswered Questions:** In the Aftermath, half of Naomi's questions go unanswered (16 of 31, 52%). Alex's questions are ignored at a much lower rate (3 of 14, 21%). 

## 3. Verified Corrections & Known Gaps

- **The 11 July Reconnection:** The 6.8-day silence following the conflict was broken by a 7.3-second message on 11 July at 20:07 (*"Sorry, I've been asleep all day"*). Originally labeled `Unknown`, manual listening confirmed the speaker was **Naomi**.
- **Permanent Gaps:** Three Conflict-phase events (`B122`, `B127`, `B128`) exist in screenshots but have no underlying `.aac` audio files. They are permanently untranscribable gaps in the timeline.
- **ID Integrity:** `events.jsonl` EIDs were renumbered in August. All downstream artifacts (like `aftermath_stats.json`, `claims.json`, `turn_structure_aftermath.json`) have been structurally repaired to point to the correct events.

## 4. Rules

This project is strictly in **Analysis Mode**. There is no coaching system, playbook, or message drafting. The focus is exclusively on structural extraction, identifying patterns, assessing fairness, and analyzing the emotional and factual dynamics present in the transcripts and data artifacts. Do not draft messages or prescribe actions for the user.
