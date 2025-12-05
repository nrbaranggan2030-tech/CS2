"""
Budget Tracker
A beginner-friendly program to track expenses, manage allowance, and summarize spending.
Created by:
- Nessy Ruby P. Baranggan
- Lourice Jay G. Bagnol
- Stella Emmanuelle M. Hermosilla
"""

import datetime

# Initialize data structures
expenses = []
daily_summary = {}
weekly_summary = {}
monthly_summary = {}

def get_budget():
    while True:
        try:
            budget = float(input("Enter your monthly budget: "))
            if budget <= 0:
                print("Budget must be greater than 0. Try again.")
            else:
                return budget
        except ValueError:
            print("Invalid input. Please enter a number.")

def add_expense():
    while True:
        category = input("Enter expense category (Food, Transportation, School Supplies, etc.): ").strip()
        if not category:
            print("Category cannot be blank.")
            continue

        try:
            amount = float(input("Enter expense amount: "))
            if amount < 0:
                print("Amount cannot be negative.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        date = datetime.date.today()
        expense = {"date": date, "category": category, "amount": amount}
        expenses.append(expense)

        # Update daily summary
        daily_summary[date] = daily_summary.get(date, 0) + amount
        # Update weekly summary
        week = date.isocalendar()[1]
        weekly_summary[week] = weekly_summary.get(week, 0) + amount
        # Update monthly summary
        month = date.month
        monthly_summary[month] = monthly_summary.get(month, 0) + amount

        print(f"\nExpense added successfully! Remaining budget: {calculate_remaining_budget():.2f}")
        break

def calculate_remaining_budget():
    total_expenses = sum(expense['amount'] for expense in expenses)
    return monthly_budget - total_expenses

def view_summaries():
    print("\n--- Daily Summary ---")
    for date, total in daily_summary.items():
        print(f"{date}: {total:.2f}")

    print("\n--- Weekly Summary ---")
    for week, total in weekly_summary.items():
        print(f"Week {week}: {total:.2f}")

    print("\n--- Monthly Summary ---")
    for month, total in monthly_summary.items():
        print(f"Month {month}: {total:.2f}")

def main():
    global monthly_budget
    print("Welcome to Budget Tracker!")
    monthly_budget = get_budget()

    while True:
        add_expense()
        view = input("\nDo you want to view summaries? (yes/no): ").strip().lower()
        if view == "yes":
            view_summaries()

        another = input("\nDo you want to add another expense? (yes/no): ").strip().lower()
        if another != "yes":
            print("\nThank you for using Budget Tracker!")
            view_summaries()
            break

if __name__ == "__main__":
    main()
