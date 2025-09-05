# q4_scatter.py

import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

# Data
fuel = [3.6, 6.7, 9.8, 11.2, 14.7]
mass = [0.45, 0.91, 1.36, 1.81, 2.27]

# DataFrame
df = pd.DataFrame({"Mass": mass, "Fuel": fuel})
df.to_csv("fuel_mass_data.csv", index=False)

# Scatter plot
sns.set(style="whitegrid", palette="pastel")
plt.figure(figsize=(6, 4))
sns.scatterplot(x="Mass", y="Fuel", data=df, color="coral", s=100)
plt.title("Fuel Consumption vs Mass of Car")
plt.xlabel("Mass (tons)")
plt.ylabel("Fuel Consumption (L/100km)")
plt.tight_layout()
plt.savefig("scatterplot.png")
plt.close()

# Correlation calculation
corr = df["Mass"].corr(df["Fuel"])

# Determine type of correlation
if corr > 0:
    direction = "positive"
elif corr < 0:
    direction = "negative"
else:
    direction = "no"

# For this simple data set, visual inspection suffices for linearity
# But in a more advanced setting, you'd use regression or scatterplot shape
relationship = "linear" if abs(corr) > 0.7 else "weak or non-linear"

# Save correlation results to file
with open("correlation_result.txt", "w") as f:
    f.write("Correlation Analysis between Mass and Fuel Consumption:\n")
    f.write(f"  Correlation Coefficient: {corr:}\n")
    f.write(f"  Direction: {direction.capitalize()} correlation\n")
    f.write(f"  Relationship Type: {relationship.capitalize()} relationship\n")