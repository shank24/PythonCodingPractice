class Calculator:

    #class variables
    num=100

    #Default constructor    
    def __init__(self,a,b):
        #Instance variables
        self.a = a
        self.b = b
        print("Object is Created automatically")

    def getData(self):
        print("I am now executing getData")

    def Summation(self):
        return self.a + self.b + self.num

ob = Calculator(2,3)
#print(ob.getData())
print(ob.Summation())
print(ob.num)

ob1 = Calculator(4,5)
#print(ob1.getData())
print(ob1.Summation())
print(ob1.num)

