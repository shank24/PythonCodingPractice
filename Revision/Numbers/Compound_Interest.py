
def compound_interest(p,r,t):
    val = pow( (1 + r / 100), t)
    a = p * (val)
    ci= a - p
    return ci



p = int(input('Enter Principal'))
r = float(input('Enter Rate'))
t = int(input('Enter Time'))

print("The Compound Interest Is ", compound_interest(p,r,t))
