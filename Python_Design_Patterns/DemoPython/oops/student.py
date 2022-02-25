class Student:
    major="CSE"

    def __init__(self,rollno,name):
        self.roll=rollno
        self.name=name

s1=Student(1,'John')
s2=Student(2,'Pohn')

print(s1.roll, Student.major, s1.name)
print(s2.roll, Student.major, s2.name)