lst =[10,20,30,"Shanky",23.5,22,45]
print(lst)

print(lst[3])
print(lst[3:6])
print(lst*2)
print(lst.__len__())

lst.append(40)
lst.remove('Shanky')
del(lst[1])
print(lst)

#lst.clear()
#print(lst)

print(max(lst))
print(min(lst))
lst.insert(3,99)
print(lst)

lst.sort()
print(lst)

print(sorted(lst))

#Reverse A List
print('List In Reverse Order - Descending')
lst.sort(reverse=True)
print(lst)