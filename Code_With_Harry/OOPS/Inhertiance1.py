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



class Programmer(Employee):

    def __init__(self,aname,asalary,arole,alanguages):
        self.name = aname
        self.salary = asalary
        self.role = arole
        #super().__init__()
        self.language =alanguages


    def printProg(self):
        return self.name, self.salary, self.role, self.language

rohan = Programmer("Rohan", 466, "Ultra Coder","Java")
cherry = Employee.from_dash("Cherry-345-Student")
rohan = Programmer("Rohan", 555, "Ultra Coder",["Python","CPP"])



print(rohan.printProg())
print(rohan.printDetails())