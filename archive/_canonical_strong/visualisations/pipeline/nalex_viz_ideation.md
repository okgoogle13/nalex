# Nalex Visualization Ideation — 4 Questions × 3 Interpretation Levels

**Status:** ideation only. No render produced. Per `index.md` §11, any variation selected here must first be flattened into `viz_schema_template.md` form before a rendering model touches it.

**Scope:** 12 variations across the 4 known visual questions. Each question gets three tiers:

| Tier | Name | Rule |
|---|---|---|
| **A** | Neutral / evidence-only | Measured quantities and their definitions. No relational language. |
| **B** | Lightly interpretive | Adds framing, ordering, or a cautious hedge ("appears consistent with"). |
| **C** | Opinionated | Explicit relational/emotional reading, drawn **only** from `phase_profile.json → tag_vocabulary.emotional_tags`, which the project already labels `INTERPRETATION`. |

**Tier-C constraint:** Tier C does not invent emotional vocabulary. It renders the project's own pre-declared interpretive tags, each carried into the artifact with its `INTERPRETATION:` prefix intact. This keeps the interpretation layer auditable and prevents the rendering model from generating new themes.

**Ranking criterion used throughout:** information added beyond the already-published headline, divided by risk of misreading. A variation that restates a known finding cleanly ranks below one that decomposes it — unless the decomposition rests on weak evidence.

---

## §0. Data-integrity constraints that bind every variation

These were verified against the inputs during this pass. Four of them change what can honestly be drawn.

**0.1 — RESOLVED. `genuine_unanswered` disagreed between the CSV and JSON exports; the CSV has been regenerated from the canonical JSON.**
`conflict_questions_annotated.csv` previously flagged **7 of 17** questions `yes` against `conflict_questions_annotated.json`/`conflict_questions_summary.json`'s **3 of 17** `true`. `refactor_questions_v2.py` — the live annotation generator per `index.md` §7.1 — writes the JSON and summary files directly and hardcodes `genuine_unanswered=True` for exactly 3 substring matches; it never touches the CSV. The CSV was a stale export from an earlier hand-annotation pass that predated this script and was never regenerated. Both files were added in the same squashed commit, so git history couldn't disambiguate — the generator logic did.

The CSV has been regenerated from the JSON (2026-08-06): all 17 rows now agree at **3/17** across every field, including `genuine_unanswered`. The figure in `nalex_viz_schema.json` (3/17) was correct throughout. The Q4 render restriction below no longer applies.

**0.2 — There is no per-event reply-latency series anywhere in the input set.**
- `events.jsonl → gap` is a **string** label, not seconds: 206 of 217 non-null values are `'0m'`, one is `'start'`, and only 10 carry real durations (`'3d07h40m'`, `'1h25m'`, …). It marks session boundaries; it is not a latency field.
- `gap_stats_out.json` has 105 numeric `gap_sec` values that join 105/105 on `sha256`, but they are **elapsed time since the previous event regardless of speaker** — 43 same-speaker, 45 cross-speaker, 17 with an unresolved predecessor (`prev_eid_unresolved`). Its cross-speaker subset yields Naomi 361s / Alex 97s, which does **not** reproduce the published Aftermath medians (169s / 122s). It also covers the Aftermath window only.

Consequence: **no distribution, violin, or histogram of reply latency is possible.** Question 2 can only be drawn from phase-level medians. Anything richer would require a metric not present in the allowed inputs.

**0.3 — `aftermath_stats.json` uses a wider window than the canonical Aftermath phase.**
Its window is "all events dated 2026-07-05 or later" = **115 events**; canonical Aftermath (`index.md` §3) is 2026-07-11..2026-07-21 = **105 events**. Its `overall` block (Naomi 66 turns / 7,557 w; Alex 49 / 2,978) therefore does not match `phase_profile.json` (61 / 6,852; 44 / 2,181) and **must not be mixed with it**. Its `sessions` array is still usable, but session 0 ("5 Jul — the night both of them said it was over") belongs to the Conflict phase and must be excluded or visually separated.

**0.4 — Conflict latency medians are ranges, and Baseline medians rest on 7–8 observations.**
`phase_profile.json` gives Conflict medians as strings `"112-120"` (Naomi) and `"70-94"` (Alex), with `latency_ratio_N_over_A` = `"1.2-1.7"`, because 36 events carry `timestamp_inferred`. `baseline_comparison_audit.json` reports the point values 120 / 94 — the top of each range. The Baseline note states its medians rest on 7 (Naomi) and 8 (Alex) observations. **Question 2 is the evidentially weakest of the four** and every variation under it must render Conflict as a band, not a point.

