# Exceptions in Python with Objects

In Python there are three generic ways to handle errors and issues in code. The three methods are try-except, if-except and an except object that can be set into the two aforementioned ways of handling errors.


## How [Logical Errors](https://www.geeksforgeeks.org/errors-and-exceptions-in-python/) Behave In Python (and Many Other Programming Languages)

An error is generally thrown when something unexpected happens in the code that should not happen. Some common error causes are



1. division by zero
2. erroneous user input
3. bad data from API
4. using wrong type of data for an operation such as adding string to an integer
5. converting string to an integer and other nonsensical conversion operations

When an error is thrown it will try to exit each function or method upwards until it finds an except block that has been designed to handle the error. If the program does not contain a suitable except handler at some level, then the program will exit with an error status. 


### Two Examples With Incorrect Operation Errors


```
a = 'a' + 1
```


which leads to the following error:

TypeError: can only concatenate str (not "int") to str


```
a = int('a')
```


which leads to the following error:

	ValueError: invalid literal for int() with base 10: 'a'


## [Try-Except](https://www.w3schools.com/python/python_try_except.asp)

When you perform an operation in Python that is prone to errors, then you may wish to use a try-block followed by an except block. The try block will execute something that you think might lead to an error such as processing user input. If the thing you attempted fails, then the except block will handle the error without crashing the whole program. It is possible to also add a finally clause that will perform some operation regardless of if the try or except block was run successfully. Below is an example of a try-except block in Python.


```
try:
           float(amount)
       except ValueError:
           raise AbortAccountTransaction("Invalid data, please enter a decimal number 
in 1 or 1.0 type of format.")
```



## If-Except Pattern

In the if-except pattern you assert that something specific should be false in terms of a boolean comparison. An example would be expecting a value inputted by an user to be greater than zero. If the condition is false, then you move into the if-block that will throw an exception. If the code moves beyond the if block you know that everything has gone correctly. Below is an example of this simple pattern.


```
if(amount <= 0):
           raise AbortAccountTransaction("Value cannot be 0 or less")
       return amount
```



## Custom Except Class With Inheritance

A custom except class is used to define a new type of error that can be caught and found in the code based on that particular error keyword. If you for example write a program that handles financial transactions you can define an Except class that is defined as an AbortAccountTransaction error. Using this allows you to catch all of these errors higher up in the code and look for specific error types in the logs for example. Below is an example:


```
class AbortAccountTransaction(Exception):
   pass
```


What happens in the above example is that the AbortAccountTransaction [inherits](https://www.w3schools.com/python/python_inheritance.asp) the Exception class as is with nothing else added to it. In essence this is simply a standard Exception that has been given a new name for easier recognition of the error context. Then any error falling under this custom Exception class can be caught using an except block as shown below:


```
   except AbortAccountTransaction as Abort:
       print(Abort)
```



## A Practical Example


### Main.py


```
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
```



### AccountsManager.py


```
from Account import *

class AccountsManager():
   def __init__(self):
       self.accounts = {}
       self.latestAccount = 0

   def findValidAccount(self, id, password):
       try:
           int(id)
       except ValueError:
           AbortAccountTransaction("Invalid account id format, please provide an integer number")
       account = self.accounts[id]
       if(account == None):
           abortAccountTransaction("Invalid account id")
       print("GOT ACCT", account)
       if(account.isValidPassword(password)):
           return account

   def addAccount(self, name, password, balance=0):
       newAccount = Account(name, password, balance)
       self.latestAccount += 1
       self.accounts[self.latestAccount] = newAccount
       return self.latestAccount

   def viewBalance(self, accountId, password):
       a = self.findValidAccount(accountId, password)
       print("Account", a.name, "has", a.balance)

   def addBalance(self, accountId, password, balance):
       a = self.findValidAccount(accountId, password)
       print("A", a)
       a.addBalance(balance)

   def withdrawBalance(self, accountId, password, balance):
       a = self.findValidAccount(accountId, password)
       a.withdrawBalance(balance, password)

   def deleteAccount(self, accountNumber):
       del self.accounts[accountNumber]
```



### Accounts.py


```
class AbortAccountTransaction(Exception):
   pass

class Account():
   def __init__(self, name, password, balance):
       self.balance = balance
       self.name = name
       self.__password = password


   def isValidPassword(self, password):
       if(password == self.__password):
           return True
       raise AbortAccountTransaction("Invalid password")

   def isValidAmount(self, amount):
       try:
           float(amount)
       except ValueError:
           raise AbortAccountTransaction("Invalid data, please enter a decimal number in 1 or 1.0 type of format.")
       if(amount <= 0):
           raise AbortAccountTransaction("Value cannot be 0 or less")
       return amount

   def addBalance(self, amount, password):
       self.isValidAmount(amount)
       self.balance += balance
       print("New balance is:", self.balance)



   def withdrawBalance(self, amount, password):
       self.isValidAmount(amount)
       if(balance > self.balance):
           AbortAccountTransaction("Cannot withdraw more than account balance", self.balance)
       else:
           self.balance -= balance


