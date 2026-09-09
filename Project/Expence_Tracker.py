# Expense Tracker #

expenses =[]    # List of expenses in fotm of dictionary
print("Welcome to Expense Tracker")
while True:

    print("===== MENU ====")
    print("1. Add Expense")
    print("2. View All Expense")
    print("3. View Total Spending")
    print("4. Exit")

    choice = int(input("Enter Your Choice (1-4): "))
# ADD EXPENSES
    if (choice == 1):
        date = input("Enter the Date: ")
        Category = input("Type of Product: ")
        Discription = input("About of Product: ")
        Price = float(input("Enter the Amount of Product: "))

        expense = {
            "date" : date,
            "Category" : Category,
            "Discription" :Discription,
            "Amount" : Price
        }

        expenses.append(expense)
        print("Expenses Added Succesfully")

# VIEW ALL EXPENSES:    
    elif (choice==2):
        if (len(expenses)==0):
            print("First! Enter the Product then View Easely--")
        else:
            print("==This is Your Expenses==")
            count = 1
            for everyinvest in expenses:
                print(f"Expense Number {count} --> {everyinvest["date"]}, {everyinvest["Category"]}, {everyinvest["Discription"]}, {everyinvest["Amount"]}")
                count = count+1

# View Total Spending
    elif (choice==3):
        total = 0
        for everyinvest in expense:
            total = total + expense["Amount"]

        print("Total Spending: ", total)

# Exit
    elif(choice==4):
        print("Thanks for You, You are use my System")
        break
    else:
        print(" Invalid Choice, Try Again..")
    

        
    






