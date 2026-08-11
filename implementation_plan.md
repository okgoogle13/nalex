# Nalex Mobile Infographic Concepts

This document presents three distinct information-architecture concepts for the Nalex mobile infographic, utilizing the Neon Tokyo-night visual direction and Material 3 Expressive principles.

## Workspace Verification
- **Confirmed Accessibility:** All requested root files, prompt architectures, analysis outputs, and visualisations are accessible and have been evaluated. 
- **Flagged Duplication:** `nalex_viz_ideation.md` exists in both `visualisations/` and `research_prompt_modes/analysis_outputs/`. 
- **Evidence Hierarchy:** Raw data (`events.jsonl`, `phase_profile.json`) and canonical synthesis (`CURRENT_STATE_CLEAN.md`, `pass_d_synthesis_report.md`) are treated as primary evidence. Prompts, schemas, and prior HTML renders are treated strictly as design references.

---

## Concept 1: The Empirical Ledger
**1. Concept name:** The Empirical Ledger
**2. Interpretive intensity:** Neutral / evidence-only
**3. Proposed vertical layout:**
   - Header: Baseline vs Aftermath Timeline
   - Metric 1: Volume Asymmetry (Word counts)
   - Metric 2: Initiation Balance (0 vs 5 sessions)
   - Metric 3: Response Latency Jump
**4. Recommended chart or visual form:** Clean horizontal bar charts for volume/latency; binary dot plots for initiation.
**5. Primary viewer takeaway:** Communication structure radically shifted after June 26, moving from balanced pacing to extreme asymmetry in volume and initiation.
**6. What appears above the fold:** One-sentence bottom line and three high-contrast metric summaries.
**7. Hidden behind progressive disclosure:** EID-level event logs, specific conversational quotes, detailed conflict timeline.
**8. How M3 Expressive styling supports comprehension:** Uses shape (rounded pills) to group data cleanly; restrained glow exclusively highlights the "Aftermath" data points to emphasize the shift.
**9. Colour, shape, containment, and typography strategy:** Deep charcoal background. Neutral violet and cool cyan for data points. Monospaced typography for numbers. Sharp containment (cards with 1px borders) emphasizes data over emotion.
**10. Mobile adaptation (Pixel 10 Pro):** Edge-to-edge cards with generous tap targets; sticky header with phase selector.
**11. One-handed interaction:** Thumb-reachable accordion toggles at the bottom to expand the timeline.
**12. Accessibility and readability:** 7:1 contrast ratios on data labels. Text labels accompany all color-coded data.
**13. How the minimal variant would work:** A single scrolling screen with the 3 main metrics and the bottom line.
**14. How the detailed variant would work:** Tapping a metric card slides up a bottom sheet with the full event ledger.
**15. Main strength:** Bulletproof against accusations of bias or over-interpretation.
**16. Main risk or tradeoff:** May feel dry and miss the core relational dynamics (the "why").
**17. Exclude, merge, or move:** Exclude emotional labels ("Cost Controller"). Move textual quotes of boundary enforcement to the detailed view.

---

## Concept 2: The Structural Shift
**1. Concept name:** The Structural Shift
**2. Interpretive intensity:** Lightly interpretive
**3. Proposed vertical layout:**
   - Header: The Relational Deadlock
   - Section 1: The Rupture (June 26 turning points)
   - Section 2: The Roles (Exhaustive Processor vs. Cost Controller)
   - Section 3: The Deadlock (Simultaneous Accountability failure)
**4. Recommended chart or visual form:** Diverging bar charts for pronoun usage ("I" vs "You"); sequenced flow diagrams for the repair protocol.
**5. Primary viewer takeaway:** The metric shifts reflect a pursuer-withdrawer dynamic triggered by an unresolved rupture and simultaneous accountability failures.
**6. What appears above the fold:** The "Deadlock" summary and a visual representation of Naomi's volume vs Alex's withdrawal.
**7. Hidden behind progressive disclosure:** Competing explanations (Regulation vs Punishment) and the detailed Two-Lane Repair Protocol.
**8. How M3 Expressive styling supports comprehension:** Uses layered elevation to separate facts (base card) from interpretation (elevated glowing badge).
**9. Colour, shape, containment, and typography strategy:** Charcoal base. Magenta for Naomi, Cyan for Alex. Interpretations are italicized and contained in distinct, softer-cornered tonal cards.
**10. Mobile adaptation (Pixel 10 Pro):** Vertical scroll telling a sequential story; large typography for key insights.
**11. One-handed interaction:** Swipeable carousels for the "Competing Explanations" cards in the thumb zone.
**12. Accessibility and readability:** Interpretation badges use shape (not just color) to denote uncertainty.
**13. How the minimal variant would work:** Top summary, diverging pronoun chart, and the recommended "Two-Lane Repair" step.
**14. How the detailed variant would work:** Expanding the roles section reveals full text quotes (the house boundary crossing, the "chaser" comment) and QA carry-forward.
**15. Main strength:** Balances empirical rigor with actionable relational context.
**16. Main risk or tradeoff:** The labels ("Processor", "Controller") might be contested if not explicitly framed as hypotheses.
**17. Exclude, merge, or move:** Exclude psychoanalysis of latent motives. Move timeline minutiae to a collapsible "Evidence Ledger".

