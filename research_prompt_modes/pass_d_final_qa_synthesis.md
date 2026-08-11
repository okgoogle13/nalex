You are now performing the second-stage synthesis pass.

The previous QA pass has already reviewed the source material and exported its findings, uncertainties, corrections, and relevant artifacts. To produce a complete and robust synthesis, you must treat the full scope of project files—spanning root data, prompts, analysis outputs, and visualizations—as your authoritative working context.

## Source Material Scope

You are expected to integrate information from the following locations:

| Location | Files |
|---|---|
| Root | `events.jsonl`, `phase_profile.json`, `aftermath_stats.json`, `baseline_comparison_audit.json`, `gap_stats_out.json`, `conflict_questions_annotated.json`, `conflict_questions_summary.json`, `CURRENT_STATE_CLEAN.md`, `index.md`, `AGENTS.md`, `claude.md` |
| `research_prompt_modes/` | `visualization_pipeline.md`, `viz_schema_template.md`, `nalex_gemini_viz_corrective_prompt.md`, pass prompts |
| `research_prompt_modes/analysis_outputs/` | `nalex_viz_schema.json`, `nalex_viz_ideation.md`, pass outputs |
| `visualisations/` | `nalex_viz_canonical_render_spec.md`, `nalex_viz_ideation.md`, `visualization_input_manifest.txt`, all rendered HTML artifacts, `nalex_mobile_infographic_schema.json` |

## Objective

Build a coherent, evidence-grounded synthesis from all the existing artifacts and source data above. Do not restart the analysis from scratch and do not silently discard prior QA findings.

Your task is to:

1. Discover and read all relevant files listed in the Source Material Scope.
2. Identify the original questions, claims, interpretations, uncertainties, and QA findings from these files.
3. Preserve distinctions between:
   - Directly observed or explicitly stated facts.
   - Reasonable interpretations.
   - Speculation or unresolved hypotheses.
4. Reconcile contradictions between artifacts.
5. Identify missing evidence, ambiguity, circular reasoning, overinterpretation, and unsupported conclusions.
6. Produce a practical synthesis that is useful for the next decision or conversation.

## Working rules

- Use the artifacts as the primary evidence base.
- Do not invent events, motives, feelings, diagnoses, or facts that are not supported by the artifacts.
- Do not treat emotional interpretations as objective facts.
- Where multiple explanations remain plausible, present them as alternatives and explain what evidence would distinguish them.
- Maintain the user’s stated boundaries, goals, and constraints.
- Prioritise clarity and usefulness over exhaustive repetition.
- Preserve uncertainty instead of forcing false confidence.
- If an artifact is incomplete, malformed, duplicated, or appears to be an outdated version, flag that explicitly.
- Do not rewrite history to make the material appear more coherent than it is.

## Required output

Create a final Markdown report with the following sections:

# 1. Executive synthesis

Give the clearest concise account of what the artifacts collectively support.

# 2. Established evidence

List only claims directly supported by the source material. For each item, identify the supporting artifact or section.

# 3. Interpretations and likely dynamics

Explain the most plausible emotional, interpersonal, behavioural, or strategic patterns. Clearly label these as interpretations rather than facts.

# 4. Competing explanations

List plausible alternative explanations where the evidence is ambiguous. For each, include:
- Supporting evidence
- Counter-evidence
- What remains unknown
- What new information would help distinguish it

# 5. QA carry-forward

Summarise every unresolved issue, caveat, correction, and confidence limitation identified during the previous QA pass. Do not omit inconvenient findings.

# 6. User position and boundaries

State:
- What the user appears to want
- What the user appears to be protecting or avoiding
- Which boundaries are explicit
- Which boundaries are inferred and therefore uncertain
- Where the user may need to make a deliberate choice

# 7. Decision-relevant implications

Explain what the synthesis means in practical terms. Focus on actionable implications rather than abstract analysis.

# 8. Recommended next steps

Provide a short prioritised list of next actions. Separate:
- Immediate low-risk actions
- Information-gathering actions
- Actions requiring a difficult conversation or commitment
- Actions that should be avoided for now

# 9. Open questions

List the smallest number of unanswered questions that would materially change the analysis.

# 10. Final confidence assessment

Give an overall confidence rating using:
- High
- Moderate
- Low

Explain the rating in terms of evidence quality, consistency, missing context, and interpretive uncertainty.

## Output standards

- Use concise headings and readable Markdown.
- Use tables only when they genuinely improve comparison.
- Quote or reference the relevant artifact when making an important claim.
- Keep facts, interpretations, and recommendations visibly separate.
- Do not overstate certainty.
- Do not provide generic advice disconnected from the artifacts.
- End with a compact section titled:

# Bottom line

State the most defensible conclusion, the main uncertainty, and the next best move in no more than three paragraphs.
