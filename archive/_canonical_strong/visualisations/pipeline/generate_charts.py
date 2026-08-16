"""
Nalex Chart Generator (Dark Surface Only)

Generates SVG charts (volume, latency, unanswered questions) for the Nalex visualization stack.
This script reads metric values directly from canonical JSON data sources (`phase_profile.json`
and `nalex_viz_schema.json`) to prevent drift.

Design stance:
- Dark-surface-only by design: axis labels, titles, grids, and annotations use Material 3 dark surface tokens.
- SVGs preserve transparent backgrounds for dark container embedding.
- Palette: Alex (#3F8AD8, blue) and Naomi (#CC7F30, orange) match the HTML evidence views.
- Silence phase ("No exchanges recorded") is rendered explicitly on all phase-based charts.
"""

import json
import os
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# Color Definitions & Theme Setup (M3 Dark Surface Aligned)
# -----------------------------------------------------------------------------

# Speaker colors matching --series-alex and --series-naomi in evidence views
COLOR_ALEX = '#3F8AD8'   # Blue
COLOR_NAOMI = '#CC7F30'  # Orange

# Answered/Unanswered palette (unchanged, distinct semantic axis)
COLOR_ANSWERED = '#4C72B0'
COLOR_UNANSWERED = '#C44E52'

# Text / Muted colors
COLOR_TEXT_MAIN = '#E2E2E9'    # --on-surface
COLOR_TEXT_MUTED = '#C3C7D3'   # --on-surface-variant
COLOR_GRID = '#3B434F'         # --outline
COLOR_DIM = '#90909A'          # --on-surface-dim

# Configure matplotlib rcParams for dark surface rendering
plt.style.use('default')
plt.rcParams.update({
    'figure.facecolor': 'none',
    'axes.facecolor': 'none',
    'savefig.facecolor': 'none',
    'text.color': COLOR_TEXT_MUTED,
    'axes.labelcolor': COLOR_TEXT_MUTED,
    'axes.edgecolor': COLOR_GRID,
    'xtick.color': COLOR_TEXT_MUTED,
    'ytick.color': COLOR_TEXT_MUTED,
    'grid.color': COLOR_GRID,
    'grid.alpha': 0.4,
    'grid.linewidth': 0.8,
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.titlecolor': COLOR_TEXT_MAIN,
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'legend.facecolor': 'none',
    'legend.edgecolor': 'none',
    'legend.labelcolor': COLOR_TEXT_MUTED,
    'figure.titlesize': 16,
})

# -----------------------------------------------------------------------------
# Paths & Data Sourcing Block
# -----------------------------------------------------------------------------

def find_repo_root():
    cur = os.path.dirname(os.path.abspath(__file__))
    for _ in range(5):
        if os.path.exists(os.path.join(cur, '_canonical_strong')):
            return cur
        parent = os.path.dirname(cur)
        if parent == cur:
            break
        cur = parent
    return os.getcwd()

repo_root = find_repo_root()

phase_profile_path = os.path.join(repo_root, '_canonical_strong', 'data', 'derived_metrics', 'phase_profile.json')
viz_schema_path = os.path.join(repo_root, '_canonical_strong', 'visualisations', 'schemas', 'nalex_viz_schema.json')

script_dir = os.path.join(repo_root, '_canonical_strong', 'visualisations', 'pipeline')
outputs_dir = os.path.join(repo_root, '_canonical_strong', 'visualisations', 'outputs')

def load_canonical_data():
    with open(phase_profile_path, 'r', encoding='utf-8') as f:
        phase_profile = json.load(f)
    with open(viz_schema_path, 'r', encoding='utf-8') as f:
        viz_schema = json.load(f)
    return phase_profile, viz_schema

phase_profile_data, viz_schema_data = load_canonical_data()

PHASES = ['Baseline', 'Conflict', 'Silence', 'Aftermath']

def save_chart(fig, filename):
    fig.tight_layout()
    path_pipeline = os.path.join(script_dir, filename)
    fig.savefig(path_pipeline, transparent=True)
    
    if os.path.exists(outputs_dir):
        path_outputs = os.path.join(outputs_dir, filename)
        fig.savefig(path_outputs, transparent=True)
        
    plt.close(fig)

def parse_range(val):
    if val is None or (isinstance(val, float) and np.isnan(val)):
        return np.nan, np.nan
    if isinstance(val, (int, float)):
        return float(val), float(val)
    if isinstance(val, str):
        if '-' in val:
            parts = val.split('-')
            return float(parts[0]), float(parts[1])
        return float(val), float(val)
    return np.nan, np.nan

