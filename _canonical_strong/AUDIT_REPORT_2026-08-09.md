# Nalex Artifact & Research Audit — 2026-08-09

Scope: `research_prompt_modes/` and `visualisations/`. Purpose: identify strong, canonical, and reusable material before any new artifact is built. No new analysis or visual design is proposed here.

**Note on project-rule tension (read first):** This project's own internal rules (`index.md`, `claude.md`, and the header of `nalex_patterns_flashcards.html`) state the Nalex mode is *analysis only* — no advice, no prescriptions, no drafted messages. The outer brief for this audit asks for *forward-focused, constructive, coaching-style* language. These two constraints conflict on at least one file (`nalex_playbook_dark_m3.html`, which the project itself flags "OUT OF MODE — NOT AN EVIDENCE ARTIFACT"). This report scores that file highly on narrative alignment with the audit brief while flagging explicitly that it violates the project's own analysis-only rule. Resolving that conflict is a decision for you, not something this audit resolves on its own.

---

## 1. Inventory

### `research_prompt_modes/`

| File | Size | Role |
|---|---|---|
| `viz_schema_template.md` | 3.6 KB | Canonical flattened-record schema contract (theme/phase/speaker/metric/evidence/confidence/visual_hint/forward_looking_evaluation) |
| `visualization_pipeline.md` | 2.6 KB | Canonical evidence-to-render workflow contract (extract → flatten → render) |
| `shared_system_prompt.md` | 1.9 KB | Base analyst system prompt — non-diagnostic framing rules, hedged language requirement |
| `pass_a_micro_session_audit.md` | 2.2 KB | Pass A prompt spec (micro-session audit) |
| `pass_b_macro_participant_profile.md` | 2.0 KB | Pass B prompt spec (macro participant profile) |
| `layer_c_repair_protocol.md` | 10.8 KB | Layer C prompt spec — "Two-Lane Repair Protocol" intervention framework |
| `pass_d_final_qa_synthesis.md` | 5.3 KB | Pass D prompt spec — second-stage synthesis instructions |
| `analysis_outputs/pass_a_output.md` | 5.2 KB | Pass A output (micro-session findings) |
| `analysis_outputs/pass_b_output.md` | 6.2 KB | Pass B output (macro participant profile) |
| `analysis_outputs/layer_c_output.md` | 4.8 KB | Layer C output — incident classification, repair protocol applied to 11 Jul incident |
| `analysis_outputs/pass_d_synthesis_report.md` | 8.2 KB | Full synthesis report (executive synthesis, evidence, interpretations, competing explanations, next steps) |
| `analysis_outputs/nalex_viz_schema.json` | 60.3 KB | Flattened schema instance for 4 visual questions — **every record carries a `forward_looking_evaluation` string** |
| `analysis_outputs/nalex_viz_ideation.md` | 27.1 KB | 12-variation ideation doc (4 questions × 3 interpretation tiers), ranks each variation |

### `visualisations/`

| File | Size | Role |
|---|---|---|
| `nalex_playbook_dark_m3.html` | 20.9 KB | Dark M3-token flip-card "Communication Playbook" — self-flagged **OUT OF MODE / prototype, not evidence** |
| `nalex_patterns_flashcards.html` | 90.3 KB | Desktop/light-mode interactive card browser — self-declared **canonical evidence artifact** |
| `nalex_mobile_v1_playful.html` | 31.3 KB | Mobile infographic, "playful" skin, dark M3-ish tokens, renders `nalex_mobile_infographic_schema.json` |
| `nalex_mobile_v2_polished.html` | 30.0 KB | Same schema, "polished" skin |
| `nalex_mobile_v3_dramatic.html` | 32.0 KB | Same schema, "dramatic" skin, scrollytelling hero |
| `nalex_mobile_infographic_render.html` | 10.7 KB | Separate, older single-screen mobile mock ("Neon Tokyo"), not tied to the v1–v3 schema |
| `nalex_mobile_infographic_schema.json` | 21.6 KB | Flattened schema instance feeding v1/v2/v3 — evidence-only, **no** `forward_looking_evaluation` field |
| `nalex_viz_canonical_render_spec.md` | 140.0 KB | Very long implementation spec for the recommended "3C" canonical render; process documentation, not a rendered artifact |
| `nalex_viz_ideation.md` | 27.1 KB | Duplicate/earlier copy of the ideation doc also found in `research_prompt_modes/analysis_outputs/` |
| `visualization_input_manifest.txt` | 0.5 KB | SHA-256 checksums for 4 canonical source files (integrity manifest) |

