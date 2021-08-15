def fun1(str):
    print("This is " + str)

fun1("Mike Ross") 

def factorial(n):
    if(n==0 | n==1):
        return 1
    else:
        print(factorial(n)*factorial(n-1))

#factorial(5)


def fact(n):
    val=1
    for i in range(n):
        val = val*(i+1)
    return val

print(fact(5))
