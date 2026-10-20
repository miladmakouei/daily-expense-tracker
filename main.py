
expense_names = []
expense_amounts = []


def add_expense():
    name = input("Enter expense name: ").strip()

    if name == "":
        print("Expense name cannot be empty.")
        return

    amount_text = input("Enter amount in toman: ")

    if not amount_text.isdigit():
        print("Please enter a valid whole number.")
        return

    amount = int(amount_text)

    if amount <= 0:
        print("Amount must be greater than zero.")
        return

    expense_names.append(name)
    expense_amounts.append(amount)

    print("Expense added successfully.")


def show_expenses():
    if len(expense_names) == 0:
        print("No expenses recorded yet.")
        return

    print("\n--- Expense List ---")

    for index in range(len(expense_names)):
        print(
            f"{index + 1}. {expense_names[index]}: "
            f"{expense_amounts[index]:,} toman"
        )


def show_total():
    total = 0

    for amount in expense_amounts:
        total = total + amount

    print(f"Total expenses: {total:,} toman")
    print(f"Number of expenses: {len(expense_amounts)}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Show total")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        show_expenses()

    elif choice == "3":
        show_total()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option. Please try again.")
