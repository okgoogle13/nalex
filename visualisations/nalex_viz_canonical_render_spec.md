# Nalex Canonical Render Implementation Specification

**Subject artifact:** "Nalex — Visualization Variation Previews" (12-variant ideation preview, `research_prompt_modes/analysis_outputs/nalex_viz_ideation.md` / `visualisations/nalex_viz_ideation.md`).
**Status:** implementation-grade handoff. Supersedes nothing; consolidates and operationalizes the ideation document, the visualization pipeline, and the existing schema/render artifacts already in the repository.
**Generated against repository state as of:** commit history through `af62ce3` ("Add viz ideation drafts and update cowork handover 2 with ideation reference"), branch `master`.

---

# 1. Purpose and delivery boundary

## 1.1 Purpose

This document specifies what a **canonical, shippable render** of the Nalex visualization program must contain, how it must be built, and what constraints bind it — as distinct from the informal preview sketches in the "Nalex — Visualization Variation Previews" artifact. It exists so that an implementer (human or model) can build the recommended first render (variant **3C**, §5) and any subsequent variant without re-deriving the evidentiary, schema, or pipeline decisions already made in `nalex_viz_ideation.md`, `phase_profile.json`, `viz_schema_template.md`, and `visualization_pipeline.md`.

## 1.2 Ideation preview vs. canonical/shipped artifact

The "Nalex — Visualization Variation Previews" artifact is explicitly self-labeled, on its own face, as **not the canonical render**:

> "**Not the canonical render.** These are informal preview sketches for design comparison only. A shipped artifact still goes through the required flatten-then-render pipeline in `research_prompt_modes/` (`viz_schema_template.md` → `visualization_pipeline.md`) per `index.md` §11. Tier-C panels render only pre-declared `INTERPRETATION` tags from `phase_profile.json` — no new emotional vocabulary is introduced."

The distinction is binding and structural, not cosmetic:

| | Ideation preview artifact | Canonical/shipped render |
|---|---|---|
| Purpose | Compare shape/framing of 12 candidate designs before committing | Deliver one validated, reproducible visual answer to one visual question |
| Data path | Approximate-scale hand-built SVGs, illustrative not exact-to-pixel | Values traceable to named, flattened schema fields |
| Schema conformance | Not required to conform to `viz_schema_template.md` | Must conform; every mark must trace to a schema record |
| Validation | None — explicitly informal | Must pass the checklist in `visualization_pipeline.md` "Validation Checklist" and this document's §9 |
| Caveats | Present as design commentary (`.notice`, `.limitation` divs) | Must be present as `render_on_face` content in the artifact body itself, not only in surrounding prose |
| Interpretation vocabulary | Uses `phase_profile.json` tags already, correctly | Must continue to use only pre-declared tags — this is a hard constraint, not a preview-only courtesy |
| Ship status | All 12 are ideation-only regardless of their internal "Final" label | Only the specific variant being built, once it passes §9, may ship |

A card in the preview artifact carrying a `.status.final` label (e.g., 1A, 1C, 2A, 3A, 3C, 4A) means "this variant is ready to be the *target* of a canonical build," not "this SVG sketch may be shipped as-is." The preview SVGs are approximate-scale mockups; none of their exact pixel geometry, font sizes, or viewBox dimensions are canonical.

## 1.3 What this specification covers

- The governing render pipeline and its mandatory documents/checkpoints (§2).
- A field-level inventory of every source file the 12 variants draw on, with type/unit/population/derivation/reproducibility notes (§3).
- Full documentation of all 12 variants — tier, rank, ship status, exact values, chart form, caveats, blockers (§4).
- An exhaustive implementation spec for the recommended first canonical render, **3C** (§5).
- The exact schema records 3C requires, with JSON examples and a patch (§6).
- Non-negotiable constraints that apply to any canonical Nalex render, not just 3C (§7).
- Visual system, typography, color, accessibility, and determinism requirements (§8).
- QA and acceptance criteria, including rollback conditions (§9).
- An ordered build plan with inputs/outputs/gates per step (§10).
- A complete, self-contained factual appendix so this document does not depend on the preview artifact remaining available (§11).

## 1.4 What this specification explicitly excludes

- **Interactivity, hover states, tooltips, filters, drilldowns, or any client-side data recomputation.** The first canonical render is a static artifact. §8.5 states the rule for *if* interactivity is added later; it is not specified here and must not be assumed present.
- **Any visual encoding, annotation, or claim not traceable to a named field in a source file listed in §3 or a schema record listed in §6.** Where this document proposes new derived fields (§6), they are explicitly marked as proposed schema additions, not as data that already exists.
- **Any new emotional, psychological, causal, or evaluative vocabulary.** Per `index.md` §11 and the ideation document's Tier-C constraint, only vocabulary already present in `phase_profile.json → tag_vocabulary` may appear in an interpretive (Tier C) render. This document does not authorize, and a renderer must not introduce, any label outside that vocabulary.
- **Coverage of variants other than 3C at implementation depth.** §4 documents all 12 variants completely (per the task requirement), but §5's exhaustive build-grade treatment — layout, accessibility, validation — is scoped to 3C only, since it is the recommended first render. A future revision of this document (or a sibling document following the same template) would be required before any other variant ships.
- **Resolution of unresolved analytic questions.** Where the underlying evidence is contested, ranged, sample-based, or upper-bound (see §3's per-file limitations and §11), this document specifies how to *display* that uncertainty; it does not resolve it.

---

# 2. Governing render pipeline

## 2.1 The three mandatory pipeline documents

Per `index.md` §11 ("Visualization Rule"), **all three files must be read before producing a visualization**:

1. **`research_prompt_modes/visualization_pipeline.md`** — the workflow itself: extract evidence from canonical sources, flatten it, then render. Defines the analysis/rendering separation as a hard rule: *"Separate analysis from rendering. Analysis extracts and normalizes evidence. Rendering formats only the provided structure. The rendering model must not infer new themes, rewrite evidence, or add analysis."*
2. **`research_prompt_modes/viz_schema_template.md`** — the flattened schema every visualization input must conform to before rendering: `theme`, `phase`, `scope`, `detail_label`, `display_instance`, `speaker`, `metric {name, value, unit}`, `evidence_quote`, `confidence`, `linked_theme`, `relation_type`, `visual_hint`, `forward_looking_evaluation`.
3. **`research_prompt_modes/nalex_gemini_viz_corrective_prompt.md`** — the corrective prompt to hand a rendering model so it behaves as "a dumb layout engine": no inferred themes, no rewritten evidence, no added analysis.

## 2.2 Required sequence: source → schema → validated render

```
canonical sources (index.md §1–§5: CURRENT_STATE_CLEAN.md, phase_profile.json,
baseline_comparison_audit.json, aftermath_stats.json, gap_stats_out.json,
conflict_questions_annotated.json / conflict_questions_summary.json, events.jsonl)
        │
        │  1. EXTRACT — pull the exact evidence needed for one visual question
        ▼
flattened schema records (viz_schema_template.md shape; see §6 for the
new records 3C requires; nalex_viz_schema.json / nalex_mobile_infographic_schema.json
show this step already performed for artifacts 1–4)
        │
        │  2. VALIDATE — run the Validation Checklist (§2.4) and this
        │     document's §9 acceptance criteria against the flattened records
        ▼
one visual question per artifact (visualization_pipeline.md "Best practices")
        │
        │  3. RENDER — hand the validated, flattened records to a rendering
        │     model constrained by nalex_gemini_viz_corrective_prompt.md;
        │     the renderer treats visual_hint as a literal instruction and
        │     invents nothing
        ▼
shipped canonical artifact (must pass §9 acceptance criteria before publication)
```

Each arrow is a checkpoint. A render must not skip from "canonical sources" directly to "shipped artifact" — this is precisely the shortcut §7.1 prohibits.

## 2.3 Mandatory handoff artifacts

| Artifact | Produced at | Consumed by | Required before |
|---|---|---|---|
| Flattened schema record set (JSON, `viz_schema_template.md` shape) | Extract step | Render step | Any rendering work begins |
| Validation checklist result (pass/fail per item in §2.4) | Validate step | Ship/no-ship decision | Rendering work begins |
| Rendering-constrained prompt (per `nalex_gemini_viz_corrective_prompt.md`) | Render step | The rendering model | The rendering model is invoked |
| §9 acceptance checklist result | Post-render QA | Publication decision | Publication |

## 2.4 Validation checkpoints (from `visualization_pipeline.md`)

**Final Verification Requirements** (verbatim, items 8–10 as numbered in the source file):
8. Canonical phase records are grouped using only the valid canonical phase enum.
9. Records marked `scope: "corpus"` or another template-defined non-phase scope are rendered only as defined by the schema and are not misrepresented as phase data.
10. Where a canonical phase has no applicable schema record for an artifact, it is shown as absent/not applicable only if the schema explicitly encodes that status; otherwise it is omitted and listed in the render audit.

**Validation Checklist** (verbatim):
- every `phase` value is either a valid canonical phase or `null` when `scope` is a template-defined non-phase scope;
- every record has a valid `scope`;
- session, gap, and corpus identifiers are stored in their designated detail field;
- phase applicability or non-applicability is explicit where required by the artifact.

The valid canonical phase enum, per `events.jsonl` and `index.md` §3, is exactly: `Baseline`, `Conflict`, `Silence`, `Aftermath`. `phase: null` is valid only for `scope: "corpus"` (or another template-defined non-phase scope), per `viz_schema_template.md`'s note: *"`phase` must be `null` only for valid non-phase records (e.g. `scope: "corpus"`)."*

## 2.5 Tier-C interpretation constraint (binding, restated for emphasis)

Tier-C panels may render **only** pre-declared `INTERPRETATION` tags from `phase_profile.json → tag_vocabulary.emotional_tags`. No new emotional, psychological, causal, or evaluative vocabulary may be introduced at render time. This applies to:

- Any label text rendered on the artifact face.
- Any annotation, caption, or micro-copy generated to "explain" a chart.
- Any alt text or text-only equivalent (§8.6) — the accessibility layer is not exempt from this constraint.

The full, closed vocabulary is reproduced in §11.2. A render may quote a tag's exact string with its prefix intact (`INTERPRETATION: ...` for `emotional_tags`, or the plain definition string for `problematic_tags`, which are **structural**, not interpretive — see §4's per-variant tag citations for the distinction). A render must **not** paraphrase, soften, intensify, or recombine these strings into new sentences that were not in the source vocabulary.

---

# 3. Evidence and source inventory

For each file: exact path, role, required fields (used by any of the 12 variants), field type/unit/population/derivation, and known limitations.

## 3.1 `events.jsonl`

**Role:** Canonical event stream; source of truth for all recomputed metrics. Per `index.md` §3, join key is always `sha256`, never `eid`. Timestamps are standardized to `YYYY-MM-DD HH:MM:SS`, except where noted (see limitations).

**Canonical phase windows** (binding, from `index.md` §3):

| Phase | Window (inclusive) |
|---|---|
| Baseline | 2026-04-01 to 2026-06-22 |
| Conflict | 2026-06-23 to 2026-07-05 |
| Silence | 2026-07-06 to 2026-07-10 |
| Aftermath (canonical) | 2026-07-11 to 2026-07-21 |

**Record shape** (observed): `cid`, `eid`, `t` (timestamp string, sometimes `~`-prefixed for approximate, sometimes minute-only precision), `s` (speaker: `Naomi` | `Alex` | `System`), `kind` (`audio` | `text` | `call` | `media`), `gap` (string label, e.g. `"0m"`, `"3d07h40m"`, `null`, `"start"` — **not seconds, not a latency field**), `txt`, `dur_s` (float, audio duration seconds; present for audio events, partially present for Conflict), `speaker_conf` (float), `src_file`, `sha256` (string, may be absent), `model_id`, `flags` (array).

**Fields required by the 12 variants (directly or via derivation):**

| Field | Type | Unit | Population | Derivation basis for downstream metrics | Status |
|---|---|---|---|---|---|
| `t` | string timestamp | — | all 378 events | Phase assignment (date range match); session grouping (60-min inter-event gap); reply latency (Δt to next cross-speaker turn) | Directly observed; 36 Conflict-phase events carry `~`-approximate or minute-only precision |
| `s` | enum string | — | all 378 events | Speaker attribution for every per-speaker metric | Directly observed |
| `kind` | enum string | — | all 378 events | Modality/channel-coverage caveats (audio-only Aftermath, mixed Conflict) | Directly observed |
| `txt` | string | — | all events with content | Word counts (regex tokenization `[A-Za-z0-9']+`), question detection (literal `?` in text) | Directly observed; word count is a derived tokenizer output, not a raw field |
| `dur_s` | float | seconds | 144/221 Conflict events, full Baseline/Aftermath | Speaking-minute charts (Baseline/Aftermath only; Conflict is a partial population and not comparable on this axis) | Directly observed where present |
| `sha256` | string or absent | — | 301/378 events (77 absent, all in Conflict) | Join key for `gap_stats_out.json` (105/105 resolve; unaffected because Aftermath-only) | Directly observed; **known schema gap** — the "always join on `sha256`" invariant in `index.md` §3 cannot be honored for the 77 sha256-less Conflict events (69 text, 3 call, 3 audio, 2 media) |
| `gap` | string label or null | — | 217 non-null of 378 | **Not usable as a latency series.** 206/217 non-null values are `'0m'`, one is `'start'`, only 10 carry real durations. Marks session boundaries only. | Directly observed; explicitly disqualified from latency use (§0.2 of ideation doc) |

**Reproducibility / sampling / missing-channel / schema-gap limitations:**

