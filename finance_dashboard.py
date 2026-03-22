import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finance_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

income = df[df['Type'] == 'Income']
expense = df[df['Type'] == 'Expense']

# KPIs
total_income = income['Amount'].sum()
total_expense = expense['Amount'].sum()
profit = total_income - total_expense
profit_margin = (profit / total_income) * 100

print("===== BUSINESS SUMMARY =====")
print("Total Income:", total_income)
print("Total Expense:", total_expense)
print("Net Profit:", profit)
print("Profit Margin (%):", round(profit_margin, 2))

# Monthly analysis
monthly = df.groupby(['Month','Type'])['Amount'].sum().unstack().fillna(0)
monthly['Profit'] = monthly['Income'] - monthly['Expense']

# 📊 Graphs
monthly[['Income','Expense']].plot(kind='bar', figsize=(10,5))
plt.title("Monthly Income vs Expense")
plt.show()

monthly['Profit'].plot(marker='o')
plt.title("Profit Trend")
plt.show()

expense.groupby('Category')['Amount'].sum().plot(kind='pie', autopct='%1.1f%%')
plt.title("Expense Distribution")
plt.show()

# 📈 Forecast (simple)
monthly['Profit Forecast'] = monthly['Profit'].rolling(2).mean()
monthly[['Profit','Profit Forecast']].plot(marker='o')
plt.title("Profit Forecast")
plt.show()

# 🧠 Insights
print("\n===== INSIGHTS =====")

top_expense = expense.groupby('Category')['Amount'].sum().idxmax()
print("Highest expense category:", top_expense)

best_month = monthly['Profit'].idxmax()
print("Most profitable month:", best_month)

loss_months = monthly[monthly['Profit'] < 0]
print("Loss months:\n", loss_months)
