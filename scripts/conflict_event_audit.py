import json
from datetime import datetime
import os

EVENTS_FILE = 'data/raw/events.jsonl'
INCIDENTS_FILE = 'analysis/timelines/nalex_incidents.json'
OUTPUT_FILE = 'analysis/audits/nalex_conflict_event_audit.md'

# Load incidents
with open(INCIDENTS_FILE, 'r') as f:
    incidents_data = json.load(f)

conflict_incidents = [inc for inc in incidents_data if inc.get('phase') == 'Conflict']

# Map eid -> incident_id
assigned_events = {}
primary_events = set()

for inc in conflict_incidents:
    iid = inc['incident_id']
    for eid in inc.get('source_event_ids', []):
        assigned_events[eid] = iid
    for quote in inc.get('key_quotes', []):
        if 'eid' in quote:
            primary_events.add(quote['eid'])

# Load events
events = []
with open(EVENTS_FILE, 'r') as f:
    for line in f:
        if line.strip():
            events.append(json.loads(line))

# Parse timestamps and sort
for e in events:
    e['dt'] = datetime.strptime(e['t'], "%Y-%m-%d %H:%M:%S")

events.sort(key=lambda x: x['dt'])

# Filter Conflict Phase: Jun 23 to Jul 5 inclusive
start_dt = datetime(2026, 6, 23)
end_dt = datetime(2026, 7, 6)

conflict_events = [e for e in events if start_dt <= e['dt'] < end_dt]

# Compute sessions (60 min gap rule)
sessions = []
current_session = []

for e in conflict_events:
    if not current_session:
        current_session.append(e)
    else:
        last_e = current_session[-1]
        gap = (e['dt'] - last_e['dt']).total_seconds() / 60.0
        if gap > 60:
            sessions.append(current_session)
            current_session = [e]
        else:
            current_session.append(e)

if current_session:
    sessions.append(current_session)

# Generate Markdown
md_lines = []
md_lines.append("# Nalex Conflict Phase — Complete Event Assignment Audit")
md_lines.append(f"*Produced {datetime.now().strftime('%Y-%m-%d')}. Source: `events.jsonl` ({len(events)} events total; {len(conflict_events)} Conflict events Jun 23–Jul 5). Session boundaries use 60-minute inter-event gap rule.*")
md_lines.append("")
md_lines.append("## Session Boundaries (computed from `events.jsonl`)")
md_lines.append("")
md_lines.append("| Session | Start | End | Events | Gap before |")
md_lines.append("|---|---|---|---|---|")

prev_session_end = None
for i, sess in enumerate(sessions):
    s_id = f"S-CONF-{i+1}"
    start_t = sess[0]['t']
    end_t = sess[-1]['t']
    count = len(sess)
    if prev_session_end:
        gap_min = (sess[0]['dt'] - prev_session_end).total_seconds() / 60.0
        if gap_min > 1440:
            gap_str = f"~{gap_min/1440:.1f} days"
        elif gap_min > 60:
            gap_str = f"~{gap_min/60:.1f} hr"
        else:
            gap_str = f"{gap_min:.1f} min"
    else:
        gap_str = "—"
    
    md_lines.append(f"| {s_id} | {start_t} | {end_t} | {count} | {gap_str} |")
    prev_session_end = sess[-1]['dt']

md_lines.append("")
md_lines.append(f"**Total: {len(conflict_events)} events across {len(sessions)} sessions.**")
md_lines.append("")
md_lines.append("## Audit: Notation")
md_lines.append("")
md_lines.append("- **Primary**: event is explicitly cited in incident key quotes.")
md_lines.append("- **Subsumed**: event is in the incident's source list but not cited as a key quote.")
md_lines.append("- **Orphan**: event falls in the Conflict phase but is not assigned to any CONF incident.")
md_lines.append("")
md_lines.append(f"## Complete Assignment Table ({len(conflict_events)} events)")
md_lines.append("")
md_lines.append("| event_id | timestamp | session_id | speaker | incident_id | assignment_status | assignment_reason |")
md_lines.append("|---|---|---|---|---|---|---|")

orphans = []

for i, sess in enumerate(sessions):
    s_id = f"S-CONF-{i+1}"
    for e in sess:
        eid = e['eid']
        ts = e['t']
        speaker = e['s']
        
        if eid in assigned_events:
            iid = assigned_events[eid]
            status = "primary" if eid in primary_events else "subsumed"
            reason = "Listed in incident source events"
        else:
            iid = "UNASSIGNED"
            status = "orphan"
            reason = "Not assigned to any CONF incident"
            orphans.append(e)
            
        # Clean text snippet for reason
        snippet = e['txt'][:50].replace('\n', ' ') + "..." if e.get('txt') else ""
        reason = f"{reason} (\"{snippet}\")"
        
        md_lines.append(f"| {eid} | {ts} | {s_id} | {speaker} | {iid} | {status} | {reason} |")

with open(OUTPUT_FILE, 'w') as f:
    f.write("\n".join(md_lines))

print(f"Generated {OUTPUT_FILE} with {len(conflict_events)} events.")
print(f"Found {len(orphans)} orphan events.")
if orphans:
    print(f"Sample orphans:")
    for o in orphans[:5]:
        print(f" - {o['eid']} at {o['t']} ({o['s']})")