- **No per-event reply-latency series exists anywhere in the input set.** Neither `gap` (a session-boundary label) nor `gap_stats_out.json`'s `gap_sec` (elapsed time regardless of speaker, Aftermath-only) is a valid substitute. Consequence: no distribution, violin, or histogram of reply latency is renderable from any combination of these sources — only phase-level medians (§3.4) are available.
- **Conflict phase event count differs by exactly 3 across sibling files**, fully reconciled: `phase_profile.json` reports 221 Conflict events; `baseline_comparison_audit.json` reports 218. `CURRENT_STATE_CLEAN.md` line 20 states *"Conflict includes 3 `System` events. Total 378."* — 221 (all events) − 3 (System) = 218 (conversational Naomi/Alex events only). Both figures are correct for their respective denominators; a canonical render must state which it is using.
- **36 Conflict events carry approximate (`~`) or minute-only timestamps**, which is why Conflict latency medians are ranges, not points (§3.4).
- **The sha256 join hole is 100% concentrated in the Conflict phase** — no Baseline, Silence, or Aftermath event lacks a `sha256`.
- **Word counts are a tokenizer-dependent derived quantity**, not a raw field; two independent tokenizations (`phase_profile.json`'s Rev-4 recomputation vs. `baseline_comparison_audit.json`) differ by <0.3% per `CURRENT_STATE_CLEAN.md` §7.1/§7.2H. Per §7.2H, **`baseline_comparison_audit.json`'s figures (Naomi 6,852 / Alex 2,181 for Aftermath) are the canonical totals for downstream visualization and extraction**; `phase_profile.json`'s 6,860/2,187 remain valid as an independent recomputation check only, not a substitute.

## 3.2 `phase_profile.json`

**Role:** The `NALex_PHASE_PROFILE` bundle — per-phase, per-speaker metrics, all independently recomputed from `events.jsonl` (Rev 4, "Claude Opus behavioural-analysis pass," generated 2026-08-02). This is the **authoritative source** for `median_reply_seconds` ranges, `session_opens`/`session_closes`, `explicit_signoff_turns`, `solo_session_turns/words`, `post_exit_tail_turns/words`, `questions_per_100_turns`, and the full `tag_vocabulary`.

**Top-level keys:** `project`, `artifact`, `revision` (4), `generated` (2026-08-02), `generated_by`, `source_of_truth` (`events.jsonl`, 378 events), `join_key` (`sha256` where present), `notes`, `tag_vocabulary` (`problematic_tags`, `emotional_tags`), `phases` (`Baseline`, `Conflict`, `Silence`, `Aftermath`), `corpus_wide`.

**Per-phase, per-speaker record shape** (`phases.<Phase>.speakers.<Speaker>`): `messages`, `words`, `mean_words_per_turn`, `median_words_per_turn`, `longest_turn_words`, `questions`, `questions_per_100_turns`, `unanswered_documented`, `unanswered_reproducible_10min_in_session`, `unanswered_rate_reproducible`, `median_reply_seconds` (number or `"lo-hi"` range string), `session_opens`, `session_closes`, `max_consecutive_turns`, `explicit_signoff_turns`, `solo_session_turns`, `solo_session_words`, `post_exit_tail_turns`, `post_exit_tail_words`.

**Per-phase `asymmetry` record shape:** `word_ratio_N_over_A`, `median_turn_len_ratio_N_over_A`, `latency_ratio_N_over_A` (number or range string), `session_opens_N_to_A`, `session_closes_N_to_A`, `explicit_signoffs_N_to_A` — all as `"N:A"` count strings.

**Per-phase `flags`, `problematic_tags`, `emotional_tags`, `notes` arrays.**

**`corpus_wide` fields:** `events` (378), `speakers` (`Alex` 188, `Naomi` 187, `System` 3), `first_event`, `last_event`, `explicit_signoffs_total` (`Alex` 15, `Naomi` 0), `sha256_coverage` (`present` 301, `absent` 77, `absent_breakdown` by kind, `note`).

**Field type/unit/population/derivation table for fields consumed by the 12 variants:**

| Field | Type | Unit | Population/denominator | Derivation | Status |
|---|---|---|---|---|---|
| `words` | integer | words | per speaker per phase | Tokenized from `events.jsonl → txt` | Derived; independently recomputed; differs from `baseline_comparison_audit.json` by <0.3% |
| `mean_words_per_turn`, `median_words_per_turn` | float | words/turn | per speaker per phase | `words / messages` (mean); statistical median of per-turn word counts | Derived |
| `median_reply_seconds` | number or `"lo-hi"` string | seconds | Baseline: 7 obs. (Naomi), 8 obs. (Alex); Conflict: range due to 36 approximate-timestamp events; Aftermath: full population | Median of cross-speaker reply-gap seconds within a session | Derived; **range-valued for Conflict**; small-n for Baseline |
| `session_opens`, `session_closes` | integer | count | per speaker per phase; denominators = `sessions_60min` (10, 10, 5) | First/last turn of each 60-minute-gap session, attributed to its speaker | Derived, mechanical (session boundary rule only) |
| `explicit_signoff_turns` | integer | count | per speaker per phase | Analyst-classified: a turn containing a verbal termination move (e.g. "I'll speak to you another time," "I'm not going to continue to argue about this tonight," "should we just put a pin in it," "I'm actually going to put my phone on silent") | **Annotated** (content-level judgment), not mechanically reproducible from `events.jsonl` by a generic rule; see §3.2.1 |
| `solo_session_turns`, `solo_session_words` | integer | turns / words | per speaker per phase | Turns occurring in a session the other party never joined | Derived, mechanical |
| `post_exit_tail_turns`, `post_exit_tail_words` | integer | turns / words | per speaker per phase | Turns occurring after the other party's final turn in a session that both parties did join | Derived, mechanical |
| `questions_per_100_turns` | float | rate | per speaker per phase | `(questions / messages) × 100` | Derived |
| `unanswered_documented` | integer | count | per speaker per phase | Analyst-assigned (content-level judgment) | **Annotated**; for Conflict-Alex specifically flagged as "roughly double any mechanical timing rule" (documented 15/44 vs. mechanical 7/44) |
| `unanswered_reproducible_10min_in_session` | integer | count | per speaker per phase | Mechanical proxy: "no turn from the other party within 10 minutes, same session" | Derived, mechanical; **diverges sharply from `unanswered_documented` for Conflict-Alex only** (7 vs. 15) — all other five cells reproduce closely |
| `tag_vocabulary.problematic_tags` | object, 20 keys | — | corpus-wide vocabulary | Fixed structural-label definitions, one line each | **Structural**, not interpretive; every tag used at least once and defined |
| `tag_vocabulary.emotional_tags` | object, 12 keys | — | corpus-wide vocabulary | Fixed `INTERPRETATION:`-prefixed definitions, one line each | **INTERPRETATION**, per source file's own label; this is the *entire* closed vocabulary Tier-C renders may draw from |
| `corpus_wide.explicit_signoffs_total` | object | count | whole 378-event corpus | Sum of `explicit_signoff_turns` across all three non-Silence phases | Derived, annotated (inherits the annotation status of its inputs) |
| `corpus_wide.sha256_coverage` | object | count | whole 378-event corpus | Count of events with/without `sha256`, broken down by `kind` | Directly observed |

**3.2.1 — `explicit_signoff_turns` derivation detail (from `CURRENT_STATE_CLEAN.md` §13, cross-referenced against `phase_profile.json`).** The classification rule is: a turn is an explicit sign-off if its text contains a verbal termination move — i.e., an utterance that announces the end of the live exchange, distinct from simply being the chronologically last turn before a session-defining gap. Exact example quotes from the source corpus (verbatim, `CURRENT_STATE_CLEAN.md` §13): *"I'll speak to you another time,"* *"I'm not going to continue to argue about this tonight,"* *"should we just put a pin in it,"* *"I'm actually going to put my phone on silent,"* *"the fucking argument is over as far as I'm concerned. I'm done talking about this,"* *"I will not be responding to any more messages."* This is a **content-level/analyst judgment**, not a keyword-matchable mechanical rule reproducible purely from `events.jsonl` by a generic script in this repository — no such extraction script currently exists in the repo (`recompute_harness.py` and `refactor_questions_v2.py` do not implement sign-off detection). See §6.9 for the backfill/reproducibility implication.

**3.2.2 — Breach/hold sub-classification (from `CURRENT_STATE_CLEAN.md` §8, not currently present as a `phase_profile.json` field).** Of Alex's 15 corpus-wide explicit sign-offs, a "breach" is defined as the speaker continuing to talk in the same session after issuing the sign-off (i.e., the announced ending did not hold); a "held" sign-off is followed by no further same-session turns from that speaker.

| | breached (kept talking in-session) | held |
|---|---|---|
| Conflict (11 sign-offs) | 9 | 2 |
| Aftermath (4 sign-offs) | 1 | 3 |

This sub-classification is **not** required by the 3C variant as specified in the ideation document, and is **not** currently a flattened schema field anywhere in the repository. It is documented here as evidence-inventory context and as a candidate future refinement (see §6.9), not as a required 3C record.

## 3.3 `baseline_comparison_audit.json`

**Role:** Point-value phase-comparison summary; the source `nalex_viz_ideation.md` designates as canonical for Q1 word-count totals (§7.2H of `CURRENT_STATE_CLEAN.md`) and as the point-value source for Q2 latency.

**Structure:** top-level keys `Baseline`, `Conflict`, `Aftermath`, each an object with: `events`, `sessions`, `N_msg`, `A_msg`, `N_w`, `A_w`, `N_wpm`, `A_wpm`, `N_lat`, `A_lat`, `N_q`, `N_unans`, `A_q`, `A_unans`, `N_run`, `A_run`, `N_opens`, `A_opens` (`N_`/`A_` prefixes = Naomi/Alex).

| Field | Type | Unit | Population | Derivation | Status |
|---|---|---|---|---|---|
| `events` | integer | count | per phase | Direct count from `events.jsonl` | Directly observed; Conflict = 218 (conversational only; see §3.1 reconciliation) |
| `N_w`, `A_w` | integer | words | per phase | Tokenized word count | Derived; canonical per §7.2H for Q1/Aftermath figures specifically |
| `N_lat`, `A_lat` | integer (point value) | seconds | per phase | Point value of median reply latency — for Conflict, **the top of the range** reported in `phase_profile.json` (120 = top of 112–120; 94 = top of 70–94) | Derived; a **single point standing in for a range** — must not be rendered without the range context from `phase_profile.json` |
| `N_q`, `A_q`, `N_unans`, `A_unans` | integer | count | per phase | Question counts (literal `?`); unanswered counts (documented/annotated, matches `phase_profile.json → unanswered_documented`) | Directly observed (`N_q`/`A_q`); annotated (`N_unans`/`A_unans`) |
| `N_opens`, `A_opens` | integer | count | per phase | Session-open counts | Directly observed, matches `phase_profile.json → session_opens` |

**Limitation:** does not carry `session_closes` or `explicit_signoff_turns` at all — those fields exist only in `phase_profile.json` and the flattened schema files (§3.6, §3.7). Does not carry the Conflict latency range, only its upper bound as a point — using this file alone for Q2 would silently convert a range into a false-precision point (this is exactly what ideation-doc variant 2B is flagged for).

## 3.4 `aftermath_stats.json`

**Role:** Session-level detail for the Aftermath window — **but using a wider window than the canonical Aftermath phase.**

**Structure:** `source_hash`, `source_file`, `generated`, `window`, `supersedes`, `rule`, `repair_note`, `items_emitted`, `known_limits`, `overall` (per-speaker: `turns`, `words`, `audio_minutes`, `mean_words_per_turn`, `median_words_per_turn`, `longest_turn_words`, `questions`, `median_reply_seconds`), `sessions` (array of per-session objects), `events`.

**Window mismatch (critical, binding constraint):** its window is "all events dated 2026-07-05 or later" = **115 events**; the canonical Aftermath phase (`index.md` §3) is 2026-07-11..2026-07-21 = **105 events**. Its `overall` block (Naomi 66 turns / 7,557 words; Alex 49 turns / 2,978 words) **does not match** `phase_profile.json`'s canonical Aftermath figures (61 / 6,852 [audit] or 6,860 [phase_profile]; 44 / 2,181 [audit] or 2,187 [phase_profile]) and **must not be mixed with them.**

**`sessions` array — record shape:** `session` (0–5), `label`, `eid_range` (2-element array), `start`, `end`, `events`, `turns` (per speaker), `words` (per speaker), `audio_minutes` (per speaker), `questions` (per speaker), `median_reply_seconds` (per speaker, present only for speakers who replied in that session).

**Session 0 exclusion (binding):** `session: 0`, labeled *"5 Jul - the night both of them said it was over,"* spans `2026-07-05 00:07:18` to `2026-07-05 00:53:54` — this date is **Conflict phase**, not Aftermath, by the canonical window. It must be excluded from, or visually separated from, any Aftermath-labeled Q2 render. The remaining `sessions[1..5]` are the five canonical Aftermath sessions and are usable.

| Field | Type | Unit | Population | Derivation | Status |
|---|---|---|---|---|---|
| `sessions[1..5].median_reply_seconds` | object, per speaker | seconds | one value per speaker per canonical Aftermath session (5 sessions) | Session-scoped median of reply gaps | Directly derived, mechanical; **only usable subset of this file for canonical Aftermath work** |
| `sessions[0]` | — | — | Conflict-phase session mislabeled into this file's window | — | **Must be excluded from canonical Aftermath renders** |
| `overall` | object | — | 115-event wider window | — | **Must not be used as a canonical Aftermath total; use `phase_profile.json`/`baseline_comparison_audit.json` instead** |

## 3.5 `gap_stats_out.json`

**Role:** Elapsed-time-between-events data, Aftermath-window only. **Not a reply-latency series** — see §3.1.

**Structure:** `_note` (a field-provenance disclaimer, quoted below), `rows` (array of 105 objects: `sha256`, `t`, `prev_t`, `prev_eid`, `local_id`, `eid`, `gap_sec`).

**Verbatim `_note`:** *"'local_id' is this artifact's private D/E/F gap-group numbering and is NOT an events.jsonl EID. 'eid' is the canonical events.jsonl id, resolved by sha256 on 2026-08-02. Prior versions stored the private id under the key 'eid', which invites bad joins."*

| Field | Type | Unit | Population | Derivation | Status |
|---|---|---|---|---|---|
| `gap_sec` | float | seconds | 105 rows, all Aftermath window, all resolve 105/105 on `sha256` | Elapsed time from `prev_t` to `t`, **regardless of which speaker sent either event** — 43 same-speaker pairs, 45 cross-speaker pairs, 17 with an unresolved predecessor (`prev_eid_unresolved`) | Directly observed/derived; **not equivalent to reply latency** — its cross-speaker subset yields Naomi 361s / Alex 97s, which does **not** reproduce the published Aftermath medians (169s / 122s) |
| Two specific large gaps used by variant 2C | float | seconds | 2 of 105 rows | Row-level `gap_sec` values: **676,768s** (before 21 Jul, `eid` `G201`) and **587,598s** (before 11 Jul, `eid` `G212`) | Directly observed; these are the "inter-contact gap" / "Silence gap" figures cited in `nalex_viz_schema.json → artifact_2_latency_convergence.records` |

**Limitation:** must be visually and definitionally separated from any true reply-latency figure if both appear in the same artifact (this is exactly the 2C caveat in §4).

## 3.6 `conflict_questions_annotated.json`

**Role:** The definitive message-level annotation layer for the Conflict-phase question sample (per `index.md` §5, superseding `conflict_questions.txt`, which lacks this layer).

**Structure:** flat array of 17 objects. Record shape: `timestamp`, `speaker` (`Naomi` | `Alex`), `text`, `answered` (`Partial` | `No` — `Yes` never occurs), `defensive` (`Y`/`N`), `accusatory` (`Y`/`N`), `rhetorical` (`Y`/`N`), `logistical` (`Y`/`N`), `intent` (`clarify` | `challenge` | `boundary` | `justify` | `deflect` | `repair`), `loop_tag` (free-form short label, e.g. `directness-loop`, `proof-loop`, `flirting-ambiguity-loop`, `repair-loop`, `blame-loop`, `avoidance-loop`, `boundary-loop`), `heat` (`tense` | `hot` | `explosive`), `risk` (free-form, e.g. `high-signal`, `repetitive`, `loaded`, `cornering`, `action-needed`), `genuine_unanswered` (boolean), `notes` (analyst free text).

**Population and sample relationship (binding caveat, verbatim from `nalex_viz_ideation.md` §4 and `nalex_viz_schema.json → artifact_4_conflict_question_function.sample_caveat`):** *"`conflict_questions_summary.json` contains 17 fully message-level-annotated questions (11 Naomi, 6 Alex), a sample of the 83 total literal-'?' questions documented for the Conflict phase (39 Naomi, 44 Alex) in `CURRENT_STATE_CLEAN.md`. Counts below describe the annotated sample only, not the full Conflict-phase question set."* The sample's speaker skew (11:6 Naomi-heavy) **inverts** the population's (39:44 Alex-heavy).

| Field | Type | Unit | Population | Derivation | Status |
|---|---|---|---|---|---|
| `answered` | enum | — | 17 annotated | Analyst judgment | **Annotated** |
| `intent`, `loop_tag`, `heat`, `risk` | enum/free-form | — | 17 annotated | Analyst judgment; per `viz_schema_template.md`, `heat`/`loop_tag`/`intent` are "optional annotation metadata fields... supplementary context only and must not be used by the renderer to select or alter visual encoding" | **Annotated** |
| `genuine_unanswered` | boolean | — | 17 annotated (3 `true`, 14 `false`) | Analyst judgment | **Annotated**; see §3.6.1 for the resolved CSV/JSON discrepancy |
| `timestamp` | string | — | 17 annotated, spanning 2026-06-26 16:04:52 to 2026-07-04 23:36:05 | Directly observed | Directly observed; **non-uniform distribution** — 12 of 17 fall on 26–27 Jun, 5 fall on 4 Jul, nothing in between |

**3.6.1 — Resolved CSV/JSON discrepancy.** `conflict_questions_annotated.csv` previously disagreed with the JSON export on `genuine_unanswered` (CSV: 7/17 `yes`; JSON: 3/17 `true`). Root cause: `refactor_questions_v2.py` (the live annotation generator per `index.md` §7.1) writes the JSON/summary files directly and hardcodes `genuine_unanswered=True` for exactly 3 substring matches; it never touched the CSV, which was a stale hand-annotation export. **The CSV has been regenerated from the JSON (2026-08-06); all 17 rows now agree at 3/17 across every field.** This is fully resolved and does not block any Q4 render.

## 3.7 Existing schema, renderer, style-token, and pipeline files that govern this artifact

**3.7.1 — `research_prompt_modes/analysis_outputs/nalex_viz_schema.json`.** A fully flattened, `viz_schema_template.md`-conformant record set already covering `artifact_1_volume_asymmetry`, `artifact_2_latency_convergence`, `artifact_3_initiation_closure`, and `artifact_4_conflict_question_function`. Each record carries `theme`, `phase`, `speaker`, `metric {name, value, unit}`, `evidence_quote`, `confidence`, `linked_theme`, `relation_type`, `visual_hint`, `forward_looking_evaluation`, `scope`, `detail_label`, `display_instance`. **This file already contains all 8 records required for 3C** — see §6's reconciliation, which corrects the ideation document's "new records needed" claim.

**3.7.2 — `visualisations/nalex_mobile_infographic_schema.json`.** A second, independently authored flattened schema (generated 2026-08-06) targeting a different form factor (a "vertical mobile infographic, single column, Pixel 10 Pro (412 x 917 dp viewport)"). It is valuable prior art for this specification because it already contains:
- A `rendering_contract` string establishing the `render_on_face` convention: *"Render only these records. Do not infer new themes, rewrite evidence, add analysis, or compute new metrics. Caveat strings marked render_on_face MUST appear in the artifact body, not in comments or footnotes."*
- An `artifact_3_initiation_closure` section with a `definitions` array giving the exact, pre-vetted wording for the two terms 3C's core claim depends on:
  - `"session close"`: *"the last turn before a 60-minute gap — a mechanical artifact, not a communicative act"*
  - `"explicit sign-off"`: *"a verbal termination move"*
- Pre-vetted `render_on_face` caveat strings for the same claim 3C makes (quoted in full in §5.7).
- An `interpretation_records` array that correctly separates `alex_withdrawal_by_exit` (tagged `INTERPRETATION`, sourced from `emotional_tags`) from `naomi_never_closes_verbally` (tagged `STRUCTURAL TAG`, sourced from `problematic_tags`) — this distinction must be preserved in any 3C render (§7).
- `render_directives` (device, viewport, design system, color roles, accessibility-adjacent rules) for its own (different) form factor. These are **not** directly reusable for 3C's card-based layout (§5.6 specifies 3C's own layout) but establish that per-render `render_directives` blocks are the established pattern in this repository.

