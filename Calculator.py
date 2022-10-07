class Calculator():
    def __init__(self):
        self.current = 0
    
    def __enterValue(self):
        x = input("Enter value:")
        return int(x)

    def __operator(self):
        o = input("Enter operator (+ or -): ")
        return o

    def currentValue(self):
        print("Current value:", self.current)

    def calculate(self):
        o = self.__operator()
        y = self.__enterValue()
        print("o", o, type(o))
        if(o == '+'):
            self.current += y
        elif(o == '-'):
            self.current -= y
        else:
            print("Incorrect operator, not performing calculation")
        self.currentValue()

    def advancedCalculate(self,x,o,y):
        if(o == '+'):
            self.current = x+y
        elif(o == '-'):
            self.current = x-y
        self.currentValue()
        

calculator = Calculator()
calculator.calculate()
calculator.advancedCalculate(2,'+',2)