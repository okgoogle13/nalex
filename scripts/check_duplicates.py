import json
import re

with open('events.jsonl', 'r', encoding='utf-8') as f:
    events = [json.loads(line) for line in f]

old_events = [e for e in events if "summaryai_import" not in e.get("flags", [])]
new_events = [e for e in events if "summaryai_import" in e.get("flags", [])]

def normalize(text):
    return re.sub(r'[^a-z0-9]', '', text.lower())

old_texts = [normalize(e['txt']) for e in old_events]
new_texts = [normalize(e['txt']) for e in new_events]

duplicates = []
unique = []

for i, n_txt in enumerate(new_texts):
    if len(n_txt) < 20: 
        unique.append(new_events[i])
        continue
        
    is_dup = False
    for j, o_txt in enumerate(old_texts):
        if len(o_txt) < 20: continue
        
        if n_txt in o_txt or o_txt in n_txt:
            duplicates.append(new_events[i])
            is_dup = True
            break
            
    if not is_dup:
        unique.append(new_events[i])

print(f"Total new events: {len(new_events)}")
print(f"Duplicates found: {len(duplicates)}")
print(f"Unique events: {len(unique)}")

if unique:
    print("Sample unique events:")
    for u in unique[:5]:
        print(f"{u['t']} - {u['s']}: {u['txt']}")
