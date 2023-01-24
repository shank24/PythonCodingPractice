stud={'John':['Py','Dj','Drf'], 'Bob':['Java','Pi','Scala'],
      'Jay':['Js','Po']}

keys = stud.keys()

for eachKey in keys:
    print("Courses taken by", eachKey, "are :")
    for eachCourse in stud[eachKey]:
        print(eachCourse)
