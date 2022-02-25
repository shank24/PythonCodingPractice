class Calculator:
#Self keyword is mandatory for calling variable names into method.
#instance and class variables have diff purpose

    #class variables
    num=100

    #Default constructor    
    def __init__(self,a,b):
        #Instance variables
        self.a = int(input('Enter a number'))
        self.b = int(input('Enter a number'))
        print("Object is Created automatically")

    def getData(self):
        print("I am now executing getData")

    def Summation(self):
        return self.a + self.b + self.num

ob = Calculator(0,0)
#print(ob.getData())
print(ob.Summation())
print(ob.num)

ob1 = Calculator(0,0)
#print(ob1.getData())
print(ob1.Summation())
print(ob1.num)

