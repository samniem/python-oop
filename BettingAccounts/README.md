## Object Manager Object and Composition

An **object manager object** [(Kalb, 2021)](https://nostarch.com/object-oriented-python) is an object that has been designed to manage other objects. Usually the other objects are of the same class as this makes developing the methods for managing those objects more straightforward. The objects to be managed are usually stored in a dictionary or a list with a logical accessing scheme such as unique dictionary keys

[Object manager object image](https://github.com/samniem/python-oop/tree/main/BettingAccounts/omo.jpg)


A **composition** ([Kalb, 2021](https://nostarch.com/object-oriented-python); [Wikipedia, 2022a](https://en.wikipedia.org/wiki/Object_composition)) describes the logical or conceptual structure of information, where one object manages one or more objects of a different type.


## Example program for creating betting accounts

The source code is available [here](https://github.com/samniem/python-oop/tree/main/BettingAccounts).


### Main.py

The main.py program imports the manager class and initializes one object based on the manager class model. Additionally, the main.py file handles user input using a while True loop.


```
from AccountsManager import *

manager = AccountsManager()
print("Input list:")
print("\tn - new account (name, password, balance)")
print("\ta - add balance (id, password, balance)")
print("\tw - withdraw balance (id, password, balance)")
print("\td - delete account (id)")
print("\tv - view balance (id, password)")
print("\tq - quit program")

while True:
   option = input("Select action: ")
   if(option == "n"):
       name = input("Add account name: ")
       pw = input("Add account password: ")
       bal = float(input("Add account balance: "))
       id = manager.addAccount(name, pw, bal)
       print("Account id is", id)
   elif(option == "v"):
       id = int(input("Please provide account id "))
       pw = input("Please provide password ")
       manager.viewBalance(id, pw)
   elif(option == "a"):
       id = int(input("Please provide account id "))
       pw = input("Please provide password ")
       bal = float(input("Please provide balance to add "))
       manager.addBalance(id, pw, bal)
   elif(option == "w"):
       id = int(input("Please provide account id "))
       pw = input("Please provide password ")
       bal = float(input("Please provide balance to withdraw "))
       manager.withdrawBalance(id, pw, bal)
   elif(option == "q"):
       break
   else:
       print("Incorrect input")
```



### AccountsManager.py

This file manages user requests made from main.py related to specific accounts. The class model for each specific account is imported from Account.py. 


```
from Account import *

class AccountsManager():
   def __init__(self):
       self.accounts = {}
       self.latestAccount = 0

   def addAccount(self, name, password, balance=0):
       newAccount = Account(name, password, balance)
       self.latestAccount += 1
       self.accounts[self.latestAccount] = newAccount
       return self.latestAccount

   def viewBalance(self, accountNumber, password):
       a = self.accounts[accountNumber]
       if(a.password == password):
           print("Account", a.name, "has", a.balance)
       else:
           print("Incorrect password")
   def addBalance(self, accountNumber, password, balance):
       a = self.accounts[accountNumber]
       a.addBalance(balance, password)
   def withdrawBalance(self, accountNumber, password, balance):
       a = self.accounts[accountNumber]
       a.withdrawBalance(balance, password)
   def deleteAccount(self, accountNumber):
       del self.accounts[accountNumber]
```



### Accounts.py

The account.py handles operations such as depositing funds and withdrawing funds for an individual betting account.


```
class Account():
   def __init__(self, name, password, balance):
       self.balance = balance
       self.name = name
       self.password = password



   def addBalance(self, balance, password):
       if(password != self.password):
           print("Incorrect password")
       elif(balance <= 0):
           print("Cannot add negative or zero balance")
       else:
           self.balance += balance



   def withdrawBalance(self, balance, password):
       if(password != self.password):
           print("Incorrect password")
       elif(balance >= 0):
           print("Cannot withdraw zero or negative balance")
       elif(balance > self.balance):
           print("Cannot withdraw more than account balance", self.balance)
       else:
           self.balance -= balance


```



## References

Kalb, I. (2021). Object-Oriented Python: Master OOP by Building Games and GUIs. No Starch Press. https://nostarch.com/object-oriented-python

Wikipedia (2022a). Object composition. https://en.wikipedia.org/wiki/Object_composition

Wikipedia (2022b). Object-oriented Design. https://en.wikipedia.org/wiki/Object-oriented_design
