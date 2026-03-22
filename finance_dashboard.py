import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("finance_data.csv")
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.to_period('M')

income = df[df['Type'] == 'Income']
expense = df[df['Type'] == 'Expense']

total_income = income['Amount'].sum()
total_expense = expense['Amount'].sum()
profit = total_income - total_expense

print("Total Income:", total_income)
print("Total Expense:", total_expense)
print("Profit:", profit)