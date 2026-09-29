expenses = []
incomes = []

while True:

    print("_____PocketLog_____")
    print("Choose an option")
    print("1 for Add Expense")
    print("2 for Add Income")
    print("3 for Check Balance")
    print("4 for View Transactions")
    print("5 for Exit")
    option = int(input("Enter an option :"))
    if option == 1:
        e_amount = int(input("Enter the amount :"))
        e_description = input("Enter the description :").lower()
        expense = {
            "amount" : e_amount, 
            "description" : e_description
        }
        expenses.append(expense)
        
    elif option == 2:
        i_amount = int(input("Enter the amount :"))
        i_description = input("Enter the description :").lower()
        income = {
            "amount" : i_amount,
            "description" : i_description
        }
        incomes.append(income)
    elif option == 3:
        t_income = 0
        t_expense = 0
        for income in incomes:
            t_income += income["amount"]
        
        for expense in expenses:
            t_expense += expense["amount"]
        balance = t_income - t_expense
        print("Balance :",balance)
    elif option == 4:
        
        print("----- Expenses -----")

        for expense in expenses:
            print("Expense | Amount:", expense["amount"], "| Description:", expense["description"])

        print("----- Income -----")

        for income in incomes:
            print("Income | Amount:", income["amount"], "| Description:", income["description"])  
    elif option == 5:
        break
    else:
        print("Choose an option between 1-5")
