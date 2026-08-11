import matplotlib.pyplot as plt
import numpy as np
import os

# Professional style setup based on data-visualization skill
plt.style.use('seaborn-v0_8-whitegrid')
plt.rcParams.update({
    'figure.figsize': (8, 5),
    'figure.dpi': 150,
    'font.size': 11,
    'axes.titlesize': 14,
    'axes.titleweight': 'bold',
    'axes.labelsize': 11,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10,
    'figure.titlesize': 16,
})

# Colorblind-friendly palettes / M3 Dark Mode aligned
# Naomi: Purple/Blueish, Alex: Orange/Brownish
COLOR_NAOMI = '#87719d'
COLOR_ALEX = '#5f7f96'

out_dir = os.path.dirname(os.path.abspath(__file__))

def create_volume_chart():
    labels = ['Baseline', 'Conflict', 'Aftermath']
    naomi_med = [44.5, 39.5, 66.0]
    alex_med = [31.5, 21.0, 26.0]

    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots(figsize=(8, 4))
    
    # Draw bars
    rects1 = ax.bar(x - width/2, naomi_med, width, label='Naomi', color=COLOR_NAOMI)
    rects2 = ax.bar(x + width/2, alex_med, width, label='Alex', color=COLOR_ALEX)

    ax.set_ylabel('Median Words per Turn')
    ax.set_title('Turn Length by Phase', fontweight='bold')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend(frameon=True)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add labels
    ax.bar_label(rects1, padding=3, fmt='%.1f')
    ax.bar_label(rects2, padding=3, fmt='%.1f')

    fig.tight_layout()
    plt.savefig(os.path.join(out_dir, 'volume_chart.svg'), transparent=True)
    plt.close()

def create_latency_chart():
    labels = ['Baseline', 'Conflict', 'Aftermath']
    naomi_speed = [484, 120, 169]
    alex_speed = [101, 94, 122]

    x = np.arange(len(labels))

    fig, ax = plt.subplots(figsize=(8, 4))
    
    ax.plot(labels, naomi_speed, marker='o', label='Naomi', color=COLOR_NAOMI, linewidth=2.5)
    ax.plot(labels, alex_speed, marker='o', label='Alex', color=COLOR_ALEX, linewidth=2.5)

    ax.set_ylabel('Median Reply Time (Seconds)')
    ax.set_title('Reply Speed by Phase', fontweight='bold')
    ax.legend(frameon=True)
    
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    for i, txt in enumerate(naomi_speed):
        ax.annotate(f"{txt}s", (x[i], naomi_speed[i]), textcoords="offset points", xytext=(0,10), ha='center', color=COLOR_NAOMI, fontweight='bold')
    for i, txt in enumerate(alex_speed):
        ax.annotate(f"{txt}s", (x[i], alex_speed[i]), textcoords="offset points", xytext=(0,-15), ha='center', color=COLOR_ALEX, fontweight='bold')

    fig.tight_layout()
    plt.savefig(os.path.join(out_dir, 'latency_chart.svg'), transparent=True)
    plt.close()

def create_unanswered_chart():
    # Conflict unanswered (content judgment)
    labels = ['Naomi', 'Alex']
    answered = [39 - 8, 44 - 15]
    unanswered = [8, 15]

    x = np.arange(len(labels))
    width = 0.5

    fig, ax = plt.subplots(figsize=(8, 4))
    
    ax.bar(labels, answered, width, label='Answered', color='#4C72B0')
    ax.bar(labels, unanswered, width, bottom=answered, label='Unanswered', color='#C44E52')

    ax.set_ylabel('Questions Count')
    ax.set_title('Questions Unanswered (Conflict Phase)', fontweight='bold')
    ax.legend(frameon=True)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    fig.tight_layout()
    plt.savefig(os.path.join(out_dir, 'unanswered_chart.svg'), transparent=True)
    plt.close()

if __name__ == '__main__':
    create_volume_chart()
    create_latency_chart()
    create_unanswered_chart()
    print("Charts generated.")
