
def simple_interest(p,r,t):
    return (p*r*t)/100


p=int(input('Enter Principal'))
r=int(input('Enter Rate'))
t=int(input('Enter Time'))

print("Simple Interest for is ", simple_interest(p,r,t))