---

## Concept 3: The Anxious-Avoidant Deadlock
**1. Concept name:** The Anxious-Avoidant Deadlock
**2. Interpretive intensity:** More opinionated, evidence-bounded
**3. Proposed vertical layout:**
   - Header: The Accountability Entanglement
   - Section 1: The Threat of Exit (Topic-Contingent Availability)
   - Section 2: The Emotional Burden (Naomi's Over-functioning)
   - Section 3: Diverting Strategies
   - Section 4: Required Interventions
**4. Recommended chart or visual form:** Asymmetric bubble visualizations (showing the weight of emotional labor); overlapping Venn diagrams for entangled grievances.
**5. Primary viewer takeaway:** The relationship is gated by Alex's threat of exit, forcing Naomi to over-function and preventing genuine accountability.
**6. What appears above the fold:** The bottom line regarding the structural deadlock and the immediate need for lane-switching.
**7. Hidden behind progressive disclosure:** The raw data metrics validating the claims and the QA confidence limitations.
**8. How M3 Expressive styling supports comprehension:** Uses intense neon gradients to highlight zones of high conflict/entanglement, drawing the eye directly to the core rupture.
**9. Colour, shape, containment, and typography strategy:** High-contrast lime for "Interventions". Unorthodox, asymmetrical card shapes represent the unbalanced dynamic.
**10. Mobile adaptation (Pixel 10 Pro):** Scroll-triggered animations (bubbles merging/expanding) as the user scrolls.
**11. One-handed interaction:** Floating Action Button (FAB) for quick access to the "Two-Lane Repair Protocol" scripts.
**12. Accessibility and readability:** Neon colors used for accents; core text remains stark white on charcoal.
**13. How the minimal variant would work:** Narrative summary and the most critical intervention step.
**14. How the detailed variant would work:** Deep dive into "Competing Explanations" and exact quotes from the July 11 aftermath.
**15. Main strength:** Highly engaging, immediately actionable, and clearly communicates the urgency of the dynamic.
**16. Main risk or tradeoff:** Could be perceived as biased or as sensationalizing the conflict.
**17. Exclude, merge, or move:** Exclude all baseline data that doesn't directly relate to the conflict/aftermath deadlock. Move raw metrics to an Appendix.

---

## Recommendations & Next Steps

1. **Rank:** 1. Concept 2 (The Structural Shift) | 2. Concept 1 (The Empirical Ledger) | 3. Concept 3 (The Anxious-Avoidant Deadlock).
2. **Recommended Concept:** Concept 2. It perfectly balances actionable relational dynamics with unassailable metric evidence.
3. **Fallback Neutral Version:** Concept 1.
4. **First Render Variant:** Start with Variant A (Minimal). Validate the visual hierarchy and neon Tokyo aesthetic before building out the complex disclosure components.
5. **First Usability Risk:** Ensuring the progressive disclosure (expanding cards/bottom sheets) is discoverable and doesn't hide critical context.
6. **First Interpretive Risk:** Ensuring the "Cost Controller" and "Exhaustive Processor" labels are clearly understood as analytical frameworks, not absolute facts.
7. **Render Brief (Concept 2):** Build a Pixel-sized vertical HTML prototype. Use a charcoal background (#121212) with cyan/magenta neon accents. Include a diverging bar chart for pronoun asymmetry, a swipeable carousel for competing explanations, and a clear "Two-Lane Repair" call to action. Layered elevation must separate metrics from interpretation.

## User Review Required
Please review the three proposed concepts above. Once you approve a concept (recommending Concept 2), we can move forward with generating the `nalex_mobile_infographic_render.html` artifact in a subsequent step.
