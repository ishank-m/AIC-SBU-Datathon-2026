import pandas as pd



file_path = "PulledData/tuitons.xlsx"
tuition_df = pd.read_excel(file_path, sheet_name="Table CP-2")
tuition_df_clean = tuition_df.iloc[31:56, [0,3]]
tuition_df_clean.columns = ["year", "tuition"]



file_path = "PulledData/loans_and_grants.xlsx"
aid_loan_df = pd.read_excel(file_path, sheet_name="Table SA-3")
aid_df_clean = aid_loan_df.iloc[66:91, [0,5,7]]
aid_df_clean.columns = ["year", "aid", "loan"]
aid_df_clean["aid"] = aid_df_clean["aid"].round(0).astype(int)
aid_df_clean["loan"] = aid_df_clean["loan"].round(0).astype(int)



file_path = "PulledData/hs_earnings.csv"
hs_earnings_df = pd.read_csv(file_path)
hs_earnings_df = hs_earnings_df.iloc[:100, [0,1]]


file_path = "PulledData/ba_earnings.csv"
ba_earnings_df = pd.read_csv(file_path)
ba_earnings_df = ba_earnings_df.iloc[:100, [0,1]]


# convert observation_date to datetime so pandas can group by year
tuition_df_clean["year"] = pd.to_datetime('20' + tuition_df_clean["year"].str[:2])
aid_df_clean["year"] = pd.to_datetime(aid_df_clean["year"].str[:4],)
hs_earnings_df["observation_date"] = pd.to_datetime(hs_earnings_df["observation_date"])
ba_earnings_df["observation_date"] = pd.to_datetime(ba_earnings_df["observation_date"])

# extract year and group by it, taking the mean of the four quarters
tuition_annual = tuition_df_clean.groupby(tuition_df_clean["year"].dt.year)["tuition"].mean().reset_index()
aid_annual = aid_df_clean.groupby(aid_df_clean["year"].dt.year)[["aid", "loan"]].mean().reset_index()
hs_annual = hs_earnings_df.groupby(hs_earnings_df["observation_date"].dt.year)["LEU0252917300Q"].mean().reset_index()
ba_annual = ba_earnings_df.groupby(ba_earnings_df["observation_date"].dt.year)["LEU0252918500Q"].mean().reset_index()

# rename columns to something clean
hs_annual.columns = ["year", "hs_earnings"]
ba_annual.columns = ["year", "ba_earnings"]

# save to csv
hs_annual.to_csv("CleanedUpData/hs_earnings_clean.csv", index=False)
ba_annual.to_csv("CleanedUpData/ba_earnings_clean.csv", index=False)
tuition_annual.to_csv("CleanedUpData/tuition_clean.csv", index=False)
aid_annual.to_csv("CleanedUpData/aid_and_loans_clean.csv", index=False)