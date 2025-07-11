import pandas as pd

# Step 1: Load both CSV files
try:
    supply_df = pd.read_csv("water_supply_log.csv")
    consumption_df = pd.read_csv("consumption_log.csv")
except Exception as e:
    print("Error reading files:", e)
    exit()

# Step 2: Merge on Date and Zone_ID
merged_df = pd.merge(supply_df, consumption_df, on=["Date", "Zone_ID"], how="inner")

# Step 3: Create Leakage Calculations
merged_df["Leakage_Liters"] = merged_df["Supplied_Water_Liters"] - merged_df["Estimated_Usage_Liters"]
merged_df["Leakage_Percent"] = (merged_df["Leakage_Liters"] / merged_df["Supplied_Water_Liters"]) * 100
merged_df["Leakage_Percent"] = merged_df["Leakage_Percent"].round(2)

# Step 4: Save to a new file
try:
    merged_df.to_csv("merged_water_analysis.csv", index=False)
    print("File 'merged_water_analysis.csv' created successfully!")
except Exception as e:
    print("Failed to save merged file:", e)

# Step 5: Show a preview
print("\n Preview of Merged Data:")
print(merged_df.head())

# --- Additional Analysis ---
# 1. Summary statistics for leakage
print("\n Leakage Summary Statistics:")
print(merged_df["Leakage_Liters"].describe())

# 2. Zone/date with highest leakage (liters)
max_leak = merged_df.loc[merged_df["Leakage_Liters"].idxmax()]
print(f"\n Highest Leakage: {max_leak['Leakage_Liters']:,} liters on {max_leak['Date']} in zone {max_leak['Zone_ID']}")

# 3. Average leakage percent per zone (top 5)
avg_leakage_percent = merged_df.groupby('Zone_ID')["Leakage_Percent"].mean().sort_values(ascending=False)
print("\n Top 5 Zones by Average Leakage Percent:")
print(avg_leakage_percent.head())
