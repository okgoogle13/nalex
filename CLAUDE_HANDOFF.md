# CLAUDE_HANDOFF.md

> **This prototype is a review baseline, not an approved final artifact.**
> **Claude Desktop must review before editing any project files.**

---

## 1. Current Project Status

Antigravity has completed the concept-design and first-render pass for the Nalex mobile infographic. The output is a **Concept 2 (The Structural Shift) Minimal Variant** HTML prototype. An internal QA review identified structural, accessibility, and interpretive problems that require a focused redesign before the prototype can be considered valid.

**Status: FROZEN.** No further modifications will be made by Antigravity.

---

## 2. Files Created or Modified

### Created by this session (in `nalex/` root or subdirectories)

| File | Location | Purpose |
|---|---|---|
| `CLAUDE_HANDOFF.md` | `nalex/` | This handoff document |
| `implementation_plan.md` | `nalex/` | Three-concept design plan with workspace verification |
| `task.md` | `nalex/` | Execution checklist (unchecked — tasks were not formally tracked) |
| `walkthrough.md` | `nalex/` | Post-render summary of what was implemented |
| `pass_d_final_qa_synthesis.md` | `research_prompt_modes/` | QA synthesis prompt with full source-material scope |
| `pass_d_synthesis_report.md` | `research_prompt_modes/analysis_outputs/` | Consolidated synthesis output from pass A, B, and layer C |
| `nalex_mobile_infographic_render.html` | `visualisations/` | The Concept 2 Minimal Variant HTML prototype |

### Pre-existing files not modified

All canonical source data, analysis outputs, prompts, visualisation specs, and prior HTML renders remain untouched.

---

## 3. Current Concept 2 Minimal Variant Implementation

The prototype is a single-page static HTML file (`visualisations/nalex_mobile_infographic_render.html`) containing:

1. **Title + bottom-line sentence** — "The dyad is locked in a pursuer-withdrawer cycle…"
2. **Pronoun Asymmetry chart** — diverging horizontal bars for Naomi vs Alex "I"/"You" counts, badged "FACT"
3. **Relational Roles card** — "Exhaustive Processor" vs "Cost Controller" grid, badged "HYPOTHESIS"
4. **Competing Explanations carousel** — two horizontally scrollable cards (Alex's Withdrawal, Naomi's Pursuit), badged "UNCERTAIN"
5. **FAB button** — "Initiate Two-Lane Repair" fixed to the bottom of the viewport

---

## 4. Design Decisions Already Made

