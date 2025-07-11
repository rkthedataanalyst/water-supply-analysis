import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed
np.random.seed(42)

# Load zone IDs from existing village file
village_df = pd.read_csv("village_master_1120.csv")
zone_ids = village_df["Zone_ID"].unique()

# Date range (30 days)
start_date = datetime(2024, 1, 1)
date_list = [start_date + timedelta(days=i) for i in range(30)]

# Generate consumption data
consumption_logs = []

for date in date_list:
    for zone in zone_ids:
        connections = np.random.randint(150, 300)  # Number of households
        avg_lpcd = round(np.random.uniform(60, 120), 2)  # Avg. Liters per capita per day
        estimated_usage = int(connections * avg_lpcd)
        consumption_logs.append([
            date.strftime("%Y-%m-%d"),
            zone,
            estimated_usage,
            connections,
            avg_lpcd
        ])

# Create DataFrame
consumption_df = pd.DataFrame(consumption_logs, columns=[
    "Date", "Zone_ID", "Estimated_Usage_Liters", "No_of_Connections", "Avg_LPCD"
])

# Save to CSV with error handling
try:
    consumption_df.to_csv("consumption_log.csv", index=False)
    print("CSV file 'consumption_log.csv' saved successfully!")
except Exception as e:
    print(f"Error saving CSV file: {e}")

# Optional preview
print(consumption_df.head())
