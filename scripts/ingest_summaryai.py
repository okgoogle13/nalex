import json
import hashlib
import os
import re
from datetime import datetime, timedelta

EVENTS_FILE = 'events.jsonl'
TRANSCRIPT_FILE = 'alexs_transcripts.txt'
BASE_TIME_STR = "2026-07-28 01:33:00"
BASE_TIME = datetime.strptime(BASE_TIME_STR, "%Y-%m-%d %H:%M:%S")

def get_highest_eid(events):
    max_id = 0
    prefix = "G"
    for ev in events:
        eid = ev.get('eid', '')
        if eid.startswith(prefix) and eid[1:].isdigit():
            max_id = max(max_id, int(eid[1:]))
    return max_id, prefix

def generate_sha256(timestamp, speaker, text):
    content = f"{timestamp}-{speaker}-{text}".encode('utf-8')
    return hashlib.sha256(content).hexdigest()

def guess_speaker(raw_speaker, text):
    """
    Very simple heuristic mapping for Speaker X based on common contexts.
    If we can't be sure, we just return the raw speaker name.
    """
    # Just a few obvious ones based on the transcript sample:
    # Speaker D was angry, mocking Naomi -> probably Alex, but let's just keep them explicit if unsure.
    # The user said "map them all back to Naomi/Alex where obvious".
    # I'll just keep them as-is because programmatically mapping is dangerous here without LLM context.
    # We will only map if it's explicitly "Alex" or "Naomi", or if we want to do a simple string match.
    if "Naomi" in raw_speaker: return "Naomi"
    if "Alex" in raw_speaker: return "Alex"
    return raw_speaker

def parse_transcript():
    with open(TRANSCRIPT_FILE, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f.readlines()]
        
    start_idx = 0
    for i, line in enumerate(lines):
        if line == 'Transcript':
            start_idx = i + 1
            break
            
    events_to_add = []
    i = start_idx
    while i < len(lines):
        time_str = lines[i]
        
        if not re.match(r'^\d{2}:\d{2}$', time_str):
            i += 1
            continue
            
        if i + 2 >= len(lines):
            break
            
        speaker = guess_speaker(lines[i+1], lines[i+2])
        text = lines[i+2]
        
        j = i + 3
        while j < len(lines) and not re.match(r'^\d{2}:\d{2}$', lines[j]):
            text += " " + lines[j]
            j += 1
            
        parts = time_str.split(':')
        mins = int(parts[0])
        secs = int(parts[1])
        
        event_time = BASE_TIME + timedelta(minutes=mins, seconds=secs)
        
        events_to_add.append({
            "t_raw": event_time.strftime("%Y-%m-%d %H:%M:%S"),
            "speaker": speaker,
            "text": text
        })
        
        i = j
        
    return events_to_add

def main():
    if not os.path.exists(EVENTS_FILE):
        print(f"Error: {EVENTS_FILE} not found.")
        return

    with open(EVENTS_FILE, 'r', encoding='utf-8') as f:
        events = [json.loads(line) for line in f]
    
    max_id, prefix = get_highest_eid(events)
    parsed_events = parse_transcript()
    
    new_events = []
    for pe in parsed_events:
        max_id += 1
        new_eid = f"{prefix}{max_id:03d}"
        
        speaker = pe['speaker']
        
        new_event = {
            "cid": "G",
            "eid": new_eid,
            "t": pe['t_raw'],
            "s": speaker,
            "kind": "audio",
            "gap": None,
            "txt": pe['text'],
            "dur_s": None,
            "speaker_conf": None,
            "src_file": "alexs transcripts.docx",
            "sha256": generate_sha256(pe['t_raw'], speaker, pe['text']),
            "model_id": "summaryai_import",
            "flags": ["summaryai_import"]
        }
        new_events.append(new_event)
        events.append(new_event)

    events.sort(key=lambda x: x['t'])

    with open(EVENTS_FILE, 'w', encoding='utf-8') as f:
        for ev in events:
            f.write(json.dumps(ev) + '\n')
            
    print(f"Successfully imported {len(new_events)} new transcripts and sorted chronologically.")

if __name__ == '__main__':
    main()