### Root files referenced by the above (for context, not primarily in scope)

- `index.md` — project index; declares canonical file roles project-wide (used throughout this audit as the arbiter of "canonical")
- `CURRENT_STATE_CLEAN.md` (67.8 KB) — single source of truth for all findings and numbers; dense, stats-heavy ledger
- `phase_profile.json` (14.9 KB) — `NALex_PHASE_PROFILE`; contains `problematic_tags` (structural) and `emotional_tags` (explicitly labeled `INTERPRETATION`)
- `NALEX_EVIDENCE_BRIEF_headline_patterns.md` (16.1 KB) — digestible interpretive summary, in scope for §3/§4 below

---

## 2. HTML Artifact Assessments

Scores 0–5. **Overall** = "keep as canonical base" potential, not an average of the other four.

### `nalex_playbook_dark_m3.html`
- Visual alignment: **4** — genuine `--md-sys-color-*` dark tokens, huge/expressive radii, spring easing; container tops out desktop-width (900px) so mobile-first is only partial.
- Interaction: **5** — flip cards, expandable "protocol" reveal, persona-split panes. The most playful/unexpected interaction model reviewed.
- Narrative alignment: **5** — genuinely forward-focused, constructive, second-person coaching ("Moving Forward" boxes), no diagnostic labels shown to the reader.
- Content discipline: **4** — short, focused cards; zero data density (no figures at all), which is "less is more" taken to its limit.
- **Overall: 3** — capped because the file is self-labeled `nalex-status: out-of-mode-prototype` and its own header states it is prescriptive, contains scripted speech, and carries zero measured figures or caveats, which conflicts with this project's analysis-only rule.
- **Verdict:** Strong on constructive tone, essentially zero on evidentiary grounding. Best available *narrative-tone donor*, not a ship-ready base.

### `nalex_patterns_flashcards.html`
- Visual alignment: **2** — light/paper aesthetic (`#faf8f5` background), no M3 token system, desktop-width container (1120px). Not dark M3, not clearly mobile-first.
- Interaction: **5** — sticky filter bar with phase/person chips, scroll progress fill, glossary tooltips, "hide interpretation" toggle, sparkline visuals. The most engineered interaction of anything reviewed.
- Narrative alignment: **2** — explicitly non-diagnostic and careful ("It does not decide who was right, and it does not suggest what anyone should do"), but that same sentence rules out forward-focused coaching by design.
- Content discipline: **3** — 23 cards across multiple themes; well filtered but not "one visual question per artifact."
- **Overall: 3** — the project's own declared canonical evidence artifact; strongest engineering and schema fidelity, wrong visual mode and wrong tone for this brief.
- **Verdict:** Strong on analytic depth and interaction discipline, weaker on constructive tone and dark-M3 alignment.

### `nalex_mobile_v1_playful.html` (representative of the v1/v2/v3 trio)
- Visual alignment: **5** — explicit Pixel 10 Pro target, asymmetric/varied radii called out in-file as "M3 Expressive," dark surface ramp, neon persona accents, `max-width:520px` mobile container with safe-area padding.
- Interaction: **4** — sticky top bar, phase cards, structured sections; less experimental than the flip-card playbook but still tactile.
- Narrative alignment: **2** — renders `nalex_mobile_infographic_schema.json`, which carries **no** `forward_looking_evaluation` field; INTERPRETATION tags are shown with their prefixes intact (non-diagnostic hygiene is good), but nothing is forward-looking.
- Content discipline: **5** — caveats are rendered on-face per record (`render_on_face: true`), one visual question per artifact block, no invented structure.
- **Overall: 4** — the strongest mobile-first, dark-M3, schema-disciplined shell in the set. Needs a narrative/coaching layer added; the visual and technical scaffolding is otherwise close to ready.
- **Verdict:** Strong base for a minimal variant once forward-looking text is layered in.
- **v2 (`polished`)** and **v3 (`dramatic`)** share the same schema and score identically on narrative/content discipline; v2 is marginally cleaner and less "expressive," v3 trades interactivity for a scrollytelling hero. Not scored separately — treat as design-skin alternates of v1, not independent candidates.

