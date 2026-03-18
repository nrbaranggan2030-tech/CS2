#  Budget Tracker with Savings Monitor

A beginner-friendly Python program designed to help students track their expenses, manage their allowance, and monitor their savings progress.

This project was created as part of a **Computer Science Performance Task** to demonstrate basic programming concepts such as input validation, data structures, and program organization.

---

#  Project Overview

Many students struggle with managing their allowance, especially those living in dormitories or managing limited weekly or monthly budgets. This program helps users record their expenses, calculate their remaining budget, and track their progress toward a savings goal.

The program runs in the **Python console** and provides simple prompts to guide users through the budgeting process.

---

#  Features

## 1. Monthly Budget Input
Users enter their monthly allowance at the start of the program.  
This serves as the basis for calculating expenses and remaining balance.

## 2. Allowed On The Spot Computation
The program allows users to perform on-the-spot computations for their monthly budget, expenses, or savings. For example, users can quickly calculate their daily spending by entering simple expressions (e.g., 70 × 6) if they only remember the cost and quantity of items purchased.  

## 3. Expense Tracking
Users can add expenses by entering a category and amount.  
Example categories include:
- Food
- Transportation
- School Supplies

Each expense is recorded and stored in the program.

## 4. Automatic Remaining Budget Calculation
After each expense entry, the program automatically calculates the remaining budget based on the total expenses recorded.

## 5. Expense Summaries
The program generates summaries of expenses including:

- Daily summaries
- Weekly summaries
- Monthly summaries

These summaries help users analyze their spending habits.

## 6. Savings Tracker
Users can set a **savings goal** and add money toward that goal.  
The program displays the user's **savings progress and percentage completed**.

This feature encourages responsible financial habits and goal-setting.

## 7. Input Validation
The program prevents invalid inputs such as:
- Text instead of numbers
- Negative values
- Blank inputs

This ensures the program runs smoothly without crashing.

## 7. Menu-Based Navigation
Users interact with the program using a simple menu system.  
Options include:

1. Add Expense  
2. Add Savings  
3. View Expense Summaries  
4. View Savings Progress  
5. Exit Program  

This makes the program easier to navigate.

---

# 🛠 Technologies Used

- **Python 3**
- Python `datetime` library
- Lists and dictionaries for data storage

Python was chosen because it is beginner-friendly and suitable for console-based applications.

---

#  How to Run the Program

1. Make sure **Python is installed** on your computer.

2. Download or clone this repository.

3. Open a **terminal or command prompt**.

4. Navigate to the project folder.

5. Run the program:

```bash
python budget_tracker.py
