import json

with open('events.jsonl', 'r', encoding='utf-8') as f:
    events = [json.loads(line) for line in f]

# Filter out the newly imported events
clean_events = [e for e in events if "summaryai_import" not in e.get("flags", [])]

with open('events.jsonl', 'w', encoding='utf-8') as f:
    for e in clean_events:
        f.write(json.dumps(e) + '\n')

print(f"Reverted! Removed {len(events) - len(clean_events)} events.")
