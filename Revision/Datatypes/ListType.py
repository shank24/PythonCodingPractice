lst=[1,2,3,4,5,0,-1]
print(lst)
print(lst[1])
print(lst[0:3])
print(lst*3)

lst.sort()
print(lst)
lst.append(34)
print(lst)
print("Deletion")
del(lst[1])

print(lst)

print(max(lst))
print(min(lst))
lst.sort(reverse=True)
print(lst)