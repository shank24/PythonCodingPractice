dict1 = {
    1:"John",
    2:"Raisen",
    3:"Bob"
}

print(dict1)
print(dict1.values())
print(dict1.items())


#Keys
key = dict1.keys()

for i in key:
    print(i)

#Values
v = dict1.values()
for i in v:
    print(i)

#Specific Key Value
print(dict1[3])

#Delete
del dict1[1]
print(dict1)