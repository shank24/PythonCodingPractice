# function solution

def even_integer_function(n):
    result = []
    for i in range(n):
        if i % 2 == 0:
            result.append(i)
    return result


val = even_integer_function(5)
print(val)


# generator Solution

def even_integer_generator(n):
    for i in range(n):
        if i % 2 == 0:
            yield i


print(list(even_integer_generator(5)))

