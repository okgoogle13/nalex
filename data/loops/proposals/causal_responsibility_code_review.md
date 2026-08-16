# Controlled-Vocabulary Design Review  
## Candidate Code: Causal-Responsibility Statement

**File:** `./data/semantic_schema/proposals/causal_responsibility_code_review.md`  
**Review date:** 2026-08-14  
**Reviewer:** Antigravity (read-only design-review pass)  
**Authority basis:** `claude.md` (approved mandate proxy; `AGENTS.md` does not exist)  
**Schema version reviewed:** `nalex_semantic_schema_v2.md`  
**Triggering pilot:** `pilots/loop_reassurance_001.proposed.json` — G148 seq 2 (removed, pending vocabulary decision H-05)

> **Status: Recommendation only. No schema change is approved by this document.**  
> This review must not be treated as evidence of any participant's intent, sincerity, remorse, or accountability quality.  
> All examples are invented and neutral. No pilot excerpts are reproduced.

---

## 1. Distinguishing Causal-Responsibility Statements from Adjacent Codes

The existing vocabulary and the proposed code each describe a distinct observable move. The following table defines the boundaries precisely.

| Code / Concept | Core observable move | What it does NOT require | Key test |
|---|---|---|---|
| **Proposed: causal-responsibility statement** | Speaker explicitly states that they caused or are at fault for a specific event or outcome | Regret, apology, explanation, or repair offer | Does the utterance name a causal agent and a specific event? |
| `apologises` | Speaker expresses general regret or sorrow | Specifying fault, an outcome, or a causal link | Is the utterance primarily a regret expression (e.g., "I'm sorry")? |
| `acknowledges_impact_of_action` | Speaker validates how an action affected the other person | Claiming causation or fault | Does the utterance focus on the other person's experience rather than who caused it? |
| **Intent explanation** *(maps to `responds_to_concern_with_explanation_of_intent`)* | Speaker describes their internal rationale | Admitting fault or outcome | Does the utterance explain why the speaker acted, rather than whether they caused harm? |
| **Repair offer** *(maps to `offers_specific_repair_step`)* | Speaker proposes a concrete remedial action | Any fault claim | Does the utterance propose a future action? |
| **Self-blame / global self-criticism** *(no current code)* | Speaker makes a sweeping negative self-evaluation unconnected to a specific event | A named specific event or outcome | Is the statement general ("I'm terrible at this") rather than event-specific ("I caused X")? |

### Distinguishing notes

**Causal-responsibility vs. apology.** An apology ("I'm sorry") expresses regret without necessarily claiming causation. A fault admission ("that was my fault") claims causation without necessarily expressing regret. They can co-occur, but neither entails the other. Coding both requires independent excerpt support for each.

**Causal-responsibility vs. impact acknowledgement.** Impact acknowledgement focuses on the effect felt by the other person ("I can see that really hurt you"). A causal-responsibility statement focuses on who caused what ("I broke it"). The locus of the statement is different: other-focused vs. event-causal.

**Causal-responsibility vs. intent explanation.** Explaining intent ("I didn't mean to cause that") is not the same as admitting causation ("I did cause that"). Intent explanations may be offered alongside, before, or instead of a fault admission and must be coded separately.

**Causal-responsibility vs. repair offer.** A repair offer is forward-looking ("I'll fix it"). A fault admission is backward-looking ("I caused it"). They can appear in the same utterance; each requires independent excerpt support.

**Causal-responsibility vs. self-blame/global self-criticism.** Self-blame involves a diffuse, unanchored negative self-evaluation ("I always mess things up"). A causal-responsibility statement is event-specific and falsifiable ("I left the window open and it flooded"). The specificity criterion is the key distinguisher.

---

## 2. Assessment of the Candidate Name `states_causal_responsibility`

