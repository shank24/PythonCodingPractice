

def isPrime(n):
    flag = True
    for i in range(2,n-1):
        if n%i == 0:
            flag = False

    if (flag):
        print(n, 'Is a Prime')
    else:
        print(n, 'Is not a Prime')


x=int(input('Enter a number'))
isPrime(x)
