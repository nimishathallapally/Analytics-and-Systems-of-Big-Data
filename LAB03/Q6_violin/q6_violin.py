# q6_violin.py
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)
std_norm = np.random.randn(200)
log_norm = np.random.lognormal(mean=0, sigma=1, size=200)

df = pd.DataFrame({"StandardNormal": std_norm, "LogNormal": log_norm})
df.to_csv("random_data.csv", index=False)

sns.set(style="whitegrid", palette="pastel")
plt.figure(figsize=(6,4))
sns.violinplot(y=std_norm, color="lightgreen")
plt.title("Violin Plot - Standard Normal")
plt.tight_layout()
plt.savefig("violin_standard_normal.png")
plt.close()

plt.figure(figsize=(6,4))
sns.violinplot(y=log_norm, color="lightcoral")
plt.title("Violin Plot - Log Normal")
plt.tight_layout()
plt.savefig("violin_log_normal.png")
plt.close()