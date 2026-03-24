import datetime

# ===============================
# DATA STORAGE
# ===============================
expenses = []
daily_summary = {}
weekly_summary = {}
monthly_summary = {}

total_savings = 0


# ===============================
# HELPER: CALCULATOR INPUT
# ===============================
def evaluate_input(user_input):
    try:
        return float(eval(user_input))
    except:
        return None


# ===============================
# INPUT FUNCTIONS
# ===============================
def get_budget():
    while True:
        user_input = input("Enter your monthly budget: ")
        value = evaluate_input(user_input)

        if value is None or value <= 0:
            print("Invalid input. Try again (you can use 1400*4).")
        else:
            return value


def get_savings_goal():
    while True:
        user_input = input("Enter your savings goal: ")
        value = evaluate_input(user_input)

        if value is None or value < 0:
            print("Invalid input.")
        else:
            return value


# ===============================
# EXPENSE FUNCTION
# ===============================
def add_expense():
    while True:

        if calculate_remaining_budget() <= 0:
            print("Budget depleted. Cannot add expense.")
            return

        category = input("Enter expense category (or type 'exit'): ").strip()

        if category.lower() == "exit":
            return

        # ✅ Only allow text
        if not category.isalpha():
            print("Invalid expense category name. Only input text.")
            continue  # stays in this function, DOES NOT go back to menu

        user_input = input("Enter expense amount (or type 'exit'): ")

        if user_input.lower() == "exit":
            return

        amount = evaluate_input(user_input)

        if amount is None or amount < 0:
            print("Invalid amount.")
            continue

        if amount > calculate_remaining_budget():
            print("Not enough remaining budget.")
            continue

        date = datetime.date.today()

        expenses.append({
            "date": date,
            "category": category,
            "amount": amount
        })

        # Update summaries
        daily_summary[date] = daily_summary.get(date, 0) + amount
        weekly_summary[date.isocalendar()[1]] = weekly_summary.get(date.isocalendar()[1], 0) + amount
        monthly_summary[date.month] = monthly_summary.get(date.month, 0) + amount

        print(f"Expense added! Remaining: {calculate_remaining_budget():.2f}")
        break

# ===============================
# SAVINGS FUNCTION
# ===============================
def add_savings():
    global total_savings

    while True:

        if calculate_remaining_budget() <= 0:
            print("Budget depleted. Cannot add savings.")
            return

        user_input = input("Enter savings amount (or type 'exit'): ")

        if user_input.lower() == "exit":
            return

        amount = evaluate_input(user_input)

        if amount is None or amount < 0:
            print("Invalid amount.")
            continue

        if amount > calculate_remaining_budget():
            print("Not enough remaining budget.")
            continue

        total_savings += amount
        print("Savings added successfully!")
        break


def edit_savings_goal():
    global savings_goal

    while True:
        print(f"Current goal: {savings_goal}")

        user_input = input("Enter new savings goal (or type 'exit'): ")

        if user_input.lower() == "exit":
            return

        value = evaluate_input(user_input)

        if value is None or value < 0:
            print("Invalid input.")
            continue

        savings_goal = value
        print("Savings goal updated!")
        break


def view_savings():
    print("\n--- SAVINGS ---")
    print(f"Goal: {savings_goal}")
    print(f"Saved: {total_savings}")

    if savings_goal > 0:
        percent = (total_savings / savings_goal) * 100
        print(f"Progress: {percent:.2f}%")

        if total_savings >= savings_goal:
            print("Goal reached!")


# ===============================
# BUDGET FUNCTIONS
# ===============================
def add_budget():
    global monthly_budget

    while True:
        user_input = input("Enter additional budget (or type 'exit'): ")

        if user_input.lower() == "exit":
            return

        amount = evaluate_input(user_input)

        if amount is None or amount < 0:
            print("Invalid amount.")
            continue

        monthly_budget += amount
        print(f"New total budget: {monthly_budget}")
        break


def calculate_remaining_budget():
    total_expenses = sum(e['amount'] for e in expenses)
    return monthly_budget - total_expenses - total_savings


# ===============================
# SUMMARY FUNCTION
# ===============================
def view_summaries():
    print("\n--- DAILY ---")
    for d, total in daily_summary.items():
        print(d, ":", total)

    print("\n--- WEEKLY ---")
    for w, total in weekly_summary.items():
        print("Week", w, ":", total)

    print("\n--- MONTHLY ---")
    for m, total in monthly_summary.items():
        print("Month", m, ":", total)


# ===============================
# MENU
# ===============================
def menu():
    print("\n====== MENU ======")
    print("1 - Add Expense")
    print("2 - Add Savings")
    print("3 - View Summaries")
    print("4 - View Savings")
    print("5 - Add Budget")
    print("6 - Edit Savings Goal")
    print("7 - Exit")


# ===============================
# MAIN
# ===============================
def main():
    global monthly_budget, savings_goal

    print("=== BUDGET TRACKER ===")

    monthly_budget = get_budget()
    savings_goal = get_savings_goal()

    while True:
        menu()
        choice = input("Choose: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            add_savings()
        elif choice == "3":
            view_summaries()
        elif choice == "4":
            view_savings()
        elif choice == "5":
            add_budget()
        elif choice == "6":
            edit_savings_goal()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
