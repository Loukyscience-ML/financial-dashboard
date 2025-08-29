import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel("Financial Analysis for XYZ Company – FY2025.xlsx", sheet_name="Sheet1")

st.set_page_config(page_title="Financial Dashboard", layout="wide")
st.title("📊 Financial Analysis for XYZ Company – FY2025")

st.header("Trial Balance Summary")
st.dataframe(df)

st.header("Department Performance")
st.dataframe(df[['Department', 'Revenue', 'Expenses', 'NetProfit']])

st.header("Monthly Financial Trends")
st.line_chart(df[['Month', 'Revenue', 'Expenses', 'NetProfit']].set_index('Month'))

st.subheader("3-Month Moving Averages")
df['Revenue_MA'] = df['Revenue'].rolling(3).mean()
df['Expenses_MA'] = df['Expenses'].rolling(3).mean()
st.line_chart(df[['Month', 'Revenue_MA', 'Expenses_MA']].set_index('Month'))

st.header("Expense Breakdown by Type")
fig, ax = plt.subplots()
expense_summary = df.groupby('AccountName')['TotalExpense'].sum().reset_index()
ax.bar(expense_summary['AccountName'], expense_summary['TotalExpense'], color="#1f77b4")
ax.set_ylabel("Total Expense")
ax.set_title("Expense Breakdown")
st.pyplot(fig)

st.header("Key Insights")
st.markdown("""
- Finance department leads profitability with 21.27% share  
- HR is the lowest contributor but still profitable  
- December shows peak revenue  
- Travel expenses dominate cost structure  
- September 2024 shows negative net profit—requires investigation
""")
