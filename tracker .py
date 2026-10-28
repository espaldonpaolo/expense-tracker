#Project: Expense Tracker - Installment 5: The Menu Comes Alive
#Author: Paolo R. Espaldon
#Description: A simple program to track expenses using a working menu.
print("=" * 40)
print(" " * 12 +"EXPENSE TRACKER")
print(" " * 6 +"Spend Smart, Save More.")
print("=" * 40)
name = input("what is your name? ")
tax_percent = int (input("Tax rate (%)? "))
budget = float(input("Budget? "))
print(f"welcome, {name}!")
subtotal = 0
count = 0
while True:
    print("\nMAIN MENU")
    print("  [1] Add an expense")
    print("  [2] View all expenses\t\t(coming soon)")
    print("  [3] Show total spent")
    print("  [4] Exit")

    choice = input ("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1

        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")

    elif choice == "2":
        print("  Coming soon: the tracker can't remember each item yet.")

    elif choice == "3":
        tax = subtotal * (tax_percent / 100)
        total = subtotal + tax
        left = budget - total
        over_budget = total > budget

        print("\nSUMMARY")
        print(f"{'Expenses:':<20}{count:>10}")
        print(f"{'Subtotal:':<20}${subtotal:>9.2f}")
        print(f"{'Tax (' + str(tax_percent) + '%):':<20}${tax:>9.2f}")
        print(f"{'Grand total:':<20}${total:>9.2f}")

        if over_budget:
            print(f"Over budget by ${total - budget:.2f}!")
        elif total > budget * 0.90:
            print(f"Careful: only ${left:.2f} left.")
        else:
            print(f"Within budget. ${left:.2f} left.")

    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print("Made by: Paolo Espaldon  |  Installment 5")
        print("=" * 40)
        break
    else:
        print("  Please choose 1, 2, 3 or 4.")