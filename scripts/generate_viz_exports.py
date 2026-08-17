#!/usr/bin/env python3
"""
Generate visualization-ready CSV exports from Nalex data pipeline.

This script transforms JSON/JSONL source data into flat CSVs aligned with
nalex_viz_projection_contract.json. All raw transcript text is stripped
before export — no txt/txt_v3/txt_raw_prior fields are permitted in outputs.

Usage:
    python scripts/generate_viz_exports.py

Outputs:
    - data/viz_exports/events_timeline.csv
    - data/viz_exports/theme_metrics.csv
    - data/viz_exports/phase_profiles.csv
    - data/viz_exports/gap_analysis.csv
    - data/viz_exports/orphan_events.csv
    - data/viz_manifest.json
"""

import json
import csv
import os
from datetime import datetime
from pathlib import Path
from typing import Any


# === Configuration ===

REPO_ROOT = Path(__file__).parent.parent
DATA_RAW = REPO_ROOT / "data" / "raw"
DATA_DERIVED = REPO_ROOT / "data" / "derived"
DATA_VIZ_EXPORTS = REPO_ROOT / "data" / "viz_exports"
ANALYSIS_AUDITS = REPO_ROOT / "analysis" / "audits"

# All field names that may contain raw transcript text — must never appear in exports
RAW_TEXT_KEYS = frozenset([
    'txt', 'txt_v3', 'txt_raw_prior', 'text', 'content', 'message',
    'transcript', 'body', 'quote', 'excerpt', 'verbatim',
])

# Ensure output directory exists
DATA_VIZ_EXPORTS.mkdir(parents=True, exist_ok=True)


# === Helper Functions ===

def load_jsonl(filepath: Path) -> list[dict]:
    """Load a JSONL file into a list of dicts."""
    if not filepath.exists():
        print(f"⚠️  File not found: {filepath}")
        return []

    records = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if not line:
                continue
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError as e:
                print(f"⚠️  JSON decode error at line {line_num}: {e}")
    return records


def load_json(filepath: Path) -> dict | list:
    """Load a JSON file."""
    if not filepath.exists():
        print(f"⚠️  File not found: {filepath}")
        return {}

    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_csv(records: list[dict], filepath: Path, fieldnames: list[str] | None = None) -> int:
    """Save records to CSV, return row count."""
    if not records:
        print(f"⚠️  No records to write to {filepath.name}")
        return 0

    if fieldnames is None:
        fieldnames = list(records[0].keys())

    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(records)

    print(f"✓ Wrote {len(records)} rows to {filepath.name}")
    return len(records)


def normalize_speaker(speaker: Any) -> str:
    """Normalize speaker name to lowercase standard form."""
    if speaker is None:
        return "unknown"

    speaker = str(speaker).lower().strip()

    if speaker in ["alex", "alexis", "user"]:
        return "alex"
    elif speaker in ["naomi", "assistant", "ai"]:
        return "naomi"
    elif speaker in ["system", "meta", "platform"]:
        return "system"

    return speaker


def strip_raw_text(event: dict) -> dict:
    """
    Return a copy of event with all raw transcript text fields removed.
    This is the privacy gate — no field in RAW_TEXT_KEYS may appear in exports.
    """
    return {k: v for k, v in event.items() if k not in RAW_TEXT_KEYS}


# === Export Functions ===

