class Student:
    def __init__(self):
        self.__id=123
        self.__name='John'

    def display(self):
        print(self.__id, self.__name)

s=Student()

s.display()


#With Object._Classname__PrivateMemberName
#Name_Mangling
print(s._Student__id)

