#Set Does not allow duplicate
#Set Does not gurrantee any order

s={10,20,30,'xxxcccvvv'}
print(s)

s.update([88,99])
print(s)

s.remove(10)
print(s)

#Converting set into a Frozen Set
f=frozenset(s)
print(f)