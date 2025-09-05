# q2_stem_leaf.py

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from collections import defaultdict

# Data
points = [22, 21, 24, 19, 27, 28, 24, 25, 29, 28, 26, 31, 28, 27, 22, 39, 20,
          10, 26, 24, 27, 28, 26, 28, 18, 32, 29, 25, 31, 27]

# Save raw data
df = pd.DataFrame({"Points": points})
df.to_csv("points_data.csv", index=False)

# 1. Ordered Stem-and-Leaf Plot (Text Output)
stem_leaf = defaultdict(list)

for p in sorted(points):
    stem = p // 10
    leaf = p % 10
    stem_leaf[stem].append(leaf)

with open("stem_leaf.txt", "w") as f:
    f.write("Stem | Leaves\n")
    f.write("--------------\n")
    for stem in sorted(stem_leaf):
        leaves = " ".join(str(leaf) for leaf in sorted(stem_leaf[stem]))
        f.write(f" {stem}   | {leaves}\n")

# 2. Boxplot for Outlier Detection
sns.set(style="whitegrid", palette="pastel")
plt.figure(figsize=(6, 4))
sns.boxplot(x=df["Points"], color="lightpink")
plt.title("Boxplot of Player Points (Outlier Detection)")
plt.tight_layout()
plt.savefig("boxplot_points.png")
plt.close()

# 3. Histogram for Distribution Shape
plt.figure(figsize=(6, 4))
sns.histplot(df["Points"], bins=8, kde=True, color="skyblue")
plt.title("Histogram of Player Points")
plt.xlabel("Points")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_points.png")
plt.close()