import pandas as pd
import numpy as np
import random

# Set seed for reproducibility
np.random.seed(42)

# Step 1: Set number of villages and zones
total_villages = 1120
zones = [f"Z{str(i).zfill(4)}" for i in range(1, 113)]  # 113 zones (approx 10 villages each)
regions = ["North", "South", "East", "West"]

# Step 2: Create dummy data
village_data = []
for i in range(total_villages):
    village = f"Village_{i+1}"
    zone_id = random.choice(zones)
    region = random.choice(regions)
    population = np.random.randint(500, 5000)
    pipe_length_km = round(np.random.uniform(5, 30), 2)
    oht_capacity_liters = np.random.randint(20000, 150000)
    village_data.append([zone_id, village, region, population, pipe_length_km, oht_capacity_liters])

# Step 3: Create DataFrame
village_df = pd.DataFrame(village_data, columns=[
    "Zone_ID", "Village", "Region", "Population", "Pipes_Length_KM", "OHT_Capacity_Liters"
])

# Step 4: Save to CSV with error handling
try:
    village_df.to_csv("village_master_1120.csv", index=False)
    print("CSV file 'village_master_1120.csv' saved successfully!")
except Exception as e:
    print(f"Error saving CSV file: {e}")

# Optional: Show top 5 rows
print(village_df.head())
