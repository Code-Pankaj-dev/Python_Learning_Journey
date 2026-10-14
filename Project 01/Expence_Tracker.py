# Expense Tracker

expenses = []    # List of expenses in the form of dictionary

print("Welcome to Expense Tracker")

while True:

    print("===== MENU =====")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter Your Choice (1-4): "))

    # ADD EXPENSE
    if choice == 1:
        date = input("Enter the Date: ")
        category = input("Type of Product: ")
        description = input("About the Product: ")
        price = float(input("Enter the Amount of Product: "))

        expense = {
            "date": date,
            "category": category,
            "description": description,
            "amount": price
        }

        expenses.append(expense)

        print("Expense Added Successfully!")

    # VIEW ALL EXPENSES
    elif choice == 2:

        if len(expenses) == 0:
            print("First, enter an expense and then view it.")
        else:
            print("===== YOUR EXPENSES =====")

            count = 1

            for everyexpense in expenses:
                print(
                    f"Expense Number {count} --> "
                    f"{everyexpense['date']}, "
                    f"{everyexpense['category']}, "
                    f"{everyexpense['description']}, "
                    f"₹{everyexpense['amount']}"
                )

                count = count + 1

    # VIEW TOTAL SPENDING
    elif choice == 3:

        total = 0

        for everyexpense in expenses:
            total = total + everyexpense["amount"]

        print("Total Spending: ₹", total)

    # EXIT
    elif choice == 4:
        print("Thanks for using my Expense Tracker!")
        break

    else:
        print("Invalid Choice, Try Again...")