### `nalex_mobile_infographic_render.html`
- Visual alignment: **3** — dark, mobile-width (420px), but "Neon Tokyo" palette without an M3 token system.
- Interaction: **3** — scroll-snap carousel and a fixed action button; shallower than the v1–v3 trio (no expand/reveal).
- Narrative alignment: **1** — labels roles as "Exhaustive Processor" / "The Sponge," uses "pursuer-withdrawer cycle" and "weaponized" without the project's `INTERPRETATION:` prefix discipline, and ends with a prescriptive call-to-action ("Initiate Two-Lane Repair"). This is the most diagnostic/pathologizing artifact reviewed.
- Content discipline: **3** — single screen, low volume, but the tone problem is independent of density.
- **Overall: 1** — do not use as a base under this brief's scoring bias.
- **Verdict:** Compact and mobile-first, but the most analytic/diagnostic-leaning artifact in the set, not constructive.
- **Risk if reused as-is:** most diagnostic/pathologizing artifact in the set; likely to undermine the constructive, forward-focused brief if it resurfaces as a template.

---

## 2.5. Scoring Bias Notes (Constructive vs Analytic)

- **Most constructive tone:** `nalex_playbook_dark_m3.html` — but explicitly out-of-mode per the project's own rules.
- **Most analytic-but-disciplined (non-diagnostic):** `nalex_patterns_flashcards.html` and the `nalex_mobile_v1/v2/v3` trio — careful evidence/interpretation separation, INTERPRETATION prefixes preserved, caveats rendered on-face. These are *not* diagnostic even though they are not forward-focused; the distinction matters. They downgrade only on "forward-focused" scoring, not on "non-pathologizing" scoring.
- **Most diagnostic/pathologizing:** `nalex_mobile_infographic_render.html` — invents unprefixed relational-role labels and a prescriptive CTA.
- **Root data files** (`phase_profile.json`, `CURRENT_STATE_CLEAN.md`) are heavy, multi-metric, and contain confidence intervals, medians, and caveats by design — appropriate as the *backbone* evidence source but explicitly downgraded as *narrative* source per the brief. Their `emotional_tags` block is useful raw material only because each entry is pre-labeled `INTERPRETATION`.

---

## 3. Research/Schema Assessments

| File | Role | Consistency |
|---|---|---|
| `research_prompt_modes/viz_schema_template.md` | Defines the flattened record schema every visualization input must conform to | Consistent with `index.md` §11 (which names it explicitly as required reading) and with `visualization_pipeline.md`; the only file that documents the `forward_looking_evaluation` field |
| `research_prompt_modes/visualization_pipeline.md` | Defines the extract → flatten → render workflow and the "dumb layout engine" rendering rule | Consistent with `index.md` §11 and `viz_schema_template.md`; short and unambiguous |
| `research_prompt_modes/analysis_outputs/nalex_viz_schema.json` | A full schema-compliant instance for 4 visual questions | Consistent with `viz_schema_template.md`'s shape; the richest source of forward-looking text tied 1:1 to evidence records |
| `research_prompt_modes/analysis_outputs/nalex_viz_ideation.md` | Ranks 12 rendering variations by risk/information-added | Internally consistent, cites its own data-integrity caveats (§0) that bind every variation; process document, not a narrative source |
| `NALEX_EVIDENCE_BRIEF_headline_patterns.md` | Digestible evidence/interpretation brief | Declared by `index.md` §2 as a legitimate quick-framing companion to `CURRENT_STATE_CLEAN.md`; consistently labels every line "Evidence –" or "Interpretation –" |
| `CURRENT_STATE_CLEAN.md` | Single source of truth ledger | Declared canonical by `index.md` §1; all other files must not contradict it. Too large/stats-heavy to serve as a narrative source, but this is its intended role — a ledger, not prose |
| `phase_profile.json` | Numeric phase bundle + tag vocabulary | Source of truth for numbers; `emotional_tags` are explicitly marked `INTERPRETATION` in the file itself — good hygiene, but this is data, not narrative |
| `research_prompt_modes/analysis_outputs/pass_d_synthesis_report.md` | Full synthesis (evidence + interpretation + recommendations) | Internally well-organized (evidence/interpretation/competing-explanations sections) but uses diagnostic-leaning shorthand ("pursuer-withdrawer cycle," "Emotional Auditor," "The Sponge") without carrying the `INTERPRETATION:` prefix discipline used elsewhere — treat with more caution as a narrative source |

