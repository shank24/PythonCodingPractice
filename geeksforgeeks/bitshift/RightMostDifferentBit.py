import math

from geeksforgeeks.bitshift.GetNumber import *

m = getFirstNumber()
n = getSecondNumber()


def posOfRightMostDiffBit(m, n):
    xor = m ^ n
    return int(math.log(((xor ^ (xor - 1)) + 1), 2))


print(posOfRightMostDiffBit(m, n))
