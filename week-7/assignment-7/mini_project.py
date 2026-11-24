import csv
import os
from datetime import datetime

path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(path):
    print(f"Error: {path} not found.")
else:
    with open(path, newline="") as f:
        rows = list(csv.DictReader(f))

    for row in rows:
        row["amount"] = float(row["amount"])

    food = []
    for row in rows:
        if row["category"] == "Food":
            food.append(row)

    total = 0
    for row in food:
        total += row["amount"]

    today = datetime.now().strftime("%B %d, %Y")
    with open("food_report.txt", "w", encoding="utf-8") as out:
        out.write(f"Food Expense Report — generated {today}\n")
        for row in food:
            out.write(f"{row['date']}: ${row['amount']:.2f}\n")
        out.write(f"Total: ${total:.2f}\n")

    print("Report written to food_report.txt")
