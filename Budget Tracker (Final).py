"""
Budget Tracker with Savings Monitor
A beginner-friendly Python program for students to track expenses,
manage allowance, and monitor savings progress.

Created by:
- Nessy Ruby P. Baranggan
- Lourice Jay G. Bagnol
- Stella Emmanuelle M. Hermosilla
"""

import datetime

# Data storage
expenses = []
daily_summary = {}
weekly_summary = {}
monthly_summary = {}

total_savings = 0
savings_goal = 0
monthly_budget = 0


# -------------------------
# INPUT FUNCTIONS
# -------------------------

def get_budget():
    while True:
        try:
            budget = float(input("Enter your monthly budget: "))
            if budget <= 0:
                print("Budget must be greater than 0.")
            else:
                return budget
        except ValueError:
            print("Invalid input. Please enter a number.")


def get_savings_goal():
    while True:
        try:
            goal = float(input("Enter your savings goal: "))
            if goal < 0:
                print("Savings goal cannot be negative.")
            else:
                return goal
        except ValueError:
            print("Invalid input. Please enter a number.")


# -------------------------
# EXPENSE FUNCTIONS
# -------------------------

def add_expense():
    while True:
        category = input("Enter expense category (Food, Transport, School, etc.): ").strip()

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

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)

        # Update summaries
        daily_summary[date] = daily_summary.get(date, 0) + amount

        week = date.isocalendar()[1]
        weekly_summary[week] = weekly_summary.get(week, 0) + amount

        month = date.month
        monthly_summary[month] = monthly_summary.get(month, 0) + amount

        print("\nExpense added successfully!")
        print(f"Remaining Budget: {calculate_remaining_budget():.2f}")

        break


# -------------------------
# SAVINGS FUNCTIONS
# -------------------------

def add_savings():
    global total_savings

    while True:
        try:
            amount = float(input("Enter amount to add to savings: "))

            if amount < 0:
                print("Amount cannot be negative.")
                continue

            if amount > calculate_remaining_budget():
                print("Not enough remaining budget to save that amount.")
                continue

            total_savings += amount

            print("\nSavings added successfully!")
            show_savings_progress()

            break

        except ValueError:
            print("Invalid input. Please enter a number.")


def show_savings_progress():
    if savings_goal == 0:
        print("No savings goal set.")
        return

    progress = (total_savings / savings_goal) * 100

    print(f"Total Savings: {total_savings:.2f}")
    print(f"Savings Goal: {savings_goal:.2f}")
    print(f"Progress: {progress:.2f}%")

    if total_savings >= savings_goal:
        print("Congratulations! You reached your savings goal!")


# -------------------------
# CALCULATIONS
# -------------------------

def calculate_remaining_budget():
    total_expenses = sum(expense['amount'] for expense in expenses)
    return monthly_budget - total_expenses - total_savings


# -------------------------
# SUMMARIES
# -------------------------

def view_summaries():

    print("\n====================")
    print("EXPENSE SUMMARIES")
    print("====================")

    print("\nDaily Summary")
    for date, total in daily_summary.items():
        print(f"{date}: {total:.2f}")

    print("\nWeekly Summary")
    for week, total in weekly_summary.items():
        print(f"Week {week}: {total:.2f}")

    print("\nMonthly Summary")
    for month, total in monthly_summary.items():
        print(f"Month {month}: {total:.2f}")


# -------------------------
# MENU SYSTEM
# -------------------------

def show_menu():

    print("\n==============================")
    print("      BUDGET TRACKER")
    print("==============================")
    print("1 - Add Expense")
    print("2 - Add Savings")
    print("3 - View Summaries")
    print("4 - View Savings Progress")
    print("5 - Exit")
    print("==============================")


# -------------------------
# MAIN PROGRAM
# -------------------------

def main():
    global monthly_budget
    global savings_goal

    print("Welcome to Budget Tracker!")

    monthly_budget = get_budget()
    savings_goal = get_savings_goal()

    while True:

        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            add_savings()

        elif choice == "3":
            view_summaries()

        elif choice == "4":
            show_savings_progress()

        elif choice == "5":
            print("\nThank you for using Budget Tracker!")
            view_summaries()
            show_savings_progress()
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
