# Daily Expense Tracker

A simple Python CLI app for recording daily expenses and calculating total spending.

این پروژه یک برنامه ساده برای ثبت و بررسی هزینه‌های روزانه است. کاربر می‌تواند هزینه‌های خود را وارد کند، فهرست آن‌ها را ببیند و مجموع مبالغ ثبت‌شده را محاسبه کند.

## Features

- Add a new expense with a name and amount
- View all recorded expenses
- Calculate total spending
- Display the number of recorded expenses
- Validate user input
- Interactive command-line menu

## Requirements

- Python 3
- No external packages required

## Project Structure

```text
daily-expense-tracker/
├── main.py
├── README.md
└── .gitignore
```

## How to Run

Run the following command from the project directory:

```bash
python3 main.py
```

## How It Works

The application stores expense names and amounts in two lists. Users can add expenses, view the list, and calculate the total amount through an interactive menu.

در این نسخه، اطلاعات فقط هنگام اجرای برنامه در حافظه نگهداری می‌شوند و پس از خروج از برنامه ذخیره نمی‌مانند.

## Concepts Practiced

- Variables and data types
- User input and output
- Conditional statements
- `while` and `for` loops
- Lists and list methods
- Functions
- Basic input validation
- Integer calculations

## Limitations

- Expenses are not saved after the program exits.
- Amounts must be entered as whole numbers.
- Expenses cannot yet be edited or deleted.

