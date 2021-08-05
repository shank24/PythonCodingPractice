#Arithmetic Operators

a = int(input('Enter a number'))
b = int(input('Enter a number'))
op = raw_input('Enter Operator')

def computeValue(a,b,op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b;
    elif op == '*':
        return a * b
    elif op == '**':
        return a ** b
    elif op == '//':
        return a // b
    elif op == '/':
        return a / b;
    elif op == '%':
        return a % b;    

#value = computeValue(a,b,op)
#print(value)

#Identity Operator
print(5 is not 7)

#Membership Operator
list = [1,2,3,4,5,6,7]
print(2 in list)