**Single best schema template file:** `research_prompt_modes/viz_schema_template.md` — it is the file `index.md` names as canonical, and it is the only file that formally defines the forward-looking field.

**Single best pipeline/contract file:** `research_prompt_modes/visualization_pipeline.md` — short, unambiguous, and explicitly named canonical by `index.md` §11.

**Best evidence brief for patterns and metrics:** `NALEX_EVIDENCE_BRIEF_headline_patterns.md` — consistently separates evidence from interpretation, states its own sourcing caveats, and is the file `index.md` itself points to for "quick framing."

---

## 4. Synthesis: Strongest Content and Canonical Candidates

### Top 3 HTML artifacts to keep/refine

1. **`nalex_mobile_v1_playful.html`** — Best M3 Expressive dark-mode, mobile-first, Pixel-10-Pro-targeted shell with disciplined, caveat-honest schema rendering. Satisfies the brief's *visual* and *content discipline* dimensions best. Fix needed: has no forward-looking/coaching text at all — would need `forward_looking_evaluation` lines (see `nalex_viz_schema.json`) merged in.
2. **`nalex_playbook_dark_m3.html`** — Best narrative and interaction-novelty match to the brief's *forward-focused, playful* dimensions. Fix needed: currently self-flagged out-of-mode, has zero measured evidence or caveats, and its coaching content is prescriptive/scripted — would need to be re-grounded in real evidence records and reframed as reflection prompts rather than instructions, to satisfy both this project's analysis-only rule and the brief's "enable reflection, don't decide" preference.
3. **`nalex_patterns_flashcards.html`** — Best interaction engineering and evidence/interpretation hygiene; the project's own declared canonical evidence artifact. Fix needed: convert light mode to dark M3 tokens, and reduce 23-card density toward "one visual question per artifact" if reused as a structural reference.

### Top 3 research/schema files to treat as canonical

1. **`research_prompt_modes/viz_schema_template.md`** — the flattened-record contract; `index.md`-designated canonical.
2. **`research_prompt_modes/visualization_pipeline.md`** — the extract → flatten → render workflow; `index.md`-designated canonical.
3. **`NALEX_EVIDENCE_BRIEF_headline_patterns.md`** — best digestible evidence/interpretation brief, `index.md`-designated quick-framing companion.

*(Honorable mention, not one of the "top 3" but flagged as strong: `research_prompt_modes/analysis_outputs/nalex_viz_schema.json` — schema-compliant and the richest source of forward-looking lines. Preserved alongside the top 3.)*

### Best narrative / coaching text

Forward-looking, non-diagnostic lines pulled from `nalex_viz_schema.json` (`forward_looking_evaluation` fields, tied to specific evidence records) and from `nalex_playbook_dark_m3.html` ("Moving Forward" panels — note this file is out-of-mode per project rules, included here only as language reference):

From `nalex_viz_schema.json`:
- "Channeling this immense drive for clarity into bounded, structured check-ins could preserve connection while preventing listener overwhelm."
- "Finding a sustainable way to increase communicative volume (e.g. written letters or scheduled topics) could help meet the partner's need for data without burning out."
- "Maintaining periods of zero contact can be a healthy regulatory mechanism."
- "Pacing responses to match the partner's baseline rhythm could reduce the feeling of anticipatory vigilance and restore conversational balance."
- "Maintaining this consistent latency even during high-conflict phases is a strength that can be leveraged to establish a reliable 'safe' response window."
- "Sharing the labor of initiation could prevent the build-up of resentment and allow the partner space to demonstrate voluntary approach."
- "Taking on intentional, small initiation tasks (e.g. a morning check-in) would disrupt the pattern of unilateral pursuit and provide needed reassurance."
- "Separating genuine requests for information from defensive boundary setting is required to break the deadlock and de-escalate the crossfire."

