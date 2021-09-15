class Employee:
    #Class Variable
    leaves = 9
    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

#name is instance variable, whereas aname is argument.
    def printDetails(self):
        return self.name, self.salary, self.role

    @classmethod
    def set_Leaves(cls,newleaves):
        cls.leaves = newleaves
    
    @classmethod
    def from_dash(cls,string):
        # params = string.split("-")
        # return cls(params[0],params[1],params[2])
        return cls(*string.split("-"))

    @staticmethod
    def printgood(str):
        return "This is good - " + str



harry = Employee("Harry", 455, "Coder")
rohan = Employee("Rohan", 466, "Ultra Coder")
cherry = Employee.from_dash("Cherry-345-Student")


Employee.set_Leaves(33)

print(harry.leaves)
print(harry.printDetails())
print(rohan.printDetails())
print(cherry.printDetails())

print(harry.printgood("Jerry")) 