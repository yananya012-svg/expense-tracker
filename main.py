# expense tracker project
expense =[] # list of expenses in form of dictionary
print("Welcome to the Expense Tracker! kitne kharch kiya aaj?")
while True:
    print("what are you upto")
    print("1. add expenses")
    print("2. view expenses")
    print("3. view total spending")
    print("4. exit")
    choice = input("enter your choice: ")

    # make sure we compare the same types
    if choice == "1":
        date = input("Enter the date: ")
        category = input("enter the category of your expenses: ")
        description = input("enter the description of your expenses: ")
        try:
            amount = float(input("enter the amount of your expenses: "))
        except ValueError:
            print("Invalid amount, please enter a number.")
            continue

        expense_item = {
            "date": date,
            "category": category,
            "description": description,
            "amount": amount
        }
        expense.append(expense_item)
        print("expense added successfully")

    elif choice == "2":
        if len(expense) == 0:
            print("no expenses to show")
        else:
            print("this is your expenses")
            count = 1
            for kharcha in expense:
                print(f"{count}. date: {kharcha['date']}, category: {kharcha['category']}, description: {kharcha['description']}, amount: {kharcha['amount']}")
                count += 1

    elif choice == "3":
        total_spending = 0
        for kharcha in expense:
            total_spending += kharcha['amount']
        print(f"your total spending is {total_spending}")

    elif choice == "4":
        print("thank you for using the expense tracker")
        break

    else:
        print("invalid choice, please try again")
