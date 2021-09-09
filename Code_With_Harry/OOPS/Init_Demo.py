class Employee:
    leaves = 9
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

#name is instance variable, whereas aname is argument.


    

    def printDetails(self):
        return self.name, self.salary, self.role

harry = Employee("Harry", 455, "Coder")
rohan = Employee("Rohan", 466, "Ultra Coder")

print(harry.printDetails())

print(rohan.printDetails())