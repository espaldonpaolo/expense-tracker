#Project: Expense Tracker - Installment 1: Landing Page 
#Author: Paolo R. Espaldon
#Description: A simple program to track expenses.
print("=" * 40)
print(" " * 12 +"EXPENSE TRACKER")
print(" " * 6 +"Spend Smart, Save More.")
print("=" * 40)
print("MAIN MENU")
print(" " * 2 + "[1] Add an expense\t\t(coming soon)")
print(" " * 2 + "[2] View all expenses\t\t(coming soon)")
print(" " * 2 + "[3] Show total spent\t\t(coming soon)")
print(" " * 2 + "[4] Exit\t\t\t(coming soon)\n")
#Project: Expense Tracker - Installment 2: Talking to the User
#Author: Paolo R. Espaldon
#Description: A simple program to track two expenses and calculate the total and average.
name = input("What is your name? ")
print("Welcome, Sam! Let's log two expenses.")
item1 = input("\nFirst expense? ")
amount1 = float(input(f"Amount? "))
item2 = input("Second expense? ")
amount2 = float(input(f"Amount? "))
total = amount1 + amount2
average = total / 2
print("-" * 40)
print("\nSUMMARY")
print(f"{item1:<25}{amount1:>10.2f}")
print(f"{item2:<25}{amount2:>10.2f}")
print(f"{'Total Spent':<25}{total:>10.2f}")
print(f"{'Average':<25}{average:>10.2f}")
print("-" * 40)
print("Made by: Paolo Espaldon | Installment 2")
print("=" * 40)