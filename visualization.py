import pandas as pd
import matplotlib.pyplot as plt

# Load the cleaned data
tuition_df = pd.read_csv("tuition_clean.csv")
aid_loan_df = pd.read_csv("aid_and_loans_clean.csv")
hs_earnings_df = pd.read_csv("hs_earnings_clean.csv")
ba_earnings_df = pd.read_csv("ba_earnings_clean.csv")



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
plt.title("Average Earnings Over the Years")
plt.xlabel("Year")
plt.ylabel("Average Earnings (USD)")
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