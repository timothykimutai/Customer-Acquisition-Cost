import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import df

# CAC distribution
plt.figure(figsize=(8,5))
sns.histplot(df["CAC"], bins=30, kde=True)
plt.title("Distribution of Customer Acquisition Cost(CAC)")
plt.show()

# CAC vs LTV scatter plot
plt.figure(figsize=(8,5))
sns.scatterplot(x=df["CAC"], y=df["LTV"], hue=df["platform"])
plt.axhline(y=df["CAC"].mean(), color='red', linestyle="--", label="Average CAC")
plt.title("CAC VS LTV")
plt.legend()
plt.show()