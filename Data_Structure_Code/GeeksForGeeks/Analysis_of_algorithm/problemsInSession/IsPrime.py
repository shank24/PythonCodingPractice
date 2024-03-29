from Code_Ground.geeksforgeeks.util.GetNumber import getFirstNumber


n = getFirstNumber()
i = 5


def FindPrime(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for x in range(i, i * i <= n, i + 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False

    return True


# Time Complexity - (Big-O(Sqrt(n)))

print(FindPrime(n))
