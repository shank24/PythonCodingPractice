# Function to find factorial of a given number
def factorial(n):
    res = 1
    for i in range(2,n+1):
        res = res*i
    return res

#Driver Code
x=int(input('Enter the number'))
print("Factorial of", x, "is", factorial(x))



