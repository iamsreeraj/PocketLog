expenses = []
incomes = []



def expense():
    e_amount = int(input("Enter the amount :"))
    e_description = input("Enter the description :").lower()
    e_category = input("Enter the catogery :").lower()
    expense_record = {
            "amount" : e_amount, 
            "description" : e_description,
            "category" : e_category
        }
    expenses.append(expense_record)
        
def income():
    i_amount = int(input("Enter the amount :"))
    i_description = input("Enter the description :").lower()
    i_category = input("Enter the catogery :").lower()
    income_record = {
            "amount" : i_amount,
            "description" : i_description,
            "category" : i_category

        }
    incomes.append(income_record)
def balance():
    t_income = 0
    t_expense = 0
    for income in incomes:
        t_income += income["amount"]
        
    for expense in expenses:
            t_expense += expense["amount"]
    balance_amount = t_income - t_expense
    print("Balance :",balance_amount)
def transactions():
    print("INCOME")
    for income in incomes:
        print(income["description"], ":", income["amount"], "| Category:", income["category"])

    print("EXPENSE")
    for expense in expenses:
        print(expense["description"], ":", expense["amount"], "| Category:", expense["category"])

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
        expense()
    elif option == 2:
            income()
    elif option == 3:
        balance()
    elif option == 4:
        transactions()
    elif option == 5:
        break