a=[1,2,3,4,5]
b=[7,8,9,10,11]

z=[]
for i in range(len(a)):
    z.append(a[i]*b[i])

print(z)

#Other way
s=[]
s=[a[i]*b[i] for i in range(len(a))]
print(s)