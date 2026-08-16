import json
import os
import sys

def get_event(eid, events_dict):
    event = events_dict.get(eid)
    if not event:
        print(f"Warning: event {eid} not found.")
        return None
        
    return {
        "event_ids": [eid],
        "speaker": event.get("s"),
        "timestamp": event.get("t"),
        "excerpt": event.get("txt"),
        "tags": [],
        "privacy_level": "standard",
        "evidence_status": "quoted",
        "source_type": "voice_transcript" if event.get("kind") == "audio" else "text_message"
    }

def main(loop_id, eids):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    events_file = os.path.join(base_dir, 'archive', 'events.jsonl.bak')
    
    events_dict = {}
    with open(events_file, 'r') as f:
        for line in f:
            if not line.strip(): continue
            ev = json.loads(line)
            events_dict[ev['eid']] = ev

    participants = set()
    events = []
    
    for eid in eids:
        if '-' in eid:
            prefix = eid[0]
            start = int(eid[1:4])
            end = int(eid[6:9])
            expanded = [f"{prefix}{str(i).zfill(3)}" for i in range(start, end + 1)]
            for expanded_eid in expanded:
                e = get_event(expanded_eid, events_dict)
                if e:
                    events.append(e)
                    participants.add(e["speaker"])
        else:
            e = get_event(eid, events_dict)
            if e:
                events.append(e)
                participants.add(e["speaker"])
            
    loop = {
        "interaction_loop_id": loop_id,
        "semantic_loop_label": loop_id.replace("_001", "").replace("loop_", "").replace("_", " ").title(),
        "participants": list(participants),
        "core_topic": "",
        "loop_start_event_id": eids[0],
        "loop_end_event_id": eids[-1],
        "events": events
    }
    
    out_file = os.path.join(base_dir, 'data', 'loops', f"{loop_id}.json")
    with open(out_file, 'w') as f:
        json.dump(loop, f, indent=2)
    print(f"Created {out_file}")

if __name__ == '__main__':
    loop_id = sys.argv[1]
    eids = sys.argv[2:]
    main(loop_id, eids)
