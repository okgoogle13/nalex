import os
import json
import hashlib

def get_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

events = []
with open("data/raw/events.jsonl") as f:
    for line in f:
        if line.strip():
            events.append(json.loads(line))

existing_files = set()
for ev in events:
    if "src_file" in ev:
        existing_files.add(os.path.basename(ev["src_file"]))
    if "media" in ev and ev["media"]:
        for m in ev["media"]:
            if "filename" in m:
                existing_files.add(os.path.basename(m["filename"]))
            if "file_path" in m:
                existing_files.add(os.path.basename(m["file_path"]))

extracted_dir = "data/audio/"
candidates = []
for f in os.listdir(extracted_dir):
    if f.startswith("._") or f.endswith(".txt"): continue
    path = os.path.join(extracted_dir, f)
    size = os.path.getsize(path)
    sha = get_hash(path)
    
    base_no_wav = f.replace(".wav", "")
    in_corpus = f in existing_files or base_no_wav in existing_files
    
    time_window = None
    if "2026-07-11-23-55" in f or "2026-07-11-23-56" in f or "2026-07-12-00" in f or "2026-07-12-01" in f:
        time_window = "S-AM-2 (G030-G100)"
        if "2026-07-12-01-31" in f:
            time_window = "S-AM-3 (G186-G188) / S-AM-2"
            
    candidates.append({
        "path": path,
        "filename": f,
        "extension": os.path.splitext(f)[1],
        "file_size": size,
        "duration": None, # skipped for now
        "creation_time": None,
        "modification_time": None,
        "channels": None,
        "sample_rate": None,
        "embedded_metadata": None,
        "associated_session": time_window,
        "overlaps_target_window": time_window is not None,
        "appears_to_contain_speech": None,
        "already_represented_in_events": in_corpus,
        "hash_sha256": sha,
        "classification": "DUPLICATE_OR_ALREADY_INGESTED" if in_corpus else "POSSIBLE_RELATED_FILE",
        "reason_for_classification": "Already in corpus" if in_corpus else "Matches timeframe but lacks speaker label."
    })

with open("data/derived/nalex_missing_alex_audio_candidates.json", "w") as f:
    json.dump(candidates, f, indent=2)

import csv
with open("data/derived/nalex_missing_alex_audio_candidates.csv", "w", newline='') as f:
    writer = csv.DictWriter(f, fieldnames=candidates[0].keys())
    writer.writeheader()
    writer.writerows(candidates)

print("Done generating JSON and CSV!")
