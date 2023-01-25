lst1=[1,2,3,4,5]
lst2=[2,2,2,2,2]

z=[]
for i in range(len(lst1)):
    z.append(lst1[i]*lst2[i])
print(z)

u=[ lst1[i]*lst2[i] for i in range(len(lst1)) ]
print(u)