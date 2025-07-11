## 🚰 Drinking Water Supply Analysis Project

A real-world inspired data analytics project that simulates and analyzes the performance of a rural drinking water supply scheme covering 1120 villages across multiple zones. The goal is to identify leakage patterns, optimize supply vs. consumption, and support data-driven maintenance decisions.

---

##  Demo

 Coming soon — Power BI dashboard hosted via GitHub or shared as report file.


## Table of Contents

- [Business Understanding] (#business-understanding)
- [Data Understanding] (#data-understanding)
- [Technologies Used] (#technologies-used)
- [Approach] (#approach)
- [Visualizations] (#visualizations)
- [Setup Instructions] (#setup-instructions)
- [Project Status] (#project-status)
- [Credits] (#credits)


## Business Understanding

This project reflects a real infrastructure initiative in a rural district, aimed at providing clean drinking water to 1120 villages via pipeline-based distribution.

As a Data Analyst, the objective is to:
- Simulate the operational data for intake, treatment, supply, and household usage
- Monitor performance zone-wise and identify inefficiencies
- Generate insights to reduce water loss and prioritize maintenance

The analysis helps public utility teams make better decisions with data.

---

## Data Understanding

The project uses 3 simulated datasets generated in Python:

- `village_master_1120.csv`: Zone-wise village details (population, pipe length, OHT capacity, etc.)
- `water_supply_log.csv`: Daily records of intake, treated, and supplied water
- `consumption_log.csv`: Daily household usage, number of connections, average LPCD

These files are merged and enriched into:  
➡ `merged_water_analysis.csv` for end-to-end analysis.

---

## Technologies Used

- **Python**: pandas, numpy (data generation, cleaning)
- **SQL**: SQLite (data loading, querying)
- **Power BI**: dashboarding, DAX calculations
- **VS Code**: coding and markdown editing
- **GitHub**: version control and project publishing

---

## Approach

1. **Data Generation**: Used Python to simulate realistic water data for 1120 villages
2. **Data Cleaning & Merging**: Created unified dataset (`merged_water_analysis.csv`) using pandas
3. **Analysis**:
   - Calculated leakage in liters and percentage
   - Identified underperforming zones and trends over time
4. **Dashboarding**:
   - Created multi-page Power BI dashboard:
     - Executive Summary
     - Zone-Level Analysis
     - Daily Monitoring
     - Maintenance Prioritization
5. **Insights**: Discovered zones with >25% leakage, recommended infrastructure audits

---

## 📈 Visualizations

**Power BI Pages Included**:
- **Page 1: Executive Summary**
  - KPI Cards (Total Supply, Usage, Leakage)
  - Trend Line (Supply vs Usage)
  - Top 10 Leakage Zones (Bar Chart)
- **Page 2: Zone-Level Analysis**
  - Matrix Heatmap of Leakage %
  - Leakage Trend over Time per Zone
- **Page 3: Daily Monitoring**
  - Histograms & stacked bar charts for daily patterns
- **Page 4: Maintenance Prioritization**
  - Critical zone flagging (`Leakage % > 25%`)

📸 _Screenshots coming soon..._



## ⚙️ Setup Instructions

To run locally:

1. Clone this repo:

git clone https://github.com/rkthedataanalyst/water-supply-analysis.git
cd water-supply-analysis

2. Install Python libraries:
pip install pandas numpy

3. Run these scripts:
python village_generator.py
python generate_water_supply_log.py
python generate_consumption_log.py
python merge_and_analyze.py

4. Open merged_water_analysis.csv in Power BI or import into SQLite for analysis.

📌 Project Status
✅ Data simulation complete

✅ Merged dataset created

✅ SQL queries tested

✅ Power BI dashboard designed

🚧 Finalizing screenshots and publishing

## 🙏 Credits

- Project designed and simulated by RK SINGH
- Inspired by real-world infrastructure planning (Govt. of India)
- Thanks to OpenAI + community for code support & ideasgit remote add origin **https://github.com/rkthedataanalyst/water-supply-analysis.git**
- Microsoft Power BI (for dashboarding tools)
- Kaggle & GitHub community for project structure ideas