**0.5 — Secondary constraints.**
- *Modality.* Baseline and Aftermath are 100% audio (52/52, 105/105). Conflict is mixed: 147 audio, 69 text, 2 media, 3 call. The `phase_profile.json` caveat applies — if Alex replied by text in July, those turns are absent by construction, so **every Aftermath asymmetry figure is an upper bound**.
- *Speaking time.* `dur_s` covers Baseline and Aftermath fully but only 144/221 Conflict events (Naomi 59/94, Alex 85/124). Speaking-minute charts are honest for Baseline and Aftermath; Conflict cannot be compared on that axis.
- *Word counts.* `phase_profile.json` and `baseline_comparison_audit.json` differ by <0.3% (tokenizer). `nalex_viz_schema.json` uses the audit figures. **Pick one source per artifact and state it.** Figures below use `baseline_comparison_audit.json`.
- *Denominators.* Sessions per phase: Baseline 10, Conflict 10, Aftermath 5. One Aftermath session = 20%.

---

## §1. Volume asymmetry across phases

Headline already established: word ratio N:A moves 1.83× → 1.12× → 3.14×.

### 1A — Grouped column chart *(neutral)* — rank 2
- **Artifact type:** static chart, final-quality.
- **Chart / layout:** three phase groups on the x-axis, two columns per group (Naomi, Alex), y = words. Ratio printed above each group as a plain label. No color semantics beyond speaker identity.
- **Helps the viewer notice:** both speakers rise steeply into Conflict; the gap nearly closes there (5,888 vs 5,233), then reopens far wider than Baseline in the Aftermath (6,852 vs 2,181). The Conflict near-parity is the non-obvious part — it contradicts a "she always talks more" reading.
- **Data fields:** `baseline_comparison_audit.json → {Baseline,Conflict,Aftermath}.{N_w,A_w}`; optionally `.{N_msg,A_msg}` as a secondary label. Equivalent to `nalex_viz_schema.json → artifact_1_volume_asymmetry.records` (renders with zero schema work).
- **Limitation:** raw word totals conflate turn count with turn length, and the phases span very different windows (83 / 13 / 11 calendar days) — the columns are not rates, so Conflict's density is invisible.
- **Best as:** **final.** Lowest-risk artifact in the set; already fully flattened.

### 1B — Mirrored butterfly with turn-length overlay *(lightly interpretive)* — rank 3
- **Artifact type:** static chart, exploratory.
- **Chart / layout:** horizontal population-pyramid — phases stacked as three rows, Naomi's words extending left, Alex's right from a shared centre axis; `mean_words_per_turn` overlaid as a dot on each bar. Framed top-to-bottom as "gap → near-parity → widest gap."
- **Helps the viewer notice:** that volume and turn-length move differently. In Conflict the bars nearly match while the turn-length dots stay far apart (Naomi 62.5, Alex 42.2 mean; medians 39.5 vs 21). Alex reaches near-parity in total words by taking *more, shorter* turns (124 vs 94) — a different mechanism from Naomi's.
- **Data fields:** `phase_profile.json → phases.*.speakers.*.{words,mean_words_per_turn,median_words_per_turn,messages}`; `asymmetry.word_ratio_N_over_A`.
- **Limitation:** the mirrored axis implies the two sides are commensurable and visually equalizes very different absolute scales; the "narrowing then widening" reading is imposed by row ordering, not by any measured trend statistic.
- **Best as:** **exploratory.** The mechanism insight is real but a butterfly is the wrong carrier for it — a slope or dual-axis chart states it more directly.

