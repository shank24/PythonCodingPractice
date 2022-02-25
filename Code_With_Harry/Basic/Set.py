s= set()
print(type(s))

list = [1,2,3,4,5]
s_From_List = set(list)
print(s_From_List)

#Adding an elements
s.add(1)
s.add(2)
s.add(3)
s1 = s.union((1,2,3,4))
print(s)
print(s1)
s2 = s.intersection(s1)
print(s2)
