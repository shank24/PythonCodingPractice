class Dog:

    ''' A Simple Dog '''

    def __init__(self,name):
        self._name= name

    def speak(self):
        return "woof"

class Cat:
    ''' A Simple Cat '''

    def __init__(self, name):
            self._name = name

    def speak(self):
            return "meow"


def get_pet(pet="dog"):
    '''The factory method'''

    pets = dict(dog=Dog("Hope"), cat=Cat("Neil"))

    return pets[pet]


d= get_pet("dog")
print(d.speak())
c = get_pet("cat")
print(c.speak())