import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

trial_balance_df = pd.read_excel("trial_balance.xlsx")

# Load your processed DataFrames
# Replace with actual loading if needed
# df = pd.read_excel("your_data.xlsx")

st.set_page_config(page_title="Financial Dashboard", layout="wide")

st.title("📊 Financial Analysis for XYZ Company – FY2025")

# Section 1: Trial Balance
st.header("Trial Balance Summary")
st.dataframe(trial_balance_df)

# Section 2: Department-Level P&L
st.header("Department Performance")
st.dataframe(dept_pnl)

# Section 3: Monthly Trends
st.header("Monthly Financial Trends")
st.line_chart(monthly_trend[["Revenue", "Expenses", "NetProfit"]])

# Section 4: Moving Averages
st.subheader("3-Month Moving Averages")
st.line_chart(monthly_trend[["Revenue_MA", "Expenses_MA"]])

# Section 5: Expense Breakdown
st.header("Expense Breakdown by Type")
fig, ax = plt.subplots()
ax.bar(expense_summary["AccountName"], expense_summary["TotalExpense"], color="#1f77b4")
ax.set_ylabel("Total Expense")
ax.set_title("Expense Breakdown")
st.pyplot(fig)

# Section 6: Key Insights
st.header("Key Insights")
st.markdown("""
- Finance department leads profitability with 21.27% share  
- HR is the lowest contributor but still profitable  
- December shows peak revenue  
- Travel expenses dominate cost structure  
- September 2024 shows negative net profit—requires investigation
""")
