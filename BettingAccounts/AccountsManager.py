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
