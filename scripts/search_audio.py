import os
import json
import zipfile
import hashlib
import subprocess
import glob
from datetime import datetime

TARGET_ZIPS = [
    "archive/Alec and naomi.zip",
    "archive/audio.zip",
    "archive/gap_audio.zip",
    "archive/remaining_gaps_112.zip",
    "archive/unpunctuated_68.zip",
    "archive/claude_handover_live_set.zip"
]

OUT_DIR = "./tmp_audio_search"
os.makedirs(OUT_DIR, exist_ok=True)

# Load existing corpus
canonical_events = []
try:
    with open("data/raw/events.jsonl", "r") as f:
        for line in f:
            if line.strip():
                canonical_events.append(json.loads(line))
except Exception as e:
    print(f"Error loading canonical events: {e}")

existing_files = set()
for ev in canonical_events:
    if "source_file" in ev:
        existing_files.add(os.path.basename(ev["source_file"]))
    if "media" in ev and ev["media"]:
        for m in ev["media"]:
            if "filename" in m:
                existing_files.add(os.path.basename(m["filename"]))
            if "file_path" in m:
                existing_files.add(os.path.basename(m["file_path"]))

candidates = []

def get_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def get_duration(path):
    return None

def process_zip(zip_path):
    print(f"Processing {zip_path}...")
    try:
        with zipfile.ZipFile(zip_path, 'r') as z:
            for info in z.infolist():
                if info.is_dir(): continue
                name = info.filename
                basename = os.path.basename(name)
                
                # Check target dates and keywords
                date_match = "2026-07-11" in name or "2026-07-12" in name
                kw_match = any(kw in name.lower() for kw in ["g030", "g031", "g032", "g100", "g186", "g187", "g188", "s-am-2", "s-am-3", "alex", "reply", "response", "side-a", "side-b"])
                
                if (date_match or kw_match) and not basename.startswith("._") and "__MACOSX" not in name:
                    ext = os.path.splitext(basename)[1].lower()
                    if ext in ['.aac', '.m4a', '.mp3', '.wav', '.caf', '.opus', '.mp4']:
                        # Extract to temp
                        out_path = os.path.join(OUT_DIR, basename)
                        if not os.path.exists(out_path):
                            with open(out_path, "wb") as f:
                                f.write(z.read(name))
                        
                        # Gather metadata
                        size = os.path.getsize(out_path)
                        sha256 = get_hash(out_path)
                        duration = get_duration(out_path)
                        
                        # Match to target window
                        # 2026-07-11 23:55 to 2026-07-12 01:31 AEST
                        # Let's extract the time from the filename "signal-YYYY-MM-DD-HH-MM-SS-MMM.aac"
                        time_window = None
                        overlap = False
                        if "2026-07-11-23-55" in name or "2026-07-11-23-56" in name or ("2026-07-12-00" in name) or ("2026-07-12-01" in name):
                            time_window = "S-AM-2 (G030-G100)"
                            overlap = True
                            if "2026-07-12-01-31" in name:
                                time_window = "S-AM-2 or S-AM-3"
                        
                        # Already ingested?
                        # Check if base filename (without .wav if it's .aac.wav) is in corpus
                        base_no_wav = basename.replace(".wav", "")
                        already_ingested = basename in existing_files or base_no_wav in existing_files
                        
                        # Just naive classification for now
                        classification = "DUPLICATE_OR_ALREADY_INGESTED" if already_ingested else ("POSSIBLE_RELATED_FILE" if overlap else "NOT_RELEVANT")
                        reason = "File matches the target date/time window but lacks explicit speaker attribution."
                        if already_ingested:
                            reason = "File or its base name is already present in the canonical events corpus."
                            
                        candidates.append({
                            "source_zip": zip_path,
                            "path": f"{zip_path}/{name}",
                            "filename": basename,
                            "extension": ext,
                            "file_size": size,
                            "duration": duration,
                            "creation_time": None, # ZIP doesn't retain creation time well
                            "modification_time": info.date_time,
                            "channels": None,
                            "sample_rate": None,
                            "embedded_metadata": None,
                            "associated_session": time_window,
                            "overlaps_target_window": overlap,
                            "appears_to_contain_speech": None, # Needs deeper analysis or manual review
                            "already_represented_in_events": already_ingested,
                            "hash_sha256": sha256,
                            "classification": classification,
                            "reason_for_classification": reason
                        })
    except Exception as e:
        print(f"Error processing {zip_path}: {e}")

for z in TARGET_ZIPS:
    if os.path.exists(z):
        process_zip(z)

with open("nalex_missing_alex_audio_candidates.json", "w") as f:
    json.dump(candidates, f, indent=2, default=str)

print(f"Saved {len(candidates)} candidates.")
