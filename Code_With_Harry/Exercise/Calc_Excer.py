class Cal:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def sum(self):
        return self.a + self.b
    def sub(self):
        return self.a - self.b
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a/self.b
    
#print(operation(a,b))

ob = Cal(4,5)
print(ob.sub())
print(ob.sum())
print(ob.mul())
print(ob.div())
