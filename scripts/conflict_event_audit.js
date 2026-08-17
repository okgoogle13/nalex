const fs = require('fs');

const EVENTS_FILE = 'data/raw/events.jsonl';
const INCIDENTS_FILE = 'analysis/timelines/nalex_incidents.json';
const OUTPUT_FILE = 'analysis/audits/nalex_conflict_event_audit.md';

// Load incidents
const incidentsData = JSON.parse(fs.readFileSync(INCIDENTS_FILE, 'utf8'));
const conflictIncidents = incidentsData.filter(inc => inc.phase === 'Conflict');

const assignedEvents = {};
const primaryEvents = new Set();

conflictIncidents.forEach(inc => {
    const iid = inc.incident_id;
    (inc.source_event_ids || []).forEach(eid => {
        assignedEvents[eid] = iid;
    });
    (inc.key_quotes || []).forEach(quote => {
        if (quote.eid) {
            primaryEvents.add(quote.eid);
        }
    });
});

// Load events
const events = fs.readFileSync(EVENTS_FILE, 'utf8')
    .split('\n')
    .filter(line => line.trim())
    .map(line => JSON.parse(line));

events.forEach(e => {
    e.dt = new Date(e.t.replace(' ', 'T') + 'Z'); // Using Z to just parse it and compare relatively
});

events.sort((a, b) => a.dt - b.dt);

// Filter Conflict Phase: Jun 23 to Jul 5 inclusive
const startDt = new Date('2026-06-23T00:00:00Z');
const endDt = new Date('2026-07-06T00:00:00Z');

const conflictEvents = events.filter(e => e.dt >= startDt && e.dt < endDt);

// Compute sessions (60 min gap rule)
const sessions = [];
let currentSession = [];

conflictEvents.forEach(e => {
    if (currentSession.length === 0) {
        currentSession.push(e);
    } else {
        const lastE = currentSession[currentSession.length - 1];
        const gapMin = (e.dt - lastE.dt) / (1000 * 60);
        if (gapMin > 60) {
            sessions.push(currentSession);
            currentSession = [e];
        } else {
            currentSession.push(e);
        }
    }
});

if (currentSession.length > 0) {
    sessions.push(currentSession);
}

// Generate Markdown
const mdLines = [];
mdLines.push("# Nalex Conflict Phase — Complete Event Assignment Audit");
mdLines.push(`*Produced ${new Date().toISOString().split('T')[0]}. Source: \`events.jsonl\` (${events.length} events total; ${conflictEvents.length} Conflict events Jun 23–Jul 5). Session boundaries use 60-minute inter-event gap rule.*`);
mdLines.push("");
mdLines.push("## Session Boundaries (computed from `events.jsonl`)");
mdLines.push("");
mdLines.push("| Session | Start | End | Events | Gap before |");
mdLines.push("|---|---|---|---|---|");

let prevSessionEnd = null;
sessions.forEach((sess, i) => {
    const sId = `S-CONF-${i + 1}`;
    const startT = sess[0].t;
    const endT = sess[sess.length - 1].t;
    const count = sess.length;
    let gapStr = "—";
    
    if (prevSessionEnd) {
        const gapMin = (sess[0].dt - prevSessionEnd) / (1000 * 60);
        if (gapMin > 1440) {
            gapStr = `~${(gapMin / 1440).toFixed(1)} days`;
        } else if (gapMin > 60) {
            gapStr = `~${(gapMin / 60).toFixed(1)} hr`;
        } else {
            gapStr = `${gapMin.toFixed(1)} min`;
        }
    }
    
    mdLines.push(`| ${sId} | ${startT} | ${endT} | ${count} | ${gapStr} |`);
    prevSessionEnd = sess[sess.length - 1].dt;
});

mdLines.push("");
mdLines.push(`**Total: ${conflictEvents.length} events across ${sessions.length} sessions.**`);
mdLines.push("");
mdLines.push("## Audit: Notation");
mdLines.push("");
mdLines.push("- **Primary**: event is explicitly cited in incident key quotes.");
mdLines.push("- **Subsumed**: event is in the incident's source list but not cited as a key quote.");
mdLines.push("- **Orphan**: event falls in the Conflict phase but is not assigned to any CONF incident.");
mdLines.push("");
mdLines.push(`## Complete Assignment Table (${conflictEvents.length} events)`);
mdLines.push("");
mdLines.push("| event_id | timestamp | session_id | speaker | incident_id | assignment_status | assignment_reason |");
mdLines.push("|---|---|---|---|---|---|---|");

const orphans = [];

sessions.forEach((sess, i) => {
    const sId = `S-CONF-${i + 1}`;
    sess.forEach(e => {
        const eid = e.eid;
        const ts = e.t;
        const speaker = e.s;
        
        let iid, status, reason;
        
        if (assignedEvents[eid]) {
            iid = assignedEvents[eid];
            status = primaryEvents.has(eid) ? "primary" : "subsumed";
            reason = "Listed in incident source events";
        } else {
            iid = "UNASSIGNED";
            status = "orphan";
            reason = "Not assigned to any CONF incident";
            orphans.push(e);
        }
        
        let snippet = "";
        if (e.txt) {
            snippet = e.txt.substring(0, 50).replace(/\n/g, ' ') + "...";
        }
        reason = `${reason} ("${snippet}")`;
        
        mdLines.push(`| ${eid} | ${ts} | ${sId} | ${speaker} | ${iid} | ${status} | ${reason} |`);
    });
});

fs.writeFileSync(OUTPUT_FILE, mdLines.join('\n'));

console.log(`Generated ${OUTPUT_FILE} with ${conflictEvents.length} events.`);
console.log(`Found ${orphans.length} orphan events.`);
if (orphans.length > 0) {
    console.log(`Sample orphans:`);
    orphans.slice(0, 5).forEach(o => {
        console.log(` - ${o.eid} at ${o.t} (${o.s})`);
    });
}