**3.7.3 — `visualisations/nalex_playbook_dark_m3.html`, `nalex_mobile_v1_playful.html`, `nalex_mobile_v2_polished.html`, `nalex_mobile_v3_dramatic.html`, `nalex_patterns_flashcards.html`.** Rendered HTML artifacts implementing the mobile-infographic schema (§3.7.2) in three stylistic directions, plus a flashcard-format artifact. Each defines its own CSS custom-property color palette (not shared across files — e.g., `nalex_mobile_v1_playful.html` uses `--naomi:#FF63C4` / `--alex:#3FE7E0`; `nalex_patterns_flashcards.html` uses `--naomi:#87719d` / `--alex:#5f7f96`). **None of these palettes is canonical for 3C** — 3C should either adopt the ideation-preview artifact's own token set (§8.3, since that is the direct visual precedent for the 12-variant comparison 3C was selected from) or define a new one; this document specifies the former as the default (§8.3).

**3.7.4 — `research_prompt_modes/nalex_gemini_viz_corrective_prompt.md`.** Referenced by `index.md` §11 as the third mandatory pipeline document. Its role (per `index.md`) is to constrain a rendering model to "dumb layout engine" behavior. `UNVERIFIED — REQUIRES SOURCE INSPECTION`: this document's exact verbatim text was not retrieved during this inspection pass; its existence and role are confirmed by `index.md` §10/§11, but its literal wording should be re-read before invoking a rendering model.

**3.7.5 — No dedicated data-dictionary, automated-validator, or CI-style schema-validation file was found in the repository** (searched for `*data_dict*`, `*style_token*`, `*renderer*`, `*validation*`, `*.css` at repository root and one level deep, excluding `_archive/`). Validation is currently manual, against the checklists in `visualization_pipeline.md` and this document's §9. `UNVERIFIED — REQUIRES SOURCE INSPECTION` if a validator exists elsewhere in the tree not covered by this search pattern.

---

# 4. Variant catalogue

All 12 variants, complete. Values are drawn from `nalex_viz_ideation.md` (source ranking/rationale text), cross-verified against `phase_profile.json`, `baseline_comparison_audit.json`, `aftermath_stats.json`, `gap_stats_out.json`, and `conflict_questions_annotated.json` (source numeric ground truth) per §3.

## Question 1 — Volume asymmetry across phases

Headline: word ratio N:A moves **1.83× → 1.12× → 3.14×** (Baseline → Conflict → Aftermath), per `baseline_comparison_audit.json`.

### 1A — Grouped columns, words per phase
- **Visual question:** How the word-volume gap between Naomi and Alex changes across Baseline → Conflict → Aftermath.
- **Tier:** A — Neutral.
- **Rank:** 2 of 3.
- **Ship status:** `FINAL`.
- **Selected/picked:** No (1C is picked for Q1).
- **Required source files/fields:** `baseline_comparison_audit.json → {Baseline,Conflict,Aftermath}.{N_w,A_w}`; optionally `.{N_msg,A_msg}`. Equivalent to `nalex_viz_schema.json → artifact_1_volume_asymmetry.records` — renders with zero schema work.
- **Population/denominator:** All words, all speakers, per phase; phases span 83/13/11 calendar days respectively.
- **Exact values:** Baseline 1,693 (N) vs. 927 (A), ratio 1.83×. Conflict 5,888 (N) vs. 5,233 (A), ratio 1.12×. Aftermath 6,852 (N) vs. 2,181 (A), ratio 3.14×.
- **Chart form:** Three phase groups on the x-axis, two columns per group (Naomi, Alex), y = words. Ratio printed above each group as a plain label. No color semantics beyond speaker identity.
- **Interpretation statement:** None required (Tier A).
- **INTERPRETATION tag:** None.
- **Mandatory caveat:** Raw totals conflate turn count with turn length; phases span very different calendar windows (83/13/11 days) — columns are not rates.
- **Data-integrity/inference risk:** Low. The Conflict near-parity (5,888 vs. 5,233) is real and non-obvious — it contradicts a "she always talks more" reading — but the chart cannot show *why* (see 1B/1C).
- **Render blockers:** None.
- **Conditions to ship:** None beyond standard §9 checks; lowest-risk artifact in the set.

### 1B — Mirrored volume, turn-length overlay
- **Visual question:** Same as 1A, decomposed by turn-length mechanism.
- **Tier:** B — Lightly interpretive.
- **Rank:** 3 of 3.
- **Ship status:** `EXPLORATORY`.
- **Selected/picked:** No.
- **Required source files/fields:** `phase_profile.json → phases.*.speakers.*.{words,mean_words_per_turn,median_words_per_turn,messages}`; `asymmetry.word_ratio_N_over_A`.
- **Population/denominator:** Same as 1A, plus per-turn statistics.
- **Exact values:** Conflict mean words/turn 62.5 (N) vs. 42.2 (A); median 39.5 (N) vs. 21 (A). Alex reaches near-parity via more, shorter turns (124 vs. 94 messages).
- **Chart form:** Horizontal population-pyramid — phases stacked as three rows, Naomi's words extending left, Alex's right from a shared centre axis; `mean_words_per_turn` overlaid as a dot on each bar.
- **Interpretation statement:** "Narrowing then widening," framed top-to-bottom.
- **INTERPRETATION tag:** None (Tier B, not C).
- **Mandatory caveat:** The mirrored axis implies commensurability it doesn't have; the "narrowing then widening" reading is imposed by row order, not a fitted trend statistic.
- **Data-integrity/inference risk:** Medium — visually equalizes very different absolute scales.
- **Render blockers:** None technical; design-form risk only.
- **Conditions to ship:** Not recommended to ship as-is; the mechanism insight is real but better delivered by a slope or dual-axis chart.

### 1C — Decomposed audience bar: who was present for the words
- **Visual question:** Same as 1A, decomposed by audience presence.
- **Tier:** C — Opinionated.
- **Rank:** 1 of 3 · **pick**.
- **Ship status:** `FINAL (CONDITIONAL ON CAVEAT SHOWN)`.
- **Selected/picked:** Yes.
- **Required source files/fields:** `phase_profile.json → phases.*.speakers.*.{words,solo_session_words,solo_session_turns,post_exit_tail_words,post_exit_tail_turns}`; interpretation labels `tag_vocabulary.emotional_tags.{naomi_unwitnessed,naomi_post_exit_continuation,naomi_escalating_elaboration}`.
- **Population/denominator:** Per speaker per phase words, decomposed into live-exchange / solo-session / post-exit-tail.
- **Exact values:** Aftermath — Naomi 2,585 of 6,852 words (37.7%) produced with no one on the other end (793 solo + 1,792 post-exit); Alex's solo and post-exit words are 0. Baseline — Naomi 1,082 of 1,693 words solo (chronic, not new).
- **Chart form:** One stacked bar per speaker per phase, segmenting each speaker's words into live exchange / solo session / post-exit tail.
- **Interpretation statement:** "A third of what she wrote had no audience" — reframes the raw 3× volume gap into an audience-presence fact.
- **INTERPRETATION tag:** `naomi_unwitnessed` — *"INTERPRETATION: posture of speaking without confirmation of being heard."* Also draws on `naomi_post_exit_continuation` (problematic/structural tag, not INTERPRETATION) and `naomi_escalating_elaboration` (emotional/INTERPRETATION).
- **Mandatory caveat:** "Post-exit" is defined by absence of turns in this corpus; the Aftermath is 100% audio — if Alex replied by text, those turns are missing by construction, and the post-exit segment is an **upper bound**, not a measurement. Must sit on the artifact face, not in a footnote.
- **Data-integrity/inference risk:** Medium-high, mitigated by the mandatory on-face caveat.
- **Render blockers:** None — required fields already exist in `phase_profile.json`.
- **Conditions to ship:** Caveat must be rendered on the artifact face.

**Q1 ranking: 1C > 1A > 1B.**

## Question 2 — Latency convergence

**The evidentially weakest question in the set** — three point-pairs, one a range, one resting on 7–8 observations.

### 2A — Slope chart, log scale, Conflict as band
- **Visual question:** How median reply latency for each speaker changes across phases.
- **Tier:** A — Neutral.
- **Rank:** 1 of 3 · **pick**.
- **Ship status:** `FINAL (CONDITIONAL ON CAVEAT SHOWN)`, specifically "Final (band + n-counts required)."
- **Selected/picked:** Yes.
- **Required source files/fields:** `phase_profile.json → phases.*.speakers.*.median_reply_seconds` (authoritative for ranges); `baseline_comparison_audit.json → *.{N_lat,A_lat}` for point values; `phase_profile.json → notes` for n=7/8 disclosure.
- **Population/denominator:** Baseline: 7 obs. (Naomi), 8 obs. (Alex). Conflict: range due to 36 approximate-timestamp events. Aftermath: full population (105 events).
- **Exact values:** Baseline 484s (N, n=7) vs. 101s (A, n=8). Conflict 112–120s (N) vs. 70–94s (A) — band, not point. Aftermath 169s (N) vs. 122s (A).
- **Chart form:** Two lines across Baseline → Conflict → Aftermath, y = median reply seconds, log scale. Conflict rendered as a **vertical band**, not a point. Baseline points annotated with observation counts.
- **Interpretation statement:** Convergence is driven almost entirely by Naomi's line falling (484s → ~120s); Alex's is close to flat throughout (101 → 70–94 → 122). "Convergence" is really "one party sped up."
- **INTERPRETATION tag:** None (Tier A).
- **Mandatory caveat:** Three observations per line is not a trend; the log axis visually compresses the Baseline gap that is the finding's whole basis.
- **Data-integrity/inference risk:** High if the band and n-counts are omitted — without them this becomes an overclaim.
- **Render blockers:** `nalex_viz_schema.json → artifact_2_latency_convergence.records` currently stores Conflict as points (120/94), not the range — **the schema records must have the range restored before this variant renders honestly** (see §6 note on this gap, which is separate from and in addition to the 3C schema work).
- **Conditions to ship:** Band + n-counts rendered on face; schema range restored first.

### 2B — Ratio vs. parity reference
- **Visual question:** Same, expressed as a single convergence ratio.
- **Tier:** B — Lightly interpretive.
- **Rank:** 3 of 3.
- **Ship status:** `DO NOT SHIP`.
- **Selected/picked:** No.
- **Required source files/fields:** `phase_profile.json → phases.*.asymmetry.latency_ratio_N_over_A`.
- **Population/denominator:** Same as 2A, collapsed to one ratio per phase.
- **Exact values:** 4.79× (Baseline) → 1.2–1.7× (Conflict) → 1.39× (Aftermath).
- **Chart form:** Single line of the ratio across three phases with a horizontal reference line at 1.0 labeled "equal response speed."
- **Interpretation statement:** "Resolution toward equality" — the asymmetry collapses after Baseline and does not return.
- **INTERPRETATION tag:** None declared; this is exactly the risk flagged below.
- **Mandatory caveat:** Parity ≠ health — both replying fast is equally consistent with a high-arousal exchange neither can leave. Conflict value is a range treated as a point.
- **Data-integrity/inference risk:** High — the parity reference line invites the exact misreading it should avoid.
- **Render blockers:** Structural — a normative reference line over three points is inherently overclaiming; no caveat placement fixes this.
- **Conditions to ship:** None — do not render for an audience.

### 2C — In-session speed vs. between-session silence
- **Visual question:** Same, decomposed into within-session responsiveness vs. between-session silence.
- **Tier:** C — Opinionated.
- **Rank:** 2 of 3.
- **Ship status:** `EXPLORATORY`.
- **Selected/picked:** No.
- **Required source files/fields:** `aftermath_stats.json → sessions[1..5].{label,start,end,median_reply_seconds,turns,words}`; `gap_stats_out.json → rows[].gap_sec` for two gaps (676,768s and 587,598s); `phase_profile.json → phases.Silence.notes` for the 6.8-day figure.
- **Population/denominator:** 5 canonical Aftermath sessions (session 0 excluded, §3.4); 2 large inter-contact gaps.
- **Exact values:** Naomi 73s reply latency in the 11 Jul session; 6.8-day silent gap before 11 Jul contact resumed; 7.8-day-equivalent 587,598s gap before Silence-adjacent contact.
- **Chart form:** Composite — upper panel per-session median reply seconds for the five sessions; lower panel, shared time axis, inter-contact gaps drawn to scale.
- **Interpretation statement:** Fast responsiveness inside a session coexists with week-long silences between them — bursty contact, not sustained contact.
- **INTERPRETATION tag:** `naomi_anticipatory_vigilance` — *"INTERPRETATION: sharply reduced latency consistent with monitoring."*
- **Mandatory caveat:** Two different units stacked — session medians are true reply latency; the gap panel is elapsed time regardless of speaker (`gap_sec`), not a latency measure. `aftermath_stats.json` session 0 (5 Jul) is Conflict-phase and must be dropped.
- **Data-integrity/inference risk:** Medium-high — requires two simultaneous caveats to remain honest.
- **Render blockers:** Session 0 exclusion must be enforced at extraction time, not left to the renderer.
- **Conditions to ship:** Not recommended as final; requires one caveat too many for a first canonical render.

**Q2 ranking: 2A > 2C > 2B. Do not render 2B first (or at all, without a redesign).**

## Question 3 — Initiation and closure asymmetry

Headline: opens 5:5 → 5:5 → 5:0; closes 4:6 → 3:7 → 5:0.

### 3A — Two-row small-multiple of 100% stacked bars
- **Visual question:** Who opens and who closes sessions, per phase.
- **Tier:** A — Neutral.
- **Rank:** 2 of 3.
- **Ship status:** `FINAL`.
- **Selected/picked:** No (3C is picked).
- **Required source files/fields:** `phase_profile.json → phases.*.speakers.*.{session_opens,session_closes}` and `phases.*.sessions_60min`; `nalex_viz_schema.json → artifact_3_initiation_closure.records` (already flattened).
- **Population/denominator:** Sessions per phase — Baseline 10, Conflict 10, Aftermath 5.
- **Exact values:** Opens: Baseline 5:5, Conflict 5:5, Aftermath 5:0. Closes: Baseline 4:6, Conflict 3:7, Aftermath 5:0.
- **Chart form:** 2 rows × 3 columns. Row 1 = opens, row 2 = closes; one column per phase. Each cell a single 100% horizontal bar split Naomi/Alex, raw counts printed inside.
- **Interpretation statement:** Opens stay even until they don't; closes drift the *other* way first (4:6 → 3:7) before flipping entirely.
- **INTERPRETATION tag:** None (Tier A).
- **Mandatory caveat:** Aftermath denominator is 5 sessions — one session is 20% of the bar; the flip to 5:0 is a small-n event.
- **Data-integrity/inference risk:** Low-medium, addressed by the caveat.
- **Render blockers:** None — renders directly from existing schema records.
- **Conditions to ship:** Standard §9 checks only.

### 3B — Opens × closes quadrant, trajectory arrows
- **Visual question:** Same, as a two-dimensional trajectory.
- **Tier:** B — Lightly interpretive.
- **Rank:** 3 of 3.
- **Ship status:** `EXPLORATORY`.
- **Selected/picked:** No.
- **Required source files/fields:** Derived shares from `phase_profile.json → phases.*.speakers.*.{session_opens,session_closes}` over `sessions_60min`.
- **Population/denominator:** Same denominators as 3A, expressed as shares (6 points: 2 speakers × 3 phases).
- **Exact values:** Same underlying counts as 3A, plotted as (opens-share, closes-share) coordinates.
- **Chart form:** Scatter, x = opens share, y = closes share; one point per speaker per phase, arrows connecting each speaker's three points in phase order.
- **Interpretation statement:** The two speakers trace opposite paths to opposite corners.
- **INTERPRETATION tag:** None declared.
- **Mandatory caveat:** Arrows imply continuous motion through a space with only 3 discrete points; the longest arrow crosses the unrepresented Silence phase (0 events).
- **Data-integrity/inference risk:** Medium-high — the trajectory metaphor over-asserts continuity.
- **Render blockers:** None technical; design-form risk only.
- **Conditions to ship:** Not recommended; elegant but overclaims continuity.

### 3C — Closes vs. explicit sign-offs
- **Visual question:** Who ends things — mechanical session closes vs. verbal sign-offs.
- **Tier:** C — Opinionated.
- **Rank:** 1 of 3 · **pick**.
- **Ship status:** `FINAL (CONDITIONAL ON CAVEAT SHOWN)`, specifically "Final (both definitions must be shown)."
- **Selected/picked:** Yes — **and this is the recommended first canonical render overall (§5).**
- **Required source files/fields:** `phase_profile.json → phases.*.speakers.*.{session_closes,explicit_signoff_turns}`; `corpus_wide.explicit_signoffs_total`; `phases.*.asymmetry.explicit_signoffs_N_to_A`.
- **Population/denominator:** Sessions per phase (10, 10, 5) for closes; whole 378-event corpus for sign-off totals.
- **Exact values:** Session closes: Baseline 4:6, Conflict 3:7, Aftermath 5:0. Explicit sign-offs: Baseline 0:0, Conflict 0:11, Aftermath 0:4. Corpus-wide: Alex 15, Naomi 0.
- **Chart form:** Paired encoding per phase — session closes as bars (mechanical), `explicit_signoff_turns` as a distinct overlaid mark (verbal). A corpus-wide strip beneath: Alex 15, Naomi 0.
- **Interpretation statement:** "Closing" means two entirely different acts. Alex ends exchanges verbally; Naomi issues zero explicit sign-offs in the entire 378-event corpus, yet is credited with 5 of 5 Aftermath closes — the residue of being the last one still speaking.
- **INTERPRETATION tag:** `alex_withdrawal_by_exit` — *"INTERPRETATION: managing load by ending exchanges rather than escalating"* — and `dyad_asymmetric_repair_expectation` — *"INTERPRETATION: each waits for the other to perform the first repair move."* Also cites the **structural** (not INTERPRETATION) tags `problematic_tags.{naomi_never_closes_verbally, dyad_no_closure_event}`, which must be rendered without an `INTERPRETATION:` prefix and without being visually indistinguishable from the two emotional tags.
- **Mandatory caveat:** "Session close" is a mechanical artifact of the 60-minute-gap rule, not a communicative act — and in the Aftermath, Naomi's 5 closes overlap her 11 post-exit tail turns, so the metric partly counts *talking after he left* as *closing*.
- **Data-integrity/inference risk:** Medium, fully mitigated by rendering both definitions on the artifact face (full exhaustive treatment in §5).
- **Render blockers:** None — see §6, which confirms all 8 required schema records already exist in `nalex_viz_schema.json`.
- **Conditions to ship:** Both definitions ("session close" and "explicit sign-off") rendered on the artifact face.

