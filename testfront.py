from backend import create_account, get_balance, deposit, withdraw, delete_account, modify_account

def menu():
    print("\n=== 🏦 Welcome to the Bank!  ===")
    print("Choose an option:")
    print("  [1] Create a New Account")
    print("  [2] Deposit Funds")
    print("  [3] Withdraw Funds")
    print("  [4] Get Current Balance")
    print("  [5] Modify Account Details")
    print("  [6] Delete Account")
    print("  [7] Exit Program")

def getinput(str):
    while True:
        try:
            return int(input(str))
        except ValueError:
            print("❌ Please enter a valid number.")

running = True
while running:
    menu()
    choice = getinput("\nEnter your choice (1-7): ")

    if choice == 1:
        username = input("Enter a username: ")
        password = input("Enter a password: ")
        print(create_account(username, password))

    elif choice == 2:
        username = input("Enter your username: ")
        amount = getinput("Enter deposit amount: $")
        print(deposit(username, amount))

    elif choice == 3:
        username = input("Enter your username: ")
        amount = getinput("Enter withdrawal amount: $")
        print(withdraw(username, amount))

    elif choice == 4:
        username = input("Enter your username: ")
        print(get_balance(username))

    elif choice == 5:
        username = input("Enter your current username: ")
        print("Modify Options:\n  [1] Change Username\n  [2] Change Password\n  [3] Change Both")
        sub_choice = getinput("Enter your choice (1-3): ")

        new_username = None
        new_password = None

        if sub_choice == 1:
            new_username = input("Enter your new username: ")
        elif sub_choice == 2:
            new_password = input("Enter your new password: ")
        elif sub_choice == 3:
            new_username = input("Enter your new username: ")
            new_password = input("Enter your new password: ")
        else:
            print("❌ Invalid option.")
            continue

        print(modify_account(username, new_username, new_password))

    elif choice == 6:
        username = input("Enter your username: ")
        print(delete_account(username))

    elif choice == 7:
        print("👋 Thanks for using C2C Bank. Goodbye!")
        running = False

    else:
        print("❌ Invalid option. Please enter a number between 1 and 7.")