# -----------------------------------------------------------------------------
# 1. Volume Chart
# -----------------------------------------------------------------------------

def create_volume_chart():
    phases_dict = phase_profile_data['phases']
    
    naomi_vals = []
    alex_vals = []
    
    for p in PHASES:
        p_data = phases_dict.get(p, {})
        speakers = p_data.get('speakers') or {}
        n_spk = speakers.get('Naomi')
        a_spk = speakers.get('Alex')
        
        naomi_vals.append(n_spk['median_words_per_turn'] if n_spk else np.nan)
        alex_vals.append(a_spk['median_words_per_turn'] if a_spk else np.nan)

    x = np.arange(len(PHASES))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 4.5))
    
    # Grid lines on Y axis only
    ax.yaxis.grid(True)
    ax.xaxis.grid(False)

    # Draw bars
    naomi_bars = [v if not np.isnan(v) else 0 for v in naomi_vals]
    alex_bars = [v if not np.isnan(v) else 0 for v in alex_vals]

    rects1 = ax.bar(x - width/2, naomi_bars, width, label='Naomi', color=COLOR_NAOMI)
    rects2 = ax.bar(x + width/2, alex_bars, width, label='Alex', color=COLOR_ALEX)

    ax.set_ylabel('Median Words per Turn')
    ax.set_title('Turn Length by Phase', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(PHASES)
    ax.legend(frameon=False)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    # Custom labels to avoid printing 0 or nan for Silence
    for i, rect in enumerate(rects1):
        if not np.isnan(naomi_vals[i]):
            h = rect.get_height()
            ax.annotate(f'{naomi_vals[i]:.1f}',
                        xy=(rect.get_x() + rect.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', color=COLOR_TEXT_MUTED)

    for i, rect in enumerate(rects2):
        if not np.isnan(alex_vals[i]):
            h = rect.get_height()
            ax.annotate(f'{alex_vals[i]:.1f}',
                        xy=(rect.get_x() + rect.get_width() / 2, h),
                        xytext=(0, 3), textcoords="offset points",
                        ha='center', va='bottom', color=COLOR_TEXT_MUTED)

    # Annotate Silence
    silence_idx = PHASES.index('Silence')
    max_y = max([v for v in naomi_vals + alex_vals if not np.isnan(v)])
    ax.text(silence_idx, max_y * 0.4, 'No exchanges recorded',
            ha='center', va='center', color=COLOR_DIM, fontstyle='italic', fontsize=10)

    save_chart(fig, 'volume_chart.svg')

# -----------------------------------------------------------------------------
# 2. Latency Chart
# -----------------------------------------------------------------------------

def create_latency_chart():
    # Source latency records from viz_schema
    records = viz_schema_data.get('artifact_2_latency_convergence', {}).get('records', [])
    
    latency_map = {
        'Naomi': {p: (np.nan, np.nan) for p in PHASES},
        'Alex': {p: (np.nan, np.nan) for p in PHASES}
    }
    
    for r in records:
        spk = r.get('speaker')
        phase = r.get('phase')
        if spk in latency_map and phase in PHASES:
            val = r.get('metric', {}).get('value')
            latency_map[spk][phase] = parse_range(val)

    naomi_lows, naomi_highs = zip(*[latency_map['Naomi'][p] for p in PHASES])
    alex_lows, alex_highs = zip(*[latency_map['Alex'][p] for p in PHASES])
    
    naomi_lows = np.array(naomi_lows, dtype=float)
    naomi_highs = np.array(naomi_highs, dtype=float)
    naomi_mids = (naomi_lows + naomi_highs) / 2.0

    alex_lows = np.array(alex_lows, dtype=float)
    alex_highs = np.array(alex_highs, dtype=float)
    alex_mids = (alex_lows + alex_highs) / 2.0

    x = np.arange(len(PHASES))

    fig, ax = plt.subplots(figsize=(8, 4.5))
    
    ax.yaxis.grid(True)
    ax.xaxis.grid(False)

    # Fill ranges for Conflict or any span where low != high
    naomi_has_range = ~np.isnan(naomi_lows) & (naomi_lows != naomi_highs)
    alex_has_range = ~np.isnan(alex_lows) & (alex_lows != alex_highs)

    if np.any(naomi_has_range):
        ax.fill_between(x, naomi_lows, naomi_highs, color=COLOR_NAOMI, alpha=0.25, where=naomi_has_range)
    if np.any(alex_has_range):
        ax.fill_between(x, alex_lows, alex_highs, color=COLOR_ALEX, alpha=0.25, where=alex_has_range)

    # Plot lines (matplotlib automatically breaks at np.nan for Silence)
    ax.plot(x, naomi_mids, marker='o', label='Naomi', color=COLOR_NAOMI, linewidth=2.5)
    ax.plot(x, alex_mids, marker='o', label='Alex', color=COLOR_ALEX, linewidth=2.5)

    ax.set_ylabel('Median Reply Time (Seconds)')
    ax.set_title('Reply Speed by Phase', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(PHASES)
    ax.legend(frameon=False)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    # Annotations with nan guards
    for i in range(len(PHASES)):
        if not np.isnan(naomi_mids[i]):
            if naomi_lows[i] != naomi_highs[i]:
                lbl = f"{int(naomi_lows[i])}–{int(naomi_highs[i])}s\n(med conf)"
            else:
                lbl = f"{int(naomi_mids[i])}s"
            ax.annotate(lbl, (x[i], naomi_highs[i]), textcoords="offset points",
                        xytext=(0, 8), ha='center', color=COLOR_NAOMI, fontweight='bold', fontsize=9)

        if not np.isnan(alex_mids[i]):
            if alex_lows[i] != alex_highs[i]:
                lbl = f"{int(alex_lows[i])}–{int(alex_highs[i])}s\n(med conf)"
            else:
                lbl = f"{int(alex_mids[i])}s"
            ax.annotate(lbl, (x[i], alex_lows[i]), textcoords="offset points",
                        xytext=(0, -22), ha='center', color=COLOR_ALEX, fontweight='bold', fontsize=9)

    # Annotate Silence
    silence_idx = PHASES.index('Silence')
    ax.text(silence_idx, 250, 'No exchanges recorded',
            ha='center', va='center', color=COLOR_DIM, fontstyle='italic', fontsize=10)

    save_chart(fig, 'latency_chart.svg')

# -----------------------------------------------------------------------------
# 3. Unanswered Questions Chart
# -----------------------------------------------------------------------------

def create_unanswered_chart():
    conflict_spk = phase_profile_data['phases']['Conflict']['speakers']
    
    naomi_q = conflict_spk['Naomi']['questions']
    naomi_unans_doc = conflict_spk['Naomi']['unanswered_documented']
    naomi_unans_rep = conflict_spk['Naomi']['unanswered_reproducible_10min_in_session']
    
    alex_q = conflict_spk['Alex']['questions']
    alex_unans_doc = conflict_spk['Alex']['unanswered_documented']
    alex_unans_rep = conflict_spk['Alex']['unanswered_reproducible_10min_in_session']

    speakers = ['Naomi', 'Alex']
    answered_doc = [naomi_q - naomi_unans_doc, alex_q - alex_unans_doc]
    unanswered_doc = [naomi_unans_doc, alex_unans_doc]

    x = np.arange(len(speakers))
    width = 0.45

    fig, ax = plt.subplots(figsize=(8, 4.8))
    
    ax.yaxis.grid(True)
    ax.xaxis.grid(False)

    rects1 = ax.bar(speakers, answered_doc, width, label='Answered', color=COLOR_ANSWERED)
    rects2 = ax.bar(speakers, unanswered_doc, width, bottom=answered_doc, label='Unanswered', color=COLOR_UNANSWERED)

    ax.set_ylabel('Questions Count')
    ax.set_title('Questions Unanswered (Conflict Phase)', fontweight='bold')
    ax.legend(frameon=False)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(True)
    ax.spines['bottom'].set_visible(True)

    # Bar labels
    for i, (ans, unans) in enumerate(zip(answered_doc, unanswered_doc)):
        ax.annotate(f"{ans}", xy=(x[i], ans / 2.0), ha='center', va='center', color='#FFFFFF', fontweight='bold')
        ax.annotate(f"{unans}", xy=(x[i], ans + unans / 2.0), ha='center', va='center', color='#FFFFFF', fontweight='bold')

    # Footnote line for reproducible timing rule comparison
    footnote_text = f"10-min timing rule counterpart: Naomi {naomi_unans_rep} of {naomi_q}, Alex {alex_unans_rep} of {alex_q}"
    fig.text(0.5, 0.02, footnote_text, ha='center', color=COLOR_TEXT_MUTED, fontsize=9.5, fontstyle='italic')

    # Adjust layout to make room for footnote
    fig.subplots_adjust(bottom=0.15)
    save_chart(fig, 'unanswered_chart.svg')

# -----------------------------------------------------------------------------
# Main Execution
# -----------------------------------------------------------------------------

if __name__ == '__main__':
    create_volume_chart()
    create_latency_chart()
    create_unanswered_chart()
    print("Charts generated successfully.")
