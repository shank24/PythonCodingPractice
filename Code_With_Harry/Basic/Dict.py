#Dictionary
d1 = {}
#print(type(d1))
d2 = {"Shank":"Canada",
"Rohit":"United",
"Kanika":"Australia",
"Piyush":{"2018":"Delhi",
"2019":"Noida",
"2020":"San Francisco"}}
print(d2)

print(d2["Shank"])
print(d2["Piyush"]["2018"])

#Added a value in the Dictionary.
d2["Ankit"]="Junk Food"
#print(d2)

#Removing value in Dictionary.
del d2["Ankit"]
print(d2)

#Use of copy(), will not delete,
#but it will create a shallow copy.
d4=d2.copy()

del d4["Shank"]

print(d4)
print(d2)

#With this approach, it will update in d2 also
d3 = d2
print(d3)

d3["Ankit"]="Junk Food 123"
print(d3)
print(d2)

print(d2.get("Shank"))
d2.update({"Shawn":"Crabs"})
print(d2)

print("Keys ******** \n", d2.keys())
print("Items ******* \n", d2.items())