- **Colour mapping:** Magenta (#ff007f) = Naomi, Cyan (#00e5ff) = Alex, Lime (#b2ff05) = action/CTA.
- **Dark-mode base:** Charcoal #121212 with elevated surfaces at #1e1e1e and #2c2c2c.
- **Evidence/interpretation separation:** Pill-shaped "FACT" badge (white on black, rounded) vs outline "HYPOTHESIS" badge (grey border, italic, square corners). Different card elevation and border-radius to reinforce the distinction.
- **FAB as single actionable exit:** The "Two-Lane Repair" recommendation is surfaced as the only call to action.
- **Max container width:** 420px for Pixel 10 Pro portrait.

---

## 5. Evidence Sources Used

The prototype draws data from:

- `pass_b_output.md` — pronoun counts (Naomi: 486 "You" / 455 "I"; Alex: 85 "You" / 146 "I"), word-count averages, initiation ratios
- `pass_a_output.md` — turning-point identification, withdrawal events
- `layer_c_output.md` — boundary-crossing incident classification, diverting strategy labels, Two-Lane Repair Protocol
- `pass_d_synthesis_report.md` — consolidated bottom line, competing explanations, recommended next steps

The prototype does **not** directly reference `events.jsonl`, `phase_profile.json`, or `CURRENT_STATE_CLEAN.md`. All data is mediated through the analysis outputs.

---

## 6. Known Deviations from the Original Specification

### Content density (FAIL)

The original Minimal Variant spec requires exactly five items:

1. One-sentence bottom line ✅ present
2. Three most important evidence-backed observations — ✅ partially (pronoun chart is one; the other two are not clearly separated)
3. Main uncertainty — ❌ not present as a named element
4. Most relevant boundary, risk, or constraint — ❌ not present as a named element
5. One recommended next step — ✅ present (FAB)

The prototype **adds** two sections that belong in the Detailed Variant:
- The "Relational Roles" interpretive card
- The "Competing Explanations" carousel

### Carousel design (FAIL)

The implementation plan placed competing explanations behind progressive disclosure. The prototype puts them on the main scroll as a horizontal carousel with no scroll indicator, violating both the spec and mobile discoverability norms.

---

## 7. Accessibility Issues Identified

| Issue | Severity |
|---|---|
| `#aaaaaa` on `#121212` = ~3.8:1 contrast (below WCAG AA for body text) | High |
| `user-scalable=no` blocks pinch-to-zoom | High |
| No `<link>` to Google Fonts Inter — silently falls back to system fonts | Medium |
| Bar segment labels (0.75rem, black on magenta/cyan) may fall below 4.5:1 | Medium |
| No ARIA labels, roles, or landmarks beyond basic heading structure | Medium |
| Carousel has no scroll indicator, dot pagination, or accessible navigation | Medium |
| Hidden scrollbar (`::-webkit-scrollbar { display: none }`) on scrollable content | Low |

---

## 8. Over-Interpretive Wording Identified

| Current wording | Problem |
|---|---|
| "The dyad **is** locked in a pursuer-withdrawer cycle" | States interpretation as fact |
| "Word choice **reveals** a massive imbalance in structural focus" | "Reveals" implies pronoun counts prove the interpretation |
| "Exits are abrupt, unilateral, and **weaponized**" | Strongest interpretive claim, presented without hedge |
| "Over-functions to prevent erasure" | Asserts motive as fact |
| "Strictly rations emotional availability via withdrawal to prevent engulfment" | Asserts motive as fact |

All five need bounded language per `AGENTS.md`: "appears consistent with…", "may suggest…", "this could reflect…".

---

## 9. Content That Must Move to the Detailed Variant

- **Relational Roles card** (Exhaustive Processor / Cost Controller) → Detailed Variant, Section 2
- **Competing Explanations carousel** (Alex's Withdrawal, Naomi's Pursuit) → Detailed Variant, expandable section
- **Interpretive framing** in the pronoun chart description → replace with neutral label in Minimal; move interpretation to Detailed

---

## 10. Required Next Action

**Focused redesign of the Minimal Variant only:**

1. Reduce to the five required content blocks.
2. Remove Relational Roles from Minimal.
3. Remove Competing Explanations from Minimal.
4. Remove the hidden horizontal carousel.
5. Rewrite overconfident interpretive wording.
6. Preserve the FACT/HYPOTHESIS badge distinction where relevant.
7. Fix contrast and text readability (`--text-secondary` must be at least #c0c0c0 or equivalent for 4.5:1).
8. Remove `user-scalable=no`.
9. Add semantic structure and accessible labels.
10. Load Inter font or declare a visible fallback strategy.
11. Keep the dark Tokyo-night and Material 3 Expressive direction restrained.
12. Do **not** begin the Detailed Variant.

---

## 11. Review Authority

**Claude Desktop must review the handoff, verify the assessment, and obtain explicit user approval before modifying any project files.**

Antigravity will not make further changes to this prototype. The current HTML file should be preserved as a backup before any edits are made.

---

## Project File Map (for Claude Desktop orientation)

```
nalex/
├── CLAUDE_HANDOFF.md              ← this file
├── implementation_plan.md         ← three-concept design plan
├── task.md                        ← execution checklist
├── walkthrough.md                 ← post-render summary
├── CURRENT_STATE_CLEAN.md         ← canonical analysis (source of truth)
├── AGENTS.md                      ← project rules and analytical stance
├── claude.md                      ← project-specific Claude instructions
├── index.md                       ← authoritative file/artifact map
├── events.jsonl                   ← canonical event stream
├── phase_profile.json             ← derived phase metrics
├── aftermath_stats.json           ← derived aftermath metrics
├── baseline_comparison_audit.json ← derived baseline metrics
├── gap_stats_out.json             ← derived gap metrics
├── conflict_questions_annotated.json
├── conflict_questions_summary.json
├── NALEX_EVIDENCE_BRIEF_headline_patterns.md
├── research_prompt_modes/
│   ├── shared_system_prompt.md
│   ├── pass_a_micro_session_audit.md
│   ├── pass_b_macro_participant_profile.md
│   ├── layer_c_repair_protocol.md
│   ├── pass_d_final_qa_synthesis.md    ← QA synthesis prompt
│   ├── visualization_pipeline.md
│   ├── viz_schema_template.md
│   ├── nalex_gemini_viz_corrective_prompt.md
│   └── analysis_outputs/
│       ├── pass_a_output.md
│       ├── pass_b_output.md
│       ├── layer_c_output.md
│       ├── pass_d_synthesis_report.md  ← consolidated synthesis
│       ├── nalex_viz_schema.json
│       └── nalex_viz_ideation.md
└── visualisations/
    ├── nalex_mobile_infographic_render.html  ← THE PROTOTYPE (review baseline)
    ├── nalex_mobile_infographic_schema.json
    ├── nalex_viz_canonical_render_spec.md
    ├── nalex_viz_ideation.md
    ├── visualization_input_manifest.txt
    ├── nalex_mobile_v1_playful.html    ← prior render (reference only)
    ├── nalex_mobile_v2_polished.html   ← prior render (reference only)
    ├── nalex_mobile_v3_dramatic.html   ← prior render (reference only)
    ├── nalex_patterns_flashcards.html  ← prior render (reference only)
    └── nalex_playbook_dark_m3.html     ← prior render (reference only)
```