From `nalex_playbook_dark_m3.html` (out-of-mode prototype; language reference only):
- "When seeking connection, plainly state the emotional need directly instead of asking questions."
- "Responding to the emotion behind the question is just as important as the literal answer. Acknowledging you heard her counts as a valid response."
- "Withdrawing to protect your energy is valid and necessary, but doing so constructively requires communicating that you are stepping away."
- "A pause is a tool for repair, not an evasion tactic."

### Recommended canonical base for next artifact run

**HTML shell:** `nalex_mobile_v1_playful.html`
**Schema:** `research_prompt_modes/viz_schema_template.md`, populated with `forward_looking_evaluation` content in the style of `nalex_viz_schema.json`

Why: `nalex_mobile_v1_playful.html` is the only artifact that already satisfies the brief's mobile-first, M3 Expressive dark-mode, and schema-discipline requirements simultaneously. `viz_schema_template.md` is the project's own designated canonical contract and is the only schema file that formally supports a forward-looking field — pairing it with the already-written `forward_looking_evaluation` lines in `nalex_viz_schema.json` gives a next artifact both a compliant visual base and ready constructive text, without needing new analysis.

---

## Files to review later (ambiguous or out of primary scope, not moved)

- `nalex_viz_canonical_render_spec.md` (140 KB) — extremely detailed implementation spec for the "3C" render; likely valuable but too large and process-oriented to score as a narrative or schema source in this pass.
- `nalex_viz_ideation.md` — exists in **two locations** (`research_prompt_modes/analysis_outputs/` and `visualisations/`) with identical size; likely a duplicate. Not deleted or deduplicated per instructions — flagged here for your attention. **Recommendation:** keep one copy (e.g. in `research_prompt_modes/analysis_outputs/`, where `index.md` §10 already documents it) and delete or archive the other to avoid future confusion.
- `research_prompt_modes/analysis_outputs/pass_d_synthesis_report.md` and `research_prompt_modes/pass_d_final_qa_synthesis.md` — the synthesis report is well-structured but uses diagnostic-leaning shorthand ("pursuer-withdrawer," "Emotional Auditor," "The Sponge") without the `INTERPRETATION:` prefix discipline seen elsewhere; useful for full context, not recommended as a narrative source without editing.
- `nalex_mobile_infographic_schema.json` — the evidence-only payload the v1/v2/v3 trio renders; not forward-focused itself (no `forward_looking_evaluation` field) so not moved, but relevant context if `nalex_mobile_v1_playful.html` is extended.
- `CURRENT_STATE_CLEAN.md`, `phase_profile.json` — confirmed canonical per `index.md` but out of scope for "narrative/schema" triage; left in place as the project's central ledger.

---

## Manifest — files copied into `_canonical_strong/`

**Note:** the mount for this project folder does not permit deleting the original files from this environment (`rm` returns `Operation not permitted`), so these files were **copied**, not moved — originals remain in their source locations, and the copies in `_canonical_strong/` carry a triage annotation at the top (HTML comment / Markdown note / JSON `_canonical_triage_note` key).

- `visualisations/nalex_mobile_v1_playful.html` → `_canonical_strong/nalex_mobile_v1_playful.html` — strongest mobile-first M3 dark-mode + schema-disciplined base
- `visualisations/nalex_playbook_dark_m3.html` → `_canonical_strong/nalex_playbook_dark_m3.html` — strongest forward-focused coaching narrative (project-flagged out-of-mode)
- `visualisations/nalex_patterns_flashcards.html` → `_canonical_strong/nalex_patterns_flashcards.html` — strongest interaction engineering, declared canonical evidence artifact
- `research_prompt_modes/viz_schema_template.md` → `_canonical_strong/viz_schema_template.md` — canonical schema contract
- `research_prompt_modes/visualization_pipeline.md` → `_canonical_strong/visualization_pipeline.md` — canonical pipeline contract
- `NALEX_EVIDENCE_BRIEF_headline_patterns.md` → `_canonical_strong/NALEX_EVIDENCE_BRIEF_headline_patterns.md` — best evidence brief
- `research_prompt_modes/analysis_outputs/nalex_viz_schema.json` → `_canonical_strong/nalex_viz_schema.json` — richest source of forward-looking, schema-tied coaching lines

---

**Next:** use `nalex_mobile_v1_playful.html` + `viz_schema_template.md` + `nalex_viz_schema.json` forward-looking lines as the base for a one-shot artifact creation prompt.
