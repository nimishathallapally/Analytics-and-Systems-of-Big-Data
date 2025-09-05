import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib

# ----------------------------
# User config
input_dir = "./input"
output_dir = "./output"
matplotlib.use("Agg")
plt.style.use("seaborn-v0_8-pastel")
# ----------------------------

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# ==================================================
# Part 1: Two Arrays Relationship Visualization
# ==================================================

# Generate two numeric arrays
x = np.random.rand(200)
y = x * 0.5 + np.random.normal(0, 0.1, 200)  # correlated with noise

# Scatter Plot
plt.figure(figsize=(5,4))
plt.scatter(x, y, alpha=0.7, color="skyblue")
plt.title("Scatter Plot of Two Arrays")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "q2_arrays_scatter.png"))
plt.close()

# Hexbin Plot
plt.figure(figsize=(5,4))
plt.hexbin(x, y, gridsize=20, cmap="Blues")
plt.colorbar(label="count")
plt.title("Hexbin Plot of Two Arrays")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "q2_arrays_hexbin.png"))
plt.close()

# Correlation Heatmap
corr = np.corrcoef(x, y)
plt.figure(figsize=(4,3))
sns.heatmap(corr, annot=True, cmap="Blues", xticklabels=["x","y"], yticklabels=["x","y"])
plt.title("Correlation Heatmap (Arrays)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "q2_arrays_corr_heatmap.png"))
plt.close()

print("✅ Q2 Part 1 (Arrays) plots saved.")

# ==================================================
# Part 2: Extend to Iris Dataset
# ==================================================

# Load Iris
csv_path = os.path.join(input_dir, "Iris.csv")
df = pd.read_csv(csv_path)

if "Id" in df.columns:
    df = df.drop(columns=["Id"])

df = df.rename(columns={
    "SepalLengthCm": "SepalLength",
    "SepalWidthCm": "SepalWidth",
    "PetalLengthCm": "PetalLength",
    "PetalWidthCm": "PetalWidth",
    "Species": "target"
})

# Pick subset: SepalLength vs PetalLength
x = df["SepalLength"]
y = df["PetalLength"]

# Scatter Plot
plt.figure(figsize=(5,4))
plt.scatter(x, y, alpha=0.7, color="coral")
plt.title("Iris: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "q2_iris_scatter.png"))
plt.close()

# Hexbin Plot
plt.figure(figsize=(5,4))
plt.hexbin(x, y, gridsize=20, cmap="Greens")
plt.colorbar(label="count")
plt.title("Iris Hexbin: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "q2_iris_hexbin.png"))
plt.close()

# Correlation Heatmap (using subset of attributes)
subset = df[["SepalLength","PetalLength","PetalWidth","SepalWidth"]]
plt.figure(figsize=(4,3))
sns.heatmap(subset.corr(), annot=True, cmap="Blues", fmt=".2f")
plt.title("Correlation Heatmap (Iris subset)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "q2_iris_corr_heatmap.png"))
plt.close()

print("✅ Q2 Part 2 (Iris) plots saved.")
print(f"📂 All Q2 outputs in: {output_dir}")
