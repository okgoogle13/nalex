# Source Confidence Calibration Review

## Corpus profile

An analysis of the raw `events.jsonl` corpus (378 total events) reveals the following distribution for `speaker_conf`:

- **Total events:** 378
- **Null `speaker_conf` count:** 217
- **Valid `speaker_conf` count:** 161
- **Minimum:** 0.0665
- **Maximum:** 0.6622
- **Median:** 0.4234
- **Quartile 1 (25th percentile):** 0.3520
- **Quartile 3 (75th percentile):** 0.5153
- **Model distribution:** `faster-whisper/large-v3` (206 events), `faster-whisper/medium` (95 events)

*Note: A significant portion of events (217) have a null `speaker_conf`, which includes direct text events or older transcriptions lacking confidence scores.*

## What speaker_conf appears to represent

The precise technical semantics of speaker_conf are not established from accessible project materials. It is retained as an uninterpreted source-system field and must not be treated as a validated probability of speaker identity, transcript accuracy, factual accuracy, or intent.

## Current schema-label alignment

A review of the event IDs in `canonical_loop_records.json` and `loop_reassurance_001.proposed.json` alongside the raw `events.jsonl` data shows:
- **G092** (`speaker_conf`: ~0.526) mapped to "medium".
- **G147** (`speaker_conf`: ~0.292) mapped to "low".
- **G148** (`speaker_conf`: ~0.371, `txt_restored_20260802`) mapped to "low".
- **G149** (`speaker_conf`: ~0.453) mapped to "medium".

Currently, the qualitative "high", "medium", and "low" schema labels appear to be derived from a mixture of the raw numeric `speaker_conf` score and ad-hoc analyst judgment (e.g., downgrading restored text to "low" despite a score that might otherwise border on medium). There is no documented, formalized threshold.

## Exploratory corpus distribution only

Quartile bands may describe relative positions within this corpus, but they do not establish qualitative confidence levels and must not be used as automatic pilot-eligibility thresholds.

Direct-text records may support source/account provenance only where that provenance is documented. Speaker identity remains as-recorded, uncertain, human-confirmed, or not-assessed; it is not automatically upgraded by message format.

## Independent source-quality flags

Source-quality confidence (e.g., `source_quality`, `requires_audio_review`, `unverified_or_ambiguous_claims`) must remain independent from `speaker_confidence`. A high `speaker_conf` from the model does not guarantee literal transcript accuracy and cannot clear a `requires_audio_review` flag.

## Non-numeric source-review policy

- No restored text unless a human source review verifies the exact retained excerpt.
- Every coded event must retain source-event ID, timestamp, speaker as recorded, source type, and material source limitations.
- Any uncertainty that could change the observation code or loop boundary requires human source review before private-canonical admission.
- Private-proposed records may retain unresolved uncertainty only when their display mode is private_only and the uncertainty is explicit.
- Raw speaker_conf may be recorded but cannot by itself pass or fail eligibility.

## Retrospective qualification test

Testing the proposed eligibility policy against the existing proposed candidates:

- **Candidate 1 (Loop House Visit 001 - G042, G181):** Both events currently have `requires_audio_review: true`. 
- **Candidate 2 (Loop Reassurance 001 - G148, G149, G092):** G148 has a `txt_restored_20260802` flag and all events currently have `requires_audio_review: true`.

**Conclusion:** No currently reviewed candidate is approved as a clean private pilot. This result arises from documented restoration, incomplete context, and unresolved source-review requirements—not from a validated numerical confidence threshold. A broader candidate search or human source review would be required to determine whether another candidate is eligible.

## Recommended future source assessment

{
  "source_provenance": "documented | partial | unknown",
  "speaker_identity_status": "as_recorded | human_confirmed | uncertain | not_assessed",
  "transcript_status": "direct_text | automated_transcript | restored_text | unknown",
  "source_review_status": "unreviewed | human_source_reviewed | audio_reviewed",
  "raw_speaker_conf": "number | null",
  "raw_speaker_conf_semantics": "not_established",
  "coding_eligibility": "private_proposed_only | review_required | excluded"
}

This is a recommendation for future schema design only, not an approved schema change.
