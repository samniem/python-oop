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
    
