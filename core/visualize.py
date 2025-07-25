import json
import os
from collections import Counter
from datetime import datetime
import plotly.graph_objs as go

def plot_browser_activity(json_path, output_path):
    if not os.path.exists(json_path):
        print(f"[ERROR] {json_path} not found.")
        return

    with open(json_path, 'r') as file:
        data = json.load(file)

    timestamps = [entry['timestamp'] for entry in data if 'timestamp' in entry]
    if not timestamps:
        print("[INFO] No timestamps found.")
        return

    # Convert to datetime.date and count visits per day
    dates = [datetime.fromisoformat(ts).date() for ts in timestamps]
    counter = Counter(dates)
    sorted_dates = sorted(counter.items())

    x = [str(date) for date, _ in sorted_dates]
    y = [count for _, count in sorted_dates]

    # Build Plotly graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=x, y=y, mode='lines+markers', name='Visits'))

    fig.update_layout(
        title="📅 Browser Activity Timeline",
        xaxis_title="Date",
        yaxis_title="Number of Visits",
        template="plotly_dark"
    )

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.write_html(output_path)
    print(f"[+] Timeline visualization saved to {output_path}")
