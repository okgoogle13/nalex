# Layer C: Repair Protocol and Intervention

This mode is explicitly designed to model **behavioral intervention strategies** based on the "Victim’s Perspective of Forgiveness Seeking Behaviors After Transgressions."

## 1. Core Clinical Inference: The Two-Lane Repair Protocol

The core goal of this protocol is to adapt the four-part forgiveness model into a mutual accountability structure when victim/offender roles alternate. 

### Key Principles
- **Evaluate from the victim's perspective:** Is the repair behavior effective for safety, meaning, and forgiveness?
- **Separate grievances:** Do not globalize blame or victimhood across incidents. Analyze each incident separately.
- **Evidence of change:** Require evidence of change before reconciliation for severe, intentional, or repeated harms.
- **No simultaneous accountability:** Do not seek accountability from the other person while being held accountable. Separate grievances into different "lanes."
- **Constructive vs. Diverting:** Distinguish constructive repair (apology, restorative action, caring) from diverting strategies (excuses, minimization, blame shift, avoidance, justification). Counter-accusation, self-defense, or role reversal during the other’s repair process = diversion.

### Lane A: Alex is the current offender, Naomi is the current victim
**Goal:** Keep Alex out of defensive diversion and move him into constructive repair behaviors.

1. **Name the lane:**
   - “Right now I want to stay with your experience of this incident.”
   - “In this conversation, I am focusing on what I did and how it affected you.”
2. **Deliver an apology with responsibility, not self-protection:**
   - “I did X.”
   - “I can see it hurt you in Y way.”
   - “I take responsibility for that.”
   - *Avoid:* “but,” “you also,” “I only did it because,” “it wasn’t that bad.”
3. **Offer restorative action:**
   - “What I will change is Z.”
   - “The safeguard I will put in place is A.”
   - “You should be able to observe this change by B.”
4. **Add relational caring:**
   - “I care about your sense of safety with me.”
   - “I want to rebuild trust, not just end the argument.”
5. **Reserve Alex’s grievance for a later lane:**
   - “I also have my own hurt, and I want us to address that separately so it doesn’t take away from repairing this moment first.”

**Lane A Prohibited Moves (Diverting Strategies):**
- “You made me do it.” / “You’re overreacting.” / “That’s not what happened.” / “You do the same thing to me.” / “Can we stop talking about this?”

### Lane B: Alex is the current victim, Naomi is the current offender
**Goal:** Give Alex a structured path to seek accountability without collapsing into counterattack or global blame.

1. **Name the incident specifically:**
   - “I want to talk about one specific event where I felt hurt.”
   - “I want us to stay with this episode rather than all of our history.”
2. **State impact without accusation inflation:**
   - “When X happened, I felt dismissed / blamed / unsafe / unseen.”
   - “The part that affected me most was Y.”
3. **Request accountability in the same four-factor language:**
   - *Apology request:* “I need clear acknowledgment of what happened without minimising it.”
   - *Restorative request:* “I need to know what will be different next time.”
   - *Caring request:* “I need signs that my pain matters to you, not just problem-solving.”
   - *Anti-diversion request:* “I need us not to switch immediately into my faults while I am trying to explain this.”
4. **Define what accountability would look like:**
   - “For me to feel this is addressed, I need A, B, and C.”
5. **Avoid global identity claims:**
   - *Prefer:* “In this incident I felt victimized by what happened.”
   - *Avoid:* “I am the real victim in this relationship.”

### Decision Rule for Mutual Accountability
- If the conversation started because Naomi is addressing Alex’s harmful behavior, Alex’s hurt can be acknowledged but should be scheduled into Lane B later.
- If the conversation started because Alex is disclosing his own hurt, Naomi’s accountability should be assessed using the same four-factor structure.
- If both are highly activated, pause the conversation and require each partner to write a one-incident statement before discussion resumes.

---

## 2. Analysis Heuristics for Case Formulation

**Heuristic 1: Distinguish grievance from diversion**
Ask of every Alex statement: Is this helping Naomi feel understood, safer, or more able to forgive? Or is this mainly protecting Alex from shame, blame, or powerlessness? If mainly self-protective in Naomi’s repair lane, classify as diversion.

**Heuristic 2: Match repair depth to offense profile**
Use three modifiers: Severity, Intentionality, Frequency. As these increase, apology-only repair becomes less sufficient and restorative action becomes more central.

**Heuristic 3: Evaluate accountability symmetry across time, not within a single exchange**
Healthy fairness does not require both partners to be held equally accountable in the same 10-minute conversation. Fairness can be achieved across a sequence of discrete, role-specific repair episodes.

**Heuristic 4: Watch for pseudo-mutuality**
A common failure mode is surface-level “we both hurt each other” language that appears balanced but functionally erases the immediate victim’s experience. Pseudo-mutuality often masks the use of a diverting strategy.

---

## 3. High-Value Takeaways for the Analysis Stack

