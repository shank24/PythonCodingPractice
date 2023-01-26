class ObjCount:
    numberOfObj = 0

    def __init__(self):
        ObjCount.numberOfObj+=1
    @staticmethod
    def display():
        print(ObjCount.numberOfObj)

o1=ObjCount()
o2=ObjCount()

ObjCount.display()