### 1C — Decomposed audience bar: who was present for the words *(opinionated)* — rank 1
- **Artifact type:** static chart, final-quality (needs new schema records).
- **Chart / layout:** one stacked bar per speaker per phase, segmenting each speaker's words into **in live exchange** / **solo session** (other party never joined) / **post-exit tail** (other party has left). Annotated with the project's own interpretive tags.
- **Helps the viewer notice:** that in the Aftermath **2,585 of Naomi's 6,852 words (37.7%) are produced with no one on the other end** — 793 solo + 1,792 post-exit — while Alex's solo and post-exit words are 0. It reframes "she wrote 3× more" into "a third of what she wrote had no audience," which is a different and more actionable fact. The same decomposition at Baseline (1,082 solo of 1,693) shows this is chronic, not new.
- **Data fields:** `phase_profile.json → phases.*.speakers.*.{words,solo_session_words,solo_session_turns,post_exit_tail_words,post_exit_tail_turns}`; interpretation labels from `tag_vocabulary.emotional_tags.{naomi_unwitnessed,naomi_post_exit_continuation,naomi_escalating_elaboration}` — each rendered with its `INTERPRETATION:` prefix visible.
- **Limitation:** "post-exit" is defined by absence of turns in this corpus, and the Aftermath is 100% audio — if Alex replied by text in July, those turns are missing by construction and the post-exit segment is an **upper bound**, not a measurement. The caveat must sit on the artifact face, not in a footnote.
- **Best as:** **final,** conditional on that caveat being rendered.

**Ranking: 1C > 1A > 1B.** 1C decomposes rather than restates and is the only variation here that changes what a reader would do next. 1A is the safe canonical render. 1B's insight is real but better delivered by another form.

---

## §2. Latency convergence

**Read §0.2 and §0.4 first.** This is the weakest question in the set: three point-pairs, one of which is a range and one of which rests on 7–8 observations. Every variation below is constrained by that.

### 2A — Slope chart with uncertainty band *(neutral)* — rank 1
- **Artifact type:** static chart, final-quality.
- **Chart / layout:** two lines (Naomi, Alex) across Baseline → Conflict → Aftermath, y = median reply seconds on a log scale (the 484→94 span needs it). Conflict rendered as a **vertical band** (Naomi 112–120, Alex 70–94), not a point. Baseline points annotated with their observation counts (n=7, n=8).
- **Helps the viewer notice:** the convergence is driven almost entirely by Naomi's line falling 484s → ~120s, not by Alex moving; his line is close to flat across all three phases (101 → 70–94 → 122). "Convergence" is really "one party sped up."
- **Data fields:** `phase_profile.json → phases.*.speakers.*.median_reply_seconds` (authoritative for the ranges); `baseline_comparison_audit.json → *.{N_lat,A_lat}` for point values; `phase_profile.json → notes` for the n=7/8 disclosure. Matches `nalex_viz_schema.json → artifact_2_latency_convergence.records`, except the schema stores Conflict as points 120/94 — **the schema records would need the range restored before this renders honestly.**
- **Limitation:** three observations per line is not a trend; the log axis visually compresses the Baseline gap that is the finding's whole basis.
- **Best as:** **final,** only with the band and the n-counts rendered. Without them it becomes an overclaim.

### 2C — Inside-session speed vs between-session silence *(opinionated)* — rank 2
- **Artifact type:** composite chart, exploratory.
- **Chart / layout:** upper panel — per-session median reply seconds for the five canonical Aftermath sessions; lower panel, shared time axis — the inter-contact gaps drawn to scale (6.8 days before 11 Jul, 7.8 days before 21 Jul). Two different units, deliberately stacked to make the contrast structural.
- **Helps the viewer notice:** responsiveness inside a session (Naomi 73s in the 11 Jul session) coexists with week-long silences between them. The pattern is bursty contact, not sustained contact — which the phase-level median alone hides entirely.
- **Data fields:** `aftermath_stats.json → sessions[1..5].{label,start,end,median_reply_seconds,turns,words}`; `gap_stats_out.json → rows[].gap_sec` for the two large gaps (676,768s and 587,598s); `phase_profile.json → phases.Silence.notes` for the 6.8-day figure. Interpretation label: `emotional_tags.naomi_anticipatory_vigilance` (`INTERPRETATION: sharply reduced latency consistent with monitoring`).
- **Limitation:** `aftermath_stats.json` session 0 (5 Jul) is **Conflict-phase** and must be dropped (§0.3); and per §0.2 the `gap_sec` values are inter-event gaps, not reply latencies, so the two panels are measuring different things and must be labeled as such rather than read as one series.
- **Best as:** **exploratory.** The framing is good but it requires two caveats to survive, which is one too many for a final artifact.

