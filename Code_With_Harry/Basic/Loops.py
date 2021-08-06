
list1 = [["Harry",1], ["Carry",2] ,
         ["Marry",3], ["Larry",4]]

dict1 = dict(list1)
print(dict1)

#Basic list
for l,value in list1:
    print(l,value)

#With Dictionary
for l, value in dict1.items():
    print (l, value)

#Only keys
for l in dict1:
    print (l)

#Only Values
for l in dict1.values():
    print (l)