| Criterion | Assessment |
|---|---|
| **Precise** | Adequate. The name correctly targets the observable act (stating) and the semantic content (causal responsibility). It does not collapse into apology, impact, or intent. Minor precision risk: "causal responsibility" spans two concepts (causation and moral responsibility) that may not always co-occur in a statement. See misuse risk below. |
| **Neutral** | Yes. The name assigns no valence, no sincerity judgment, no evaluation of accountability quality. It describes a linguistic act, not a relational outcome. |
| **Observable** | Yes. The trigger is the presence of an explicit statement in the transcript — no inference about speaker state is required to apply the code. The coding rationale should quote the specific clause. |
| **Reusable across cases** | Yes. Fault admissions appear in many relational contexts and loop types. The code is not specific to apology sequences, conflict sequences, or repair arcs. |

**Identified precision gap.** "Causal responsibility" conflates two separable claims: (a) "I caused X" (causal attribution) and (b) "I am at fault for X" (moral responsibility). In the triggering event, both appear in the same clause. In other cases, a speaker may say "I caused X" without claiming fault, or claim fault without specifying causation. The code definition should clarify whether it applies to either or both, and whether the specificity criterion (named event or outcome) is required. This is a definition-drafting matter, not a reason to reject the code name.

---

## 3. Alternative Name Proposals

Three alternatives are proposed. Each is evaluated independently; they are not ranked.

---

### 3.1 `attributes_fault_to_self`

**Definition:**  
Speaker explicitly assigns fault, blame, or causal responsibility for a specific named event or outcome to themselves.

**Inclusion criteria:**
- An explicit first-person fault or blame claim is present in the text.
- The claim is anchored to a specific event, action, or outcome (not a global self-evaluation).
- The statement is made by the speaker about their own role.

**Exclusion criteria:**
- Rhetorical or sarcastic fault admissions where context clearly signals non-literal intent (flag `requires_audio_review: true` and defer coding).
- General self-criticism without event specification ("I'm always to blame for everything").
- Statements where fault is assigned to circumstances, not the self ("the pipe was already weak").
- Apologies, impact acknowledgements, intent explanations, and repair offers coded separately — co-occurrence does not merge them.

**Neutral example:**  
Speaker A says: "That leak — yeah, I didn't tighten the fitting properly. That's on me."  
The statement names a specific action (not tightening the fitting) and assigns fault to the speaker. Code applies.

**Non-example:**  
Speaker A says: "I'm sorry this happened to you."  
Expresses regret; does not claim personal causation of a specific event. Code does not apply; `apologises` is the correct code.

**Likely misuse risk:**  
Coders may apply this code to rhetorical or emphatic fault language ("oh sure, blame me for everything") where context signals sarcasm rather than genuine admission. The inclusion criterion requiring event-specificity partially guards against this, but transcript-only coding will remain vulnerable without audio review where tone is material.

---

### 3.2 `states_specific_causal_fault`

**Definition:**  
Speaker explicitly states that they caused or were at fault for a specific, named event or outcome, naming both the cause (themselves) and the effect (the event or outcome).

**Inclusion criteria:**
- The utterance contains both a self-referential fault or causation claim and a reference to a specific event or outcome.
- Both elements (self as causal agent + named event/outcome) must be present in the excerpt — not reconstructed from context.
- The statement is in the declarative, not the conditional or rhetorical mode.

**Exclusion criteria:**
- Statements that name causation but not fault ("I did it, but it was the right thing to do").
- Apologies, impact acknowledgements, and repair offers coded separately.
- Self-blame without event specificity.
- Utterances where the fault claim is embedded in a conditional or hypothetical ("if that was my fault, then...").

**Neutral example:**  
Speaker B says: "I know I sent that message at the wrong time — that was my mistake."  
Names the event (the message) and assigns fault to self. Code applies.

**Non-example:**  
Speaker B says: "I could have handled things better."  
Modal phrasing without event specificity and without an explicit fault claim. Closer to self-criticism than a fault admission. Code does not apply.

**Likely misuse risk:**  
The dual-element requirement (self + named event) may lead coders to over-specify the evidence requirement and under-apply the code where the named event is clearly implied by context but not restated in the clause. Coding rationale must document what excerpt language establishes each element.

---

### 3.3 `claims_causal_agency`

**Definition:**  
Speaker explicitly positions themselves as the cause of a specific event or outcome, whether or not moral fault is expressed.

**Inclusion criteria:**
- Speaker names themselves (explicitly or through first-person pronoun) as the cause of an identified event or outcome.
- Causation is stated, not implied.
- Applies whether or not the speaker uses the language of fault, blame, or regret.

