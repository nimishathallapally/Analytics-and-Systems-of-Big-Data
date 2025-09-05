import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
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

# Load Iris dataset
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

# ==================================================
# Correlogram 1: Correlation Heatmap
# ==================================================
plt.figure(figsize=(6,5))
corr = df[["SepalLength","SepalWidth","PetalLength","PetalWidth"]].corr()
sns.heatmap(corr, annot=True, cmap="Blues", fmt=".2f", cbar=True, square=True)
plt.title("Correlogram - Iris Attribute Correlations")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "q3_correlogram_heatmap.png"))
plt.close()

# ==================================================
# Correlogram 2: Pairplot (Scatter + Histograms)
# ==================================================
sns.pairplot(df, vars=["SepalLength","SepalWidth","PetalLength","PetalWidth"], hue="target",
             diag_kind="hist", palette="Set2")
plt.suptitle("Correlogram - Iris Pairwise Relationships", y=1.02)
plt.savefig(os.path.join(output_dir, "q3_correlogram_pairplot.png"))
plt.close()

print(f"✅ Q3 correlogram plots saved in {output_dir}")

# ==================================================
# Inferences (to be included in report / assignment)
# ==================================================
inferences = """
Inferences from Correlogram (Iris dataset):
1. Petal Length and Petal Width are highly correlated (strong positive correlation ~0.96).
   -> These two features carry similar information for classification.
2. Sepal Length also correlates moderately with Petal Length (~0.87).
3. Sepal Width shows weak/negative correlation with Sepal Length and Petal Length.
   -> Indicates Sepal Width is somewhat independent.
4. Pairplot shows clear class separation:
   - Setosa is easily separable using Petal Length/Petal Width (distinct cluster).
   - Versicolor and Virginica overlap but still show trends.
5. Petal-based features are better predictors of species than Sepal-based features.
"""

print(inferences)
