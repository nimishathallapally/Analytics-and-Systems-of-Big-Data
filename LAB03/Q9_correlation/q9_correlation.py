# q9_correlation.py
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

temp = [98, 87, 90, 85, 95, 75]
customers = [15, 12, 10, 10, 16, 7]

df = pd.DataFrame({"Temperature": temp, "Customers": customers})
df.to_csv("icecream_data.csv", index=False)

sns.set(style="whitegrid", palette="pastel")
plt.figure(figsize=(6,4))
sns.scatterplot(x="Temperature", y="Customers", data=df, color="orchid", s=100)
plt.title("Ice-Cream Customers vs Temperature")
plt.tight_layout()
plt.savefig("correlation.png")
plt.close()

corr = df.corr().iloc[0,1]
print("Correlation:", corr)