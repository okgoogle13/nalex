# Pilot Loop Audit: loop_house_visit_001

## Purpose
This document audits the selection, boundaries, and limitations of the proposed JSON extraction for loop_house_visit_001. It evaluates the loop's suitability as a test for the nalex_semantic_schema_v2 structure.

## Selection Rationale
This loop (G042 → G181) provides a tight "Call and Response" dynamic isolating a single explicit boundary statement and a direct, multi-part response. It tests the schema's ability to handle ordered observable moves (contesting facts, explaining intent, acknowledging impact) without relying on arbitrary time gaps or aggregate metrics.

## Boundary Definition
- **Start**: G042 (Naomi articulates the house-visit boundary concern).
- **End**: G181 (Alex responds directly to the house-visit narrative).
- **Excluded Event**: G180. This event occurs chronologically between G042 and G181 but was excluded because it introduces a distinct, parallel dispute about name-calling and trust.
- **Boundary Confidence**: Medium. While semantically coherent, the exclusion of G180 means this is not a literal uninterrupted turn-by-turn exchange.

## Limitations & Integrity Concerns
- **Source Limitations**: The primary evidence relies on automated voice transcripts. These transcripts lack essential non-verbal context (tone, pacing, inflection) necessary to distinguish between earnestness, hostility, or defensiveness.
- **Audio Review Requirements**:
  - Compare the literal spoken wording against the redacted text in both excerpts.
  - Verify the transcript's use of the word "coerced" in G181 (potential colloquialism or error).
  - Assess contiguous context to determine if the acknowledgment regarding "rejection" in G181 actually addresses the house-visit concern raised in G042.

## Suitability
- **Private Schema Test**: Highly suitable. It successfully demonstrates the separation of observation from interpretation and tests the nuanced factual vocabulary.
- **Shareable Artifact**: Not suitable pending human review. The presence of raw swearing, vulnerability, and unresolved transcription ambiguities requires this pilot to remain at `privacy_level: private_evidence` and `coding_review_status: proposed`.

## Audit Table

| Claim | Supporting event | Evidence status | Action required |
| :--- | :--- | :--- | :--- |
| Alex "coerced" Naomi out of the apartment. | G181 | Ambiguous (potential transcription error or slang) | Audio review to confirm literal transcript wording and tone. |
| Alex's acknowledgment of upset ("rejection's not nice") is a direct response to the house-visit boundary. | G181 | Unclear | Audio review to assess contiguous context; maintain partly_addresses_prior_concern pending review. |
| The redacted excerpt accurately reflects the semantic core of the raw audio. | G042, G181 | Unverified | Audio review to compare literal spoken wording against the redacted text. |
