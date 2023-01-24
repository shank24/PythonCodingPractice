dict1={1:"John", 2:"Ravi", 3:"Bill"}
print(dict1)
k=dict1.keys()
print(k)

for i in k:
    print(i)
print(dict1.values())
print(dict1.items())

del dict1[1]
print(dict1)

