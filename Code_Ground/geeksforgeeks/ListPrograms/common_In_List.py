lst1=[1,2,3,4,5]
lst2=[1,2,3,2,2]

z=[]
for i in range(len(lst1)):
    if lst1[i]==lst2[i]:
        z.append(lst1[i])

print(z)

u=[]
for i in lst1:
    if i in lst2:
        u.append(i)

print(u)

#list comprehension

res=[i for i in lst1 if i in lst2]
print(res)