### 2B — Ratio-convergence line against a parity reference *(lightly interpretive)* — rank 3
- **Artifact type:** static chart, exploratory.
- **Chart / layout:** single line of `latency_ratio_N_over_A` across the three phases (4.79 → 1.2–1.7 → 1.39) with a horizontal reference line at 1.0 labeled "equal response speed."
- **Helps the viewer notice:** the responsiveness asymmetry collapses after Baseline and does not return.
- **Data fields:** `phase_profile.json → phases.*.asymmetry.latency_ratio_N_over_A`.
- **Limitation:** the parity line invites the exact misreading to avoid — a ratio near 1.0 is not evidence of a healthier exchange; both parties responding fast is equally consistent with a high-arousal exchange neither can leave. The Conflict value is also a range, so the slope into parity is partly an artifact of timestamp handling (§0.4).
- **Best as:** **exploratory only.** Do not ship; a single derived ratio over three points with a normative reference line carries more suggestion than evidence.

**Ranking: 2A > 2C > 2B.** 2A is the only one that can be made honest without stacking caveats. 2C reframes usefully but needs two. 2B should not be rendered for an audience.

---

## §3. Initiation and closure asymmetry

Headline: opens 5:5 → 5:5 → 5:0; closes 4:6 → 3:7 → 5:0.

### 3A — Two-row small-multiple of 100% stacked bars *(neutral)* — rank 2
- **Artifact type:** static chart, final-quality.
- **Chart / layout:** 2 rows × 3 columns. Row 1 = session opens, row 2 = session closes; one column per phase. Each cell a single 100% horizontal bar split Naomi/Alex, with raw counts printed inside (denominators 10 / 10 / 5).
- **Helps the viewer notice:** opens are perfectly even until they aren't — 5:5, 5:5, then 5:0 — while closes drift steadily the *other* way first (4:6 → 3:7) before flipping entirely. The two rows move independently until the Aftermath, where both go monochrome.
- **Data fields:** `phase_profile.json → phases.*.speakers.*.{session_opens,session_closes}` and `phases.*.sessions_60min`; `nalex_viz_schema.json → artifact_3_initiation_closure.records` (all 12 records already flattened).
- **Limitation:** the Aftermath denominator is 5 sessions, so one session is 20% of the bar — the flip to 5:0 is a small-n event and the 100% normalization makes it look more absolute than the count supports.
- **Best as:** **final.** Renders directly from existing schema records.

### 3B — Opens × closes quadrant with phase trajectory *(lightly interpretive)* — rank 3
- **Artifact type:** static chart, exploratory.
- **Chart / layout:** scatter, x = share of session opens, y = share of session closes; one point per speaker per phase (6 points), arrows connecting each speaker's three points in phase order. Quadrants labeled descriptively ("opens more / closes more").
- **Helps the viewer notice:** the two speakers trace opposite paths to opposite corners — Alex from the closes-heavy region to the origin, Naomi to (1,1).
- **Data fields:** derived shares from `phase_profile.json → phases.*.speakers.*.{session_opens,session_closes}` over `sessions_60min`.
- **Limitation:** the arrows imply continuous motion through a space where only three discrete measurements exist, and the Silence phase (0 events) sits between Conflict and Aftermath unrepresented — the longest arrow crosses a period with no data at all.
- **Best as:** **exploratory.** Elegant but the trajectory metaphor asserts more continuity than three points can carry.

### 3C — Who ends things: closes plus explicit sign-offs *(opinionated)* — rank 1
- **Artifact type:** composite chart, final-quality (needs new schema records).
- **Chart / layout:** paired encoding per phase — session closes as bars (mechanical: last turn in the window) and `explicit_signoff_turns` as a distinct overlaid mark (verbal: an actual sign-off move). A corpus-wide strip beneath: Alex 15, Naomi 0.
- **Helps the viewer notice:** that "closing" means two entirely different acts for the two speakers. Alex ends exchanges **verbally** — 0 sign-offs at Baseline, 11 in Conflict, 4 in Aftermath. Naomi issues **zero explicit sign-offs in the entire 378-event corpus**, yet is credited with 5 of 5 Aftermath closes. Her "closes" are not endings; they are the residue of being the last one still speaking.
- **Data fields:** `phase_profile.json → phases.*.speakers.*.{session_closes,explicit_signoff_turns}`; `corpus_wide.explicit_signoffs_total` (Alex 15, Naomi 0); `phases.*.asymmetry.explicit_signoffs_N_to_A` (`"0:0"`, `"0:11"`, `"0:4"`). Interpretation labels: `emotional_tags.{alex_withdrawal_by_exit,dyad_asymmetric_repair_expectation}` and `problematic_tags.{naomi_never_closes_verbally,dyad_no_closure_event}`, rendered with prefixes intact.
- **Limitation:** "session close" is a mechanical artifact of the 60-minute gap rule, not a communicative act — and in the Aftermath Naomi's 5 closes overlap her 11 post-exit tail turns, so the metric partly counts *talking after he left* as *closing*. The artifact must define both terms on its face or it will be read as "she ends conversations," which is close to the opposite of what the data shows.
- **Best as:** **final,** conditional on both definitions being rendered.

