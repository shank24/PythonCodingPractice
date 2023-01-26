class Student:
    major='CSE'

    def __init__(self,rollno,name):
        self.rollno = rollno
        self.name = name

s1=Student(11,'KKL')
print(Student.major,s1.name,s1.rollno)