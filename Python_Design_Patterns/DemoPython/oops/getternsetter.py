class Programmer:

    def setName(self,n):
        self.name=n

    def getName(self):
        return self.name

    def setSalary(self,sal):
        self.salary=sal

    def getSalary(self):
        return self.salary

    def setTechnologies(self,techs):
        self.technologies=techs

    def getTechnologies(self):
        return self.technologies

p1=Programmer()

p1.setName('John')
p1.setSalary(10000)
p1.setTechnologies(['Java','Python'])

print(p1.getName(),'\n',p1.getSalary(),'\n',p1.getTechnologies())