def export_events_timeline() -> int:
    """
    Export events.jsonl to CSV aligned with nalex_viz_projection_contract.json.

    Contract fields (structure-only, NO raw text):
        record_id, timestamp, event_type, speaker_role, phase,
        loop_type, sequence, move_codes,
        direct_response_status, repair_response_status,
        source_review_state, projection_eligibility, privacy_level

    All raw text fields (txt, txt_v3, txt_raw_prior, etc.) are EXCLUDED.
    """
    print("\n📊 Exporting events timeline...")

    events = load_jsonl(DATA_RAW / "events.jsonl")

    rows = []
    leaked = 0
    for seq, event in enumerate(events, 1):
        # Strip all raw text before anything else — privacy gate
        safe = strip_raw_text(event)

        row = {
            'record_id':              safe.get('eid') or safe.get('event_id') or safe.get('id', ''),
            'timestamp':              safe.get('t') or safe.get('timestamp') or safe.get('ts', ''),
            'event_type':             safe.get('type') or safe.get('event_type') or safe.get('kind', ''),
            'speaker_role':           normalize_speaker(
                                          safe.get('speaker') or safe.get('s') or safe.get('participant', '')
                                      ),
            'phase':                  safe.get('phase') or safe.get('relationship_phase') or '',
            'loop_type':              safe.get('loop_type') or safe.get('loop_id') or safe.get('communication_loop', ''),
            'sequence':               seq,
            'move_codes':             json.dumps(safe.get('move_codes', []), ensure_ascii=False),
            'direct_response_status': safe.get('direct_response_status', ''),
            'repair_response_status': safe.get('repair_response_status', ''),
            'source_review_state':    safe.get('source_review_state') or safe.get('review_status', ''),
            'projection_eligibility': safe.get('projection_eligibility', True),
            'privacy_level':          safe.get('privacy_level', ''),
        }

        # Sanity-check: no field value should contain raw text key names
        for val in row.values():
            if isinstance(val, str) and any(k in val for k in ('txt_raw_prior', 'txt_v3', '"txt"')):
                leaked += 1
                break

        rows.append(row)

    if leaked:
        print(f"🚨 WARNING: {leaked} rows may still contain raw text references — review manually")
    else:
        print(f"  ✓ Privacy check: no raw text key references detected in output values")

    fieldnames = [
        'record_id', 'timestamp', 'event_type', 'speaker_role', 'phase',
        'loop_type', 'sequence', 'move_codes',
        'direct_response_status', 'repair_response_status',
        'source_review_state', 'projection_eligibility', 'privacy_level',
    ]

    return save_csv(rows, DATA_VIZ_EXPORTS / "events_timeline.csv", fieldnames)


def export_theme_metrics() -> int:
    """
    Export flattened_themes_metrics.json to CSV.

    Actual structure (2026-08-16):
        [{ phase, speaker, hard_metrics: {messages, words}, extracted_themes: [] }]
    """
    print("\n📊 Exporting theme metrics...")

    data = load_json(DATA_DERIVED / "flattened_themes_metrics.json")

    if isinstance(data, list):
        records = data
    elif isinstance(data, dict):
        records = data.get('themes', data.get('data', []))
    else:
        print("⚠️  Unexpected theme metrics structure")
        return 0

    rows = []
    for rec in records:
        hard = rec.get('hard_metrics', {})
        if not isinstance(hard, dict):
            hard = {}
        themes = rec.get('extracted_themes', [])
        if not isinstance(themes, list):
            themes = []

        row = {
            'phase':            rec.get('phase', ''),
            'speaker':          normalize_speaker(rec.get('speaker', '')),
            'message_count':    hard.get('messages', 0),
            'word_count':       hard.get('words', 0),
            'theme_count':      len(themes),
            'extracted_themes': json.dumps(themes, ensure_ascii=False),
        }
        rows.append(row)

    fieldnames = ['phase', 'speaker', 'message_count', 'word_count', 'theme_count', 'extracted_themes']
    return save_csv(rows, DATA_VIZ_EXPORTS / "theme_metrics.csv", fieldnames)