**Q3 ranking: 3C > 3A > 3B.**

## Question 4 — Conflict question function

**The annotated layer is 17 questions (11 Naomi, 6 Alex) against a Conflict-phase population of 83 literal-'?' questions (39 Naomi, 44 Alex)** — a ~20% non-random sample whose speaker skew *inverts* the population's.

### 4A — Two-panel population/sample split
- **Visual question:** Within the annotated 17-question sample, what share is genuinely unanswered vs. serving another function — set against the 83-question population it's drawn from.
- **Tier:** A — Neutral.
- **Rank:** 1 of 3 · **pick**.
- **Ship status:** `FINAL`.
- **Selected/picked:** Yes.
- **Required source files/fields:** `baseline_comparison_audit.json → Conflict.{N_q,A_q,N_unans,A_unans}` and `Baseline.{…}`; `conflict_questions_annotated.json → [].intent`; `nalex_viz_schema.json → artifact_4_conflict_question_function.sample_caveat` verbatim.
- **Population/denominator:** Left panel: 83-question Conflict population. Right panel: 17-question annotated sample. Explicitly disjoint, no shared scale.
- **Exact values:** Population: Naomi 39 asked / 8 unanswered, Alex 44 asked / 15 unanswered (Conflict); Naomi 12/6, Alex 4/1 (Baseline, for contrast). Sample: 17 questions by `intent` — challenge 5, boundary 5, clarify 4, justify 1, deflect 1, repair 1.
- **Chart form:** Deliberately disjoint panels with a visible divider, labeled "20% sample — not drawn from the left panel."
- **Interpretation statement:** Alex asks more questions and has more go unanswered, reversing the Baseline pattern; the annotated sample skews Naomi-heavy while the population skews Alex-heavy, so the right panel cannot be read as evidence about the left.
- **INTERPRETATION tag:** None (Tier A).
- **Mandatory caveat:** Alex's documented 15/44 unanswered figure is "roughly double any mechanical timing rule (7/44)" and is a content-level judgment not reproducible from `events.jsonl`.
- **Data-integrity/inference risk:** Low — this variant's whole design is structured to prevent the sample-as-population error.
- **Render blockers:** None.
- **Conditions to ship:** Sample caveat rendered on face.

### 4B — Intent × answered matrix
- **Visual question:** Same, cross-tabulated by intent and answer completeness.
- **Tier:** B — Lightly interpretive.
- **Rank:** 3 of 3.
- **Ship status:** `EXPLORATORY`.
- **Selected/picked:** No.
- **Required source files/fields:** `conflict_questions_annotated.json → [].{intent,answered,speaker}`.
- **Population/denominator:** 17 annotated questions × 6 intents × 2 answered-states (`Partial`/`No`) × 2 speakers.
- **Exact values:** `answered`: Partial 10, No 7, Yes 0 (of 17). Most cells at 0 or 1 (`justify`, `deflect`, `repair` each have exactly one observation).
- **Chart form:** Heatmap/dot matrix, 6 intent categories × 2 answered states, split by speaker, cells sized or shaded by count.
- **Interpretation statement:** Not one of the 17 annotated questions is recorded as fully answered.
- **INTERPRETATION tag:** None declared.
- **Mandatory caveat:** n=17 spread over 6×2×2 leaves most cells at 0 or 1 — a heatmap over cells that sparse invites pattern-reading the counts cannot support.
- **Data-integrity/inference risk:** High for the matrix form specifically (sparse-cell over-interpretation risk); the underlying fact is sound.
- **Render blockers:** None technical; design-form risk only.
- **Conditions to ship:** Not recommended as a matrix; the one real finding belongs as an annotation on 4A instead.

### 4C — Annotated-question timeline by heat and loop
- **Visual question:** Same, as a temporal/structural map of the annotated sample.
- **Tier:** C — Opinionated.
- **Rank:** 2 of 3.
- **Ship status:** `EXPLORATORY`.
- **Selected/picked:** No.
- **Required source files/fields:** `conflict_questions_annotated.json → [].{timestamp,speaker,intent,loop_tag,heat,risk,genuine_unanswered,notes}`; `conflict_questions_summary.json → conversation_summary.{dominant_loop,core_problem,repair_attempts,boundary_statements}`; `conflict_questions_tags.csv`.
- **Population/denominator:** 17 annotated questions, non-uniformly distributed in time.
- **Exact values:** `proof-loop` carries 6 of 17 and holds 2 of the 3 canonical `genuine_unanswered` questions. 26–27 Jun cluster: 10 of 12 hot-or-explosive, intent running challenge/clarify. 4 Jul cluster (5 turns): all `tense`, intent shifting to boundary/repair/clarify.
- **Chart form:** Timeline/structured scatter, 17 questions on a time axis (26 Jun → 4 Jul), y-grouped by `loop_tag`, marks encoded by `heat`, shape by speaker. `dominant_loop` and `core_problem` quoted verbatim as standing text.
- **Interpretation statement:** The shape of the deadlock — consistent with de-escalation into boundary-setting rather than resolution, matching the phase-level `dyad_no_closure_event` tag.
- **INTERPRETATION tag:** Draws on the phase-level structural fact `dyad_no_closure_event` (a `problematic_tag`, structural not emotional); no `emotional_tags` entry is specifically cited by this variant in the ideation source.
- **Mandatory caveat:** The 17 points are non-uniform in time — 12 fall on 26–27 Jun and 5 on 4 Jul, with nothing in between — so the apparent cool-down may be an artifact of which turns were annotated, not a real trajectory.
- **Data-integrity/inference risk:** High for the "continuous history" reading a timeline invites; the underlying loop/heat facts are sound.
- **Render blockers:** None technical.
- **Conditions to ship:** Exploratory only; becomes the strongest candidate in this question if the annotation layer is extended to the full 83-question population.

**Q4 ranking: 4A > 4C > 4B.**

---

# 5. Recommended first render: 3C — Closes vs. explicit sign-offs

## 5.1 Why 3C is the recommended first canonical render

Verbatim rationale from `nalex_viz_ideation.md` §6, preserved in full:

1. **Strongest evidence base of the twelve.** Whole-population integer counts, reproducible from `events.jsonl` (for the mechanical half — session closes), with no sampling problem (unlike Q4), no range ambiguity (unlike Q2), and no tokenizer variance (unlike Q1).
2. **Highest information gain.** `explicit_signoff_turns` is the most underused field in the corpus, and the Naomi-0-of-378 figure is the single most unambiguous number in the dataset.
3. **It corrects rather than decorates.** 3A alone shows Naomi closing 5 of 5 Aftermath sessions, which reads naturally as "she ends conversations." 3C shows that reading is close to backwards. A first render that pre-empts a likely misreading is worth more than one that restates a known headline.
4. **Its interpretation is pre-sanctioned.** `alex_withdrawal_by_exit` and `naomi_never_closes_verbally` already exist in `phase_profile.json` with their status declared — Tier C invents nothing.

## 5.2 Why its evidence base is stronger than the other variants

- **Vs. Q1 (volume):** word counts carry <0.3% tokenizer variance across sources (§3.1); 3C's counts (session closes, sign-off turns) are integer counts with no tokenizer dependency.
- **Vs. Q2 (latency):** Q2's Conflict-phase medians are ranges resting partly on 36 approximate-timestamp events, and Baseline rests on 7–8 observations. 3C's Conflict/Aftermath figures are exact, whole-population integer counts (10 sessions, 10 sessions, 5 sessions; 378 total events for the sign-off corpus total) with no approximation.
- **Vs. Q4 (questions):** Q4's most interesting layer (17-question annotation) is an admitted ~20% non-random sample whose skew inverts the population it's drawn from. 3C's sign-off counts are drawn from the **entire** 378-event corpus, not a sample.

## 5.3 The exact core claim 3C is permitted to make