**Ranking: 3C > 3A > 3B.** 3C uses the most underexploited field in the corpus (`explicit_signoff_turns`), rests on whole-population counts, and corrects a likely misreading of 3A rather than merely decorating it. 3A is the clean canonical version. 3B over-asserts continuity.

---

## §4. Conflict question function

**Read §0.1 first.** The annotated layer is **17 questions (11 Naomi, 6 Alex)** against a Conflict-phase population of **83 literal-'?' questions (39 Naomi, 44 Alex)** — a ~20% non-random sample whose speaker skew *inverts* the population's. `nalex_viz_schema.json` already carries this as `sample_caveat`; it is the dominant risk in this question.

### 4A — Two-panel population / sample split *(neutral)* — rank 1
- **Artifact type:** static two-panel chart, final-quality.
- **Chart / layout:** deliberately disjoint panels with a visible divider. **Left (population):** Conflict question counts and documented-unanswered counts per speaker — Naomi 39 asked / 8 unanswered, Alex 44 asked / 15 unanswered. **Right (sample):** the 17 annotated questions broken down by `intent`. Different axes, different denominators, no shared scale, divider labeled "20% sample — not drawn from the left panel."
- **Helps the viewer notice:** first, the population-level inversion that gives the phase its name — **Alex asks more questions (44 vs 39) and has more go unanswered (15 vs 8)**, reversing the Baseline pattern (Naomi 12/6, Alex 4/1). Second, and structurally, that the annotated sample skews Naomi 11:6 while the population skews Alex 39:44 — so the right panel cannot be read as evidence about the left.
- **Data fields:** `baseline_comparison_audit.json → Conflict.{N_q,A_q,N_unans,A_unans}` and `Baseline.{…}` for contrast; `conflict_questions_annotated.json → [].intent`; `nalex_viz_schema.json → artifact_4_conflict_question_function.sample_caveat` verbatim.
- **Limitation:** `phase_profile.json` warns that Alex's documented 15/44 unanswered figure is "roughly double any mechanical timing rule (7/44)" and is a content-level judgment **not reproducible from `events.jsonl`** — so the left panel's most striking number is analyst-assigned, and must be marked as such.
- **Best as:** **final.** The only variation that structurally prevents the sample-as-population error.

### 4C — Annotated-question timeline by heat and loop *(opinionated)* — rank 2
- **Artifact type:** timeline / structured scatter, exploratory.
- **Chart / layout:** the 17 annotated questions on a time axis (26 Jun → 4 Jul), y-grouped by `loop_tag`, marks encoded by `heat` (tense / hot / explosive), shape by speaker. `dominant_loop` and `core_problem` quoted verbatim from `conversation_summary` as standing text, not paraphrased.
- **Helps the viewer notice:** the shape of the deadlock. `proof-loop` carries 6 of 17 and holds 2 of the 3 canonical `genuine_unanswered` questions. And the sample's two clusters look qualitatively different: the 26–27 Jun cluster is 10 of 12 hot-or-explosive with `intent` running challenge/clarify, while all 5 of the 4 Jul turns are `tense` with `intent` shifting to boundary/repair/clarify. Consistent with de-escalation into boundary-setting rather than resolution — which matches the phase-level fact that Conflict ends with `dyad_no_closure_event`.
- **Data fields:** `conflict_questions_annotated.json → [].{timestamp,speaker,intent,loop_tag,heat,risk,genuine_unanswered,notes}`; `conflict_questions_summary.json → conversation_summary.{dominant_loop,core_problem,repair_attempts,boundary_statements}`; `conflict_questions_tags.csv` for on-artifact tag definitions.
- **Limitation:** the 17 points are non-uniform in time — **12 fall on 26–27 Jun and 5 on 4 Jul, with nothing in between** — so the apparent cool-down may be an artifact of which turns were annotated rather than a real trajectory. A timeline is the form most likely to be read as a continuous history, which this sample is not.
- **Best as:** **exploratory.** Becomes the strongest candidate in this question if the annotation layer is extended to the full 83.

