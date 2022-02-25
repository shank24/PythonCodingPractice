class Patient:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.clinical= []

    def addClinicalData(self,clinical):
        self.clinical.append(clinical)



class Clinical:
    def __init__(self,componentName,componentValue):
        self.compName=componentName
        self.compVal =componentValue

p=Patient('John',40)

c1=Clinical('BP','80/120')
c2=Clinical('heartRate','80pm')

p.addClinicalData(c1)
p.addClinicalData(c2)

print(p.name)
for eachClinical in p.clinical:
    print(eachClinical.compName)
    print(eachClinical.compVal)



