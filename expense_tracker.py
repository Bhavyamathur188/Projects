import csv
import os

FILE_NAME = "expenses.csv"

expenses = []


def load_expenses():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append({
                    "Date": row["Date"],
                    "Category": row["Category"],
                    "Description": row["Description"],
                    "Amount": float(row["Amount"])
                })


def save_expenses():
    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Date", "Category", "Description", "Amount"]

        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()

        for expense in expenses:
            writer.writerow(expense)


def add_expense():
    print("\nAdd Expense")

    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    description = input("Enter Description: ")

    try:
        amount = float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount.")
        return

    expenses.append({
        "Date": date,
        "Category": category,
        "Description": description,
        "Amount": amount
    })

    save_expenses()

    print("Expense added successfully.")


def view_expenses():

    if not expenses:
        print("\nNo expenses found.")
        return

    print("\nExpense List")
    print("-" * 70)

    for expense in expenses:
        print(
            f"{expense['Date']} | "
            f"{expense['Category']} | "
            f"{expense['Description']} | "
            f"${expense['Amount']:.2f}"
        )


def total_expense():

    total = sum(expense["Amount"] for expense in expenses)

    print(f"\nTotal Expense: ${total:.2f}")


def menu():

    load_expenses()

    while True:

        print("\n===== EXPENSE TRACKER =====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            total_expense()

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


menu()