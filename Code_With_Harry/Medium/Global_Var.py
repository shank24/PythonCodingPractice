#Global Scope
l=10

def function(n):
    #Local Scope
    #l=6
    global l
    l = l+50
    m=9
    print(m,l)
    print(n,"Via Function")

function("Calling function")


#Global always look out for out of function declarations.
x=123
def fun1():
    x=20
    def fun2():
        global x
        x=90
    print("Before calling fun2()",x)
    fun2()
    print("After calling fun2()",x)
        
fun1()
#Now global variable created the variable outside
print(x)