def export_phase_profiles() -> int:
    """
    Export phase_profile.json to CSV.

    Actual structure:
        { tag_vocabulary: {}, phases: { Baseline: {...}, Conflict: {...}, ... }, corpus_wide: {...} }

    Phase metrics are nested under the 'phases' key — not at the top level.
    """
    print("\n📊 Exporting phase profiles...")

    data = load_json(DATA_DERIVED / "phase_profile.json")

    # The real phase data is under 'phases', not at the top level
    phases_dict = data.get('phases', {}) if isinstance(data, dict) else {}

    rows = []
    for phase_name, metrics in phases_dict.items():
        if not isinstance(metrics, dict):
            continue

        speakers = metrics.get('speakers', {})
        naomi = speakers.get('Naomi') or speakers.get('naomi') or {}
        alex = speakers.get('Alex') or speakers.get('alex') or {}
        asym = metrics.get('asymmetry') or {}

        row = {
            'phase_name':             phase_name,
            'window':                 metrics.get('window', ''),
            'calendar_days':          metrics.get('calendar_days', 0),
            'event_count':            metrics.get('events', 0),
            'sessions_60min':         metrics.get('sessions_60min', 0),
            'contact_days':           metrics.get('contact_days', 0),
            'naomi_messages':         naomi.get('messages', 0) if isinstance(naomi, dict) else 0,
            'naomi_words':            naomi.get('words', 0) if isinstance(naomi, dict) else 0,
            'naomi_questions':        naomi.get('questions', 0) if isinstance(naomi, dict) else 0,
            'naomi_median_reply_sec': naomi.get('median_reply_seconds', '') if isinstance(naomi, dict) else '',
            'alex_messages':          alex.get('messages', 0) if isinstance(alex, dict) else 0,
            'alex_words':             alex.get('words', 0) if isinstance(alex, dict) else 0,
            'alex_questions':         alex.get('questions', 0) if isinstance(alex, dict) else 0,
            'alex_median_reply_sec':  alex.get('median_reply_seconds', '') if isinstance(alex, dict) else '',
            'word_ratio_n_over_a':    asym.get('word_ratio_N_over_A', '') if isinstance(asym, dict) else '',
            'session_opens_n_to_a':   asym.get('session_opens_N_to_A', '') if isinstance(asym, dict) else '',
            'session_closes_n_to_a':  asym.get('session_closes_N_to_A', '') if isinstance(asym, dict) else '',
            'flags':                  json.dumps(metrics.get('flags', []), ensure_ascii=False),
        }
        rows.append(row)

    fieldnames = [
        'phase_name', 'window', 'calendar_days', 'event_count', 'sessions_60min', 'contact_days',
        'naomi_messages', 'naomi_words', 'naomi_questions', 'naomi_median_reply_sec',
        'alex_messages', 'alex_words', 'alex_questions', 'alex_median_reply_sec',
        'word_ratio_n_over_a', 'session_opens_n_to_a', 'session_closes_n_to_a', 'flags',
    ]

    return save_csv(rows, DATA_VIZ_EXPORTS / "phase_profiles.csv", fieldnames)


def export_gap_analysis() -> int:
    """
    Export gap_stats_out.json to CSV.

    Actual structure:
        { _note: "...", rows: [ {sha256, t, prev_t, prev_eid, local_id, eid, gap_sec}, ... ] }
    """
    print("\n📊 Exporting gap analysis...")

    data = load_json(DATA_DERIVED / "gap_stats_out.json")

    raw_rows = []
    if isinstance(data, dict):
        raw_rows = data.get('rows', [])
    elif isinstance(data, list):
        raw_rows = data

    rows = []
    for rec in raw_rows:
        if not isinstance(rec, dict):
            continue

        gap_sec = rec.get('gap_sec', '')
        gap_min = ''
        if gap_sec != '':
            try:
                gap_min = round(float(gap_sec) / 60, 2)
            except (ValueError, TypeError):
                pass

        rows.append({
            'gap_id':         rec.get('local_id', ''),
            'event_id':       rec.get('eid', ''),
            'prev_event_id':  rec.get('prev_eid') or rec.get('prev_eid_unresolved', ''),
            'timestamp':      rec.get('t', ''),
            'prev_timestamp': rec.get('prev_t', ''),
            'gap_seconds':    gap_sec,
            'gap_minutes':    gap_min,
            'sha256':         rec.get('sha256', ''),
        })

    fieldnames = [
        'gap_id', 'event_id', 'prev_event_id',
        'timestamp', 'prev_timestamp',
        'gap_seconds', 'gap_minutes', 'sha256',
    ]

    return save_csv(rows, DATA_VIZ_EXPORTS / "gap_analysis.csv", fieldnames)


