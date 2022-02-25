#list is like array_list

values = [1,2,3,4,5,"range"]

for i in values:
    print (i)

print (values[-1])
print(values[2:4])

#insert at the specific index
values.insert(3,"Google")
#at the end.
values.append(99)
print (values)
