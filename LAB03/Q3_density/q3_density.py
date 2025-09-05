# q3_density.py

import pandas as pd
import matplotlib
matplotlib.use('Agg')  # For headless environments
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import numpy as np
from collections import Counter

# Data
water = [3.2, 3.5, 3.6, 2.5, 2.8, 5.9, 2.9, 3.9, 4.9, 6.9, 7.9, 8.0, 3.3, 6.6, 4.4]
beverages = [2.2, 2.5, 2.6, 1.5, 3.8, 1.9, 0.9, 3.9, 4.9, 6.9, 0.1, 8.0, 0.3, 2.6, 1.4]

df = pd.DataFrame({"Water": water, "Beverages": beverages})
df.to_csv("consumption_data.csv", index=False)

# Function to calculate statistics
def calculate_stats(data):
    mean = np.mean(data)
    median = np.median(data)
    mode_data = stats.mode(data, keepdims=True)
    mode = mode_data.mode[0] if mode_data.count[0] > 1 else "None"
    skewness = stats.skew(data)
    return mean, median, mode, skewness

# Save statistics
with open("consumption_stats.txt", "w") as f:
    for col in df.columns:
        data = df[col]
        mean, median, mode, skew = calculate_stats(data)
        f.write(f"{col} Consumption Statistics:\n")
        f.write(f"  Mean: {mean:.2f} L\n")
        f.write(f"  Median: {median:.2f} L\n")
        f.write(f"  Mode: {mode} L\n")
        f.write(f"  Skewness: {skew:.2f} ({'Right-skewed' if skew > 0 else 'Left-skewed' if skew < 0 else 'Symmetric'})\n\n")

# Plot density and rug plots
for col in df.columns:
    plt.figure(figsize=(6, 4))
    sns.kdeplot(df[col], fill=True, color="skyblue", alpha=0.6)
    sns.rugplot(df[col], color="black")
    plt.title(f"Density & Rug Plot of {col} Consumption")
    plt.xlabel("Litres")
    plt.ylabel("Density")
    plt.tight_layout()
    plt.savefig(f"density_{col.lower()}.png")
    plt.close()