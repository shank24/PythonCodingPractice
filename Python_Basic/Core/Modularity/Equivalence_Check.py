a = [[1 , 2], [3 , 4] ]
b = a[:]
print(a is b)
print(a == b)
a[0]=[9 , 8]

print(a[0], b[0])
a[1].append(5)
print(a[1], b[1])

c=[21, 45]
d = c * 5
print(d)

s = [[-1 , +1]] * 5
print(s)
s[2].append(8)
print(s)
