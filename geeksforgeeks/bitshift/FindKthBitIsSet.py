from geeksforgeeks.bitshift.GetNumber import *

m = getFirstNumber()
n = getSecondNumber()


# Using Right Shift
def findKthBitIsSetUsingRightShift(m,n):
    return ((m >> n) & 1) == 1


# Using Left Shift
def findKthBitIsSetUsingLeftShift(m,n):
    return (m & (1 << n)) != 0


print(findKthBitIsSetUsingRightShift(m, n))
print(findKthBitIsSetUsingLeftShift(m, n))

