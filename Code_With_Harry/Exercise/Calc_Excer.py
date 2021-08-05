a = int(input('Enter First Number'))
b = int(input('Enter Second Number'))
op = raw_input('Enter the operator')

def operation(a,b):
    if op == '+':
        return a + b
    elif op == '-':
        if a>b:
            return a - b
        else:
            return b - a
    elif op =='*':
        return a * b
    else:
        return a/b
    
print(operation(a,b))


