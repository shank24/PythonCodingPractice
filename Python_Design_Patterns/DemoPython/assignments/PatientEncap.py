class Patient:

    def setId(self,pId):
        self.pId=pId

    def getId(self):
        return self.pId

    def setName(self,name):
        self.name=name

    def getName(self):
        return self.name


    def setSSN(self,ssn):
        self.ssn=ssn
    def getSSN(self):
        return self.ssn

p=Patient()

p.setId(123)
p.setName('Sheldon')
p.setSSN(123456)

print(p.getId(),'\n', p.getName(),'\n', p.getSSN())
