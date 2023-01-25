x=123

def display():
    x=345
    print(globals()['x'])
    print(x)

print(x)
display()