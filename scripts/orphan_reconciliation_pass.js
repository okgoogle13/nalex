const fs = require('fs');
const path = require('path');

const EVENTS_FILE = 'data/raw/events.jsonl';
const INCIDENTS_FILE = 'analysis/timelines/nalex_incidents.json';
const EXTRACT_FILE = 'analysis/audits/orphan_extracts.json';

// Load events
const events = fs.readFileSync(EVENTS_FILE, 'utf8')
    .split('\n')
    .filter(line => line.trim())
    .map(line => JSON.parse(line));

events.forEach(e => {
    e.dt = new Date(e.t.replace(' ', 'T') + 'Z');
});
events.sort((a, b) => a.dt - b.dt);

const startDt = new Date('2026-06-23T00:00:00Z');
const endDt = new Date('2026-07-06T00:00:00Z');
const conflictEvents = events.filter(e => e.dt >= startDt && e.dt < endDt);

const conflictEids = new Set(conflictEvents.map(e => e.eid));

// Load incidents
const incidentsData = JSON.parse(fs.readFileSync(INCIDENTS_FILE, 'utf8'));
const conflictIncidents = incidentsData.filter(inc => inc.phase === 'Conflict');

// Reconciliation Pass
console.log("--- RECONCILIATION REPORT ---");
const assignedTo = {};
let hasReconciliationErrors = false;

conflictIncidents.forEach(inc => {
    const iid = inc.incident_id;
    const sourceIds = inc.source_event_ids || [];
    
    sourceIds.forEach(eid => {
        // Malformed check
        if (!eid || typeof eid !== 'string') {
            console.log(`[MALFORMED] ${iid} has a malformed source ID: ${eid}`);
            hasReconciliationErrors = true;
        }
        
        // Missing / Unreferenced check
        if (!conflictEids.has(eid)) {
            console.log(`[MISSING/UNREFERENCED] ${iid} references '${eid}' which is not in the Jun 23-Jul 5 events window.`);
            hasReconciliationErrors = true;
        }
        
        // Duplicate check
        if (assignedTo[eid]) {
            console.log(`[DUPLICATE] '${eid}' is assigned to both ${assignedTo[eid]} and ${iid}.`);
            hasReconciliationErrors = true;
        } else {
            assignedTo[eid] = iid;
        }
    });
});

if (!hasReconciliationErrors) {
    console.log("All source_event_ids are valid, unique, and present in the window.");
}

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
if (currentSession.length > 0) sessions.push(currentSession);

// Extract Orphan Blocks
const orphanBlocks = [];

sessions.forEach((sess, i) => {
    const sId = `S-CONF-${i + 1}`;
    
    // Find contiguous blocks of orphans in this session
    let currentBlock = [];
    
    sess.forEach((e, idx) => {
        if (!assignedTo[e.eid]) {
            currentBlock.push({
                eid: e.eid,
                t: e.t,
                s: e.s,
                txt: e.txt
            });
        } else {
            if (currentBlock.length > 0) {
                orphanBlocks.push({
                    session: sId,
                    type: 'prefix/mid',
                    events: currentBlock
                });
                currentBlock = [];
            }
        }
    });
    
    if (currentBlock.length > 0) {
        // If the whole session was orphans, mark it as 'full_session', else 'suffix'
        const type = (currentBlock.length === sess.length) ? 'full_session' : 'suffix';
        orphanBlocks.push({
            session: sId,
            type: type,
            events: currentBlock
        });
    }
});

fs.writeFileSync(EXTRACT_FILE, JSON.stringify(orphanBlocks, null, 2));
console.log(`\nExtracted ${orphanBlocks.length} orphan blocks to ${EXTRACT_FILE} for semantic review.`);
