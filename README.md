#  Budget Tracker with Savings Monitor

A beginner-friendly Python program designed to help students track their expenses, manage their allowance, and monitor their savings progress.

This project was created as part of a **Computer Science Performance Task** to demonstrate basic programming concepts such as input validation, data structures, and program organization.


#  Project Overview

Many students struggle with managing their allowance, especially those living in dormitories or managing limited weekly or monthly budgets. This program helps users record their expenses, calculate their remaining budget, and track their progress toward a savings goal.

The program runs in the **Python console** and provides simple prompts to guide users through the budgeting process.


#  Features

## 1. Monthly Budget Input
Users enter their monthly allowance. The program also supports on-the-spot calculations (e.g., "1400*4").

## 2. Expense Tracking
Users input expense categories and amounts. Categories only accept text input to ensure clean data.

## 3. Automatic Remaining Budget Calculation
The program automatically updates and displays the remaining budget after every transaction.

## 4. Expense Summaries
The system generates:
- Daily summaries
- Weekly summaries
- Monthly summaries

## 5. Savings Tracker
Users can:
- Set a savings goal
- Add savings
- View progress toward the goal

## 6. Editable Savings Goal
Users can update their savings goal anytime during program execution.

## 7. Budget Top-Up Feature
Users can add additional budget (e.g., extra allowance).

## 8. Smart Input System (Calculator Support)
Users can input expressions like:
- 1400*4
- 500+200

## 9. Input Validation
- Prevents invalid numbers
- Prevents negative values
- Ensures expense categories are text-only

## 10. Menu-Based Navigation
The program includes a structured menu system with options to:
1. Add Expense  
2. Add Savings  
3. View Summaries  
4. View Savings Progress  
5. Add Budget  
6. Edit Savings Goal  
7. Exit  

## 11. Feature-Level Exit System
Users can type **"exit"** inside any feature to return to the main menu without restarting the program.

## 12. Budget Protection System
The program prevents:
- Adding expenses when budget is depleted
- Adding savings beyond remaining budget

# 🛠 Technologies Used

- **Python 3**
- Python `datetime` library
- Lists and dictionaries for data storage

Python was chosen because it is beginner-friendly and suitable for console-based applications.


#  How to Run the Program

1. Make sure **Python is installed** on your computer.

2. Download or clone this repository.

3. Open a **terminal or command prompt**.

4. Navigate to the project folder.

5. Run the program:

```bash
python budget_tracker.py
