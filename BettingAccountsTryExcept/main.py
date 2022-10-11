from AccountsManager import *

manager = AccountsManager()
print("Input list:")
print("\tn - new account (name, password, balance)")
print("\ta - add balace (id, password, balance)")
print("\tw - withdraw balance (id, password, balance)")
print("\td - delete account (id)")
print("\tv - view balance (id, password)")
print("\tq - quit program")

while True:
    option = input("Select action: ")
    try:
        if(option == "n"):
            name = input("Add account name: ")
            pw = input("Add account password: ")
            amt = input("Add account balance: ")
            id = manager.addAccount(name, pw, amt)
            print("Account id is", id)
        elif(option == "v"):
            id = input("Please provide account id: ")
            pw = input("Please provide password: ")
            manager.viewBalance(id, pw)
        elif(option == "a"):
            id = input("Please provide account id: ")
            pw = input("Please provide password: ")
            amt = input("Please provide balance to add: ")
            manager.addBalance(id, pw, amt)
        elif(option == "w"):
            id = input("Please provide account id: ")
            pw = input("Please provide password: ")
            amt = input("Please provide balance to withdraw: ")
            manager.withdrawBalance(id, pw, amt)
        elif(option == "q"):
            break
        else:
            print("Incorrect input")
    except AbortAccountTransaction as Abort:
        print(Abort)