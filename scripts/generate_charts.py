import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

os.makedirs('visualizations/outputs', exist_ok=True)

print("Loading data...")
events_df = pd.read_csv('data/viz_exports/events_timeline.csv')
theme_df = pd.read_csv('data/viz_exports/theme_metrics.csv')
phase_df = pd.read_csv('data/viz_exports/phase_profiles.csv')

print("1. Communication Timeline by Speaker")
# Ensure timestamp is datetime
events_df['timestamp'] = pd.to_datetime(events_df['timestamp'])

# Create a scatter/timeline plot
fig1 = px.scatter(
    events_df, 
    x='timestamp', 
    y='event_type', 
    color='speaker',
    title="Communication Timeline by Speaker",
    hover_data=['text', 'phase']
)
fig1.write_html('visualizations/outputs/communication_timeline.html')

print("4. Theme Frequency Distribution")
# Bar chart showing theme frequency
fig4 = go.Figure(data=[
    go.Bar(name='Alex', x=theme_df['theme_name'], y=theme_df['speaker_alex_count']),
    go.Bar(name='Naomi', x=theme_df['theme_name'], y=theme_df['speaker_naomi_count'])
])
fig4.update_layout(barmode='stack', title="Theme Frequency Distribution by Speaker")
fig4.write_html('visualizations/outputs/theme_frequency.html')

print("3. Phase Duration Comparison")
# Horizontal bar chart for phase durations
fig3 = px.bar(
    phase_df,
    y='phase_name',
    x='duration_days',
    orientation='h',
    color='avg_sentiment',
    color_continuous_scale=['red', 'yellow', 'green'],
    title="Phase Duration and Sentiment"
)
fig3.write_html('visualizations/outputs/phase_duration.html')

print("All charts generated successfully in visualizations/outputs/")
