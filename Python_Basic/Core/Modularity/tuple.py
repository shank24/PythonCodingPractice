t = ["Norway", 4.953, 1]

print(t)
print(len(t))

a = ((220, 234), (122, 123))
print(a[1][1])

# Tuples should be comma separated
h = (391)
print(type(h))


def minmax(items):
    return min(items), max(items)

#Tuple unpacking
lower, upper = minmax([12, 13, 14, 151, 121, 989])
print(lower)
print(upper)

(a,(b,(c,d))) = (4,(3,(2,1)))
print(a,b,c,d)

a='jelly'
b='bean'

a,b = b,a
print(a,b`)