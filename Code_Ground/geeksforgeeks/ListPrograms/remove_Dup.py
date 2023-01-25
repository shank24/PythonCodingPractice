
l1=input('Enter a list of elements')
print(l1)
s=set(l1)
l2=[]

for each_Value in l1:
    if each_Value not in l2:
        l2.append(each_Value)

print(l2)
print(s)