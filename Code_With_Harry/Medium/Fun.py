a = 4
b = 80

#Built In Function
c = sum((a,b))
print c

#User Defined Function
def function1(a,b):
    print("You are in the function",a+b)

function1(2,3)

def function2(a,b):
    average = (a+b)/2
    print(average)
    return average

value = function2(10,20)

print (value)