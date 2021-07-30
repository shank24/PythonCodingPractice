student = {
    "John": ['Python','Django','DRF'],
    "Bob" : ['Java','JPA','Spring'],
    "Jim" : ['JS','Node','React']
}

Keys = student.keys()

for eachKey in Keys:
    print("Courses taken by", eachKey, " are : ")
    for eachCourse in student[eachKey]:
        print(eachCourse)


print(student["John"])