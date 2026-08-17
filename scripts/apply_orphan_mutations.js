const fs = require('fs');

const INCIDENTS_FILE = 'analysis/timelines/nalex_incidents.json';
const EXTRACTS_FILE = 'analysis/audits/orphan_extracts.json';

const incidents = JSON.parse(fs.readFileSync(INCIDENTS_FILE, 'utf8'));
const extracts = JSON.parse(fs.readFileSync(EXTRACTS_FILE, 'utf8'));

// Helper to get EIDs from a session
function getSessionEids(sessionName, exclude = []) {
    let eids = [];
    extracts.filter(b => b.session === sessionName).forEach(b => {
        b.events.forEach(e => {
            if (!exclude.includes(e.eid)) {
                eids.push(e.eid);
            }
        });
    });
    return eids;
}

const sconf1Eids = getSessionEids('S-CONF-1');
const sconf2Eids = getSessionEids('S-CONF-2');
const sconf5Eids = getSessionEids('S-CONF-5', ['B024']);
const sconf7Eids = getSessionEids('S-CONF-7');
const sconf10Eids = getSessionEids('S-CONF-10', ['C005']);

// CREATE CONF-00a
incidents.unshift({
  "incident_id": "CONF-00a",
  "phase": "Conflict",
  "session": "S-CONF-1",
  "label": "Misunderstanding regarding avoiding Ned",
  "event_type": "Interpersonal confrontation",
  "date_time_start": "2026-06-23T00:45:00",
  "date_time_end": "2026-06-23T01:06:36",
  "source_event_ids": sconf1Eids,
  "participants": ["Naomi", "Alex"],
  "significance_tags": ["miscommunication", "pre-conflict"],
  "speaker_accounts": {},
  "key_quotes": [],
  "confidence": "High",
  "ordering_status": "Confirmed. Precedes CONF-00b.",
  "outcome": "Resolved with lingering confusion."
});

// CREATE CONF-00b
incidents.splice(1, 0, {
  "incident_id": "CONF-00b",
  "phase": "Conflict",
  "session": "S-CONF-2",
  "label": "Escalation of misunderstanding into gaslighting accusations",
  "event_type": "Interpersonal confrontation",
  "date_time_start": "2026-06-23T02:57:00",
  "date_time_end": "2026-06-23T03:50:00",
  "source_event_ids": sconf2Eids,
  "participants": ["Naomi", "Alex"],
  "significance_tags": ["gaslighting-accusation", "pre-conflict"],
  "speaker_accounts": {},
  "key_quotes": [],
  "confidence": "Medium",
  "ordering_status": "Confirmed. Related to CONF-00a.",
  "outcome": "Unresolved. Naomi goes to sleep."
});

// EXPAND CONF-01
const conf01 = incidents.find(i => i.incident_id === 'CONF-01');
if (conf01) {
    conf01.source_event_ids = [...new Set([...sconf5Eids, ...conf01.source_event_ids])];
}

// EXPAND CONF-02
const conf02 = incidents.find(i => i.incident_id === 'CONF-02');
if (conf02) {
    conf02.source_event_ids = [...new Set([...sconf7Eids, ...conf02.source_event_ids])];
}

// EXPAND CONF-03
const conf03 = incidents.find(i => i.incident_id === 'CONF-03');
if (conf03) {
    conf03.source_event_ids = [...new Set([...sconf10Eids, ...conf03.source_event_ids])];
}

fs.writeFileSync(INCIDENTS_FILE, JSON.stringify(incidents, null, 2));
console.log('Successfully mutated nalex_incidents.json');
