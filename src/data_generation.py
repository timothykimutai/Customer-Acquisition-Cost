import pandas as pd
import numpy as np

# Set random seed
np.random.seed(42)

# Number of records
num_records = 1000

# Generate marketing data
marketing_data =pd.DataFrame({
    "customer_id": np.arange(1, num_records + 1),
    "platform": np.random.choice(["Google", "Facebook", "Instagram", "LinkedIn"], num_records),
    "ad_spend": np.random.uniform(50, 500, num_records), # Ad spend in USD
    "clicks": np.random.randint(10, 500, num_records), 
    "conversions": np.random.randint(1, 50, num_records),
    "impressions": np.random.randint(1000, 50000, num_records)
})
# Sales data
sales_data = pd.DataFrame({
    "customer_id": np.arange(1, num_records+1),
    "total_revenue": np.random.uniform(100, 2000, num_records),
    "repeat_purchases": np.random.randint(1, 5, num_records),
    "unique_customers": np.random.randint(1, 3, num_records)
})
# Save data to CSV
marketing_data.to_csv("data/marketing_data.csv", index=False)
sales_data.to_csv("data/sales_data.csv", index=False)

print("Marketing and sales data generated and saved successfully!")