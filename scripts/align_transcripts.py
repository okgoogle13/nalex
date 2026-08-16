import json
import re
import difflib

# 1. Load canonical events for the conflict
with open('events.jsonl', 'r', encoding='utf-8') as f:
    events = [json.loads(line) for line in f]

# The conflict was roughly June 26-27. Let's grab all events from June 26 23:00 to June 27 03:00
target_events = []
for e in events:
    if "2026-06-26 23:" <= e['t'] or e['t'].startswith("2026-06-27"):
        # Just grab the core conflict window
        if e['t'] < "2026-06-27 10:00:00":
            target_events.append(e)

# 2. Load Alex's transcript
with open('alexs_transcripts.txt', 'r', encoding='utf-8') as f:
    lines = [line.strip() for line in f.readlines()]
start_idx = 0
for i, line in enumerate(lines):
    if line == 'Transcript':
        start_idx = i + 1
        break

alex_events = []
i = start_idx
while i < len(lines):
    time_str = lines[i]
    if not re.match(r'^\d{2}:\d{2}$', time_str):
        i += 1
        continue
    if i + 2 >= len(lines): break
    speaker = lines[i+1]
    text = lines[i+2]
    j = i + 3
    while j < len(lines) and not re.match(r'^\d{2}:\d{2}$', lines[j]):
        if lines[j]:
            text += " " + lines[j]
        j += 1
    alex_events.append({"time": time_str, "speaker": speaker, "txt": text})
    i = j

# 3. Alignment
def normalize(t):
    return re.sub(r'[^a-z0-9]', '', t.lower())

# Build lists for difflib
canon_texts = [normalize(e.get('txt', '')) for e in target_events]
alex_texts = [normalize(a['txt']) for a in alex_events]

# We want to find which chunks align. Since alex's events might be split differently, 
# a straight sequence matcher might be tricky, but let's try.
# Actually, let's just print a timeline based on text searches.

results = []
for a in alex_events:
    n_a = normalize(a['txt'])
    if len(n_a) < 10:
        continue
    
    match_idx = -1
    for idx, c in enumerate(canon_texts):
        if n_a in c or c in n_a or difflib.SequenceMatcher(None, n_a, c).ratio() > 0.8:
            match_idx = idx
            break
            
    if match_idx != -1:
        a['matched_canon'] = target_events[match_idx]
    else:
        a['matched_canon'] = None

with open('alignment_report.txt', 'w', encoding='utf-8') as f:
    for a in alex_events:
        if a.get('matched_canon'):
            f.write(f"MATCH: {a['time']} {a['speaker']}\n")
            f.write(f"  ALEX:  {a['txt'][:100]}...\n")
            f.write(f"  NAOMI: {a['matched_canon']['txt'][:100]}...\n")
        else:
            f.write(f"MISSING FROM NAOMI: {a['time']} {a['speaker']}\n")
            f.write(f"  ALEX:  {a['txt']}\n")

# Now check missing from Alex
alex_all_text = "".join(alex_texts)
with open('alignment_report.txt', 'a', encoding='utf-8') as f:
    f.write("\n\n--- MISSING FROM ALEX ---\n")
    for idx, c in enumerate(canon_texts):
        if len(c) > 20 and c not in alex_all_text:
            # Maybe fuzzy match
            if not any(difflib.SequenceMatcher(None, a, c).ratio() > 0.8 for a in alex_texts):
                e = target_events[idx]
                f.write(f"MISSING FROM ALEX: {e['t']} {e.get('s', '?')}\n")
                f.write(f"  NAOMI: {e.get('txt', '')[:100]}...\n")

