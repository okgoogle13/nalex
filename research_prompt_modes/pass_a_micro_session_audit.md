# Pass A: Micro-Session Audit

## Context
Use this for a specific excerpt, session, or short time window. 
*Note: Always apply the `shared_system_prompt.md` before executing this pass.*

## Task
Analyze the provided phase-constrained extract by applying two distinct sublenses:

### 1. Defense Marker Lens
- Identify candidate defense mechanisms for each participant (e.g., intellectualization, splitting, projection, withdrawal, defended invulnerability).
- For each defense, infer the plausible latent anxiety activated (e.g., dread of conflict, fear of abandonment), framed as a hypothesis.
- Describe the immediate conversational consequence (e.g., escalation, avoidance, exit) and link to existing findings.

### 2. Rupture/Repair Lens
- Identify structural turning points (TPs), explicitly stating how a defense mechanism catalyzed the rupture.
- Track shifts in tone (accusation, sarcasm), participation (silence, exit), and structure (monologues vs. short replies).
- Identify corresponding repair attempts (direct or structural) or avoidance responses.
- State whether the rupture was left unresolved and link to canonical findings.

### 3. Stance/Mirroring Note (Optional)
- Only when the excerpt clearly supports it, briefly note the dominant stance (e.g., explainer, minimizer) or significant shifts in pronoun usage and lexical mirroring.

## Output Format
Produce a chronological Markdown report for the session:

### Turning Point [N]: [Short Label]
**Phase / Session:** [e.g., Conflict, Session X (EIDs ...)]

- **Trigger:** [Verbatim quotes with timestamps/EIDs]
- **Defense & Anxiety (Lens 1):** [Candidate defense] -> [Hypothesized latent anxiety]. [Immediate relational effect].
- **Rupture/Repair Dynamics (Lens 2):** 
  - *Observable shifts:* [Tone, participation, pacing changes]
  - *Trajectory:* [Repair attempt, avoidance, or unresolved]
- **Stance/Mirroring (Optional):** [Notable shifts in pronoun/stance]
- **Link to Canonical Findings:** [e.g., "This withdrawal precipitates the 6.8-day silence"]
