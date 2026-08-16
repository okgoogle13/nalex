# Next Candidate Pilot Loops

Based on a preliminary review of `events.jsonl`, the following two small loops are recommended for extraction into the semantic schema format.

## Candidate 1: Guilt and Reassurance (G148 - G092)
- **Events Involved**: G148 (Naomi), G149 (Naomi), G092 (Alex)
- **Interaction Type**: Repair-seeking / Reassurance
- **Why it is useful**: This loop tests the schema's ability to model an expression of guilt/fault ("actually it is my fault", "how can I help?") and a subsequent reassurance/de-escalation ("I mean, you know I'm kind of teasing... It's all good"). It provides a contrast to conflict-oriented loops, testing the `invites_closeness`, `acknowledges_impact_of_action`, and `accepts_repair` vocabularies.
- **Prerequisite Checks**: Confirm the exact wording against audio (flags indicate `txt_restored_20260802`), as the semantic distinction between genuine fault admission and defensive deflection relies entirely on tone.

## Candidate 2: Pingas/Money Dispute (G106 - G110 - G155)
- **Events Involved**: G106 (Alex), G110 (Naomi), G155 (Alex)
- **Interaction Type**: Factual contestation / Accountability
- **Why it is useful**: Tests the schema's ability to handle multi-turn factual disputes. Alex explains intent regarding drug splitting (G106), Naomi directly contests this account (G110: "That was your suggestion..."), and Alex concedes/clarifies his intent (G155: "Yeah, it was my suggestion... I'm not upset"). This will exercise `contests_stated_account` and `responds_to_concern_with_explanation_of_intent` across three turns.
- **Prerequisite Checks**: Ensure the boundary is contained strictly to the money/drugs split and doesn't overlap with unrelated intervening events. Audio review recommended for G110 due to very low speaker confidence (0.06).
