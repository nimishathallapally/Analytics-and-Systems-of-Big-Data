import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib
from scipy import stats

# ----------------------------
# User config
input_dir = "./input"
output_dir = "./output"
matplotlib.use("Agg")  # for headless environments
# ----------------------------

# Ensure output directory exists
os.makedirs(output_dir, exist_ok=True)

# Load iris dataset
csv_path = os.path.join(input_dir, "Iris.csv")
df = pd.read_csv(csv_path)

# If the dataset has an "Id" column, drop it
if "Id" in df.columns:
    df = df.drop(columns=["Id"])

# Rename columns for consistency
df = df.rename(columns={
    "SepalLengthCm": "SepalLength",
    "SepalWidthCm": "SepalWidth",
    "PetalLengthCm": "PetalLength",
    "PetalWidthCm": "PetalWidth",
    "Species": "target"
})

species_list = df["target"].unique()
plt.style.use("seaborn-v0_8-pastel")

# ----------------------------
# Helper: save table to PNG
def save_table_as_png(df_table, title, filename):
    fig, ax = plt.subplots(figsize=(max(8, len(df_table.columns)*1.5), 0.7*len(df_table)+2))
    ax.axis("tight")
    ax.axis("off")
    table = ax.table(
        cellText=df_table.values,
        colLabels=df_table.columns,
        rowLabels=df_table.index,
        loc="center"
    )
    table.auto_set_font_size(False)
    table.set_fontsize(8)
    table.scale(1.2, 1.2)
    plt.title(title, pad=20)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, filename))
    plt.close()

# ----------------------------
# 1. Bar/Column Chart (Mean Sepal Length per Species)
plt.figure(figsize=(6,4))
mean_vals = df.groupby("target")["SepalLength"].mean()
mean_vals.plot(kind="bar", color=plt.cm.Pastel1.colors)
plt.title("Average Sepal Length by Species")
plt.ylabel("Mean Sepal Length (cm)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "bar_chart.png"))
plt.close()

# Table: mean values used
bar_table = mean_vals.round(2).reset_index()
bar_table.columns = ["Species", "Mean Sepal Length"]
save_table_as_png(bar_table, "Mean Sepal Length by Species", "bar_chart_table.png")

# ----------------------------
# 2. Pie Chart (proportion)
counts = df["target"].value_counts()
plt.figure(figsize=(5,5))
counts.plot.pie(autopct="%.1f%%", colors=plt.cm.Pastel1.colors)
plt.title("Species Distribution")
plt.ylabel("")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "pie_chart.png"))
plt.close()
save_table_as_png(counts.to_frame("count"), "Pie Chart Data", "pie_chart_table.png")

# ----------------------------
# 3. Doughnut Chart
plt.figure(figsize=(5,5))
plt.pie(counts, labels=counts.index, autopct="%.1f%%",
        colors=plt.cm.Pastel2.colors, wedgeprops=dict(width=0.4))
plt.title("Species Distribution (Doughnut)")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "doughnut_chart.png"))
plt.close()
# reuse same counts table
save_table_as_png(counts.to_frame("count"), "Doughnut Chart Data", "doughnut_chart_table.png")

# ----------------------------
# 4. Pareto Chart
sorted_counts = counts.sort_values(ascending=False)
cum_pct = sorted_counts.cumsum() / sorted_counts.sum() * 100
plt.figure(figsize=(6,4))
sorted_counts.plot(kind="bar", color="skyblue")
plt.twinx()
cum_pct.plot(marker="o", color="red")
plt.ylabel("Cumulative %")
plt.title("Pareto Chart - Species Count")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "pareto_chart.png"))
plt.close()
pareto_df = pd.DataFrame({"count": sorted_counts, "cumulative %": cum_pct.round(2)})
save_table_as_png(pareto_df, "Pareto Chart Data", "pareto_chart_table.png")

# ----------------------------
# 5. Scatter Plot (Sepal Length vs Width by Species)
plt.figure(figsize=(6,4))
for species in species_list:
    subset = df[df["target"] == species]
    plt.scatter(subset["SepalLength"], subset["SepalWidth"], label=species, alpha=0.7)
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
plt.title("Sepal Dimensions Scatter Plot")
plt.legend()
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "scatter_plot.png"))
plt.close()

# Table: first 10 rows for SepalLength & SepalWidth per species
scatter_tables = []
for species in species_list:
    sample = df[df["target"] == species][["SepalLength","SepalWidth"]].head(10)
    scatter_tables.append(sample.reset_index(drop=True).rename_axis(f"{species}").T)
scatter_table = pd.concat(scatter_tables, axis=0)
save_table_as_png(scatter_table, "Scatter Plot Data (first 10 rows per species)", "scatter_plot_table.png")

# ----------------------------
# 6. Line Chart (mean of features)
line_stats = df.groupby("target")[["SepalLength","SepalWidth","PetalLength","PetalWidth"]].mean().round(2).T
line_stats.plot(marker="o")
plt.title("Mean Feature Values per Species")
plt.ylabel("cm")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "line_chart.png"))
plt.close()
save_table_as_png(line_stats, "Line Chart Data", "line_chart_table.png")

# ----------------------------
# 7. Radar Chart
categories = ["SepalLength","SepalWidth","PetalLength","PetalWidth"]
radar_vals = df.groupby("target")[categories].mean()
angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
angles += angles[:1]
plt.figure(figsize=(6,6))
ax = plt.subplot(111, polar=True)
for species in species_list:
    vals = radar_vals.loc[species].tolist()
    vals += vals[:1]
    ax.plot(angles, vals, label=species)
    ax.fill(angles, vals, alpha=0.2)
ax.set_thetagrids(np.degrees(angles[:-1]), categories)
plt.title("Radar Chart of Mean Dimensions")
plt.legend(loc="upper right", bbox_to_anchor=(1.2,1.05))
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "radar_chart.png"))
plt.close()
save_table_as_png(radar_vals.round(2), "Radar Chart Data", "radar_chart_table.png")

# ----------------------------
# 8. Area Chart (Mean, Min, Max Sepal Length per Species)
plt.figure(figsize=(6,4))
area_stats = df.groupby("target")["SepalLength"].agg(["mean", "min", "max"])
area_stats.plot.area(alpha=0.6)
plt.title("Sepal Length Stats by Species (Area Chart)")
plt.ylabel("Sepal Length (cm)")
plt.xlabel("Species")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "area_chart.png"))
plt.close()

# Table: mean, min, max
area_table = area_stats.round(2).reset_index()
save_table_as_png(area_table, "Sepal Length Stats by Species", "area_chart_table.png")

# ----------------------------
# 9. Histogram (Sepal Length distribution)
plt.figure(figsize=(6,4))
plt.hist(df["SepalLength"], bins=15, color="lightcoral", edgecolor="black", alpha=0.7)  # no density=True
plt.title("Histogram of Sepal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "histogram.png"))
plt.close()

# Table: histogram bin counts
counts, bins = np.histogram(df["SepalLength"], bins=15)
hist_table = pd.DataFrame({"Bin Start": bins[:-1], "Bin End": bins[1:], "Count": counts})
save_table_as_png(hist_table, "Histogram of Sepal Length (bin counts)", "histogram_table.png")

print(f"✅ All plots and tables saved in: {output_dir}")