import questionary
import time
from accountClasses import *

def askUser():
    print()
    choice = questionary.select(
        "🏦 What do you want to do?",
        choices = [
            "➕ Add New Account",
            "🗑️ Delete Bank Account",
            "💰 Deposit Money",
            "💸 Withdraw Money",
            "🧾 Check Balance",
            "🔍 Search Account",
            "📋 In-order Traversal",
            "🧭 Pre-order Traversal",
            "🔄 Post-order Traversal",
            "❌ Exit Program"
        ]
    ).ask()
    return choice

try:
    print("\nWelcome to the Bank Account Management System!\n")
    a = Account()
    while True:
        choice = askUser()
        
        if choice == "➕ Add New Account":
            accNum = int(input("Enter New Account Number: "))
            accName = input("Enter Your Full Name: ")
            balance = float(input("Enter the Balance: "))
            a.add_NewAcc(accNum, accName, balance)
        
        elif choice == "🗑️ Delete Bank Account":
            accNum = int(input("Enter Your Account Number: "))
            a.delete_Acc(accNum)
        
        elif choice == "💰 Deposit Money":
            accNum = int(input("Enter Your Account Number: "))
            depositAmount = float(input("Enter the amount of money: "))
            a.deposit(accNum, depositAmount)
        
        elif choice == "💸 Withdraw Money":
            accNum = int(input("Enter Your Account Number: "))
            withdrawAmount = float(input("Enter the amount of money: "))
            a.withdrawal(accNum, withdrawAmount)
        
        elif choice == "🧾 Check Balance":
            accNum = int(input("Enter Your Account Number: "))
            account = a.check_Balance(accNum)
            print(account)
        
        elif choice == "🔍 Search Account":
            accNum = int(input("Enter Your Account Number: "))
            account = a.searchAcc(accNum)
            print(account)
        
        elif choice == "📋 In-order Traversal":
            print(a.inOrder(a.root))
        
        elif choice == "🧭 Pre-order Traversal":
            print(a.preOrder(a.root))
        
        elif choice == "🔄 Post-order Traversal":
            print(a.postOrder(a.root))
        
        elif choice == "❌ Exit Program":
            print("Exiting the program.\n")
            break
        
        else:
            print("\nInvalid choice. Please try again.\n")
        
        time.sleep(1)

except ValueError as e:
    print(f"\n⚠️ Error: {e}\n")

except Exception as e:
    print(f"\n⚠️ An unexpected error occurred: {e}\n")

except KeyboardInterrupt:
    print("\n⚠️ Program interrupted by user.\n")