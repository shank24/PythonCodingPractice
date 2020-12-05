import math

from geeksforgeeks.bitshift.GetNumber import getFirstNumber

n = getFirstNumber()


def getSetFirstBitFrmRight(n):
    if n == 0:
        return 0;
    else:
        return int(math.log(((n ^ (n - 1)) + 1), 2))


print(getSetFirstBitFrmRight(n))
