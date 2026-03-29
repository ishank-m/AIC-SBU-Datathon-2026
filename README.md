# Education Track

## Question/Proposal: The Cost of College Has Risen. Has Financial Return Kept Up?

# Setup
Since we're working on python 3.14 for this, we'd need the pandas, openpyxl, matplotlib, and the urllib. 
make sure you install pandas, matplotlib, and openpyxl using 

```bash
pip install pandas matplotlib openpyxl
```
We created 3 separate python files for a smoother workflow, a setup.py file that fetches all the required dataset from web using python's built-in urllib library, a cleanup.py that cleans up the fetched dataset using pandas and openpyxl libraries, and a visualization.py that uses the cleaned-up data and graphs it using matplotlib with pandas libraries. 

Import the urllib as such to get started with pulling the dataset from web:

```bash
import urllib.request as urllib;
```

Rest of the code is in setup.py file which basically just fetches all the required datasets from the web.

# Data Clean-up
We use pandas and openpyxl libraries for cleaning up data. openpyxl is a library that helps manipulate Excel files (.xlsx).

Before you begin, make sure to import the libraries:

```python
import pandas as pd
import openpyxl as openpyxl
```

Ensure these libraries are installed using:

```python
pip install pandas matplotlib openpyxl
```

The following script processes raw datasets, extracts relevant columns, converts dates, and aggregates yearly data:

```python
import pandas as pd
import openpyxl as openpyxl

# Tuition Data
file_path = "tuitons.xlsx"
tuition_df = pd.read_excel(file_path, sheet_name="Table CP-2")
tuition_df_clean = tuition_df.iloc[31:56, [0,3]]
tuition_df_clean.columns = ["year", "tuition"]

# Aid and Loan Data
file_path = "loans_and_grants.xlsx"
aid_loan_df = pd.read_excel(file_path, sheet_name="Table SA-3")
aid_df_clean = aid_loan_df.iloc[66:91, [0,5,7]]
aid_df_clean.columns = ["year", "aid", "loan"]
aid_df_clean["aid"] = aid_df_clean["aid"].round(0).astype(int)
aid_df_clean["loan"] = aid_df_clean["loan"].round(0).astype(int)

# High School Earnings
file_path = "hs_earnings.csv"
hs_earnings_df = pd.read_csv(file_path)
hs_earnings_df = hs_earnings_df.iloc[:100, [0,1]]

# Bachelor's Earnings
file_path = "ba_earnings.csv"
ba_earnings_df = pd.read_csv(file_path)
ba_earnings_df = ba_earnings_df.iloc[:100, [0,1]]

# Convert to datetime
tuition_df_clean["year"] = pd.to_datetime('20' + tuition_df_clean["year"].str[:2])
aid_df_clean["year"] = pd.to_datetime(aid_df_clean["year"].str[:4])
hs_earnings_df["observation_date"] = pd.to_datetime(hs_earnings_df["observation_date"])
ba_earnings_df["observation_date"] = pd.to_datetime(ba_earnings_df["observation_date"])

# Group by year (annual averages)
tuition_annual = tuition_df_clean.groupby(tuition_df_clean["year"].dt.year)["tuition"].mean().reset_index()
aid_annual = aid_df_clean.groupby(aid_df_clean["year"].dt.year)[["aid", "loan"]].mean().reset_index()
hs_annual = hs_earnings_df.groupby(hs_earnings_df["observation_date"].dt.year)["LEU0252917300Q"].mean().reset_index()
ba_annual = ba_earnings_df.groupby(ba_earnings_df["observation_date"].dt.year)["LEU0252918500Q"].mean().reset_index()

# Rename columns
hs_annual.columns = ["year", "hs_earnings"]
ba_annual.columns = ["year", "ba_earnings"]

# Save cleaned data
hs_annual.to_csv("hs_earnings_clean.csv", index=False)
ba_annual.to_csv("ba_earnings_clean.csv", index=False)
tuition_annual.to_csv("tuition_clean.csv", index=False)
aid_annual.to_csv("aid_and_loans_clean.csv", index=False)
```

What this script does:
- Extracts relevant rows and columns from raw datasets
- Cleans and formats numeric values
- Converts date fields into proper datetime format
- Aggregates quarterly data into yearly averages
- Outputs clean CSV files for visualization


# Visualizations


# Trends
