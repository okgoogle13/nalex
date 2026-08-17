const fs = require('fs');
const path = require('path');

const INCIDENTS_FILE = 'analysis/timelines/nalex_incidents.json';
const EXTRACTS_FILE = 'analysis/audits/orphan_extracts.json';
const CSV_OUT = 'analysis/audits/nalex_orphan_event_mapping_2026-08-16.csv';

const incidents = JSON.parse(fs.readFileSync(INCIDENTS_FILE, 'utf8'));
const extracts = JSON.parse(fs.readFileSync(EXTRACTS_FILE, 'utf8'));

// Gather assigned IDs
const assignedIds = new Set();
incidents.forEach(inc => {
    inc.source_event_ids.forEach(id => assignedIds.add(id));
});

// Flatten orphans
const orphans = [];
extracts.forEach(block => {
    block.events.forEach(e => {
        orphans.push({
            eid: e.eid,
            t: e.t,
            txt: e.txt,
            session_id: block.session
        });
    });
});

let csv = "event_id,timestamp,session_id,original_assignment,proposed_classification,proposed_parent,confidence,evidence_basis,boundary_or_exclusion_reason,review_status\n";

function escapeCSV(str) {
    if (!str) return '""';
    const clean = str.replace(/"/g, '""').replace(/\n/g, ' ');
    return `"${clean}"`;
}

// Logic variables for validation
let allocations = 0;
let exclusions = 0;
let sConf5Allocations = 0;
let sConf5Excluded = 0;
let sConf10Allocations = 0;
let sConf10Excluded = 0;

orphans.forEach(o => {
    let classification = "baseline";
    let parent = "null";
    let confidence = "High";
    let evidence = o.txt;
    let boundary = "null";

    if (o.eid === 'B024') {
        classification = "uncertain";
        parent = "null";
        confidence = "Low";
        evidence = "Video/media clip visible in screenshot; no transcript available.";
        boundary = "Excluded: lack of transcript context.";
    } else if (o.eid === 'C005') {
        classification = "uncertain";
        parent = "null";
        confidence = "Low";
        evidence = "Missed voice call - 7:22 pm.";
        boundary = "Excluded: system event lacking context.";
    } else if (o.session_id === 'S-CONF-1') {
        classification = "new_incident";
        parent = "PROPOSED-CONF-00A";
        evidence = "Contains language clarifying earlier Ned dispute";
    } else if (o.session_id === 'S-CONF-2') {
        classification = "new_incident";
        parent = "PROPOSED-CONF-00B";
        evidence = "Escalates earlier Ned dispute into gaslighting claims";
        confidence = "Medium";
    } else if (o.session_id === 'S-CONF-5') {
        classification = "continuation";
        parent = "PROPOSED-CONTEXT-S-CONF-5";
        evidence = "Direct temporal and thematic buildup to CONF-01 (sanding table/loneliness)";
        confidence = "Medium";
    } else if (o.session_id === 'S-CONF-7') {
        if (o.eid === 'B064') {
            classification = "continuation";
            parent = "PROPOSED-CONTEXT-S-CONF-7";
            evidence = "Naomi asserts she was chilling; marks sub-boundary of re-escalation";
            boundary = "Internal sub-boundary of re-escalation within block";
        } else {
            classification = "continuation";
            parent = "PROPOSED-CONTEXT-S-CONF-7";
            evidence = "Interspersed texts responding to main June 26/27 argument in CONF-02";
            confidence = "Medium";
        }
    } else if (o.session_id === 'S-CONF-10') {
        if (o.eid === 'C056') {
            classification = "continuation";
            parent = "PROPOSED-CONTEXT-S-CONF-10";
            evidence = "Naomi 'Is that a signing off message?'; transition from logistics to conflict";
            boundary = "Marks transition from logistical delay to active conflict";
        } else {
            classification = "continuation";
            parent = "PROPOSED-CONTEXT-S-CONF-10";
            evidence = "Logistics discussing meeting up that precede and contribute to CONF-03 fight";
            confidence = "Medium";
        }
    }

    if (evidence.length > 80) evidence = evidence.substring(0, 77) + "...";

    csv += `${o.eid},${o.t},${o.session_id},null,${classification},${parent},${confidence},${escapeCSV(evidence)},${escapeCSV(boundary)},proposed\n`;

    // Counting for validations
    if (['continuation', 'new_incident'].includes(classification)) {
        allocations++;
        if (o.session_id === 'S-CONF-5') sConf5Allocations++;
        if (o.session_id === 'S-CONF-10') sConf10Allocations++;
    } else {
        exclusions++;
        if (o.session_id === 'S-CONF-5') sConf5Excluded++;
        if (o.session_id === 'S-CONF-10') sConf10Excluded++;
    }
});

fs.writeFileSync(CSV_OUT, csv);

// Validations:
console.log("--- VALIDATIONS ---");
const uniqueRows = new Set(orphans.map(o => o.eid));
console.log("All 178 rows have unique event_id:", uniqueRows.size === 178);
console.log("No assigned ID appears in CSV:", orphans.every(o => !assignedIds.has(o.eid)));

// Basic counts
console.log(`Total allocations: ${allocations}`);
console.log(`Total exclusions: ${exclusions}`);
console.log(`Sum matches 178: ${allocations + exclusions === 178}`);

// S-CONF-5 checks
console.log(`S-CONF-5 allocations: ${sConf5Allocations} (expected 26)`);
console.log(`S-CONF-5 exclusions: ${sConf5Excluded} (expected 1 for B024)`);

// S-CONF-10 checks
console.log(`S-CONF-10 allocations: ${sConf10Allocations} (expected 57)`);
console.log(`S-CONF-10 exclusions: ${sConf10Excluded} (expected 1 for C005)`);

console.log("--- END ---");
