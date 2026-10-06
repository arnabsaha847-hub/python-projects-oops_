def check_balance(balance):
    print("Current Balance: is:", balance)

def deposit(balance):
    amount = float(input ("enter deposit amount: "))

    if amount >0:
        balance += amount
        print("Deposit successful. New balance is:", balance)
        print("New balance:", balance)
    else:
        print("Invalid deposit amount.")

        return balance

def withdraw(balance):
    amount = float(input("Enter withdrawal amount: "))

    if amount <= 0:
        print("Invalid withdrawal amount.")
    elif amount > balance:
        print("Insufficient balance.")
    else:
        balance -= amount
        print("please collect your cash.")
        print("remaining balance:", balance)

    return balance

correct_pin = "1234"
pin = input("Enter your PIN:")

if pin == correct_pin:
    print("\nLogin successful!")

    balance = 5000

    while True:
        print("\n----ATM Menu----")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            check_balance(balance)
        elif choice == "2":
            balance = deposit(balance)
        elif choice == "3":
            balance = withdraw(balance)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
else:
    print("Incorrect PIN. Access denied.")
