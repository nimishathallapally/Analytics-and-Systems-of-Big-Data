import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

data = {
    "Step": ["Requirement Elicitation", "Requirement Analysis", "Software Development", "Debugging & Testing", "Others"],
    "Hours": [50, 110, 250, 180, 70]
}
df = pd.DataFrame(data)

# Sort data by Hours descending (funnel top to bottom)
df = df.sort_values(by="Hours", ascending=False).reset_index(drop=True)

# Normalize widths for funnel shape
max_hours = df["Hours"].max()
widths = df["Hours"] / max_hours

fig, ax = plt.subplots(figsize=(6, 5))

# Parameters to position bars horizontally centered
y_pos = range(len(df))
bar_height = 0.8

for i, (step, width) in enumerate(zip(df["Step"], widths)):
    # Bar width scaled, centered at 0.5 (to look like funnel)
    left = 0.5 - width / 2
    ax.barh(i, width, height=bar_height, left=left, color="skyblue", edgecolor="black")
    ax.text(0.5, i, f"{step} ({df['Hours'][i]} hrs)", va='center', ha='center', fontsize=9, color='black')

# Remove axes details
ax.set_yticks([])
ax.set_xticks([])
ax.set_xlim(0,1)
ax.invert_yaxis()
ax.set_title("Funnel Chart - Product Development Steps", fontsize=14)

plt.tight_layout()
plt.savefig("funnel_chart.png")
plt.close()