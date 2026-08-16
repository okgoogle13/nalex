# Nalex Semantic Schema v2

## Purpose and Scope
This schema defines a semantically driven data model for Project Nalex. It replaces the legacy reliance on mechanical metrics (e.g., reply latency, raw question counts, arbitrary 60-minute session gaps) with a structure optimized for mapping relational moves, boundaries, and accountability. It is designed to support constructive reflection, rupture/repair analysis, and safe visualization generation.

## Core Design Principles
- **Semantic Boundaries over Temporal Gaps:** Interaction loops are defined by the introduction and resolution/termination of a specific topic or concern, not by the time elapsed between messages.
- **Observation / Interpretation Separation:** Factual observations (what happened) must be strictly separated from interpretations (what it might mean).
- **Neutral Default:** Factual vocabulary must not embed conclusions about motive, intent, or pathology.
- **Traceability:** Every observation or interpretation must link to a specific source event or excerpt.
- **Artifact Controls:** The schema enforces privacy layers, distinguishing between raw private evidence and shareable paraphrases.
- **Deprecation of Low-Value Metrics:** Reply latency, word volume, raw question counts, phase framing (Baseline/Conflict/Aftermath), and gap duration are explicitly excluded as primary analytic drivers.

## Full Schema Structure
```json
{
  "loop": {
    "interaction_loop_id": "string",
    "semantic_loop_label": "string",
    "participants": [
      "string"
    ],
    "core_topic": "string",
    "loop_start_event_id": "string",
    "loop_end_event_id": "string",
    "loop_outcome": "unresolved | paused | repair_attempted | partially_repaired | resolved | response_provided | unclear",
    "repair_response_status": "no_repair_offer | possible_repair_opening | repair_offer_made | received | not_received | unclear",
    "boundary_confidence": "high | medium | low",
    "boundary_rationale": "string",
    "intervening_events_note": {
      "excluded_event_ids": ["string"],
      "reason": "string",
      "effect_on_boundary_confidence": "string"
    },
    "source_limitations": "string",
    "related_loop_ids": ["string"],
    "selection_reason": "string"
  },
  "events": [
    {
      "source": {
        "source_event_ids": [
          "string"
        ],
        "source_order": "integer",
        "timestamps": [
          "string"
        ],
        "speaker": "string",
        "minimal_redacted_excerpt": "string",
        "excerpt_mode": "exact_quote | redacted_quote | neutral_paraphrase",
        "evidence_type": "direct_text | transcript_summary | inferred_from_context",
        "source_quality": "direct_text | voice_transcript | transcript_with_known_errors | contextual_summary",
        "source_quality_note": "string | null",
        "speaker_confidence": "high | medium | low"
      },
      "evidence_integrity": {
        "claim_to_excerpt_alignment": "high | medium | low",
        "unverified_or_ambiguous_claims": ["string"],
        "requires_audio_review": "boolean"
      },
      "observation": {
        "observable_moves": [
          {
            "sequence": "integer",
            "code": "string (from factual vocabulary)",
            "evidence_reference": "string",
            "coding_rationale": "string"
          }
        ],
        "target_or_topic": "string",
        "need_or_boundary": {
          "content": "string | null",
          "basis": "explicit_statement | constrained_paraphrase | analyst_inference | none",
          "evidence_reference": "string | null",
          "uncertainty_note": "string | null"
        },
        "response_to_prior_move": "string | null",
        "explicit_statement_of_impact": "string | null",
        "explicit_statement_of_intent": "string | null",
        "explicit_request_for_response": "string | null",
        "direct_response_status": "addresses_prior_concern | partly_addresses_prior_concern | does_not_address_prior_concern | not_applicable | unclear",
        "context_facts": "string",
        "interaction_state_after_event": "connected | strained | ruptured | repair_opening | paused | unclear"
      },
      "interpretation": {
        "interpretation_tags": [
          {
            "tag": "string (from interpretation vocabulary)",
            "confidence": "high | medium | low",
            "interpretation_basis": "explicit_statement | strong_contextual_support | tentative_pattern",
            "linked_observation_sequences": ["integer"],
            "uncertainty_note": "string",
            "alternative_reading": "string"
          }
        ]
      },
      "coding_metadata": {
        "coded_by": "gemini | human_reviewed | claude_code | ai_proposed_pending_human_review",
        "coding_version": "string",
        "review_notes": "string | null",
        "coding_review_status": "proposed | checked_against_source | approved_for_private_artifact | approved_for_shareable_artifact"
      },
      "artifact_controls": {
        "privacy_level": "private_evidence | shareable_paraphrase | do_not_display",
        "shareability_notes": "string",
        "suitable_for": [
          "shared",
          "alex_reflection",
          "naomi_reflection",
          "facilitator_only"
        ],
        "visual_weight": "primary | supporting | appendix_only",
        "display_mode": "paraphrase | short_excerpt | private_only"
      }
    }
  ]
}
```

