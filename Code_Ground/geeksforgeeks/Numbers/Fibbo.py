def fibbonaci(n):

    if n<=0:
        print('Incorrect Input')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibbonaci(n-1) + fibbonaci(n-2)

print(fibbonaci(10))