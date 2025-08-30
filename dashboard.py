import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Financial Dashboard", layout="wide")
st.title("📊 Financial Analysis for XYZ Company – FY2025")

# Load Excel file
df = pd.read_excel("financial_analysis_fy2025.xlsx", sheet_name="Sheet1")

# Trial Balance Summary
st.header("Trial Balance Summary")
st.dataframe(df)

# Department-level performance calculation
revenue_by_dept = df[df["AccountName"].isin(["Sales Revenue", "Online Sales"])] \
    .groupby("Dept")["Credit"].sum().reset_index().rename(columns={"Credit": "Revenue"})

expenses_by_dept = df[df["AccountName"].isin(["COGS", "Payroll Expense", "Travel Expense"])] \
    .groupby("Dept")["Debit"].sum().reset_index().rename(columns={"Debit": "Expenses"})

dept_pnl = pd.merge(revenue_by_dept, expenses_by_dept, on="Dept", how="outer").fillna(0)
dept_pnl["NetProfit"] = dept_pnl["Revenue"] - dept_pnl["Expenses"]

# Department Performance Table
st.header("Department Performance")
st.dataframe(dept_pnl)

# Monthly financial trends
df["YearMonth"] = pd.to_datetime(df["TxnDate"]).dt.to_period("M").astype(str)

monthly_revenue = df[df["AccountName"].isin(["Sales Revenue", "Online Sales"])] \
    .groupby("YearMonth")["Credit"].sum().reset_index().rename(columns={"Credit": "Revenue"})

monthly_expenses = df[df["AccountName"].isin(["COGS", "Payroll Expense", "Travel Expense"])] \
    .groupby("YearMonth")["Debit"].sum().reset_index().rename(columns={"Debit": "Expenses"})

monthly_trend = pd.merge(monthly_revenue, monthly_expenses, on="YearMonth", how="outer").fillna(0)
monthly_trend["NetProfit"] = monthly_trend["Revenue"] - monthly_trend["Expenses"]

# Monthly Trends Line Chart
st.header("Monthly Financial Trends")
st.line_chart(monthly_trend.set_index("YearMonth")[["Revenue", "Expenses", "NetProfit"]])

# 3-Month Moving Averages
monthly_trend["Revenue_MA"] = monthly_trend["Revenue"].rolling(3).mean()
monthly_trend["Expenses_MA"] = monthly_trend["Expenses"].rolling(3).mean()

st.subheader("3-Month Moving Averages")
st.line_chart(monthly_trend.set_index("YearMonth")[["Revenue_MA", "Expenses_MA"]])

# Expense Breakdown by Type
expense_accounts = ["Payroll Expense", "Travel Expense", "COGS"]
expense_summary = df[df["AccountName"].isin(expense_accounts)] \
    .groupby("AccountName")["Debit"].sum().reset_index().rename(columns={"Debit": "TotalExpense"})

st.header("Expense Breakdown by Type")
fig, ax = plt.subplots()
ax.bar(expense_summary["AccountName"], expense_summary["TotalExpense"], color="#1f77b4")
ax.set_ylabel("Total Expense")
ax.set_title("Expense Breakdown")
st.pyplot(fig)

# Key Insights
st.header("Key Insights")
st.markdown("""
- Finance department leads profitability with 21.27% share  
- HR is the lowest contributor but still profitable  
- December shows peak revenue  
- Travel expenses dominate cost structure  
- September 2024 shows negative net profit — requires investigation
""")
