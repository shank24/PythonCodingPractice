class Employee:
    leaves = 9
    pass

harry = Employee()
rohan = Employee()

harry.name = "Shank"
harry.salary = 234
harry.role = "Coder"
rohan.name = "Rohan"
rohan.salary = 23434
rohan.role = "Ultra Coder"

print(harry.name)
print(harry.leaves)
print(Employee.__dict__)
Employee.leaves = 12
harry.leaves = 144
print(harry.leaves)

print(harry.__dict__)
print(Employee.__dict__)