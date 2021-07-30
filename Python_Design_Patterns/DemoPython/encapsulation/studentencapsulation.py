class Student:

    def setId(self,studid):
        self.studid=studid

    def getId(self):
        return self.studid

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name


s=Student()
s.setId(12)
s.setName('John')
print(s.getId(),s.getName())

