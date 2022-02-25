l1 = ["Carrot","Potato","Tomato", "Cucumber"]

i=1
for item in l1:
    if i%2 is not 0:
        print(item)
    i=i+1

#Enumerate Demo 

for index, item in enumerate(l1):
    if index%2==0:
        print(item)


