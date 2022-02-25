from Code_Ground.geeksforgeeks.util.GetNumber import getFirstNumber

n = getFirstNumber()


def recursiveWay(n):
    if n == 0:
        return 0
    else:
        return n + recursiveWay(n - 1)


def ArithmeticWay(n):
    return n * (n + 1) / 2


print(recursiveWay(5))
print(ArithmeticWay(5))