class Employee:
    leaves = 9

    def printDetails(self):
        return self.name, self.salary, self.role

harry = Employee()
rohan = Employee()

harry.name = "Shank"
harry.salary = 234
harry.role = "Coder"

rohan.name = "Rohan"
rohan.salary = 23434
rohan.role = "Ultra Coder"

print(harry.printDetails())

print(rohan.printDetails())