**Exclusion criteria:**
- Statements of intent ("I meant to do X") without a causation claim.
- Statements that locate cause externally ("the pipe was thin").
- Hypotheticals and conditionals.
- Global self-criticism without event reference.

**Neutral example:**  
Speaker C says: "I'm the one who left the door unlocked."  
First-person causal claim, named event. Code applies whether or not the speaker adds "I'm sorry" or "it was fine."

**Non-example:**  
Speaker C says: "That window has been broken for months."  
Attributes a state to an object, not causation to the self. Code does not apply.

**Likely misuse risk:**  
By omitting the word "fault," this name is more neutral but may cause confusion when a statement attributes causation without any self-criticism ("I did that intentionally and I'd do it again"). The code would technically apply, but coders might not recognize it without clear guidance. The name may also blur the boundary with `responds_to_concern_with_explanation_of_intent` where intent explanations implicitly claim causal agency. The definition must explicitly exclude intent-without-fault statements.

---

## 4. Recommendation

**Recommended action: Approve a new code.**

**Recommended code name: `states_causal_responsibility`** (the candidate name), with a revised definition.

### Rationale

1. **A real gap exists.** The triggering event in `loop_reassurance_001` is correctly identified in the audit as uncoded. The statement "Actually, it is my fault" is neither `acknowledges_impact_of_action` (which requires impact-on-other-person focus), nor `apologises` (which requires a regret expression), nor any other current vocabulary code. The gap is genuine.

2. **The candidate name is adequate.** It is neutral, observable, and reusable. The precision gap (causation vs. moral responsibility) is addressable in the definition rather than the name. None of the three alternatives are clearly superior: `attributes_fault_to_self` introduces "blame" language with slightly more valence; `states_specific_causal_fault` is verbose and the dual-element requirement may over-constrain; `claims_causal_agency` strips "fault" language, which separates the code from the common case it is intended to cover and risks boundary confusion with intent explanations.

3. **The code belongs in the observation layer only.** See §5.

4. **Revised definition to accompany approval (proposed):**

> **`states_causal_responsibility`** — Speaker explicitly states that they caused or were at fault for a specific named event or outcome. Requires: (a) first-person causal or fault claim, and (b) reference to a specific event or outcome (not a global self-evaluation). Code applies regardless of whether regret, apology, intent explanation, or repair offer co-occurs; each of those moves must be coded separately from independent excerpt support. Does not require audio-confirmed sincerity; where tone is material to whether the statement is literal, set `requires_audio_review: true`.

---

## 5. Layer Assignment

**Recommendation: Observation layer only.**

| Layer | Assessment |
|---|---|
| **Observation layer** | Yes. The code describes an externally verifiable linguistic act (an explicit statement in the transcript). It does not require inference about speaker state, motive, or relational outcome. It is appropriately placed alongside existing observation-layer codes such as `acknowledges_impact_of_action` and `apologises`. |
| **Interpretation layer** | No. The statement is factual and text-verifiable. Moving it to the interpretation layer would incorrectly imply that the analyst is inferring something rather than recording a stated fact. |

The sincerity, quality, or relational effect of a causal-responsibility statement is an interpretive question. If a coder wishes to record a reading about what the admission *means* (e.g., possible deflection, possible genuine accountability), that reading belongs in `interpretation_tags` under an existing or future interpretation-vocabulary entry — it must not be embedded in the observation code itself.

---

## 6. Primary Misuse Risk

**The single greatest misuse risk is reading sincerity or accountability quality from the code.**

A code named `states_causal_responsibility` describes only the linguistic surface: the speaker said words that claim causation or fault for a specific event. It does not establish that the admission was sincere, that the causal claim was accurate, that accountability followed, or that repair was attempted or accepted. Any downstream analysis, visualization, or narrative that treats the code as evidence of genuine accountability or remorse has moved from observation to interpretation without authorization.

The definition, coding rationale guidance, and any schema documentation should explicitly repeat this boundary.

---

*This review is a recommendation only. No entry may be added to `nalex_semantic_schema_v2.md` without explicit human approval. No pilot event may be recoded on the basis of this document alone.*
