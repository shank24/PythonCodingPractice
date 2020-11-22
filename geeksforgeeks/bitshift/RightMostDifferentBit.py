import math
m = int(input('Enter the number'))
n = int(input('Enter the number'))

def posOfRightMostDiffBit(m,n):
    xor=m^n
    return int(math.log(((xor ^ (xor-1))+1),2));

print(posOfRightMostDiffBit(m,n))
