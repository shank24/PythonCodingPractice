a = 123
b = 234


def getId(variable):
    return id(variable)


print(getId(a))
print(getId(b))

b = a
print(getId(b) == getId(a))

