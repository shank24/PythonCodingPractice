#Calling function and deleting function.

# def func1():
#     print("Func1")

# func2=func1
# del func1
# func2()

#Returning function via function.
 
# def funret(num):
#     if num==0:
#         return print
#     if num==1:
#         return sum 
    
# a = funret(1)
# print(a)

#Calling function inside function.

# def executor(func):
#     func("This")
# executor(print)


#Decorators

def decorator(func1):
    def nowexec():
        print("Executing Now")
        func1()
        print("Func1 executed")
    return nowexec

@decorator
def whoisalex():
    print("Alex is a good boy")

#whoisalex = decorator(whoisalex)

whoisalex()