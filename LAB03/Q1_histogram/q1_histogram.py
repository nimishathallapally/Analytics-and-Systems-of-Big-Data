# q1_histogram.py
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

ages = [7, 9, 27, 28, 55, 45, 34, 65, 54, 67, 34, 23, 24, 66, 53, 45, 44, 88, 22, 33, 55, 35, 33, 37, 47, 41, 31, 30, 29, 12]

# Save data
df = pd.DataFrame({"Age": ages})
df.to_csv("age_data.csv", index=False)

# Plot histograms with different bin sizes
sns.set(style="whitegrid", palette="pastel")
for bins in [5, 10, 15]:
    plt.figure(figsize=(6,4))
    sns.histplot(df["Age"], bins=bins, kde=False, color="skyblue", edgecolor="black")
    plt.title(f"Histogram of Customer Ages (bins={bins})")
    plt.xlabel("Age")
    plt.ylabel("Frequency")
    plt.tight_layout()
    plt.savefig(f"histogram_bins_{bins}.png")
    plt.close()