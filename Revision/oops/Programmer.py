class Program:
    def setName(self,n):
        self.name = n

    def getName(self):
        return self.name

    def display(self):
        print(self.getName())

p1=Program()
p1.setName('OOO')
p1.display()