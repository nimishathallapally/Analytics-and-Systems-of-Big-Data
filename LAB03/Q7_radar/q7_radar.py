# q7_radar.py
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

categories = ["Textile", "Jewellery", "Cleaning Essentials", "Cosmetics"]
data = {
    "Q1": [10, 5, 15, 14],
    "Q2": [6, 5, 20, 10],
    "Q3": [8, 2, 16, 21],
    "Q4": [13, 4, 15, 11]
}
df = pd.DataFrame(data, index=categories)
df.to_csv("ads_data.csv")

# Radar chart
labels = list(df.index)
angles = np.linspace(0, 2*np.pi, len(labels), endpoint=False).tolist()
angles += angles[:1]

plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)

for quarter in df.columns:
    values = df[quarter].tolist()
    values += values[:1]
    ax.plot(angles, values, label=quarter)
    ax.fill(angles, values, alpha=0.25)

ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)
plt.title("Radar Chart - Ads Developed per Quarter")
plt.legend(loc="upper right", bbox_to_anchor=(1.2, 1.1))
plt.tight_layout()
plt.savefig("radar_chart.png")
plt.close()