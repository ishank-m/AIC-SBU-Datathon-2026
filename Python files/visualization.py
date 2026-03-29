import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
tuition_df = pd.read_csv("CleanedUpData/tuition_clean.csv")
aid_loan_df = pd.read_csv("CleanedUpData/aid_and_loans_clean.csv")
hs_earnings_df = pd.read_csv("CleanedUpData/hs_earnings_clean.csv")
ba_earnings_df = pd.read_csv("CleanedUpData/ba_earnings_clean.csv")



# Plot tuition over the years
plt.figure(figsize=(10, 5))
plt.plot(tuition_df["year"], tuition_df["tuition"], marker='o')
plt.title("Average Tuition Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Tuition (USD)")
plt.grid()
plt.show()

# Plot aid and loans over the years
plt.figure(figsize=(10, 5))
plt.plot(aid_loan_df["year"], aid_loan_df["aid"], marker='o', label='Aid')
plt.plot(aid_loan_df["year"], aid_loan_df["loan"], marker='o', label='Loan')
plt.title("Average Aid and Loans Over the Years")
plt.xlabel("Year")
plt.ylabel("Amount (USD)")
plt.legend()
plt.grid()
plt.show()

# Plot earnings for high school and bachelor's degree over the years
plt.figure(figsize=(10, 5))
plt.plot(hs_earnings_df["year"], hs_earnings_df["hs_earnings"], marker='o', label='High School')
plt.plot(ba_earnings_df["year"], ba_earnings_df["ba_earnings"], marker='o', label='Bachelor\'s Degree')
plt.title("Median Earnings Over the Years")
plt.xlabel("Year")
plt.ylabel("Median Earnings (USD)")
plt.legend()
plt.grid()
plt.show()


# Plotting the wage premium ration
earnings_df = pd.merge(hs_earnings_df,ba_earnings_df,on="year",how="inner")
earnings_df["wage_premium"] = (earnings_df["ba_earnings"] / earnings_df["hs_earnings"])
plt.figure(figsize=(10, 5))
plt.plot(earnings_df["year"], earnings_df["wage_premium"], marker='o')
plt.title("College Wage Premium Over Time")
plt.xlabel("Year")
plt.ylabel("Bachelor's / High School Earnings Ratio")
plt.grid()
plt.show()

# Plot indexed growth (tuition, loans, aid, wage premium all vs 2000 baseline)
df = pd.merge(earnings_df, tuition_df, on="year")
df = pd.merge(df, aid_loan_df, on="year")

base = df[df["year"] == 2000].iloc[0]
df["tuition_idx"] = df["tuition"] / base["tuition"] * 100
df["loan_idx"]    = df["loan"] / base["loan"] * 100
df["aid_idx"]     = df["aid"] / base["aid"] * 100
df["premium_idx"] = df["wage_premium"] / base["wage_premium"] * 100

plt.figure(figsize=(10, 5))
plt.plot(df["year"], df["tuition_idx"], marker='o', label="Tuition Cost")
plt.plot(df["year"], df["premium_idx"], marker='o', label="Wage Premium")
plt.plot(df["year"], df["loan_idx"],    marker='o', label="Student Loans", linestyle="--")
plt.plot(df["year"], df["aid_idx"],     marker='o', label="Financial Aid",  linestyle=":")
plt.axhline(100, color="gray", lw=0.8, linestyle="--")
plt.title("College Costs vs. Wage Premium Since 2000 (Indexed to 2000 = 100)")
plt.xlabel("Year")
plt.ylabel("Index (2000 = 100)")
plt.legend()
plt.grid()
plt.show()

# Plot ROI ratio (wage premium / tuition)
df["roi_ratio"] = (df["wage_premium"]*52) / df["tuition"]

plt.figure(figsize=(10, 5))
plt.plot(df["year"], df["roi_ratio"], marker='o')
plt.title("College Wage Premium ROI Over Time")
plt.xlabel("Year")
plt.ylabel("Annual Wage Premium / Tuition")
plt.grid()
plt.show()