3C may claim, and only claim: **"Closing" a conversation is not one act but two, and the two acts are performed by different people.** Specifically:
- Alex ends live exchanges with an explicit verbal termination move 15 times across the corpus (11 in Conflict, 4 in Aftermath, 0 in Baseline).
- Naomi never does this — 0 times across all 378 events, all three active phases.
- The separate, purely mechanical "session close" tally (whoever's turn happens to precede a 60-minute silence) shows the *opposite* surface pattern in the Aftermath: Naomi closes 5 of 5 sessions there, after Alex closed the majority in both prior phases (6 of 10 Baseline, 7 of 10 Conflict).
- These two facts, shown together, demonstrate that the mechanical "session close" tally, read alone, would support a materially misleading claim ("she ends things") that the sign-off data contradicts.

## 5.4 The exact claim 3C must not make

- It must **not** claim Naomi "never ends conversations" is evidence of healthier, more open, or more committed communication, nor that Alex's sign-offs are evidence of avoidance, unhealthy withdrawal, or bad faith — no clinical, motive-attributing, or evaluative claim beyond the pre-declared `INTERPRETATION` tag text is permitted (§2.5).
- It must **not** claim that Naomi's Aftermath "closes" are equivalent, functionally or experientially, to Alex's mechanical closes in earlier phases — the render must show, not elide, that Naomi's 5 Aftermath closes overlap her 11 post-exit tail turns (§5.7).
- It must **not** present the sign-off count as evidence about *why* either party behaves as they do — only the `INTERPRETATION`-tagged hypothesis text already declared in `phase_profile.json` may gesture at motive, and only with its prefix visible.
- It must **not** claim the "breach" sub-pattern (§3.2.2 — 9 of Alex's 11 Conflict sign-offs were followed by more talking in the same session) unless that sub-pattern is added as a new schema record first (it is not currently a flattened field; see §6.9). The base 3C render as specified in this document does not include the breach data.

## 5.5 All population counts, phase counts, corpus-wide counts, and definitions

| Metric | Baseline | Conflict | Aftermath | Corpus-wide |
|---|---|---|---|---|
| Sessions (60-min-gap rule) | 10 | 10 | 5 | — |
| Session opens (N:A) | 5:5 | 5:5 | 5:0 | — |
| Session closes (N:A) | 4:6 | 3:7 | 5:0 | — |
| Explicit sign-offs (N:A) | 0:0 | 0:11 | 0:4 | Alex 15, Naomi 0 |
| Total corpus events | — | — | — | 378 (Alex 188, Naomi 187, System 3) |

**Definition — "session close":** the last turn before a 60-minute inter-event gap. A mechanical artifact of the sessionization rule, **not** necessarily a communicative act.

**Definition — "explicit sign-off":** a turn whose text contains a verbal termination move — an utterance that announces the end of the live exchange (e.g. *"I'll speak to you another time,"* *"I'm not going to continue to argue about this tonight,"* *"should we just put a pin in it,"* *"I'm actually going to put my phone on silent"*). An analyst-classified content judgment (§3.2.1), not a keyword-matchable mechanical rule.

## 5.6 Interpretation tag: `alex_withdrawal_by_exit`

Exact string, from `phase_profile.json → tag_vocabulary.emotional_tags`:

> `alex_withdrawal_by_exit`: **"INTERPRETATION: managing load by ending exchanges rather than escalating"**

This tag must render with its `INTERPRETATION:` prefix intact and must not be paraphrased. It may be accompanied — but must remain visually distinct from — the structural (non-`INTERPRETATION`) tags this variant also cites:
- `naomi_never_closes_verbally` (from `problematic_tags`): **"Zero explicit sign-off moves in the phase."**
- `dyad_no_closure_event` (from `problematic_tags`): **"Phase ends without a mutual termination or repair turn."**
- `dyad_asymmetric_repair_expectation` (from `emotional_tags`): **"INTERPRETATION: each waits for the other to perform the first repair move."**

## 5.7 The mandatory caveat

Two equivalent, source-vetted wordings exist in the repository; either is acceptable, and the render should use one verbatim rather than compose a new paraphrase:

**From `nalex_viz_ideation.md` §3 (3C entry):**
> *"'Session close' is a mechanical artifact of the 60-minute gap rule, not a communicative act — and in the Aftermath Naomi's 5 closes overlap her 11 post-exit tail turns, so the metric partly counts talking after he left as closing. The artifact must define both terms on its face or it will be read as 'she ends conversations,' which is close to the opposite of what the data shows."*

**From `visualisations/nalex_mobile_infographic_schema.json` (`artifact_3_initiation_closure.caveats`, `render_on_face: true`):**
> *"Naomi's 5 Aftermath closes overlap her 11 post-exit turns — the metric partly counts talking after he left as closing."*
> *"Aftermath denominator is 5 sessions. One session is 20% of the bar."*

Both the session-close and explicit-sign-off **definitions** (§5.5) must also appear on the artifact face per the same file's `definitions` array (`render_on_face: true` for both).

## 5.8 Concrete layout specification for the canonical render

**Title:** "Who Ends Things: Session Closes vs. Explicit Sign-Offs"

**Subtitle:** "Naomi ends 0 of 378 conversations verbally. Alex ends 15. The mechanical 'session close' tally tells a different story."

**Panel structure (top to bottom):**

1. **Definitions strip** (always visible, not collapsible, not a tooltip): two short definition cards, side by side —
   - Card A: "SESSION CLOSE — the last turn before a 60-minute gap. A mechanical artifact, not a communicative act."
   - Card B: "EXPLICIT SIGN-OFF — a verbal termination move."
2. **Panel 1 — Session closes (mechanical), by phase.** Three grouped bars (Baseline, Conflict, Aftermath), each split Naomi/Alex, with the raw N:A ratio printed inside or above each bar (4:6, 3:7, 5:0). Denominator (10/10/5 sessions) printed under each phase label.
3. **Panel 2 — Explicit sign-offs (verbal), by phase.** Same three-phase x-axis, aligned under Panel 1 for direct visual comparison. Bars for Naomi are present but at zero height in every phase (0:0, 0:11, 0:4) — do not omit the zero bar; its visible absence is the finding.
4. **Corpus-wide strip** beneath both panels: a single labeled bar or count pair, "Alex 15 : Naomi 0," explicitly scoped "across all 378 events, all phases."
5. **Interpretation block:** the `alex_withdrawal_by_exit` tag (with `INTERPRETATION:` prefix) and the two structural tags (`naomi_never_closes_verbally`, `dyad_no_closure_event`), visually distinguished from each other (§7, §8.4) and from the measured panels above.
6. **Caveat block** (always visible, on the artifact face, not a footnote or hover state): the §5.7 caveat text, plus the Aftermath 20%-denominator note.
7. **Source footnote:** "Source: phase_profile.json → phases.*.speakers.*.{session_closes, explicit_signoff_turns}; corpus_wide.explicit_signoffs_total. Session boundary: 60-minute inter-event gap."

**Phase ordering:** Baseline → Conflict → Aftermath, left to right, consistently across both panels. Silence is not shown (0 events, not applicable per §2.4 item 10 — Silence has no `session_closes`/`explicit_signoff_turns` records because it has zero events; it must be omitted, not shown as a zero bar, since the schema does not encode an explicit "not applicable" status for it — see §6 for the distinction between a true zero and an inapplicable phase).

**Labels:** every bar carries its exact integer count as an on-bar or above-bar label (no reliance on axis gridlines alone for precision reading). Phase denominators (sessions or corpus size) are printed, not implied.

**Annotations:** the Aftermath session-close bar (5:0, Naomi) must carry a direct annotation pointing to the post-exit-tail caveat — e.g., a footnote marker or connecting line to the caveat block — because this is the single most likely misreading point in the artifact.

**Color mapping:** Naomi and Alex each get one fixed hue used consistently across both panels and the corpus strip (see §8.3 for exact values). The two *panels* (mechanical vs. verbal) should be distinguished by panel position/framing/iconography, not by additional color — reserve color exclusively for speaker identity to avoid a competing color channel.

**Legend:** one shared legend for both panels (Naomi swatch, Alex swatch), positioned once, not repeated per panel.

**Denominator disclosures:** session counts (10/10/5) under Panel 1's phase labels; "378 events, all phases" under the corpus strip; explicit "5 sessions — one session is 20% of this bar" note attached to the Aftermath column specifically.

**Footnotes:** source footnote (above) plus a data-vintage note ("phase_profile.json Rev 4, generated 2026-08-02").

**Caveat placement:** on the artifact face, in a permanently visible block (§5.7) — never behind a hover, click, tooltip, or "learn more" affordance, per §7's ban on interaction-dependent disclosure of essential caveats.

## 5.9 Accessibility requirements

- **Non-color encoding:** Naomi/Alex must be distinguishable by a second channel beyond hue — e.g., a fixed left/right position convention (Naomi always left or always upper in every grouped pair), a text label on or adjacent to every bar, and/or a distinct fill pattern (solid vs. hatched) for colorblind-safe redundancy. Do not rely on hue alone anywhere in the artifact, including the corpus-wide strip.
- **Readable text equivalent:** every numeric claim in §5.5 must also exist as plain-text content in the artifact's DOM/alt-text layer (not only as an SVG/canvas visual mark), so it is available to a screen reader or a text-extraction pass without rendering the graphic.
- **Contrast:** text and data-ink must meet at least WCAG AA contrast against their background in both light and dark presentation, if both are supported (§8.2).
- **Alt text:** a single alt-text/summary string must state the core claim (§5.3) and the two headline numbers (Alex 15, Naomi 0) without requiring the visual to be parsed — see §8.6 for the exact required content.

## 5.10 Validation tests that must pass before publishing

1. **Field-trace test:** every number appearing on the artifact face is traceable to a named field in §5.5's table (no manually re-typed or re-derived number).
2. **Zero-bar test:** the Naomi explicit-sign-off bars render at visibly zero height in all three phases, not omitted from the chart.
3. **Definition-on-face test:** both definitions from §5.5 appear in the rendered output itself (screenshot/DOM check), not only in this specification or in surrounding chat/documentation.
4. **Caveat-on-face test:** the §5.7 caveat text (or the verbatim alternative) appears in the rendered output itself, not behind an interaction.
5. **Tag-prefix test:** `alex_withdrawal_by_exit` renders with its `INTERPRETATION:` prefix; `naomi_never_closes_verbally` and `dyad_no_closure_event` render without an `INTERPRETATION:` prefix and are visually distinguished from the `INTERPRETATION`-tagged content (§7, §8.4).
6. **Denominator-visibility test:** the Aftermath 5-session denominator and the 378-event corpus denominator are both visible on the artifact face.
7. **Silence-phase test:** Silence does not appear as a zero-value bar; it is either fully omitted with the omission logged in the render audit (per Validation Checklist item 10, §2.4), or explicitly marked "not applicable — 0 events" if the schema is extended to encode that status.
8. **No-new-vocabulary test:** a manual or automated diff of every label string against §11.2's closed tag vocabulary confirms no string outside that vocabulary (or outside plain measured-value labels) appears.
9. **Accessibility test:** §5.9's non-color-encoding and contrast requirements pass a manual or automated check (e.g., simulate protanopia/deuteranopia and confirm speaker identity remains distinguishable).
10. **Reproducibility test:** re-running the extraction step against the current `phase_profile.json` yields byte-identical values to those hardcoded in §5.5 (i.e., the render is generated from data, not hand-transcribed).

## 5.11 Failure modes that would make the render misleading or non-compliant

- Showing session-close counts without the explicit-sign-off counts alongside them (reintroduces the exact "she ends conversations" misreading 3C exists to correct).
- Showing explicit-sign-off counts without the corpus-wide "0 for Naomi" framing (loses the single most unambiguous number in the dataset).
- Omitting the post-exit-tail overlap caveat for Naomi's Aftermath closes (makes her 5:0 closure figure look like five clean, symmetrical endings when 11 of the underlying turns are post-exit-tail turns).
- Placing any required caveat or definition behind a hover state, tooltip, click-to-expand, or footnote asterisk with no visible expansion (violates §7's interaction-independence rule and this document's §1.4 exclusion of interactivity from the first render).
- Using color alone to distinguish Naomi/Alex (accessibility failure, §5.9).
- Blending the `INTERPRETATION`-tagged and structural-tagged text into a single undifferentiated "interpretation" block (erases the STRUCTURAL vs. INTERPRETATION distinction that `phase_profile.json`'s own tag_vocabulary maintains).
- Introducing any new descriptive or evaluative language not present in §11.2's tag vocabulary or in the plain measured labels (e.g., inventing "assertive," "avoidant," "healthier," or similar unlicensed vocabulary).
- Rendering the Silence phase as a zero bar rather than omitting it or explicitly marking it not-applicable (violates Validation Checklist item 10).
- Hardcoding the displayed values rather than deriving them from the schema records in §6 (breaks the reproducibility test, §5.10 item 10, and violates §7's traceability requirement).

---

# 6. Schema additions for 3C

## 6.1 Reconciliation with `nalex_viz_ideation.md` §5

The ideation document's §5 cross-cutting table states 3C requires new records: *"`explicit_signoff_turns` × 2 speakers × 3 phases (6) + corpus totals (2)"* = 8 new records. **On inspection of the current repository state, all 8 of these records already exist**, fully flattened, in `research_prompt_modes/analysis_outputs/nalex_viz_schema.json → artifact_3_initiation_closure.records`:

- Baseline: Naomi `explicit_signoff_turns` = 0; Alex = 0.
- Conflict: Naomi `explicit_signoff_turns` = 0; Alex = 11.
- Aftermath: Naomi `explicit_signoff_turns` = 0; Alex = 4.
- Corpus (`scope: "corpus"`, `detail_label: "Corpus"`): Naomi `explicit_signoffs_total` = 0; Alex `explicit_signoffs_total` = 15.

All six phase-level values and both corpus-level values cross-verify exactly against `phase_profile.json`'s `phases.*.speakers.*.explicit_signoff_turns` and `corpus_wide.explicit_signoffs_total`. The `session_opens`/`session_closes` records this variant also needs are likewise already present in the same schema file (matching `phase_profile.json` exactly: Baseline 4:6, Conflict 3:7, Aftermath 5:0 for closes).

**This supersedes the "new records needed" note in `nalex_viz_ideation.md` §5** for 3C specifically — it likely predates this schema file reaching its current, complete state, or was not cross-checked against it at write time. The 8 records below are therefore documented as **VERIFY** (confirm presence, correctness, and schema-conformance) rather than **CREATE**. No blocking schema work stands between the current repository state and a 3C render.

## 6.2 The 8 records

### Record 1 — Baseline session closes (Naomi)
- **ID:** `3c-r01`
- **Field/record name:** `session_closes` (Baseline, Naomi)
- **Source file/path:** `phase_profile.json → phases.Baseline.speakers.Naomi.session_closes`; mirrored in `nalex_viz_schema.json → artifact_3_initiation_closure.records[2]`
- **Datatype:** integer, permitted values 0–10 (bounded by `sessions_60min`)
- **Scope:** phase, speaker
- **Extraction/derivation rule:** count of sessions (60-minute-gap groups) whose last turn is attributed to Naomi, within the Baseline window (2026-04-01..2026-06-22)
- **Validation:** `session_closes.Naomi + session_closes.Alex == sessions_60min` for the phase (4 + 6 = 10 ✓)
- **Ambiguous cases:** a session with a single turn (no exchange) still has exactly one close, attributed to that turn's speaker — no special handling needed
- **Consumed by renderer as:** Panel 1, Baseline column, Naomi segment
- **Status:** raw-derived (mechanical, not annotated)

```json
{
  "id": "3c-r01",
  "theme": "initiation_closure_asymmetry",
  "phase": "Baseline",
  "scope": "phase",
  "detail_label": null,
  "display_instance": null,
  "speaker": "Naomi",
  "metric": { "name": "session_closes", "value": 4, "unit": "count" },
  "evidence_quote": "Baseline closes: Alex 6, Naomi 4",
  "confidence": "high",
  "linked_theme": "unilateral_initiation",
  "relation_type": "contrasts",
  "visual_hint": "bar"
}
```

### Record 2 — Baseline session closes (Alex)
- **ID:** `3c-r02`
- **Field/record name:** `session_closes` (Baseline, Alex)
- **Source file/path:** `phase_profile.json → phases.Baseline.speakers.Alex.session_closes`
- **Datatype:** integer, 0–10
- **Scope:** phase, speaker
- **Extraction/derivation rule:** as Record 1, attributed to Alex
- **Validation:** paired sum check with Record 1 (§6.2, Record 1)
- **Ambiguous cases:** none beyond Record 1
- **Consumed by renderer as:** Panel 1, Baseline column, Alex segment
- **Status:** raw-derived

```json
{
  "id": "3c-r02",
  "theme": "initiation_closure_asymmetry",
  "phase": "Baseline",
  "scope": "phase",
  "detail_label": null,
  "display_instance": null,
  "speaker": "Alex",
  "metric": { "name": "session_closes", "value": 6, "unit": "count" },
  "evidence_quote": "Baseline closes: Alex 6, Naomi 4",
  "confidence": "high",
  "linked_theme": "unilateral_initiation",
  "relation_type": "contrasts",
  "visual_hint": "bar"
}
```

### Record 3 — Conflict session closes (Naomi)
- **ID:** `3c-r03`
- **Source file/path:** `phase_profile.json → phases.Conflict.speakers.Naomi.session_closes`
- **Datatype:** integer, 0–10
- **Scope:** phase, speaker
- **Extraction/derivation rule:** as Record 1, Conflict window (2026-06-23..2026-07-05)
- **Validation:** 3 + 7 = 10 ✓
- **Ambiguous cases:** none additional
- **Consumed by renderer as:** Panel 1, Conflict column, Naomi segment
- **Status:** raw-derived

```json
{
  "id": "3c-r03",
  "theme": "initiation_closure_asymmetry",
  "phase": "Conflict",
  "scope": "phase",
  "detail_label": null,
  "display_instance": null,
  "speaker": "Naomi",
  "metric": { "name": "session_closes", "value": 3, "unit": "count" },
  "evidence_quote": "Conflict closes: Alex 7, Naomi 3",
  "confidence": "high",
  "linked_theme": "unilateral_initiation",
  "relation_type": "contrasts",
  "visual_hint": "bar"
}
```

### Record 4 — Conflict session closes (Alex)
- **ID:** `3c-r04`
- **Source file/path:** `phase_profile.json → phases.Conflict.speakers.Alex.session_closes`
- **Datatype:** integer, 0–10
- **Scope:** phase, speaker
- **Extraction/derivation rule:** as Record 3, attributed to Alex
- **Validation:** paired sum check
- **Ambiguous cases:** none additional
- **Consumed by renderer as:** Panel 1, Conflict column, Alex segment
- **Status:** raw-derived

```json
{
  "id": "3c-r04",
  "theme": "initiation_closure_asymmetry",
  "phase": "Conflict",
  "scope": "phase",
  "detail_label": null,
  "display_instance": null,
  "speaker": "Alex",
  "metric": { "name": "session_closes", "value": 7, "unit": "count" },
  "evidence_quote": "Conflict closes: Alex 7, Naomi 3",
  "confidence": "high",
  "linked_theme": "unilateral_initiation",
  "relation_type": "contrasts",
  "visual_hint": "bar"
}
```

### Record 5 — Aftermath session closes (Naomi)
- **ID:** `3c-r05`
- **Source file/path:** `phase_profile.json → phases.Aftermath.speakers.Naomi.session_closes`
- **Datatype:** integer, 0–5
- **Scope:** phase, speaker
- **Extraction/derivation rule:** as Record 1, Aftermath window (2026-07-11..2026-07-21)
- **Validation:** 5 + 0 = 5 ✓; **must render with the "one session = 20% of the bar" caveat attached** (§5.7)
- **Ambiguous cases:** this figure overlaps `post_exit_tail_turns` for Naomi (11 turns) — the record itself is unambiguous, but its *display* must carry the overlap caveat; see §5.8 annotation requirement
- **Consumed by renderer as:** Panel 1, Aftermath column, Naomi segment (with mandatory annotation)
- **Status:** raw-derived

```json
{
  "id": "3c-r05",
  "theme": "initiation_closure_asymmetry",
  "phase": "Aftermath",
  "scope": "phase",
  "detail_label": null,
  "display_instance": null,
  "speaker": "Naomi",
  "metric": { "name": "session_closes", "value": 5, "unit": "count" },
  "evidence_quote": "Aftermath closes: Naomi 5, Alex 0",
  "confidence": "high",
  "linked_theme": "unilateral_initiation",
  "relation_type": "escalates",
  "visual_hint": "bar"
}
```

### Record 6 — Aftermath session closes (Alex)
- **ID:** `3c-r06`
- **Source file/path:** `phase_profile.json → phases.Aftermath.speakers.Alex.session_closes`
- **Datatype:** integer, 0–5
- **Scope:** phase, speaker
- **Extraction/derivation rule:** as Record 5, attributed to Alex
- **Validation:** paired sum check; a value of 0 must render as a visible zero-height bar, not be omitted (§5.10 item 2)
- **Ambiguous cases:** none additional
- **Consumed by renderer as:** Panel 1, Aftermath column, Alex segment
- **Status:** raw-derived

```json
{
  "id": "3c-r06",
  "theme": "initiation_closure_asymmetry",
  "phase": "Aftermath",
  "scope": "phase",
  "detail_label": null,
  "display_instance": null,
  "speaker": "Alex",
  "metric": { "name": "session_closes", "value": 0, "unit": "count" },
  "evidence_quote": "Aftermath closes: Naomi 5, Alex 0",
  "confidence": "high",
  "linked_theme": "unilateral_initiation",
  "relation_type": "escalates",
  "visual_hint": "bar"
}
```

### Record 7 — Corpus-wide explicit sign-off total (Naomi)
- **ID:** `3c-r07`
- **Source file/path:** `phase_profile.json → corpus_wide.explicit_signoffs_total.Naomi`; mirrored in `nalex_viz_schema.json → artifact_3_initiation_closure.records[19]` (`scope: "corpus"`)
- **Datatype:** integer, permitted values 0–378
- **Scope:** corpus
- **Extraction/derivation rule:** sum of `explicit_signoff_turns` across Baseline + Conflict + Aftermath for Naomi (0 + 0 + 0 = 0)
- **Validation:** must equal the sum of the three phase-level `explicit_signoff_turns` records for Naomi (all zero)
- **Ambiguous cases:** none — this is the cleanest number in the dataset (§5.1 item 2)
- **Consumed by renderer as:** corpus-wide strip, Naomi value
- **Status:** derived (from annotated inputs — inherits the content-judgment status of `explicit_signoff_turns`, §3.2.1)

```json
{
  "id": "3c-r07",
  "theme": "initiation_closure_asymmetry",
  "phase": null,
  "scope": "corpus",
  "detail_label": "Corpus",
  "display_instance": null,
  "speaker": "Naomi",
  "metric": { "name": "explicit_signoffs_total", "value": 0, "unit": "count" },
  "evidence_quote": "Corpus total explicit signoffs",
  "confidence": "high",
  "linked_theme": "withdrawal_by_exit",
  "relation_type": "supports",
  "visual_hint": "strip"
}
```

### Record 8 — Corpus-wide explicit sign-off total (Alex)
- **ID:** `3c-r08`
- **Source file/path:** `phase_profile.json → corpus_wide.explicit_signoffs_total.Alex`
- **Datatype:** integer, 0–378
- **Scope:** corpus
- **Extraction/derivation rule:** sum of `explicit_signoff_turns` across Baseline + Conflict + Aftermath for Alex (0 + 11 + 4 = 15)
- **Validation:** must equal the sum of the three phase-level `explicit_signoff_turns` records for Alex
- **Ambiguous cases:** the underlying per-turn classification is a content judgment (§3.2.1); the sum itself is arithmetic once the per-turn classification is accepted
- **Consumed by renderer as:** corpus-wide strip, Alex value
- **Status:** derived (from annotated inputs)

```json
{
  "id": "3c-r08",
  "theme": "initiation_closure_asymmetry",
  "phase": null,
  "scope": "corpus",
  "detail_label": "Corpus",
  "display_instance": null,
  "speaker": "Alex",
  "metric": { "name": "explicit_signoffs_total", "value": 15, "unit": "count" },
  "evidence_quote": "Corpus total explicit signoffs",
  "confidence": "high",
  "linked_theme": "withdrawal_by_exit",
  "relation_type": "supports",
  "visual_hint": "strip"
}
```

## 6.3 Supplementary records already present but required for context (not new)

The 8 records above are the mechanical/verbal-close counts. 3C's layout (§5.8) also requires the six phase-level `explicit_signoff_turns` records (Baseline/Conflict/Aftermath × Naomi/Alex) for Panel 2 — these are **also already present** in `nalex_viz_schema.json` (verified in §6.1) and are not double-counted as "new" here; they are the phase-level components that Records 7–8 sum.

## 6.4 Backfill strategy for existing corpus records

No backfill is required — §6.1 establishes all 8 records already exist and cross-verify against `phase_profile.json`. If a future revision of `events.jsonl` adds events (e.g., a re-purged or extended corpus), the backfill procedure is:
1. Re-run the `explicit_signoff_turns` content-judgment classification (§3.2.1) against any new events — this step requires human/analyst review, as no automated classifier exists in the repository.
2. Re-run the mechanical `session_closes` derivation (60-minute-gap sessionization, last-turn attribution) — this step is fully automatable from `recompute_harness.py`'s existing `sessionize()` function pattern.
3. Regenerate `phase_profile.json` (bump `revision`), then regenerate the corresponding records in `nalex_viz_schema.json`.
4. Re-run §5.10's validation suite before re-shipping.

## 6.5 Idempotent generation requirements

- Regenerating the 8 records from `phase_profile.json` at any time must produce byte-identical values given unchanged source data (pure derivation, no randomness, no timestamp-dependent logic).
- The corpus-total records (7–8) must always be regenerated as the sum of the current phase-level records, never hand-edited independently — this prevents silent drift between the phase-level and corpus-level figures.
- Record `id` values (`3c-r01`…`3c-r08`, introduced by this document for traceability) are stable identifiers for this specification's own cross-referencing; they are not currently present as a field in `viz_schema_template.md`'s record shape and would need to be added to the schema template (§6.7) if adopted as a persistent, addressable ID scheme.

## 6.6 Schema versioning and migration notes

- `phase_profile.json` is already versioned (`"revision": 4`) and carries a `generated`/`generated_by` provenance pair — any future change to the 8 records' source values must bump this revision and update `generated`.
- `nalex_viz_schema.json` and `nalex_mobile_infographic_schema.json` do not currently carry their own revision numbers. This document recommends adding a top-level `"schema_revision"` and `"generated_from_phase_profile_revision"` pair to any schema file consumed by a canonical renderer, so a render can assert at build time that it was generated against the `phase_profile.json` revision it expects (fail closed if mismatched).
- No migration is required for the 8 records themselves (§6.1); the recommendation above is a forward-looking hardening measure, not a current gap that blocks 3C.

## 6.7 Complete proposed schema patch (JSON Schema fragment)

The following JSON Schema fragment formalizes the `viz_schema_template.md` record shape as it applies to the 8 records in §6.2, sufficient for implementation without guesswork. It is additive — it does not change any existing field in `viz_schema_template.md`.

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://nalex.local/schema/artifact_3_initiation_closure.json",
  "title": "Nalex artifact_3_initiation_closure record (3C canonical render)",
  "type": "object",
  "required": ["theme", "phase", "scope", "speaker", "metric", "evidence_quote", "confidence", "visual_hint"],
  "properties": {
    "id": { "type": "string", "pattern": "^3c-r[0-9]{2}$", "description": "Stable identifier for this specification's cross-referencing (§6.5); not part of viz_schema_template.md's base shape." },
    "theme": { "type": "string", "const": "initiation_closure_asymmetry" },
    "phase": {
      "type": ["string", "null"],
      "enum": ["Baseline", "Conflict", "Silence", "Aftermath", null],
      "description": "null permitted only when scope == 'corpus'."
    },
    "scope": { "type": "string", "enum": ["phase", "corpus"] },
    "detail_label": {
      "type": ["string", "null"],
      "description": "null when scope == 'phase'; 'Corpus' when scope == 'corpus'."
    },
    "display_instance": { "type": "null" },
    "speaker": { "type": "string", "enum": ["Naomi", "Alex"] },
    "metric": {
      "type": "object",
      "required": ["name", "value", "unit"],
      "properties": {
        "name": { "type": "string", "enum": ["session_closes", "explicit_signoff_turns", "explicit_signoffs_total"] },
        "value": { "type": "integer", "minimum": 0, "maximum": 378 },
        "unit": { "type": "string", "const": "count" }
      }
    },
    "evidence_quote": { "type": "string", "minLength": 1 },
    "confidence": { "type": "string", "enum": ["low", "medium", "high"] },
    "linked_theme": { "type": ["string", "null"] },
    "relation_type": { "type": "string", "enum": ["supports", "contrasts", "repeats", "escalates", "repairs", "diverges"] },
    "visual_hint": { "type": "string", "enum": ["bar", "strip"] }
  },
  "allOf": [
    {
      "if": { "properties": { "scope": { "const": "phase" } } },
      "then": {
        "properties": {
          "phase": { "enum": ["Baseline", "Conflict", "Aftermath"] },
          "detail_label": { "const": null },
          "metric": { "properties": { "name": { "enum": ["session_closes", "explicit_signoff_turns"] } } }
        }
      }
    },
    {
      "if": { "properties": { "scope": { "const": "corpus" } } },
      "then": {
        "properties": {
          "phase": { "const": null },
          "detail_label": { "const": "Corpus" },
          "metric": { "properties": { "name": { "const": "explicit_signoffs_total" } } }
        }
      }
    }
  ]
}
```

**Cross-record consistency rules (not expressible in single-record JSON Schema, must be enforced at the record-set level):**
- For each phase, `session_closes.Naomi + session_closes.Alex == phase_profile.json.phases.<phase>.sessions_60min`.
- `explicit_signoffs_total.Naomi == sum(explicit_signoff_turns.Naomi across Baseline, Conflict, Aftermath)`, and likewise for Alex.
- Every `phase` value present in the record set matches a key in `phase_profile.json.phases`.

---

# 7. Canonical render constraints

Non-negotiable constraints for any shipped Nalex visualization, restated here as a consolidated checklist (each traces to §2, §3, §5, or `index.md`/`viz_schema_template.md`/`visualization_pipeline.md`):

- [ ] **No rendering directly from unflattened or undocumented source data.** Every render must pass through the flatten step (§2.2) into `viz_schema_template.md`-conformant records before any layout work begins.
- [ ] **All display values must trace to named schema fields.** Every number, label, or count on the artifact face must be attributable to a specific `metric.name` in a specific record (§5.10 item 1).
- [ ] **All derived values must be reproducible.** A derived value (e.g., a corpus total, a ratio) must be regenerable from its stated inputs by a stated rule (§6.5) — no manually asserted derived numbers.
- [ ] **No new interpretation vocabulary at render time.** Only strings from `phase_profile.json → tag_vocabulary` (both `problematic_tags` and `emotional_tags`) may appear as interpretive/structural labels; see the closed vocabulary in §11.2.
- [ ] **Tier C requires its declared interpretation tag and its mandatory caveat, both present and both on the artifact face.** A Tier-C render missing either is non-compliant regardless of visual quality.
- [ ] **Definitions that could be confused must appear within the visual itself**, not only in external documentation — e.g., 3C's "session close" vs. "explicit sign-off" definitions (§5.5, §5.8).
- [ ] **Denominators, n-counts, ranges, missingness, and coverage constraints must be visible when material to interpretation** — e.g., Aftermath's 5-session denominator, Baseline's 7/8-observation latency sample, Conflict's 36-approximate-timestamp range basis, the 17-of-83 Q4 sample ratio.
- [ ] **No smoothing, fitted trends, trajectory implications, or false continuity unless expressly supported and declared.** Three-point "slopes" (Q2) must not imply a continuous trend; trajectory arrows (3B, rejected for exactly this reason) must not imply motion through unmeasured time.
- [ ] **No visual encoding that implies commensurability where it is not valid** — e.g., 1B's mirrored-axis butterfly chart is flagged precisely because it visually equalizes non-commensurable absolute scales.
- [ ] **No concealment of sample/population mismatch** — 4A's entire design exists to prevent exactly this; any Q4 render must carry the population/sample distinction structurally, not as a caption.
- [ ] **No presentation of upper bounds as measured facts** — every Aftermath asymmetry figure (volume, initiation/closure, latency) is an upper bound on the true asymmetry because the Aftermath window is 100% audio and any text replies from Alex are invisible to the corpus by construction (§3.4, §11.3). This must be disclosed wherever such a figure is the primary claim.
- [ ] **No interaction-dependent disclosure of essential caveats.** A caveat required by this document must render on the static artifact face; it must not be gated behind hover, click, tooltip, or accordion expansion (§1.4, §5.11).

---

# 8. Visual system and implementation details

## 8.1 Output format, dimensions, responsive behaviour, export

- **Output format:** self-contained static HTML/SVG artifact (matching the established pattern of every rendered artifact in `visualisations/`), or a static image export (PNG/SVG) of the same. No client-side data fetching, no external stylesheet/script/font dependencies (this matches the existing `render_directives.rules` convention in `nalex_mobile_infographic_schema.json`: *"Fully self-contained: no external fonts, scripts, or images."*).
- **Dimensions:** desktop-first, card/panel layout matching the ideation-preview artifact's own grid convention (`viewBox="0 0 320 168"` per-card SVGs inside a `.cards { grid-template-columns: repeat(3, 1fr) }` container that collapses to one column under 920px) — 3C's canonical render should use a comparable single-artifact-width layout (not constrained to a 320×168 card, since it is now the full artifact, not one of twelve comparison cards), with the multi-panel structure of §5.8 laid out vertically.
- **Responsive behaviour:** the artifact body must not scroll horizontally at any viewport width; any content wider than the viewport (e.g., a wide table) must scroll inside its own `overflow-x: auto` container, not the page.
- **Export requirements:** `UNVERIFIED — REQUIRES SOURCE INSPECTION` — no existing export pipeline (e.g., automated PNG snapshotting) was found in the repository; if one is required, it must be specified separately.

## 8.2 Typography, spacing, colour, contrast, annotations, source-note rules

- **Typography:** system font stack (matches every existing rendered artifact: `-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif` for body text; a monospace stack — `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` — for all numeric/tabular values, matching the `.mono` convention already established in the ideation-preview artifact's own CSS).
- **Spacing:** consistent card/panel padding and gap values; no cramped caveat text — caveat and definition blocks must be legibly sized, not shrunk to fit (the ideation preview's own `.limitation` class at 11px is near the minimum acceptable size and should not be reduced further for the canonical render).
- **Colour:** see §8.3.
- **Contrast:** minimum WCAG AA (4.5:1 for body text, 3:1 for large text/UI components) in whichever theme(s) are shipped.
- **Annotations:** connector lines or footnote markers used for the mandatory Aftermath-close/post-exit-tail annotation (§5.8) must be legible at the artifact's minimum supported viewport width.
- **Source-note rules:** every panel's source footnote (§5.8) must name the exact source file and field path, not just "source: internal data."

## 8.3 Semantic colour mapping for Naomi and Alex, with accessibility fallback

The ideation-preview artifact ("Nalex — Visualization Variation Previews") already establishes a token set for this exact comparison; this document specifies **adopting it directly** for the 3C canonical render, since it is the artifact 3C was selected from and preserves visual continuity for anyone comparing the canonical render back to the ideation set:

**Light theme:**
```css
--naomi: #1f6f66;       /* teal-green */
--naomi-soft: rgba(31,111,102,.14);
--alex: #b3562c;        /* burnt orange */
--alex-soft: rgba(179,86,44,.14);
--gold: #a9821c;        /* caveat/annotation accent */
--ink: #161f1c; --ink-2: #455049; --ink-3: #78837c;
--paper: #eef1ef; --paper-raised: #ffffff;
--line: #ccd3cd; --line-soft: #dde3de;
```

**Dark theme:**
```css
--naomi: #57c2b1;
--naomi-soft: rgba(87,194,177,.16);
--alex: #e2925c;
--alex-soft: rgba(226,146,92,.16);
--gold: #d4ac4a;
--ink: #e9efec; --ink-2: #aebab2; --ink-3: #7c8a81;
--paper: #0f1513; --paper-raised: #161e1b;
--line: #2a332d; --line-soft: #212a24;
```

Naomi = teal/green family; Alex = orange/amber family in both themes — chosen in the source artifact for hue separation. **Fallback encoding for colour-vision accessibility (required, not optional):** pair every color-coded mark with a redundant non-color channel — a text label, a fixed position (Naomi consistently left/first in every grouped pair), and/or a fill pattern distinction (e.g., solid fill for Naomi, a diagonal-hatch or outline fill for Alex) so the chart remains legible under deuteranopia/protanopia simulation and in grayscale printouts.

The `--gold` accent is reserved for caveat/annotation emphasis (matching its use in the source artifact's `.warn` block and `.recommend` section) and must not be reused as a third speaker-identity color.

## 8.4 Visual differentiation: observations vs. interpretation labels vs. caveats

Three visually distinct treatments are required, matching the pattern already established across the ideation-preview artifact and `nalex_mobile_infographic_schema.json`:

1. **Observations (measured values):** rendered as primary chart marks (bars, counts) in the Naomi/Alex hue pair (§8.3), with tabular-numeral labels.
2. **Interpretation labels:** rendered in a visually distinct block — different background treatment (e.g., a tinted panel using a tier-specific accent, matching the source artifact's `--tier-c` / `--tier-c-bg` convention), always carrying their exact prefix (`INTERPRETATION:` for `emotional_tags`; no prefix, but a distinct "STRUCTURAL" label or icon, for `problematic_tags`) — these two tag types must remain visually distinguishable from each other, not merged into one undifferentiated "interpretation" box (§5.6, §7).
3. **Caveats:** rendered in the `--gold`-accented block style already established (`.warn` in the source artifact — border-left accent, distinct background), always on the artifact face (§5.7, §7).

## 8.5 Tooltip and hover-state rules (for future addition only)

The first canonical 3C render ships with **no tooltips or hover states** (§1.4). If interactivity is added in a later revision:
- Any content currently required to be visible on the artifact face by this document (§5.5, §5.7, §7) must **remain** visible on the face; tooltips may only add supplementary detail (e.g., exact source timestamps, individual quote text), never the caveats, definitions, or core numeric claims themselves.
- The artifact must remain fully understandable — every required test in §5.10 must still pass — with all interactivity disabled or unavailable (e.g., screen-reader use, static export, print).
- Hover-revealed content must have a non-hover equivalent (e.g., focus-visible keyboard access, or a persistent "show details" affordance that does not require a pointing device).

## 8.6 Required alt text and text-only equivalent

A single alt-text/summary string, required at ship time:

> "Bar chart comparing two ways of measuring who ends conversations between Naomi and Alex across three phases (Baseline, Conflict, Aftermath). Mechanical session closes: Baseline 4 Naomi to 6 Alex, Conflict 3 to 7, Aftermath 5 to 0. Explicit verbal sign-offs, the same phases: 0 to 0, 0 to 11, 0 to 4 — Alex issues 15 verbal sign-offs across the whole corpus of 378 events; Naomi issues zero. Session close is a mechanical artifact of a 60-minute silence gap, not necessarily a communicative act; Naomi's five Aftermath closes overlap eleven turns she made after Alex had already left the conversation."

A parallel text-only equivalent (a plain-language paragraph or definition list, not just the alt attribute) must exist in the artifact's DOM so the full numeric content of §5.5 is extractable without rendering graphics.

## 8.7 Deterministic rendering requirements and snapshot-test guidance

- Given the same source data (`phase_profile.json` at a fixed revision), the render must produce byte-identical (or pixel-identical, for a rasterized export) output on every run — no randomized layout, no non-deterministic ordering of records, no client-clock-dependent content (e.g., no "generated X minutes ago" text).
- **Snapshot-test guidance:** capture a reference render (HTML DOM snapshot and/or rasterized image) at ship time; CI or manual regression checks should diff future renders against this snapshot and require an explicit, reviewed change (not a silent diff) whenever the output changes — whether due to a data update (`phase_profile.json` revision bump) or a layout change.
- `UNVERIFIED — REQUIRES SOURCE INSPECTION`: no existing snapshot-testing harness was found in the repository; this is a recommended practice for the canonical render pipeline, not a currently implemented one.

---

# 9. Data QA and acceptance criteria

## 9.1 Pre-render data checks

- [ ] `phase_profile.json` is the current revision (`revision: 4` at time of writing) and its `generated`/`generated_by` fields are recorded alongside the render's own build metadata.
- [ ] All 8 records in §6.2 are present, correctly scoped, and pass the JSON Schema fragment in §6.7.
- [ ] Cross-record consistency rules (§6.7) pass: phase-level `session_closes` sums equal `sessions_60min`; corpus-level `explicit_signoffs_total` equals the sum of phase-level `explicit_signoff_turns`.

## 9.2 Schema validation checks

- [ ] Every record's `phase` is a valid canonical phase (`Baseline`, `Conflict`, `Silence`, `Aftermath`) or `null` with `scope: "corpus"` (Validation Checklist, §2.4).
- [ ] Every record has a valid `scope` (`phase` or `corpus` for 3C's record set).
- [ ] `detail_label` is `null` for `scope: "phase"` records and `"Corpus"` for `scope: "corpus"` records, per §6.7's `allOf` conditional.
- [ ] No record's `metric.value` exceeds its population bound (10 for Baseline/Conflict session counts, 5 for Aftermath, 378 for corpus-wide counts).

## 9.3 Count reconciliation tests against `events.jsonl`

- [ ] Total corpus event count (378) and speaker split (Alex 188, Naomi 187, System 3) reconcile with `phase_profile.json → corpus_wide` and `CURRENT_STATE_CLEAN.md § 7.1`'s independent recomputation.
- [ ] Phase event counts (52 Baseline / 221 Conflict [including 3 System] or 218 [conversational only] / 0 Silence / 105 Aftermath) reconcile per the §3.1 reconciliation note — the render's own source citation must state which figure (221 vs. 218) it is using and why.
- [ ] Session counts (10 / 10 / 5) reconcile between `phase_profile.json`, `baseline_comparison_audit.json`, and `nalex_viz_schema.json`.

## 9.4 Tests for phase ordering and speaker attribution

- [ ] Phases render left-to-right in chronological order: Baseline, Conflict, Aftermath (Silence omitted per §5.8/§2.4 item 10).
- [ ] Every bar/mark's speaker attribution matches its source record's `speaker` field exactly (no swapped Naomi/Alex labels).

## 9.5 Tests for explicit-sign-off classification

- [ ] The rendered Alex sign-off counts (0, 11, 4) and Naomi counts (0, 0, 0) match `phase_profile.json → phases.*.speakers.*.explicit_signoff_turns` exactly.
- [ ] The corpus-wide totals (Alex 15, Naomi 0) match `phase_profile.json → corpus_wide.explicit_signoffs_total` exactly and equal the sum of the phase-level values.
- [ ] The render does not claim the sign-off classification is mechanically reproducible from `events.jsonl` by a generic rule — it must be labeled (in source footnote or caveat) as a content-level/analyst judgment (§3.2.1), consistent with how `unanswered_documented` is treated elsewhere in the corpus.

## 9.6 Tests for session-close calculation and the 60-minute-gap rule

- [ ] The rendered session-close counts (4:6, 3:7, 5:0) match `phase_profile.json → phases.*.speakers.*.session_closes` exactly.
- [ ] The artifact face states the 60-minute-gap definition verbatim or near-verbatim to §5.5's definition — not merely referenced externally.
- [ ] The Aftermath 5:0 figure carries its "one session = 20% of the bar" denominator caveat (§5.7) directly adjacent to or annotating that specific bar, not only in a general caveat block elsewhere.

## 9.7 Tests ensuring all required caveats, definitions, tags, and n-counts render

- [ ] Both definitions (§5.5) are present in the rendered DOM/output (§5.10 item 3).
- [ ] Both mandatory caveats (§5.7) are present in the rendered DOM/output (§5.10 item 4).
- [ ] The `alex_withdrawal_by_exit` tag renders with its `INTERPRETATION:` prefix (§5.10 item 5).
- [ ] The structural tags (`naomi_never_closes_verbally`, `dyad_no_closure_event`) render without an `INTERPRETATION:` prefix and are visually distinguished from the `INTERPRETATION`-tagged content (§5.10 item 5, §8.4).
- [ ] All required denominators (10, 10, 5 sessions; 378 corpus events) are visible on the artifact face (§5.10 item 6).

## 9.8 Visual QA checklist

- [ ] Naomi and Alex are distinguishable by at least two channels (color + position or color + label/pattern) throughout (§5.9, §8.3).
- [ ] Contrast meets WCAG AA in every shipped theme (§8.2).
- [ ] No horizontal page scroll at any supported viewport width (§8.1).
- [ ] No content is clipped, truncated, or overlapping at minimum supported viewport width.
- [ ] The Naomi zero-height sign-off bars are visibly present (not collapsed to nothing/invisible) in all three phases (§5.10 item 2).

## 9.9 Publication acceptance criteria

A render may be published only if:
- [ ] Every item in §9.1–§9.8 passes.
- [ ] Every failure mode in §5.11 has been explicitly checked and ruled out.
- [ ] Every constraint in §7 has been explicitly checked and ruled out.
- [ ] The alt-text/text-only equivalent (§8.6) is present and matches the current data.
- [ ] A snapshot/reference version of the render has been captured for future regression comparison (§8.7).

## 9.10 Rollback / "do not ship" condition list

Do not ship, or immediately roll back, if any of the following is true:
- Any number on the artifact face cannot be traced to a named field in §6.2's record set (§7, §5.10 item 1/10).
- The Naomi explicit-sign-off zero bars are missing/omitted rather than rendered at zero height (§5.10 item 2, §5.11).
- Either mandatory definition or mandatory caveat (§5.5, §5.7) is missing from the artifact face, or is present only behind an interaction (§5.10 items 3–4, §7).
- The `INTERPRETATION:` prefix is missing from `alex_withdrawal_by_exit` or `dyad_asymmetric_repair_expectation`, or is incorrectly applied to a `problematic_tags` entry (§5.10 item 5).
- The Aftermath 5-session or 378-event corpus denominator is not visible (§5.10 item 6).
- The Silence phase is rendered as a zero-value bar rather than omitted or explicitly marked not-applicable (§5.10 item 7, §2.4 item 10).
- Any label string outside the closed tag vocabulary (§11.2) or plain measured-value labels appears anywhere in the artifact, including alt text (§5.10 item 8, §2.5).
- Naomi/Alex are distinguishable by color alone, with no redundant non-color encoding (§5.10 item 9, §5.9).
- Re-extraction from the current `phase_profile.json` does not reproduce the exact values hardcoded/displayed in the artifact (§5.10 item 10, §8.7).

---

# 10. Build plan

Ordered implementation plan from repository inspection through final export. Each step states inputs, outputs, validation gate, failure condition, and files created/modified.

### Step 1 — Confirm pipeline documents and current data revision
- **Inputs:** `index.md` §11, `research_prompt_modes/visualization_pipeline.md`, `research_prompt_modes/viz_schema_template.md`, `research_prompt_modes/nalex_gemini_viz_corrective_prompt.md`, `phase_profile.json` (`revision` field).
- **Outputs:** confirmed pipeline understanding; recorded `phase_profile.json` revision number for provenance (§6.6).
- **Validation gate:** all three mandatory pipeline documents have been read (per `index.md` §11's explicit requirement); the corrective-prompt document's exact current text has been re-read (§3.7.4 flags this as unverified in this pass).
- **Failure condition:** any of the three mandatory documents is missing, unreadable, or contradicts this specification — halt and reconcile before proceeding.
- **Files created/modified:** none.

### Step 2 — Verify the 8 required schema records
- **Inputs:** `research_prompt_modes/analysis_outputs/nalex_viz_schema.json → artifact_3_initiation_closure.records`; `phase_profile.json → phases.*.speakers.*.{session_closes,explicit_signoff_turns}` and `corpus_wide.explicit_signoffs_total`.
- **Outputs:** confirmation (or correction) that all 8 records from §6.2 are present and correct; if any are missing or incorrect, generate/patch them per §6.7's schema fragment.
- **Validation gate:** §9.1 pre-render checks and §9.2 schema validation checks pass.
- **Failure condition:** any record is missing, mis-scoped, or its value disagrees with `phase_profile.json` — do not proceed to Step 3 until resolved.
- **Files created/modified:** `research_prompt_modes/analysis_outputs/nalex_viz_schema.json` (only if a correction/addition is needed — expected to be a no-op per §6.1's finding).

### Step 3 — Count reconciliation against `events.jsonl`
- **Inputs:** `events.jsonl`, `phase_profile.json`, `baseline_comparison_audit.json`, `CURRENT_STATE_CLEAN.md` §7.
- **Outputs:** confirmed reconciliation table (§3.1's 221-vs-218 note; §9.3's checklist).
- **Validation gate:** §9.3 passes.
- **Failure condition:** an unreconciled count discrepancy beyond the documented and explained ones in §3.1/§3.4 — if found, treat as a new data-integrity finding requiring its own caveat before proceeding.
- **Files created/modified:** none (read-only verification step); if a genuine new discrepancy is found, it should be logged as an addendum to this document or to `nalex_viz_ideation.md` §0.

### Step 4 — Draft the flattened record set for the render (extraction output)
- **Inputs:** the 8 verified records (Step 2), plus the definitions and caveat strings (§5.5, §5.7), plus the tag vocabulary citations (§5.6).
- **Outputs:** a single JSON file (e.g., `research_prompt_modes/analysis_outputs/nalex_viz_3c_canonical.json`) containing exactly the records, definitions, and caveats the render will consume — no more, no less — following the pattern already established in `nalex_mobile_infographic_schema.json`'s `artifact_3_initiation_closure` block (§3.7.2), adapted to 3C's own layout (§5.8) rather than the mobile-infographic form factor.
- **Validation gate:** the file validates against §6.7's JSON Schema fragment; every caveat/definition string matches §5.5/§5.7 verbatim or near-verbatim.
- **Failure condition:** any field in the draft file cannot be traced to §6.2 or §5.5/§5.7 — remove it or trace it before proceeding.
- **Files created/modified:** new file, e.g. `research_prompt_modes/analysis_outputs/nalex_viz_3c_canonical.json`.

### Step 5 — Render construction
- **Inputs:** the flattened record file from Step 4; the layout spec (§5.8); the visual system spec (§8); the corrective-prompt constraints (§2.1 item 3, §3.7.4).
- **Outputs:** a self-contained static HTML/SVG artifact implementing §5.8's layout exactly, styled per §8.
- **Validation gate:** the renderer (human or model) has been constrained per `nalex_gemini_viz_corrective_prompt.md`'s "dumb layout engine" rule — no new structure invented, `visual_hint` values treated literally per `viz_schema_template.md`'s renderer semantics.
- **Failure condition:** the renderer infers new themes, rewrites evidence, adds analysis, or invents structure not present in the Step 4 record file — reject the output and re-render.
- **Files created/modified:** new file, e.g. `visualisations/nalex_3c_canonical_render.html`.

### Step 6 — Validation pass
- **Inputs:** the rendered artifact from Step 5; all of §9's checklists.
- **Outputs:** a completed §9 checklist (pass/fail per item), and a completed §5.10 validation-tests result.
- **Validation gate:** every item in §9.1–§9.9 passes.
- **Failure condition:** any §9 item fails, or any §5.11 failure mode is present, or any §9.10 rollback condition is triggered — return to Step 4 or 5 as appropriate; do not proceed to Step 7.
- **Files created/modified:** a validation record (e.g., appended to this document's §9 as a dated pass/fail log, or a separate QA note file).

### Step 7 — Accessibility review
- **Inputs:** the rendered artifact from Step 5 (post any Step 6 fixes); §5.9 and §8.6's requirements.
- **Outputs:** confirmed non-color encoding, contrast, alt-text, and text-only-equivalent presence.
- **Validation gate:** §5.10 item 9 and §9.8's contrast/distinguishability checks pass, ideally including a simulated colorblindness check.
- **Failure condition:** speaker identity is not distinguishable without color, or contrast fails WCAG AA, or alt text/text-equivalent is missing or inaccurate — return to Step 5.
- **Files created/modified:** none beyond fixes folded back into the Step 5 output file.

### Step 8 — Snapshot capture and final export
- **Inputs:** the fully validated, accessibility-reviewed artifact.
- **Outputs:** a reference snapshot (DOM and/or rasterized image) per §8.7; the final shippable artifact file.
- **Validation gate:** §9.9 publication acceptance criteria all pass; the snapshot has been captured and stored.
- **Failure condition:** any §9.9 item is unmet — do not publish; return to the relevant earlier step.
- **Files created/modified:** the final artifact file (published/shared per whatever mechanism is used for `visualisations/` outputs); a snapshot reference file if a snapshot-testing harness is adopted (currently unverified to exist, §8.7).

---

# 11. Appendix: complete factual basis

This appendix restates, in one place, the complete factual data and caveats used by all 12 variants, so this document can stand alone even if the ideation-preview artifact becomes unavailable.

## 11.1 Canonical phase windows and corpus totals

| Phase | Window (inclusive) | Calendar days | Events | Sessions (60-min rule) | Contact days |
|---|---|---|---|---|---|
| Baseline | 2026-04-01 to 2026-06-22 | 83 | 52 | 10 | 10 |
| Conflict | 2026-06-23 to 2026-07-05 | 13 | 221 (incl. 3 System) / 218 (conversational) | 10 | 6 |
| Silence | 2026-07-06 to 2026-07-10 | 5 | 0 | 0 | 0 |
| Aftermath (canonical) | 2026-07-11 to 2026-07-21 | 11 | 105 | 5 | 4 |

**Corpus-wide:** 378 total events; speakers Alex 188, Naomi 187, System 3. First event 2026-04-01 23:34:40; last event 2026-07-21 21:48:45 (Naomi). `sha256` present on 301/378 events, absent on 77 (69 text, 3 call, 3 audio, 2 media), all 77 in the Conflict phase.

**Excluded from all phases ("The Purge," `CURRENT_STATE_CLEAN.md` §1):** December 2025–March 2026 audio (30 events, Naomi speaking to third parties, not Alex) is excluded from the corpus entirely and is not part of any figure in this document.

**Note on the wider "5 July onward" Aftermath window used by `aftermath_stats.json` (115 events):** this is a non-canonical, wider window that includes Conflict-phase session 0 (5 Jul). The canonical Aftermath boundary is 11 July; using the wider window moves the volume ratio from 3.14× to 2.54× — any artifact using the wider window must label it explicitly and must not be conflated with canonical Aftermath figures.

## 11.2 Complete tag vocabulary (`phase_profile.json → tag_vocabulary`)

**`problematic_tags`** (20 keys — structural, not `INTERPRETATION`):

| Tag | Definition |
|---|---|
| `naomi_volume_dominance` | Naomi out-words Alex by a wide margin in the phase |
| `naomi_wpm_escalation` | Naomi's per-turn length rises sharply relative to prior phase |
| `naomi_high_question_load` | Naomi carries ≥35 questions per 100 turns |
| `naomi_unanswered_bid_rate_high` | ~50% of Naomi's questions get no other-party turn within 10 min in-session |
| `naomi_unreciprocated_sessions` | Sessions containing only Naomi turns |
| `naomi_post_exit_continuation` | Substantial output after the other party has left the session |
| `naomi_unilateral_initiation` | Naomi opens all sessions in the phase |
| `naomi_never_closes_verbally` | Zero explicit sign-off moves in the phase |
| `alex_low_content_initiation` | Alex's session opens are mostly single-turn drops that generate no exchange |
| `alex_terse_turn_floor` | Alex's median turn length is roughly half Naomi's or lower |
| `alex_bimodal_turn_length` | Low median with rare very long turns; mean masks the floor |
| `alex_question_burst_pressure` | Runs of ≥3 consecutive Alex turns each carrying a question |
| `alex_bare_punctuation_prompting` | Content-free "?" turns used as prompts |
| `alex_explicit_termination_moves` | Verbal sign-offs used to end live exchanges |
| `alex_zero_initiation` | Alex opens no sessions in the phase |
| `alex_topic_contingent_availability` | Engages readily on neutral topics, exits soon after grievance topics are raised |
| `dyad_question_crossfire` | Both parties above 35 questions per 100 turns simultaneously |
| `dyad_mutual_non_answering` | Both parties' questions go unaddressed at comparable rates |
| `dyad_low_contact_high_burst` | Few contact days, very high events per contact day |
| `dyad_no_closure_event` | Phase ends without a mutual termination or repair turn |

**`emotional_tags`** (12 keys — **`INTERPRETATION`**, the entire closed vocabulary any Tier-C render may draw from):

| Tag | Definition |
|---|---|
| `naomi_chronic_unanswered_bids` | INTERPRETATION: sustained experience of questions not landing |
| `naomi_unwitnessed` | INTERPRETATION: posture of speaking without confirmation of being heard |
| `naomi_pursuing` | INTERPRETATION: initiation and volume consistent with pursuit |
| `naomi_escalating_elaboration` | INTERPRETATION: adding length in response to non-response |
| `naomi_seeking_acknowledgement` | INTERPRETATION: explicit and repeated demand for acknowledgement over resolution |
| `naomi_anticipatory_vigilance` | INTERPRETATION: sharply reduced latency consistent with monitoring |
| `alex_constrained_engagement` | INTERPRETATION: present but rationing contribution |
| `alex_withdrawal_by_exit` | INTERPRETATION: managing load by ending exchanges rather than escalating |
| `alex_over_vigilant_pursuit` | INTERPRETATION: high-frequency questioning consistent with alarm-seeking |
| `alex_feeling_ambushed` | INTERPRETATION: stated experience of being blamed or attacked without warning |
| `alex_defended_invulnerability` | INTERPRETATION: asserted imperviousness to harm as a protective stance |
| `dyad_asymmetric_repair_expectation` | INTERPRETATION: each waits for the other to perform the first repair move |

Per `phase_profile.json → notes`: *"problematic_tags and emotional_tags are Claude-assigned analytic labels, not measured quantities. emotional_tags are INTERPRETATION."* All 32 tags are used at least once in the per-phase `problematic_tags`/`emotional_tags` arrays; no tag is used without this definition.

## 11.3 Per-phase, per-speaker metrics (complete, from `phase_profile.json`)

| Metric | Baseline Naomi | Baseline Alex | Conflict Naomi | Conflict Alex | Aftermath Naomi | Aftermath Alex |
|---|---|---|---|---|---|---|
| messages | 32 | 20 | 94 | 124 | 61 | 44 |
| words (phase_profile) | 1,697 | 928 | 5,873 | 5,227 | 6,860 | 2,187 |
| words (baseline_comparison_audit, canonical for Q1/Aftermath per §7.2H) | 1,693 | 927 | 5,888 | 5,233 | 6,852 | 2,181 |
| mean words/turn | 53.0 | 46.4 | 62.5 | 42.2 | 112.5 | 49.7 |
| median words/turn | 44.5 | 31.5 | 39.5 | 21 | 66 | 26 |
| longest turn (words) | 218 | 138 | 381 | 435 | 928 | 357 |
| questions | 12 | 4 | 39 | 44 | 31 | 14 |
| questions per 100 turns | 37.5 | 20.0 | 41.5 | 35.5 | 50.8 | 31.8 |
| unanswered (documented) | 6 | 1 | 8 | 15 | 16 | 3 |
| unanswered (10-min mechanical proxy) | 6 | 2 | 7 | 7 | 16 | 4 |
| unanswered rate (mechanical) | 50% | 50% | 18% | 16% | 52% | 29% |
| median reply seconds | 484 (n=7) | 101 (n=8) | "112-120" | "70-94" | 169 | 122 |
| session opens | 5 | 5 | 5 | 5 | 5 | 0 |
| session closes | 4 | 6 | 3 | 7 | 5 | 0 |
| max consecutive turns | 16 | 4 | 11 | 7 | 12 | 7 |
| explicit sign-off turns | 0 | 0 | 0 | 11 | 0 | 4 |
| solo-session turns | 16 | 5 | 2 | 6 | 8 | 0 |
| solo-session words | 1,082 | 335 | 18 | 56 | 793 | 0 |
| post-exit-tail turns | 1 | 5 | 10 | 12 | 11 | 0 |
| post-exit-tail words | 78 | 102 | 414 | 843 | 1,792 | 0 |

**Per-phase asymmetry ratios:**

| | Baseline | Conflict | Aftermath |
|---|---|---|---|
| word_ratio_N_over_A | 1.83 | 1.12 | 3.14 |
| median_turn_len_ratio_N_over_A | 1.41 | 1.88 | 2.54 |
| latency_ratio_N_over_A | 4.79 | "1.2-1.7" | 1.39 |
| session_opens_N_to_A | 5:5 | 5:5 | 5:0 |
| session_closes_N_to_A | 4:6 | 3:7 | 5:0 |
| explicit_signoffs_N_to_A | 0:0 | 0:11 | 0:4 |

**Per-phase flags, problematic_tags, emotional_tags:**

- **Baseline** — flags: `baseline_chronic_asymmetry`. problematic_tags: `naomi_volume_dominance`, `naomi_high_question_load`, `naomi_unanswered_bid_rate_high`, `naomi_unreciprocated_sessions`, `naomi_never_closes_verbally`, `alex_low_content_initiation`, `alex_terse_turn_floor`. emotional_tags: `naomi_chronic_unanswered_bids`, `naomi_unwitnessed`, `alex_constrained_engagement`.
- **Conflict** — flags: `conflict_question_inversion`. problematic_tags: `dyad_question_crossfire`, `dyad_mutual_non_answering`, `dyad_low_contact_high_burst`, `naomi_high_question_load`, `alex_question_burst_pressure`, `alex_bare_punctuation_prompting`, `alex_explicit_termination_moves`, `alex_terse_turn_floor`, `alex_bimodal_turn_length`. emotional_tags: `alex_over_vigilant_pursuit`, `alex_feeling_ambushed`, `alex_withdrawal_by_exit`, `naomi_seeking_acknowledgement`, `dyad_asymmetric_repair_expectation`.
- **Silence** — flags: `no_contact`. No problematic_tags or emotional_tags (0 events).
- **Aftermath** — flags: `aftermath_unilateral_initiation`, `aftermath_volume_amplification`, `aftermath_initiation_shift`. problematic_tags: `naomi_volume_dominance`, `naomi_wpm_escalation`, `naomi_high_question_load`, `naomi_unanswered_bid_rate_high`, `naomi_unreciprocated_sessions`, `naomi_post_exit_continuation`, `naomi_unilateral_initiation`, `naomi_never_closes_verbally`, `alex_zero_initiation`, `alex_terse_turn_floor`, `alex_bimodal_turn_length`, `alex_explicit_termination_moves`, `alex_topic_contingent_availability`, `dyad_no_closure_event`. emotional_tags: `naomi_pursuing`, `naomi_escalating_elaboration`, `naomi_seeking_acknowledgement`, `naomi_anticipatory_vigilance`, `naomi_unwitnessed`, `naomi_chronic_unanswered_bids`, `alex_constrained_engagement`, `alex_withdrawal_by_exit`, `alex_defended_invulnerability`, `dyad_asymmetric_repair_expectation`.

**Per-phase notes (verbatim from `phase_profile.json`):**

- Baseline: "4 of Alex's 5 session opens are 1-2 turn drops that produce no exchange." "5 of Naomi's 12 questions occur in sessions Alex never joins; her unanswered rate is largely structural absence, not selective refusal." "Latency medians rest on 7 (Naomi) and 8 (Alex) observations."
- Conflict: "148 of 218 conversational events (68%) fall in two sessions: 26-27 Jun (77 ev / 276 min) and 4-5 Jul (71 ev / 332 min)." "36 events carry approximate or minute-only timestamps; Conflict latency medians move with how these are handled." "The documented Alex unanswered figure (15/44) is roughly double any mechanical timing rule (7/44). It is a content-level judgment and is not reproducible from events.jsonl."
- Silence: "6.8-day gap measured event-to-event (5 Jul 00:53 -> 11 Jul 20:07). Broken by Naomi."
- Aftermath: "Naomi opens 5/5 and closes 5/5 sessions; Alex opens 0 and closes 0. In Baseline and Conflict Alex closed the majority (6/10 and 7/10)." "2,585 of Naomi's 6,860 words (37.7%) are produced after Alex has left the session or in sessions he never joins." "Alex issues 4 explicit sign-offs; Naomi issues 0 in the entire corpus." "CAVEAT: the Aftermath window is 100% audio (105/105). The Conflict phase contained 69 text events (38 Alex / 31 Naomi). If Alex replied by text in July, those turns are absent by construction, and initiation/unanswered figures are upper bounds on the asymmetry. Naomi's turns in the two 'Naomi-only' sessions visibly respond to live Alex input."

## 11.4 `baseline_comparison_audit.json` — complete point-value table

| | Baseline | Conflict | Aftermath |
|---|---|---|---|
| events | 52 | 218 | 105 |
| sessions | 10 | 10 | 5 |
| N_msg / A_msg | 32 / 20 | 94 / 124 | 61 / 44 |
| N_w / A_w | 1,693 / 927 | 5,888 / 5,233 | 6,852 / 2,181 |
| N_wpm / A_wpm | 53 / 46 | 63 / 42 | 112 / 50 |
| N_lat / A_lat (point value; Conflict = top of range) | 484 / 101 | 120 / 94 | 169 / 122 |
| N_q / N_unans | 12 / 6 | 39 / 8 | 31 / 16 |
| A_q / A_unans | 4 / 1 | 44 / 15 | 14 / 3 |
| N_run / A_run (max consecutive turns) | 16 / 4 | 11 / 7 | 12 / 7 |
| N_opens / A_opens | 5 / 5 | 5 / 5 | 5 / 0 |

## 11.5 `aftermath_stats.json` — session-level detail (canonical sessions 1–5 only; session 0 excluded, §3.4)

| Session | Label | Window | Naomi turns/words | Alex turns/words | Naomi median reply (s) | Alex median reply (s) |
|---|---|---|---|---|---|---|
| 0 (EXCLUDED — Conflict phase) | "5 Jul – the night both of them said it was over" | 2026-07-05 00:07:18–00:53:54 | 5 / 705 | 5 / 797 | 132 | 1,034 |
| 1 | "11 Jul evening – first contact after 6 days" | 2026-07-11 20:07:12–22:53:24 | 19 / 1,138 | 21 / 798 | 73 | 109 |
| 4 | (per `nalex_viz_schema.json` session-level records) | — | — | — | 583 | 343 |
| 5 | (per `nalex_viz_schema.json` session-level records) | — | — | — | 206 | 124 |

`overall` block (115-event wider window, **non-canonical, do not mix with canonical Aftermath figures**): Naomi 66 turns / 7,557 words / 53.1 audio-minutes / mean 114.5 wpt / median 66 wpt / longest 925 words / 31 questions / 140s median reply. Alex 49 turns / 2,978 words / 25.3 audio-minutes / mean 60.8 wpt / median 26 wpt / longest 435 words / 14 questions / 124s median reply.

## 11.6 `gap_stats_out.json` — the two large gaps used by variant 2C

| `eid` | `t` (event time) | `prev_t` | `prev_eid` | `gap_sec` | Context |
|---|---|---|---|---|---|
| G201 | 2026-07-21 19:04:12 | 2026-07-13 23:04:44 | G207 | 676,768.0 | Aftermath inter-contact gap before 21 Jul |
| G212 | 2026-07-11 20:07:12 | 2026-07-05 00:53:54 | C083 | 587,598.0 | Silence-phase gap before 11 Jul contact resumes (≈6.8 days, matches `phases.Silence.notes`) |

105 rows total, all resolve 105/105 on `sha256`, Aftermath window only. `gap_sec` is elapsed time regardless of speaker (43 same-speaker pairs, 45 cross-speaker pairs, 17 with unresolved predecessor) — **not** a reply-latency measure (§3.5).

## 11.7 `conflict_questions_annotated.json` — all 17 records (complete)

| # | Timestamp | Speaker | Intent | Loop tag | Heat | Answered | Genuine unanswered | Risk |
|---|---|---|---|---|---|---|---|---|
| 1 | 2026-06-26 16:04:52 | Naomi | clarify | directness-loop | tense | Partial | **true** | high-signal |
| 2 | 2026-06-26 16:09:07 | Naomi | clarify | proof-loop | tense | Partial | false | repetitive |
| 3 | 2026-06-26 21:57:59 | Naomi | challenge | flirting-ambiguity-loop | hot | No | false | loaded |
| 4 | 2026-06-26 22:03:28 | Naomi | challenge | proof-loop | hot | No | false | cornering |
| 5 | 2026-06-26 23:56:48 | Alex | boundary | repair-loop | hot | Partial | false | action-needed |
| 6 | 2026-06-27 00:00:29 | Naomi | clarify | proof-loop | hot | No | false | high-signal |
| 7 | 2026-06-27 00:09:53 | Alex | boundary | flirting-ambiguity-loop | hot | Partial | false | high-signal |
| 8 | 2026-06-27 00:18:08 | Naomi | challenge | blame-loop | explosive | No | false | cornering |
| 9 | 2026-06-27 00:31:20 | Alex | justify | proof-loop | hot | Partial | **true** | high-signal |
| 10 | 2026-06-27 00:33:55 | Naomi | deflect | proof-loop | hot | No | false | repetitive |
| 11 | 2026-06-27 00:50:44 | Alex | challenge | avoidance-loop | hot | Partial | false | high-signal |
| 12 | 2026-06-27 00:54:31 | Naomi | challenge | flirting-ambiguity-loop | hot | No | false | high-signal |
| 13 | 2026-07-04 22:07:17 | Alex | repair | repair-loop | tense | Partial | false | high-signal |
| 14 | 2026-07-04 23:19:28 | Naomi | boundary | directness-loop | tense | Partial | false | high-signal |
| 15 | 2026-07-04 23:26:11 | Naomi | boundary | directness-loop | tense | Partial | false | high-signal |
| 16 | 2026-07-04 23:33:09 | Naomi | boundary | boundary-loop | tense | Partial | false | high-signal |
| 17 | 2026-07-04 23:36:05 | Alex | clarify | proof-loop | tense | No | **true** | high-signal |

**Totals:** 17 questions (11 Naomi, 6 Alex). `answered`: Partial 10, No 7, Yes 0. `intent`: challenge 5, boundary 5, clarify 4, justify 1, deflect 1, repair 1. `heat`: hot 9, tense 7, explosive 1. `genuine_unanswered`: true 3 (records 1, 9, 17), false 14. `loop_tag` distribution: `proof-loop` 6, `directness-loop` 3, `flirting-ambiguity-loop` 3, `repair-loop` 2, `boundary-loop` 1, `blame-loop` 1, `avoidance-loop` 1. Timestamp span: 2026-06-26 16:04:52 to 2026-07-04 23:36:05, non-uniform — 12 records on 26–27 Jun, 5 records on 4 Jul, none between.

**`conversation_summary` (from `conflict_questions_summary.json`), verbatim:**
- `dominant_loop`: "Retrieval vs. Proof Deadlock"
- `core_problem`: "One party repeatedly demands specific proof of intent (e.g. regarding flirting and avoidance) and the other refuses to supply or restate it, leading to character attacks. Accusatory questions are weaponized as pressure, while requests for concrete examples go unanswered."

## 11.8 Cross-cutting data-integrity constraints (from `nalex_viz_ideation.md` §0, complete)

1. **Resolved:** the `genuine_unanswered` CSV/JSON discrepancy (7/17 vs. 3/17) is resolved as of 2026-08-06; the CSV has been regenerated from the JSON and both now agree at 3/17 (§3.6.1).
2. **No per-event reply-latency series exists.** Neither `events.jsonl → gap` (a session-boundary label, not seconds) nor `gap_stats_out.json → gap_sec` (elapsed time regardless of speaker, Aftermath-only, does not reproduce published medians) can substitute for one. Only phase-level medians are renderable for Q2.
3. **`aftermath_stats.json` uses a wider window** (115 events, "5 Jul onward") than canonical Aftermath (105 events, 11–21 Jul). Its `overall` block must not be mixed with `phase_profile.json`'s canonical figures; its `sessions` array is usable only with session 0 excluded or separated.
4. **Conflict latency medians are ranges** ("112-120" Naomi, "70-94" Alex), and Baseline medians rest on 7 (Naomi) / 8 (Alex) observations — Q2 is the evidentially weakest of the four questions; every Q2 variant must render Conflict as a band, not a point.
5. **Secondary constraints:**
   - *Modality:* Baseline and Aftermath are 100% audio (52/52, 105/105). Conflict is mixed: 147 audio, 69 text, 2 media, 3 call (sums to 221, the all-events figure). If Alex replied by text in July, those turns are absent by construction — every Aftermath asymmetry figure is an upper bound.
   - *Speaking time:* `dur_s` covers Baseline and Aftermath fully but only 144/221 Conflict events (Naomi 59/94, Alex 85/124). Conflict cannot be compared on a speaking-minutes axis.
   - *Word counts:* `phase_profile.json` and `baseline_comparison_audit.json` differ by <0.3% (tokenizer). Canonical for Q1/Aftermath: `baseline_comparison_audit.json` figures (§7.2H).
   - *Denominators:* sessions per phase — Baseline 10, Conflict 10, Aftermath 5. One Aftermath session = 20% of that phase's bar.

## 11.9 Schema-readiness table (from `nalex_viz_ideation.md` §5, with §6.1's correction applied)

| Variant | New records ideation doc flagged as needed | Current repository status |
|---|---|---|
| 1C | `solo_session_words`, `post_exit_tail_words` × 2 speakers × 3 phases (12) | Present in `phase_profile.json`; **not yet independently confirmed flattened into `nalex_viz_schema.json`'s `artifact_1_volume_asymmetry`** — `UNVERIFIED — REQUIRES SOURCE INSPECTION` for the exact flattened-record count beyond what was directly observed in this pass (records for these fields were seen present in the schema dump reviewed during this pass, appearing complete for all 3 phases × 2 speakers, but a field-by-field cross-check against all 12 expected records was not exhaustively re-verified after the initial read). |
| 2A | Conflict `median_reply_seconds` restored to range form (2 records amended) | **Confirmed still needed** — `nalex_viz_schema.json → artifact_2_latency_convergence` currently stores Conflict as point values (120/94), not the authoritative range (112–120/70–94); this is a real, outstanding blocker for variant 2A specifically (§4, Q2/2A render blockers), separate from and not resolved by this document's 3C-focused schema work. |
| 2C | Aftermath per-session `median_reply_seconds` (5) + 2 inter-contact gaps | Session-level records observed present in `nalex_viz_schema.json → artifact_2_latency_convergence` (sessions 1, 4, 5 explicitly seen; sessions 2–3 not independently confirmed in this pass) plus both gap records (676,768s, 587,598s), present. |
| **3C** | `explicit_signoff_turns` × 2 speakers × 3 phases (6) + corpus totals (2) | **Confirmed fully present and correct** — see §6.1. This is the variant this document builds. |
| 4C | 17 annotated questions as records with `heat` / `loop_tag` / `intent` | `UNVERIFIED — REQUIRES SOURCE INSPECTION` — not confirmed flattened into `nalex_viz_schema.json` as 17 discrete display-ready records with these three fields attached in this pass; `conflict_questions_annotated.json` itself (§3.6, §11.7) carries the raw data and is a valid direct extraction source regardless. |

## 11.10 Existing prior-art render precedent (from `visualisations/nalex_mobile_infographic_schema.json`, complete relevant excerpt)

Verbatim `rendering_contract`: *"Render only these records. Do not infer new themes, rewrite evidence, add analysis, or compute new metrics. Caveat strings marked render_on_face MUST appear in the artifact body, not in comments or footnotes."*

Verbatim `artifact_3_initiation_closure.definitions`:
- `{"term": "session close", "text": "the last turn before a 60-minute gap — a mechanical artifact, not a communicative act", "render_on_face": true}`
- `{"term": "explicit sign-off", "text": "a verbal termination move", "render_on_face": true}`

Verbatim `artifact_3_initiation_closure.caveats`:
- `{"text": "Naomi's 5 Aftermath closes overlap her 11 post-exit turns — the metric partly counts talking after he left as closing.", "render_on_face": true}`
- `{"text": "Aftermath denominator is 5 sessions. One session is 20% of the bar.", "render_on_face": true}`

Verbatim `artifact_3_initiation_closure.interpretation_records`:
- `{"tag": "alex_withdrawal_by_exit", "text": "INTERPRETATION: managing load by ending exchanges rather than escalating", "source": "phase_profile.json tag_vocabulary.emotional_tags"}`
- `{"tag": "naomi_never_closes_verbally", "text": "STRUCTURAL TAG: zero explicit sign-off moves in the phase", "source": "phase_profile.json tag_vocabulary.problematic_tags"}`
- `{"tag": "dyad_asymmetric_repair_expectation", "text": "INTERPRETATION: each waits for the other to perform the first repair move", "source": "phase_profile.json tag_vocabulary.emotional_tags"}`

This precedent's `STRUCTURAL TAG:` prefix convention for `problematic_tags` (as distinct from `INTERPRETATION:` for `emotional_tags`) is adopted by this document (§5.6, §7, §8.4) as the required visual/textual differentiation mechanism.
