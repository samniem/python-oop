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