- The most important unit is the **incident**, not the relationship-wide identity claim.
- Alex’s “I am a victim too” content should be modeled as either a valid separate-lane grievance or a same-lane diverting maneuver; that distinction is analytically central.
- A fair system does not equalise blame in real time, but allocates structured accountability to each person in the correct lane over time.
- When harm is repeated, severe, or seen as intentional, your analytical weighting should shift toward evidence of restorative action rather than rhetorical apology.
- Naomi’s accountability can be fully preserved without weakening Alex’s accountability by using role-specific, time-separated repair sequences.

---

## 4. Suggested Coding Schema for Gemini Ingestion

```yaml
case_model:
  source_article: "Victim’s Perspective of Forgiveness Seeking Behaviors After Transgressions"
  source_id: "page:1"
  framework:
    constructive_behaviors:
      - apology
      - restorative_action
      - relational_caring
    defensive_behaviors:
      - diverting_strategy
    offense_modifiers:
      - severity
      - intentionality
      - frequency
    forgiveness_outcomes:
      - avoidance
      - revenge
      - benevolence
  incident_unit:
    id: string
    date_or_relative_time: string
    current_victim: [alex, naomi, mixed, unclear]
    current_offender: [alex, naomi, mixed, unclear]
    severity: low|moderate|high
    intentionality: low|moderate|high
    frequency: one_off|repeated|chronic
    alex_statements:
      - text: string
        labels: [apology, restorative_action, relational_caring, diverting_strategy, neutral]
        rationale: string
    naomi_statements:
      - text: string
        labels: [apology, restorative_action, relational_caring, diverting_strategy, neutral]
        rationale: string
    lane_assignment:
      active_lane: lane_a_or_lane_b
      lane_rationale: string
    observed_effects:
      naomi_avoidance: decrease|no_change|increase|unknown
      naomi_revenge: decrease|no_change|increase|unknown
      naomi_benevolence: decrease|no_change|increase|unknown
      alex_avoidance: decrease|no_change|increase|unknown
      alex_revenge: decrease|no_change|increase|unknown
      alex_benevolence: decrease|no_change|increase|unknown
    analyst_notes:
      - string
```

---

## 5. Prompt Templates for Gemini 3.1 Pro

### Prompt 1: Incident classification
```xml
<task>
You are analyzing a relationship incident using a victim-perspective forgiveness-seeking framework. 
1. Identify who is the current victim and current offender in this specific incident. 
2. Classify each relevant statement as apology, restorative_action, relational_caring, diverting_strategy, or neutral. 
3. Flag whether Alex’s claim of victimhood is being expressed as a separate grievance or as a diverting strategy inside Naomi’s repair lane. 
4. Rate severity, intentionality, and frequency from the text only. 
5. Infer likely effects on avoidance, revenge, and benevolence. 
6. Output JSON only. 
</task>
<rule>
Do not collapse the whole relationship into one victim/offender narrative. Analyze this incident discretely.
</rule>
```

### Prompt 2: Accountability balancing
```xml
<task>
Given the incident analysis, determine whether fairness should be pursued:
- within the current conversation, or
- across separate repair lanes.
</task>
<guidance>
Prefer separate repair lanes when the currently accountable partner is trying to introduce their own grievance in a way that functions as excuse, minimization, blame shift, or role reversal. 
</guidance>
<output>
Return:
- recommended lane
- evidence phrases
- risk of diversion
- next best intervention script
</output>
```

### Prompt 3: Script generation
```xml
<task>
Generate two outputs:
1. A non-diverting script Alex can use if Naomi is the current victim.
2. A concise accountability request Alex can use if he is the current victim.
</task>
<constraints>
- No blame-shifting.
- No minimization.
- No mutualizing language inside the wrong lane.
- Include one apology/restorative/caring component where relevant.
- Keep each script under 120 words.
</constraints>
```

---

## 6. Compact Rules Engine

```json
{
  "rules": [
    { 
      "id": "separate-lanes", 
      "if": "speaker_is_current_offender AND introduces_own_grievance", 
      "then": "classify_as_potential_diversion_and_schedule_separate_lane" 
    },
    { 
      "id": "high-severity-repair", 
      "if": "severity=high OR intentionality=high OR frequency=chronic", 
      "then": "require_restorative_action_not_just_apology" 
    },
    { 
      "id": "constructive-cluster", 
      "if": "statement_contains_responsibility + impact_acknowledgment + change_plan", 
      "then": "classify_constructive_repair" 
    },
    { 
      "id": "diverting-cluster", 
      "if": "statement_contains_excuse OR minimization OR blame_shift OR avoidance OR role_reversal", 
      "then": "classify_diverting_strategy" 
    },
    { 
      "id": "fairness-over-time", 
      "if": "both_partners_have_valid_grievances", 
      "then": "sequence_accountability_across_incidents_not_simultaneously" 
    }
  ]
}
```
