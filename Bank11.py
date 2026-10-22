bank_accounts = {
    "111": {"name": "sreenu", "balance": 1000, "pin": "1234"},
    "222": {"name": "hema", "balance": 2000, "pin": "5678"}
}

def create_account():
    acc_number = input("Enter new account number: ")
    
    if acc_number in bank_accounts:
        print("Account already exists")
    else:
        name = input("Enter name: ")
        pin = input("Set 4-digit PIN: ")
        balance = float(input("Enter initial balance: "))
        
        bank_accounts[acc_number] = {
            "name": name,
            "balance": balance,
            "pin": pin
        }
        print("Account created successfully")

def login():
    acc_number = input("Enter account number: ")
    pin = input("Enter PIN: ")
    
    if acc_number in bank_accounts and bank_accounts[acc_number]["pin"] == pin:
        print(f"Welcome {bank_accounts[acc_number]['name']}")
        return acc_number
    else:
        print("Invalid account or PIN")
        return None

def deposit(acc_number):
    amount = float(input("Enter amount to deposit: "))
    
    if amount > 0:
        bank_accounts[acc_number]["balance"] += amount
        print(f"Deposited {amount}. Balance: {bank_accounts[acc_number]['balance']}")
    else:
        print("Invalid amount")

def withdraw(acc_number):
    amount = float(input("Enter amount to withdraw: "))
    
    if amount <= bank_accounts[acc_number]["balance"]:
        bank_accounts[acc_number]["balance"] -= amount
        print(f"Withdrawn {amount}. Balance: {bank_accounts[acc_number]['balance']}")
    else:
        print("Insufficient balance")

def check_balance(acc_number):
    print(f"Balance: {bank_accounts[acc_number]['balance']}")


# 🔁 Main Program
while True:
    print("\n--- Bank System ---")
    print("1. Create Account")
    print("2. Login")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        create_account()
        
    elif choice == "2":
        user = login()
        
        if user:
            while True:
                print("\n--- Account Menu ---")
                print("1. Deposit")
                print("2. Withdraw")
                print("3. Check Balance")
                print("4. Logout")
                
                option = input("Enter option: ")
                
                if option == "1":
                    deposit(user)
                elif option == "2":
                    withdraw(user)
                elif option == "3":
                    check_balance(user)
                elif option == "4":
                    print("Logged out")
                    break
                else:
                    print("Invalid option")
                    
    elif choice == "3":
        print("Thank you!")
        break
    else:
        print("Invalid choice")    9176664747       9585465603 