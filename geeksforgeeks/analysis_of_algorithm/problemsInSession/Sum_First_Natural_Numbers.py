from geeksforgeeks.util.GetNumber import getFirstNumber

n = getFirstNumber()


def fun1(n):
    if n == 0 or n < 0:
        return 0
    return int(n * (n + 1) / 2)


def fun2(n):
    if n == 0 or n < 0:
        return 0
    sum = 0
    for i in range(1, n + 1):
        sum += i
    return sum


def fun3(n):
    if n == 0 or n < 0:
        return 0
    sum = 0
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            sum += 1
    return sum


print(fun1(5))
print(fun2(5))
print(fun3(5))
