lst=[1,2,3,4,5]

sum = reduce(lambda x, y: x + y, lst)
prod = reduce(lambda x, y: x * y, lst)

print(sum)
print(prod)