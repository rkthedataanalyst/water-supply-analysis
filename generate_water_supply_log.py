import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Set random seed
np.random.seed(42)

# Load zone IDs from the village master file
village_df = pd.read_csv("village_master_1120.csv")
zone_ids = village_df["Zone_ID"].unique()

# Set date range (e.g., Jan 2024 – 30 days)
start_date = datetime(2024, 1, 1)
date_list = [start_date + timedelta(days=x) for x in range(30)]

# Generate daily water supply logs
supply_logs = []

for date in date_list:
    for zone in zone_ids:
        intake = np.random.randint(90000, 130000)
        treated = intake - np.random.randint(1000, 5000)
        supplied = treated - np.random.randint(2000, 8000)
        supply_logs.append([
            date.strftime("%Y-%m-%d"),
            zone,
            intake,
            treated,
            supplied
        ])

# Create DataFrame
supply_df = pd.DataFrame(supply_logs, columns=[
    "Date", "Zone_ID", "Intake_Water_Liters", "Treated_Water_Liters", "Supplied_Water_Liters"
])

# Save to CSV with error handling
try:
    supply_df.to_csv("water_supply_log.csv", index=False)
    print("CSV file 'water_supply_log.csv' saved successfully!")
except Exception as e:
    print(f"Error saving CSV file: {e}")

# Optional preview
print(supply_df.head())

# --- Additional Analysis ---
# 1. Total water supplied per zone
total_supplied_per_zone = supply_df.groupby('Zone_ID')['Supplied_Water_Liters'].sum()
print("\nTotal water supplied per zone (top 5):")
print(total_supplied_per_zone.sort_values(ascending=False).head())

# 2. Daily total water supplied across all zones
total_supplied_per_day = supply_df.groupby('Date')['Supplied_Water_Liters'].sum()
print("\nTotal water supplied per day (top 5):")
print(total_supplied_per_day.head())

# 3. Average intake, treated, and supplied water per zone
avg_per_zone = supply_df.groupby('Zone_ID')[['Intake_Water_Liters', 'Treated_Water_Liters', 'Supplied_Water_Liters']].mean()
print("\nAverage intake, treated, and supplied water per zone (top 5):")
print(avg_per_zone.head())

# 4. Zones with highest and lowest total supply
max_zone = total_supplied_per_zone.idxmax()
min_zone = total_supplied_per_zone.idxmin()
print(f"\nZone with highest total supply: {max_zone} ({total_supplied_per_zone[max_zone]:,.0f} liters)")
print(f"Zone with lowest total supply: {min_zone} ({total_supplied_per_zone[min_zone]:,.0f} liters)")
