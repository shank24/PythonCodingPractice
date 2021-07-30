#List Example
countries=["India", "Canada", "USA"]
print(countries)

#Adding at the End
countries.append("China")

#Removing Via Index
countries.__delitem__(1)
print(countries)

#Adding Country In a Middle
countries.insert(2,"Sweden")
print(countries)

#Set Example

countries1 = {'Iran','UAE','Saudi Arabia'}
print(countries1)

#Adding at the End
countries1.update(['Bhutan'])
print(countries1)

#Remove By Index
countries1.remove('Iran')
print(countries1)

#Adding Country In a Middle
countries1.add("Japan")
print(countries1)