def create_account():
    print("Account created successfully")

def deposit():
    print("Amount deposited")

def withdraw():
    print("Amount withdrawn")

def checkbalance():
    print("Your balance is 1000")

print("1. Create Account")
print("2. Deposit")
print("3. Withdraw")
print("4. Check Balance")

choice = input("Enter your choice: ")

if choice == "1":
    create_account()
elif choice == "2":
    deposit()
elif choice == "3":
    withdraw()
elif choice == "4":
    checkbalance()
else:
    print("Invalid choice")