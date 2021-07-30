w = "the quick brown fox jumped over the lazy dog".split()
print(w)
i = w.index('fox')
print(i)
print(w.count('the'))

print(2 in [2,3,4,5,6])
print(2 not in [2,3,4,5,6])


u = "jackdaws love my big sphinx of quartz".split()
print(u)
del u[2]
print(u)
u.remove('jackdaws')
print(u)

a = "I accidentally the whole universe".split()
print(a)
a.insert(2, "destroyed" )
print(a)

m = [2,1,3]
n=  [7,8,9]
k= m+n
print(k)
k.extend([45,54])
print(k)

g = [12,4,5]
g.reverse()
print(g)
g.sort()
print(g)
#DESCEND Sort
g.sort(reverse=True)
print(g)





