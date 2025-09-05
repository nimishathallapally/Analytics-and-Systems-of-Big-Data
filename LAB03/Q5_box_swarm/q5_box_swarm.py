# q5_box_swarm.py

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Data
chairs = [35, 54, 60, 65, 66, 67, 69, 70, 72, 73, 75, 76,
          54, 25, 15, 60, 65, 66, 67, 69, 70, 72, 130, 73, 75, 76]

# DataFrame
df = pd.DataFrame({"Chairs": chairs})
df.to_csv("chairs_data.csv", index=False)

# --- BOX PLOT ---
sns.set(style="whitegrid", palette="pastel")
plt.figure(figsize=(6, 4))
sns.boxplot(x="Chairs", data=df, color="lightblue")
plt.title("Box Plot of Chairs in Classes")
plt.tight_layout()
plt.savefig("boxplot_chairs.png")
plt.close()

# --- SWARM PLOT ---
plt.figure(figsize=(6, 4))
sns.swarmplot(x="Chairs", data=df, color="darkblue", alpha=0.7)
plt.title("Swarm Plot of Chairs in Classes")
plt.tight_layout()
plt.savefig("swarmplot_chairs.png")
plt.close()

# --- OUTLIER DETECTION (IQR method) ---
Q1 = np.percentile(chairs, 25)
Q3 = np.percentile(chairs, 75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = [x for x in chairs if x < lower_bound or x > upper_bound]

# Save outlier results
with open("outliers_chairs.txt", "w") as f:
    f.write("Outlier Detection (IQR method):\n")
    f.write(f"  Q1: {Q1}\n")
    f.write(f"  Q3: {Q3}\n")
    f.write(f"  IQR: {IQR}\n")
    f.write(f"  Lower Bound: {lower_bound}\n")
    f.write(f"  Upper Bound: {upper_bound}\n")
    f.write(f"  Outliers: {outliers}\n")
    f.write(f"  Number of Outliers: {len(outliers)}\n")