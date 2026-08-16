# Data Viz Quick Start Guide

## Overview

This pipeline transforms Nalex relationship data into CSV format optimized for **Claude Codes data viz plugin**.

## Step 1: Generate CSV Exports

From the repo root:

```bash
python scripts/generate_viz_exports.py
```

**Output:**
- `data/viz_exports/events_timeline.csv`
- `data/viz_exports/theme_metrics.csv`
- `data/viz_exports/phase_profiles.csv`
- `data/viz_exports/gap_analysis.csv`
- `data/viz_exports/orphan_events.csv`
- `data/viz_manifest.json` (auto-generated index)

## Step 2: Load into Claude Codes

1. Open Claude Codes with data viz plugin enabled
2. Load any CSV from `data/viz_exports/`
3. Reference `data/viz_manifest.json` for column documentation

## Step 3: Run Visualizations

See `docs/viz_artifact_ideas.md` for 15+ ready-to-use prompt templates.

**Example prompts:**

> "Create a timeline showing all events colored by speaker (Alex vs Naomi)"

> "Plot sentiment_score over time as a line chart with separate lines for each speaker"

> "Create a bar chart comparing expected_value vs actual_value from gap_analysis.csv"

## Data Flow

```
data/raw/events.jsonl          ──┐
data/derived/*.json              ├──> generate_viz_exports.py ──> data/viz_exports/*.csv
analysis/audits/*orphan*.csv    ──┘                                      │
                                                                         ↓
                                                                  Claude Codes Data Viz
                                                                         │
                                                                         ↓
                                                                  visualizations/outputs/
```

## Column Standards

All CSVs follow these conventions:

| Column | Format | Values |
|--------|--------|--------|
| `timestamp` | ISO 8601 | `2026-08-16T12:19:08Z` |
| `speaker` | normalized | `alex`, `naomi`, `system`, `unknown` |
| `event_type` | schema | From `schema/nalex_semantic_schema_v2.md` |
| `phase` | string | Relationship phase identifier |
| `loop_id` | string | Communication loop ID (if applicable) |

## Refresh Data

When source data changes:

```bash
# Regenerate all CSVs
python scripts/generate_viz_exports.py

# Verify manifest
cat data/viz_manifest.json
```

## Troubleshooting

**No data in CSVs:**
- Check source files exist in `data/raw/` and `data/derived/`
- Run script and check for warning messages

**Wrong column names:**
- Script uses flexible key mapping (tries multiple field names)
- Check `metadata_json` column for unmapped fields

**Orphan events outdated:**
- Script picks most recent `analysis/audits/nalex_orphan_event_mapping_*.csv`
- Generate new orphan mapping first if needed

## Next Steps

1. ✅ Generate CSVs (done)
2. ⏳ Load into Claude Codes
3. ⏳ Create visualizations from `docs/viz_artifact_ideas.md`
4. ⏳ Save outputs to `visualizations/outputs/`
5. ⏳ Commit successful viz artifacts

---

**Files added in this commit:**
- `scripts/generate_viz_exports.py` - Export pipeline
- `data/viz_exports/README.md` - Dataset documentation
- `docs/viz_artifact_ideas.md` - Visualization prompts
- `.gitignore` - Updated to exclude generated CSVs

**Commit:** `55dfd6e` - "feat: add data viz export pipeline for Claude Codes"
