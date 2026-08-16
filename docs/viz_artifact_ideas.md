# Visualization Artifact Ideas

Prompt templates and analysis queries for Claude Codes data viz plugin.

## Timeline Visualizations

### 1. Communication Timeline by Speaker
**Load:** `events_timeline.csv`

**Prompt:**
> Create a timeline visualization showing all events colored by speaker (Alex vs Naomi). Use timestamp on the x-axis and event_type on the y-axis. Add phase boundaries as vertical bands.

**Insights:**
- Communication frequency patterns
- Speaker dominance over time
- Phase transitions

### 2. Sentiment Trajectory
**Load:** `events_timeline.csv`

**Prompt:**
> Plot sentiment_score over time as a line chart, with separate lines for Alex and Naomi. Add a moving average trendline (window=10 events).

**Insights:**
- Emotional convergence/divergence
- Sentiment volatility
- Recovery patterns after conflict

### 3. Phase Duration Comparison
**Load:** `phase_profiles.csv`

**Prompt:**
> Create a horizontal bar chart showing duration_days for each phase, ordered chronologically. Color-code by avg_sentiment (green=positive, red=negative).

**Insights:**
- Phase stability
- Emotional tone by phase
- Relationship evolution pace

## Theme Analysis

### 4. Theme Frequency Distribution
**Load:** `theme_metrics.csv`

**Prompt:**
> Create a sorted bar chart showing theme frequency (count) for all themes. Add speaker_alex_count and speaker_naomi_count as stacked bars within each theme.

**Insights:**
- Dominant communication topics
- Speaker-specific theme preferences
- Theme balance

### 5. Theme Sentiment Heatmap
**Load:** `theme_metrics.csv`

**Prompt:**
> Create a heatmap with themes on the y-axis and speakers on the x-axis. Color cells by avg_sentiment (or speaker-specific sentiment if available).

**Insights:**
- Emotional valence by topic
- Speaker disagreement on themes
- Sensitive topics

### 6. Theme Distribution by Phase
**Load:** `theme_metrics.csv` (parse phase_distribution JSON)

**Prompt:**
> Parse the phase_distribution column and create a stacked area chart showing theme frequency across phases.

**Insights:**
- Theme evolution over relationship stages
- Phase-specific communication patterns

## Gap Analysis

### 7. Expected vs Actual Communication
**Load:** `gap_analysis.csv`

**Prompt:**
> Create a bullet chart or paired bar chart comparing expected_value vs actual_value for each gap. Color by priority (red=high, yellow=medium, green=low).

**Insights:**
- Communication deficits
- Priority intervention areas
- Progress toward relationship goals

### 8. Gap Magnitude Scatter
**Load:** `gap_analysis.csv`

**Prompt:**
> Create a scatter plot with gap_magnitude on the x-axis and priority on the y-axis. Size points by gap_percentage.

**Insights:**
- High-impact gaps
- Prioritization matrix
- Quick wins vs major work

## Orphan Event Analysis

### 9. Orphan Event Timeline
**Load:** `orphan_events.csv`

**Prompt:**
> Plot orphan events on a timeline, colored by orphan_type. Add annotations for expected_parent and expected_child where available.

**Insights:**
- Timeline gaps
- Missing context
- Data quality issues

### 10. Orphan Type Distribution
**Load:** `orphan_events.csv`

**Prompt:**
> Create a pie chart or bar chart showing the count of each orphan_type.

**Insights:**
- Most common data quality issues
- Systematic gaps in conversation flow

## Advanced Composite Visualizations

### 11. Multi-Metric Dashboard
**Load:** All CSVs

**Prompt:**
> Create a 2x2 dashboard:
> - Top-left: Events timeline (line chart by speaker)
> - Top-right: Theme frequency (bar chart)
> - Bottom-left: Phase sentiment (radar chart)
> - Bottom-right: Gap analysis (bullet chart)

**Insights:**
- Holistic relationship state
- Cross-metric correlations

### 12. Communication Loop Sankey
**Load:** `events_timeline.csv` (filter where loop_id is not empty)

**Prompt:**
> Create a Sankey diagram showing flow between loop_id values. Width = event count.

**Insights:**
- Recurring communication patterns
- Loop resolution rates
- Stuck loops

### 13. Speaker Interaction Network
**Load:** `events_timeline.csv`

**Prompt:**
> Create a network graph where nodes are speakers and edges represent event sequences (A→B messages). Weight edges by frequency.

**Insights:**
- Communication reciprocity
- Dominant interaction patterns
- Third-party dynamics (if system participant)

## Intervention Planning

### 14. Priority Intervention Matrix
**Load:** `gap_analysis.csv`, `phase_profiles.csv`

**Prompt:**
> Create a 2x2 matrix with:
> - X-axis: gap_magnitude
> - Y-axis: phase avg_sentiment (inverse, so negative sentiment = high priority)
> - Quadrant labels: "Urgent", "Monitor", "Maintain", "Low Priority"

**Insights:**
- Where to focus intervention efforts
- Risk assessment

### 15. Theme-Based Intervention Targets
**Load:** `theme_metrics.csv`

**Prompt:**
> Create a scatter plot with frequency on x-axis and avg_sentiment on y-axis. Size points by (speaker_alex_count - speaker_naomi_count) absolute difference.

**Insights:**
- High-frequency negative themes (intervention targets)
- Imbalanced themes (need for perspective-taking)
- Positive themes to reinforce

## Usage Notes

1. **Load data first:** Always load the relevant CSV(s) before running visualization prompts.

2. **Reference manifest:** Check `viz_manifest.json` for column names and data types.

3. **Iterate:** Start with simple charts, then add complexity (filters, aggregations, annotations).

4. **Export:** Save successful visualizations as artifacts in `artifacts/` or `visualizations/outputs/`.

5. **Update:** Re-run `generate_viz_exports.py` when source data changes, then regenerate visualizations.

---

*Last updated: 2026-08-16*
