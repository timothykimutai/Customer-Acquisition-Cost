import pandas as pd
import numpy as np

# Load data
marketing_data = pd.read_csv("data/marketing_data.csv")
sales_data = pd.read_csv("data/sales_data.csv")

# print the first 5 rows of data
print(marketing_data.head(10))
print(sales_data.head(10))

# Merge data
df = pd.merge(marketing_data, sales_data, on="customer_id")

# Feature engineering
df["CAC"] = df["ad_spend"] / df["conversions"] # Cost of Acquisition
df["LTV"] = df["total_revenue"] / df["unique_customers"] # Life time value
df["ROI"] = df["total_revenue"] - df["ad_spend"] / df["ad_spend"] # Return on Investment

# Fill missing values
df.fillna(0, inplace=True)

print(df.head())