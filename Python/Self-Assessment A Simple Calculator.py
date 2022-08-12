# Name: Ho Yeung Chan (Sunny)    Date: 12 Aug 2022
class SimpleCalculator:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def addition(self):
        print("Sum is", self.a+self.b)
    def subtraction(self):
        print("Difference is", self.a-self.b)
    def multiplication(self):
        print("Product is", self.a*self.b)
    def division(self):
        print("Quotient is", self.a/self.b)
        
a = float(input("Enter a float/int number: "))
b = float(input("Enter another number: "))
operation = input("Enter an operation (addition, subtraction, multiplication, division) or type Quit/Exit to quit: ").lower()

cal = SimpleCalculator(a,b)
while operation != "quit" and operation != "exit":
    if operation == "addition":
        cal.addition()
    elif operation == "subtraction":
        cal.subtraction()
    elif operation == "multiplication":
        cal.multiplication()
    else:
        cal.division()
    a = float(input("Enter a float/int number: "))
    b = float(input("Enter another number: "))
    operation = input("Enter an operation (addition, subtraction, multiplication, division) or type Quit/Exit to quit: ").lower()