def export_orphan_events() -> int:
    """
    Export orphan event mapping CSV from analysis/audits/.

    Reads nalex_orphan_event_mapping_*.csv and maps its actual columns:
        event_id, timestamp, session_id, original_assignment,
        proposed_classification, proposed_parent, confidence,
        evidence_basis, boundary_or_exclusion_reason, review_status
    """
    print("\n📊 Exporting orphan events...")

    # Find most recent orphan mapping file
    orphan_files = sorted(ANALYSIS_AUDITS.glob("nalex_orphan_event_mapping_*.csv"))

    if not orphan_files:
        print("⚠️  No orphan mapping files found")
        return 0

    latest_orphan = orphan_files[-1]
    print(f"  Found: {latest_orphan.name}")

    rows = []
    with open(latest_orphan, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            std_row = {
                'orphan_id':                    row.get('event_id', ''),
                'timestamp':                    row.get('timestamp', ''),
                'session_id':                   row.get('session_id', ''),
                'original_assignment':          row.get('original_assignment', ''),
                'proposed_classification':      row.get('proposed_classification', ''),
                'proposed_parent':              row.get('proposed_parent', ''),
                'confidence':                   row.get('confidence', ''),
                'evidence_basis':               row.get('evidence_basis', ''),
                'boundary_or_exclusion_reason': row.get('boundary_or_exclusion_reason', ''),
                'review_status':                row.get('review_status', ''),
            }
            rows.append(std_row)

    fieldnames = [
        'orphan_id', 'timestamp', 'session_id',
        'original_assignment', 'proposed_classification', 'proposed_parent',
        'confidence', 'evidence_basis', 'boundary_or_exclusion_reason', 'review_status',
    ]

    return save_csv(rows, DATA_VIZ_EXPORTS / "orphan_events.csv", fieldnames)


def verify_no_raw_text_leak(filepath: Path) -> int:
    """
    Verify that no known raw-text keys appear in any cell of a CSV.
    Returns count of suspect rows (0 = clean, -1 = file not found).
    """
    if not filepath.exists():
        return -1

    suspect = 0
    with open(filepath, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            for val in row.values():
                if val and any(key in val for key in ['txt_raw_prior', 'txt_v3', '"txt"']):
                    suspect += 1
                    break
    return suspect


def generate_manifest(total_rows: dict[str, int]) -> None:
    """
    Generate viz_manifest.json indexing all exported datasets.
    Updated to reflect corrected column schemas.
    """
    print("\n📋 Generating viz manifest...")

    manifest = {
        "datasets": [
            {
                "name": "events_timeline",
                "path": "viz_exports/events_timeline.csv",
                "rows": total_rows.get('events_timeline', 0),
                "description": "Structural event timeline aligned to nalex_viz_projection_contract.json — no raw text",
                "primary_keys": ["record_id"],
                "viz_types": ["timeline", "scatter", "line", "bar"],
                "schema_note": "Fields: record_id, timestamp, event_type, speaker_role, phase, loop_type, sequence, move_codes, direct_response_status, repair_response_status, source_review_state, projection_eligibility, privacy_level"
            },
            {
                "name": "theme_metrics",
                "path": "viz_exports/theme_metrics.csv",
                "rows": total_rows.get('theme_metrics', 0),
                "description": "Per-phase/per-speaker message and word counts with extracted themes",
                "primary_keys": ["phase", "speaker"],
                "viz_types": ["bar", "pie", "heatmap"],
                "schema_note": "Fields: phase, speaker, message_count, word_count, theme_count, extracted_themes"
            },
            {
                "name": "phase_profiles",
                "path": "viz_exports/phase_profiles.csv",
                "rows": total_rows.get('phase_profiles', 0),
                "description": "Relationship phase metrics — event counts, session counts, per-speaker breakdowns",
                "primary_keys": ["phase_name"],
                "viz_types": ["bar", "radar", "timeline"],
                "schema_note": "Fields: phase_name, window, calendar_days, event_count, naomi_*/alex_* speaker metrics, asymmetry ratios, flags"
            },
            {
                "name": "gap_analysis",
                "path": "viz_exports/gap_analysis.csv",
                "rows": total_rows.get('gap_analysis', 0),
                "description": "Inter-event silence gaps sorted by duration",
                "primary_keys": ["gap_id"],
                "viz_types": ["bar", "scatter", "histogram"],
                "schema_note": "Fields: gap_id (local_id), event_id, prev_event_id, timestamp, prev_timestamp, gap_seconds, gap_minutes, sha256"
            },
            {
                "name": "orphan_events",
                "path": "viz_exports/orphan_events.csv",
                "rows": total_rows.get('orphan_events', 0),
                "description": "Events without confirmed incident assignment — proposed classifications and review status",
                "primary_keys": ["orphan_id"],
                "viz_types": ["table", "scatter"],
                "schema_note": "Fields: orphan_id, timestamp, session_id, original_assignment, proposed_classification, proposed_parent, confidence, evidence_basis, boundary_or_exclusion_reason, review_status"
            }
        ],
        "schema_version": "v2",
        "contract": "schema/contracts/nalex_viz_projection_contract.json",
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "generated_by": "generate_viz_exports.py",
        "privacy_note": "events_timeline.csv contains NO raw transcript text. All txt/txt_v3/txt_raw_prior fields stripped at export.",
        "column_conventions": {
            "timestamp": "ISO 8601 or YYYY-MM-DD HH:MM:SS from source",
            "speaker_role": "Normalized: alex | naomi | system | unknown",
            "event_type": "From nalex_semantic_schema_v2.md",
            "phase": "Relationship phase identifier (Baseline/Conflict/Silence/Aftermath)",
            "record_id": "Canonical EID from events.jsonl"
        }
    }

    manifest_path = REPO_ROOT / "data" / "viz_manifest.json"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"✓ Wrote viz_manifest.json")


def main():
    """Main export pipeline."""
    print("=" * 60)
    print("Nalex Data Viz Export Pipeline")
    print("=" * 60)
    print(f"Output directory: {DATA_VIZ_EXPORTS}")

    total_rows = {}

    # Run all exports
    total_rows['events_timeline'] = export_events_timeline()
    total_rows['theme_metrics'] = export_theme_metrics()
    total_rows['phase_profiles'] = export_phase_profiles()
    total_rows['gap_analysis'] = export_gap_analysis()
    total_rows['orphan_events'] = export_orphan_events()

    # Generate manifest
    generate_manifest(total_rows)

    # Privacy verification
    print("\n🔒 Privacy verification...")
    events_csv = DATA_VIZ_EXPORTS / "events_timeline.csv"
    leaked = verify_no_raw_text_leak(events_csv)
    if leaked == 0:
        print(f"  ✓ events_timeline.csv: no raw text leak detected")
    elif leaked < 0:
        print(f"  ⚠️  events_timeline.csv not found for verification")
    else:
        print(f"  🚨 events_timeline.csv: {leaked} rows contain raw text keys — REVIEW REQUIRED")

    # Summary
    print("\n" + "=" * 60)
    print("✅ Export Complete!")
    print("=" * 60)
    print(f"Total datasets: {len(total_rows)}")
    print(f"Total rows exported: {sum(total_rows.values())}")
    print("\nFiles created:")
    for name, count in total_rows.items():
        status = "✓" if count > 0 else "⚠️ "
        print(f"  {status} {name}.csv ({count} rows)")
    print(f"  ✓ viz_manifest.json")
    print("\nNext steps:")
    print("  1. Review CSVs in data/viz_exports/")
    print("  2. Run non-empty column validation per file")
    print("  3. Proceed to visualization once all CSVs pass")


if __name__ == "__main__":
    main()
