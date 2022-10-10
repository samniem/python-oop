

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
    
