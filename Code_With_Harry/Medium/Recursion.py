def fun1(str):
    print("This is " + str)

fun1("Mike Ross") 

"""Recursive - Way"""
def factorial(n):
    if(n==1 or n==0):
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))

"""Iterative - Way"""
def fact(n):
    val=1
    for i in range(n):
        val = val*(i+1)
    return val

print(fact(7))

#Fibbonacci Series
def fibbonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibbonacci(n-1) + fibbonacci(n-2)
    
print(fibbonacci(7))

