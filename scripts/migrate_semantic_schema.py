import json
import os
import glob

def flatten_event(event):
    source = event.get('source', {})
    observation = event.get('observation', {})
    artifact_controls = event.get('artifact_controls', {})
    evidence_integrity = event.get('evidence_integrity', {})
    
    # Extract tags from observable_moves
    tags = []
    for move in observation.get('observable_moves', []):
        if 'code' in move:
            tags.append(move['code'])
            
    # Format the evidence status based on Plan 3
    alignment = evidence_integrity.get('claim_to_excerpt_alignment')
    evidence_status = "unverified"
    if alignment in ["high", "medium"]:
        evidence_status = "quoted"
        
    flat_event = {
        "event_ids": source.get("source_event_ids", []),
        "speaker": source.get("speaker"),
        "timestamp": source.get("timestamps", [""])[0] if source.get("timestamps") else None,
        "excerpt": source.get("minimal_redacted_excerpt"),
        "tags": tags,
        "privacy_level": artifact_controls.get("privacy_level", "standard"),
        "evidence_status": evidence_status,
        "source_type": source.get("source_quality", "unknown")
    }
    
    return flat_event

def flatten_loop(loop):
    flat_loop = {
        "interaction_loop_id": loop.get("interaction_loop_id"),
        "semantic_loop_label": loop.get("semantic_loop_label"),
        "participants": loop.get("participants", []),
        "core_topic": loop.get("core_topic"),
        "loop_start_event_id": loop.get("loop_start_event_id"),
        "loop_end_event_id": loop.get("loop_end_event_id"),
        "events": [flatten_event(e) for e in loop.get("events", [])]
    }
    return flat_loop

def migrate():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    loops_dir = os.path.join(base_dir, 'data', 'loops')
    canonical_file = os.path.join(loops_dir, 'canonical_loop_records.json')
    
    # 1. Process canonical records
    if os.path.exists(canonical_file):
        with open(canonical_file, 'r') as f:
            canonical_records = json.load(f)
            
        for loop in canonical_records:
            flat_loop = flatten_loop(loop)
            loop_id = flat_loop['interaction_loop_id']
            out_file = os.path.join(loops_dir, f"{loop_id}.json")
            with open(out_file, 'w') as f:
                json.dump(flat_loop, f, indent=2)
            print(f"Migrated {loop_id} from canonical records.")
            
    # 2. Process pilot proposals
    pilots_dir = os.path.join(loops_dir, 'pilots')
    for pilot_file in glob.glob(os.path.join(pilots_dir, '*.proposed.json')):
        with open(pilot_file, 'r') as f:
            data = json.load(f)
            
        loop_data = data.get("loop") if "loop" in data else data
        # the pilot structure puts 'events' alongside 'loop', wait let me check the file structure
        # wait, the file has "loop" and "events" at the root level!
        if "loop" in data and "events" in data:
            loop_data["events"] = data["events"]
            
        flat_loop = flatten_loop(loop_data)
        loop_id = flat_loop.get('interaction_loop_id')
        if not loop_id:
            print(f"Failed to find interaction_loop_id in {pilot_file}")
            continue
        out_file = os.path.join(loops_dir, f"{loop_id}.json")
        with open(out_file, 'w') as f:
            json.dump(flat_loop, f, indent=2)
        print(f"Migrated {loop_id} from pilots.")

if __name__ == '__main__':
    migrate()
