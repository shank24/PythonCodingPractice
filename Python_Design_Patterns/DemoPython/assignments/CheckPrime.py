
x=int(input('Enter a Number'))

primeFlag=True;

for i in range(2,x-1):
    if x%i==0:
        primeFlag=False

if(primeFlag):
    print(x, "Is Prime")
else:
    print(x, "Is Not Prime")



