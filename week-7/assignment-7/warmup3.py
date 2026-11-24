import os

print(os.getcwd())

if os.path.exists("../data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

print(os.path.join("..", "data", "expenses.csv"))
