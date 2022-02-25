x=int(input("Enter min number"))
y=int(input("Enter max number"))

if x%2 == 0: x=x+1
while x<=y:
    print(x)
    x+=2
