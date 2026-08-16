#!/usr/bin/env python3
"""
Generate visualization-ready CSV exports from Nalex data pipeline.

This script transforms JSON/JSONL source data into flat CSVs optimized for
Claude Codes data viz plugin consumption.

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


def normalize_timestamp(ts: Any) -> str:
    """Normalize timestamp to ISO 8601 format."""
    if ts is None:
        return ""
    
    # If already ISO string
    if isinstance(ts, str):
        return ts
    
    # If Unix epoch (seconds or milliseconds)
    if isinstance(ts, (int, float)):
        # Detect milliseconds
        if ts > 1e12:
            ts = ts / 1000
        return datetime.utcfromtimestamp(ts).isoformat() + "Z"
    
    return str(ts)


def normalize_speaker(speaker: Any) -> str:
    """Normalize speaker name to lowercase standard form."""
    if speaker is None:
        return "unknown"
    
    speaker = str(speaker).lower().strip()
    
    # Common normalizations
    if speaker in ["alex", "alexis", "user"]:
        return "alex"
    elif speaker in ["naomi", "assistant", "ai"]:
        return "naomi"
    elif speaker in ["system", "meta", "platform"]:
        return "system"
    
    return speaker


# === Export Functions ===

def export_events_timeline() -> int:
    """
    Export events.jsonl to flat CSV with standardized columns.
    
    Columns:
        timestamp, event_id, event_type, speaker, text, phase, loop_id, 
        sentiment_score, metadata_json
    """
    print("\n📊 Exporting events timeline...")
    
    events = load_jsonl(DATA_RAW / "events.jsonl")
    
    rows = []
    for event in events:
        # Extract fields with flexible key names
        row = {
            'timestamp': normalize_timestamp(
                event.get('timestamp') or event.get('timestamp_ms') or event.get('ts')
            ),
            'event_id': event.get('event_id') or event.get('id') or event.get('uuid', ''),
            'event_type': event.get('event_type') or event.get('type') or event.get('category', ''),
            'speaker': normalize_speaker(
                event.get('speaker') or event.get('participant') or event.get('user') or event.get('from', '')
            ),
            'text': event.get('text') or event.get('content') or event.get('message', '') or '',
            'phase': event.get('phase') or event.get('relationship_phase') or event.get('stage', ''),
            'loop_id': event.get('loop_id') or event.get('loop') or event.get('communication_loop', ''),
            'sentiment_score': event.get('sentiment_score') or event.get('sentiment') or event.get('valence', ''),
            'metadata_json': json.dumps({k: v for k, v in event.items() 
                                        if k not in ['timestamp', 'event_id', 'event_type', 
                                                     'speaker', 'text', 'phase', 'loop_id', 
                                                     'sentiment_score', 'id', 'ts', 'type', 
                                                     'category', 'participant', 'user', 'from',
                                                     'content', 'message', 'relationship_phase', 
                                                     'stage', 'communication_loop', 'sentiment', 
                                                     'valence']}, ensure_ascii=False)
        }
        rows.append(row)
    
    fieldnames = ['timestamp', 'event_id', 'event_type', 'speaker', 'text', 
                  'phase', 'loop_id', 'sentiment_score', 'metadata_json']
    
    return save_csv(rows, DATA_VIZ_EXPORTS / "events_timeline.csv", fieldnames)


def export_theme_metrics() -> int:
    """
    Export flattened_themes_metrics.json to CSV.
    
    Expected structure: list of theme objects with metrics
    """
    print("\n📊 Exporting theme metrics...")
    
    data = load_json(DATA_DERIVED / "flattened_themes_metrics.json")
    
    # Handle both list and dict-with-themes structures
    if isinstance(data, dict):
        themes = data.get('themes', data.get('data', []))
    elif isinstance(data, list):
        themes = data
    else:
        print("⚠️  Unexpected theme metrics structure")
        return 0
    
    rows = []
    for theme in themes:
        row = {
            'theme_id': theme.get('theme_id') or theme.get('id') or theme.get('name', ''),
            'theme_name': theme.get('theme_name') or theme.get('name') or theme.get('label', ''),
            'frequency': theme.get('frequency') or theme.get('count') or 0,
            'avg_sentiment': theme.get('avg_sentiment') or theme.get('sentiment_score') or '',
            'speaker_alex_count': theme.get('speaker_alex_count') or theme.get('alex_mentions', 0),
            'speaker_naomi_count': theme.get('speaker_naomi_count') or theme.get('naomi_mentions', 0),
            'phase_distribution': json.dumps(theme.get('phase_distribution', {}), ensure_ascii=False),
            'sample_quotes': json.dumps(theme.get('sample_quotes', []), ensure_ascii=False)
        }
        rows.append(row)
    
    fieldnames = ['theme_id', 'theme_name', 'frequency', 'avg_sentiment', 
                  'speaker_alex_count', 'speaker_naomi_count', 
                  'phase_distribution', 'sample_quotes']
    
    return save_csv(rows, DATA_VIZ_EXPORTS / "theme_metrics.csv", fieldnames)


def export_phase_profiles() -> int:
    """
    Export phase_profile.json to CSV.
    
    Expected structure: dict with phase names as keys, metrics as values
    """
    print("\n📊 Exporting phase profiles...")
    
    data = load_json(DATA_DERIVED / "phase_profile.json")
    
    # Handle structure
    phases = data if isinstance(data, dict) else {}
    
    rows = []
    for phase_name, metrics in phases.items():
        if not isinstance(metrics, dict):
            continue
        
        row = {
            'phase_name': phase_name,
            'start_date': metrics.get('start_date') or metrics.get('start') or '',
            'end_date': metrics.get('end_date') or metrics.get('end') or '',
            'duration_days': metrics.get('duration_days') or metrics.get('duration', 0),
            'event_count': metrics.get('event_count') or metrics.get('events', 0),
            'avg_sentiment': metrics.get('avg_sentiment') or metrics.get('sentiment', ''),
            'conflict_intensity': metrics.get('conflict_intensity') or metrics.get('conflict', ''),
            'communication_frequency': metrics.get('communication_frequency') or metrics.get('frequency', ''),
            'dominant_themes': json.dumps(metrics.get('dominant_themes', []), ensure_ascii=False),
            'description': metrics.get('description') or metrics.get('notes', '')
        }
        rows.append(row)
    
    fieldnames = ['phase_name', 'start_date', 'end_date', 'duration_days', 
                  'event_count', 'avg_sentiment', 'conflict_intensity', 
                  'communication_frequency', 'dominant_themes', 'description']
    
    return save_csv(rows, DATA_VIZ_EXPORTS / "phase_profiles.csv", fieldnames)


def export_gap_analysis() -> int:
    """
    Export gap_stats_out.json to CSV.
    
    Expected structure: dict with gap metrics
    """
    print("\n📊 Exporting gap analysis...")
    
    data = load_json(DATA_DERIVED / "gap_stats_out.json")
    
    # Flatten nested structure
    rows = []
    
    # Handle different possible structures
    if isinstance(data, dict):
        # Try to extract gaps
        gaps = data.get('gaps', data.get('metrics', data))
        
        if isinstance(gaps, dict):
            for gap_name, gap_data in gaps.items():
                if isinstance(gap_data, dict):
                    row = {
                        'gap_name': gap_name,
                        'expected_value': gap_data.get('expected', gap_data.get('expected_value', '')),
                        'actual_value': gap_data.get('actual', gap_data.get('actual_value', '')),
                        'gap_magnitude': gap_data.get('gap', gap_data.get('magnitude', gap_data.get('difference', ''))),
                        'gap_percentage': gap_data.get('gap_pct', gap_data.get('percentage', '')),
                        'category': gap_data.get('category', gap_data.get('type', '')),
                        'priority': gap_data.get('priority', gap_data.get('severity', '')),
                        'notes': gap_data.get('notes', gap_data.get('description', ''))
                    }
                    rows.append(row)
                elif isinstance(gap_data, (int, float, str)):
                    # Simple key-value gap
                    rows.append({
                        'gap_name': gap_name,
                        'actual_value': gap_data,
                        'expected_value': '',
                        'gap_magnitude': '',
                        'gap_percentage': '',
                        'category': '',
                        'priority': '',
                        'notes': ''
                    })
    
    fieldnames = ['gap_name', 'expected_value', 'actual_value', 'gap_magnitude', 
                  'gap_percentage', 'category', 'priority', 'notes']
    
    return save_csv(rows, DATA_VIZ_EXPORTS / "gap_analysis.csv", fieldnames)


def export_orphan_events() -> int:
    """
    Export orphan event mapping CSV from analysis/audits/.
    
    Finds the most recent orphan mapping file and copies it to viz_exports.
    """
    print("\n📊 Exporting orphan events...")
    
    # Find most recent orphan mapping file
    orphan_files = list(ANALYSIS_AUDITS.glob("nalex_orphan_event_mapping_*.csv"))
    
    if not orphan_files:
        print("⚠️  No orphan mapping files found")
        return 0
    
    # Sort by filename (includes date) and get most recent
    latest_orphan = sorted(orphan_files)[-1]
    print(f"  Found: {latest_orphan.name}")
    
    # Read and standardize
    rows = []
    with open(latest_orphan, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Standardize column names
            std_row = {
                'orphan_id': row.get('orphan_id') or row.get('id') or row.get('event_id', ''),
                'timestamp': row.get('timestamp') or row.get('ts', ''),
                'speaker': normalize_speaker(row.get('speaker') or row.get('participant', '')),
                'text': row.get('text') or row.get('content') or row.get('message', ''),
                'orphan_type': row.get('orphan_type') or row.get('type') or row.get('reason', ''),
                'expected_parent': row.get('expected_parent') or row.get('parent_id', ''),
                'expected_child': row.get('expected_child') or row.get('child_id', ''),
                'phase': row.get('phase', ''),
                'notes': row.get('notes') or row.get('comments', '')
            }
            rows.append(std_row)
    
    fieldnames = ['orphan_id', 'timestamp', 'speaker', 'text', 'orphan_type', 
                  'expected_parent', 'expected_child', 'phase', 'notes']
    
    return save_csv(rows, DATA_VIZ_EXPORTS / "orphan_events.csv", fieldnames)


def generate_manifest(total_rows: dict[str, int]) -> None:
    """
    Generate viz_manifest.json indexing all exported datasets.
    """
    print("\n📋 Generating viz manifest...")
    
    manifest = {
        "datasets": [
            {
                "name": "events_timeline",
                "path": "viz_exports/events_timeline.csv",
                "rows": total_rows.get('events_timeline', 0),
                "description": "Flattened event timeline with standardized columns for temporal analysis",
                "primary_keys": ["timestamp", "event_id"],
                "viz_types": ["timeline", "scatter", "line", "bar"]
            },
            {
                "name": "theme_metrics",
                "path": "viz_exports/theme_metrics.csv",
                "rows": total_rows.get('theme_metrics', 0),
                "description": "Communication theme frequency and sentiment metrics",
                "primary_keys": ["theme_id"],
                "viz_types": ["bar", "pie", "heatmap"]
            },
            {
                "name": "phase_profiles",
                "path": "viz_exports/phase_profiles.csv",
                "rows": total_rows.get('phase_profiles', 0),
                "description": "Relationship phase characteristics and metrics",
                "primary_keys": ["phase_name"],
                "viz_types": ["bar", "radar", "timeline"]
            },
            {
                "name": "gap_analysis",
                "path": "viz_exports/gap_analysis.csv",
                "rows": total_rows.get('gap_analysis', 0),
                "description": "Expected vs actual communication pattern gaps",
                "primary_keys": ["gap_name"],
                "viz_types": ["bar", "scatter", "bullet"]
            },
            {
                "name": "orphan_events",
                "path": "viz_exports/orphan_events.csv",
                "rows": total_rows.get('orphan_events', 0),
                "description": "Events without proper parent/child relationships in timeline",
                "primary_keys": ["orphan_id"],
                "viz_types": ["table", "scatter"]
            }
        ],
        "schema_version": "v2",
        "last_updated": datetime.utcnow().isoformat() + "Z",
        "generated_by": "generate_viz_exports.py",
        "column_conventions": {
            "timestamp": "ISO 8601 format (YYYY-MM-DDTHH:MM:SSZ)",
            "speaker": "Normalized: alex | naomi | system | unknown",
            "event_type": "From nalex_semantic_schema_v2.md",
            "phase": "Relationship phase identifier",
            "loop_id": "Communication loop identifier (if applicable)"
        },
        "usage_examples": [
            "Load events_timeline.csv to visualize communication patterns over time",
            "Join theme_metrics with phase_profiles to analyze theme distribution by phase",
            "Filter orphan_events by orphan_type to identify specific timeline gaps",
            "Compare gap_analysis expected vs actual values to prioritize interventions"
        ]
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
    
    # Summary
    print("\n" + "=" * 60)
    print("✅ Export Complete!")
    print("=" * 60)
    print(f"Total datasets: {len(total_rows)}")
    print(f"Total rows exported: {sum(total_rows.values())}")
    print("\nFiles created:")
    for name, count in total_rows.items():
        print(f"  - {name}.csv ({count} rows)")
    print(f"  - viz_manifest.json")
    print("\nNext steps:")
    print("  1. Review CSVs in data/viz_exports/")
    print("  2. Load into Claude Codes for visualization")
    print("  3. Reference viz_manifest.json for dataset metadata")


if __name__ == "__main__":
    main()