### 4B — Intent × answered matrix *(lightly interpretive)* — rank 3
- **Artifact type:** heatmap / dot matrix, exploratory.
- **Chart / layout:** 6 `intent` categories × 2 `answered` states (Partial / No), split by speaker, cells sized or shaded by count.
- **Helps the viewer notice:** one genuinely clean finding — **not one of the 17 annotated questions is recorded as fully answered.** The field takes only `Partial` (10) and `No` (7); `Yes` never occurs.
- **Data fields:** `conflict_questions_annotated.json → [].{intent,answered,speaker}`; `conflict_questions_tags.csv` for the `answered` definition.
- **Limitation:** n=17 spread over 6 intents × 2 states × 2 speakers leaves most cells at 0 or 1 (`justify`, `deflect`, and `repair` have exactly one observation each) — a heatmap over cells that sparse invites pattern-reading the counts cannot support.
- **Best as:** **exploratory.** The "zero fully answered" fact is worth surfacing, but it is one sentence, not a matrix — it belongs as an annotation on 4A.

**Ranking: 4A > 4C > 4B.** 4A is the only design where the sampling problem is the visual subject rather than a caption. 4C is the most informative but its form fights its sample. 4B's single real finding does not need a matrix.

---

## §5. Cross-cutting notes

**Schema readiness.** `nalex_viz_schema.json` already contains flattened records for **1A, 2A (points only), 3A, and 4A** — the four neutral-tier variations. Every B and C variation requires new records first. Specifically:

| Variation | New records needed |
|---|---|
| 1C | `solo_session_words`, `post_exit_tail_words` × 2 speakers × 3 phases (12) |
| 2A | Conflict `median_reply_seconds` restored to range form (2 records amended) |
| 2C | Aftermath per-session `median_reply_seconds` (5) + 2 inter-contact gaps |
| 3C | `explicit_signoff_turns` × 2 speakers × 3 phases (6) + corpus totals (2) |
| 4C | 17 annotated questions as records with `heat` / `loop_tag` / `intent` |

**Interpretation hygiene.** Tier C draws exclusively from `phase_profile.json → tag_vocabulary.emotional_tags`, which the source file already marks `INTERPRETATION`. No new emotional vocabulary is introduced anywhere in this document. Carry the `INTERPRETATION:` prefix into the rendered artifact rather than stripping it — per `index.md` §11 the rendering model must not add analysis, and an unprefixed emotional label is indistinguishable from a measurement once rendered.

**The audio-only caveat applies to three of the four questions.** Aftermath is 100% audio. Volume, initiation/closure, and latency Aftermath figures are all **upper bounds on the asymmetry**, not measurements. Only Question 4 (Conflict-phase, mixed modality) escapes it.

---

## §6. Recommended first render

**→ 3C — "Who ends things: session closes plus explicit sign-offs."**

Rationale:

1. **Strongest evidence base of the twelve.** Whole-population integer counts, reproducible from `events.jsonl`, with no sampling problem (unlike Q4), no range ambiguity (unlike Q2), and no tokenizer variance (unlike Q1).
2. **Highest information gain.** `explicit_signoff_turns` is the most underused field in the corpus, and the Naomi-0-of-378 figure is the single most unambiguous number in the dataset.
3. **It corrects rather than decorates.** 3A alone shows Naomi closing 5 of 5 Aftermath sessions, which reads naturally as "she ends conversations." 3C shows that reading is close to backwards. A first render that pre-empts a likely misreading is worth more than one that restates a known headline.
4. **Its interpretation is pre-sanctioned.** `alex_withdrawal_by_exit` and `naomi_never_closes_verbally` already exist in `phase_profile.json` with their INTERPRETATION status declared — Tier C invents nothing.

**Prerequisites before rendering:** add the 8 records listed in §5; render both definitions ("session close" = last turn before a 60-minute gap; "explicit sign-off" = verbal termination move) on the artifact face; and carry the Aftermath audio-only caveat as visible text.

**Safe alternative if a strictly neutral first render is required:** **1A**, which needs no schema work at all and renders directly from `artifact_1_volume_asymmetry.records`.

**Do not render first:** 2B (normative parity line over three points). The §0.1 CSV/JSON discrepancy that previously blocked Q4 renders is now resolved (see §0.1).
