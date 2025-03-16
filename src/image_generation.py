import matplotlib.pyplot as plt
import seaborn as sns
from data_loader import df

# Example: CAC Distribution
plt.figure(figsize=(8, 5))
sns.histplot(df['CAC'], bins=30, kde=True)
plt.title('Customer Acquisition Cost (CAC) Distribution')
plt.xlabel('CAC')
plt.ylabel('Frequency')
plt.savefig('images/cac_distribution.png')  # Save the figure
plt.show()
