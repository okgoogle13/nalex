import json

with open('conflict_questions_annotated.json', 'r') as f:
    messages = json.load(f)

# Ensure controlled-vocabulary fields exist for all
for m in messages:
    if 'intent' not in m: m['intent'] = ""
    if 'loop_tag' not in m: m['loop_tag'] = ""
    if 'heat' not in m: m['heat'] = ""
    if 'risk' not in m: m['risk'] = ""
    if 'rhetorical' not in m: m['rhetorical'] = "N"

for m in messages:
    text = m['text']
    gu = False
    
    # 1. Are we in a weird place? 
    if "Are we in a weird place?" in text:
        gu = True
    # 9. Would you mind telling me what your questions were?
    elif "would you mind telling me what your questions were?" in text.lower():
        gu = True
    # 17. What things I did to make you feel like I was flirting
    elif "What things I did to make you feel like I was flirting" in text:
        gu = True
    
    # Repeated questions that are unresolved (No, but can you just answer my questions from earlier?)
    # "genuine_unanswered = false for rhetorical questions, blame questions, cornering questions, repeated pressure, or questions whose real function is accusation or escalation."
    # "If a question is asked again after an unsatisfactory answer, mark it as unresolved, but do not automatically mark it as genuine unless it still meets the definition above."
    
    m['genuine_unanswered'] = gu
    if 'why_it_matters' in m:
        m['notes'] = m.pop('why_it_matters')
    if 'notes' not in m:
        m['notes'] = ""

open_questions = [m['text'] for m in messages if m['genuine_unanswered']]

# Repeated rhetoricals / pressure questions
repeated_rhetoricals = [
    m['text'] for m in messages if not m['genuine_unanswered'] and (m.get('rhetorical') == 'Y' or m.get('risk') in ['repetitive', 'cornering'] or 'answer my questions' in m['text'].lower())
]

boundary_statements = [
    m['text'] for m in messages if m.get('intent') == 'boundary'
]

repair_attempts = [
    m['text'] for m in messages if m.get('intent') == 'repair'
]

escalation_points = [
    m['text'] for m in messages if m.get('risk') in ['explosive', 'loaded'] or (m.get('intent') == 'challenge' and m.get('risk') != 'repetitive')
]

unresolved_repeated = [
    m['text'] for m in messages if 'answer my questions' in m['text'].lower() or 'answer any of my questions' in m['text'].lower()
]

loop_drivers = [
    m['text'] for m in messages if m.get('loop_tag') in ['proof-loop', 'flirting-ambiguity-loop'] and m.get('intent') == 'challenge'
]

# De-duplicate
def dedup(lst): return list(dict.fromkeys(lst))
open_questions = dedup(open_questions)
repeated_rhetoricals = dedup(repeated_rhetoricals)
boundary_statements = dedup(boundary_statements)
repair_attempts = dedup(repair_attempts)
escalation_points = dedup(escalation_points)
unresolved_repeated = dedup(unresolved_repeated)
loop_drivers = dedup(loop_drivers)

summary = {
  "conversation_summary": {
    "dominant_loop": "Retrieval vs. Proof Deadlock",
    "core_problem": "One party repeatedly demands specific proof of intent (e.g. regarding flirting and avoidance) and the other refuses to supply or restate it, leading to character attacks. Accusatory questions are weaponized as pressure, while requests for concrete examples go unanswered.",
    "open_questions": open_questions,
    "repeated_rhetoricals": repeated_rhetoricals,
    "unresolved_repeated_questions": unresolved_repeated,
    "loop_drivers": loop_drivers,
    "boundary_statements": boundary_statements,
    "repair_attempts": repair_attempts,
    "escalation_points": escalation_points
  },
  "messages": messages
}

with open('conflict_questions_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

with open('conflict_questions_annotated.json', 'w') as f:
    json.dump(messages, f, indent=2)

print("Done v2")
