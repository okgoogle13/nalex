import json, re, datetime as dt
from collections import defaultdict
import os

# Set paths based on new directory structure
BASE_DIR = '/Users/okgoogle13/Projects/Nalex'
EVENTS_PATH = os.path.join(BASE_DIR, 'data/raw/events.jsonl')
PROFILE_PATH = os.path.join(BASE_DIR, 'data/derived/phase_profile.json')
OUTPUT_PATH = os.path.join(BASE_DIR, 'data/derived/flattened_themes_metrics.json')

# 1. Load and parse events.jsonl
rows = [json.loads(l) for l in open(EVENTS_PATH)]

def parse(r):
    t = r['t'].strip().lstrip('~').strip()
    d, tm = t.split(' ', 1)
    if ':' in tm:
        p = tm.split(':')
        while len(p) < 3: p.append('00')
        tm = ':'.join(x.zfill(2) for x in p)
    else:
        tm = tm.ljust(6, '0')
        tm = f'{tm[0:2]}:{tm[2:4]}:{tm[4:6]}'
    return dt.datetime.strptime(d + ' ' + tm, '%Y-%m-%d %H:%M:%S')

for r in rows:
    r['_dt'] = parse(r)

PH = [
    ('Baseline', '2026-04-01', '2026-06-22'),
    ('Conflict', '2026-06-23', '2026-07-05'),
    ('Silence', '2026-07-06', '2026-07-10'),
    ('Aftermath', '2026-07-11', '2026-07-21')
]

def phase(r):
    d = r['_dt'].date().isoformat()
    for n, a, b in PH:
        if a <= d <= b: return n
    return 'OUT'

for r in rows:
    r['_ph'] = phase(r)
    r['_w'] = len(re.findall(r"[A-Za-z0-9']+", r.get('txt', '')))

# Compute hard metrics per phase per speaker
metrics = defaultdict(lambda: defaultdict(lambda: {'messages': 0, 'words': 0}))
for r in rows:
    if r['_ph'] != 'OUT' and r['s'] in ['Naomi', 'Alex']:
        metrics[r['_ph']][r['s']]['messages'] += 1
        metrics[r['_ph']][r['s']]['words'] += r['_w']

# 2. Load phase_profile.json
with open(PROFILE_PATH) as f:
    phase_profile = json.load(f)

# 3. Themes to embed
alex_july_themes = [
    "Setting Boundaries & Friendship Termination",
    "Emotional Vulnerability & Past Trauma",
    "Defense Against Accusations of 'Flirting' or 'Leading On'",
    "Conflict Fatigue"
]

# 4. Build flattened structure
flattened = []
for ph_name, ph_data in phase_profile.get('phases', {}).items():
    prob_tags = ph_data.get('problematic_tags', [])
    emo_tags = ph_data.get('emotional_tags', [])
    
    for speaker in ['Naomi', 'Alex']:
        # Map tags by prefix
        sp_prob_tags = [t for t in prob_tags if t.startswith(speaker.lower())]
        sp_emo_tags = [t for t in emo_tags if t.startswith(speaker.lower())]
        
        # Extracted themes
        extracted_themes = []
        if speaker == 'Alex' and ph_name in ['Conflict', 'Aftermath']:
            extracted_themes = alex_july_themes
            
        # Computed metrics
        sp_metrics = metrics.get(ph_name, {}).get(speaker, {'messages': 0, 'words': 0})
        
        flattened.append({
            'phase': ph_name,
            'speaker': speaker,
            'hard_metrics': {
                'messages': sp_metrics['messages'],
                'words': sp_metrics['words']
            },
            'canonical_tags': {
                'problematic': sp_prob_tags,
                'emotional': sp_emo_tags
            },
            'extracted_themes': extracted_themes
        })

with open(OUTPUT_PATH, 'w') as f:
    json.dump(flattened, f, indent=2)
print(f"Saved to {OUTPUT_PATH}")
