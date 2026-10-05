#Project: Expense Tracker - Installment 3: Tracker does math
#Author: Paolo R. Espaldon
#Description: A simple program to track two expenses, calculate tax, and check a budget.
print("=" * 40)
print(" " * 12 +"EXPENSE TRACKER")
print(" " * 6 +"Spend Smart, Save More.")
print("=" * 40)
print("MAIN MENU")
print(" " * 2 + "[1] Add an expense\t\t(coming soon)")
print(" " * 2 + "[2] View all expenses\t\t(coming soon)")
print(" " * 2 + "[3] Show total spent\t\t(coming soon)")
print(" " * 2 + "[4] Exit\t\t\t(coming soon)\n")
name = input("What is your name? ")
print("Welcome, Sam! Let's log two expenses.")
subtotal = 0
item1 = input("\nFirst expense? ")
amount1 = float(input(f"Amount? "))
subtotal += amount1
item2 = input("Second expense? ")
amount2 = float(input(f"Amount? "))
subtotal += amount2
average = subtotal / 2
tax_percent = int(input ("Tax rate (%)? "))
tax = subtotal * (tax_percent / 100)
total = subtotal + tax
budget = float(input("Budget ?"))
over_budget = total > budget
left = budget - total
print("-" * 40)
print("\nSUMMARY")
print(f"  - {item1}:".ljust(16) + f"${amount1}")
print(f"  - {item2}:".ljust(16) + f"${amount2}")
print(f"{'Subtotal:'.ljust(16)}${subtotal}")
print(f"{'Average:'.ljust(16)}${average}")
print(f"{('Tax (' + str(tax_percent) + '%):').ljust(16)}${tax}")
print(f"{'Grand total:'.ljust(16)}${total}")
print(f"{'Over budget?'.ljust(16)}{over_budget}")
print(f"{'Left in budget:'.ljust(16)}${left}")
print("-" * 40)
print(f"Made by: Paolo Espaldon | Installment 3")
print("=" * 40)