## Factual Controlled Vocabulary (observable_moves)
- **states_explicit_concern_or_boundary**: Clearly identifies an action or event that caused distress/crossed a limit.
- **responds_to_concern_with_explanation_of_intent**: Addresses a concern by describing internal rationale.
- **contests_stated_account**: Directly disputes the factual sequence or details of an event.
- **redirects_focus_to_other_persons_conduct**: Shifts the subject to a critique of the partner's behavior.
- **raises_counter_concern**: Introduces a new grievance about the partner.
- **uses_heightened_or_confrontational_language**: Uses profanity, insults, or explicit hostile wording.
- **acknowledges_impact_of_action**: Validates how an action affected the other person.
- **does_not_respond_to_stated_concern**: Ignores or bypasses an explicit prior concern.
- **requests_pause_or_space**: Asks for time before continuing.
- **explicitly_ends_exchange**: States an unambiguous intention to terminate the interaction.
- **offers_specific_repair_step**: Suggests concrete action to resolve the rupture.
- **seeks_clarification**: Asks for context without accusation.
- **invites_closeness**: Makes a bid for connection.
- **changes_topic_before_addressing_concern**: Shifts focus away from an active concern.
- **apologises**: Issues a general apology.
- **states_causal_responsibility**: Speaker explicitly states that they caused or were at fault for a specific event or outcome.
  - *Inclusion:* (a) An explicit first-person statement of fault or causation. (b) The statement is linked to a specific event or outcome. (c) The event or outcome may be established either in the same minimally sufficient evidence excerpt or in a directly adjacent, explicitly referenced source event. (d) When adjacent evidence is used, the coding record must include the supporting source_event_id in evidence_reference.
  - *Exclusion:* A regret expression without a causal or fault claim (use `apologises` only if independently supported); validation of another person's experience (use `acknowledges_impact_of_action` only if independently supported); an explanation of intent without an explicit causal or fault claim; a future repair offer without an explicit causal or fault claim; global self-criticism, vague guilt, or non-event-specific self-blame; hypotheticals, conditionals, sarcasm, or ambiguous statements where literal meaning cannot be established from the available source.
  - *Coding constraints:* This code records only the explicit statement. Do not infer sincerity, factual accuracy, remorse, accountability quality, motive, emotional state, manipulation, relational impact, or repair success. If tone or source ambiguity materially affects whether the statement is literal, retain the source caveat and set `requires_audio_review: true`. Co-occurring apology, impact acknowledgement, intent explanation, or repair offer must each be independently excerpt-supported and coded separately.
- **accepts_repair**: Welcomes a repair attempt.
- **declines_or_ignores_repair**: Bypasses a repair attempt.
- **re_raises_unresolved_concern**: Brings back a previously stated, unclosed issue.

## Optional Interpretation Rules
Interpretations are strictly optional.
An interpretation must not be added merely because a factual code was used (e.g., contesting facts does not automatically equal deflection).
Every interpretation tag must include a confidence level, an uncertainty_note, an alternative_reading, and linked_observation_sequences.

## Interpretation Vocabulary (interpretation_tags)
- possible_vulnerable_disclosure
- possible_deflection_of_accountability
- possible_self_protection
- possible_punitive_escalation
- possible_pseudo_mutuality
- possible_bid_for_attunement
- possible_invalidation

## Evidence Integrity Rules
Every coded event requires an evidence_integrity block confirming the alignment between the raw source claim and the provided excerpt.
Any transcription ambiguities (e.g., suspected errors in voice-to-text) must be flagged in unverified_or_ambiguous_claims and requires_audio_review set to true.

## Privacy and Artifact Control Rules
- **privacy_level** dictates usage: private_evidence must never be exposed in shared artifacts.
- **display_mode** dictates formatting: short_excerpt or paraphrase.
- **suitable_for** restricts the target audience (e.g., alex_reflection vs. shared).

## Coding Review Status
- **proposed**: Generated by AI, unverified.
- **checked_against_source**: Excerpts and timestamps verified against raw logs.
- **approved_for_private_artifact**: Vetted for internal use.
- **approved_for_shareable_artifact**: Cleared for joint viewing.

## Loop Boundary Rules
A loop is defined by the introduction and resolution/termination of a distinct semantic topic.
Chronologically intervening events may be excluded if they relate to a clearly distinct topic, provided the exclusion is documented in intervening_events_note.
Boundary confidence (high, medium, low) must reflect the continuity and clarity of the semantic chain.

## Null-State Handling for Structured Optional Objects

Where a schema field is a structured optional object (e.g., `need_or_boundary`), a bare `null` value is not an acceptable substitute for a typed null-state. The following three distinct null-states must be used explicitly:

| State | Meaning |
|---|---|
| `none` | Reviewed — no relevant content was found for this field in this event. |
| `not_assessed` | No coding determination was made; the field was not evaluated in this pass. |
| `unknown` | Evidence ambiguity prevents any determination; a coding decision could not be reached. |

**Canonical default rule:** A bare `null` must not be silently converted to `none` without an explicit canonical default decision recorded by a human reviewer. A system or agent performing normalization must flag the conversion as pending human confirmation rather than applying it automatically. If no explicit canonical default has been established for a given field, the state must be recorded as `not_assessed` until a human decision is made.
