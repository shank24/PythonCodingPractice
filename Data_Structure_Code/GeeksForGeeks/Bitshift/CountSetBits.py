from Code_Ground.geeksforgeeks.util.GetNumber import *

n = getFirstNumber()


def countSetBits(n):
    total = 0
    while n >= 1:
        total += returnCount(n)
        n = n - 1
    return total


def returnCount(n):
    count = 0
    if n == 1:
        return 1
    while n>=1:
        if n % 2 != 0:
            count = count + 1
        n /= 2
    return count


print(countSetBits(n))
