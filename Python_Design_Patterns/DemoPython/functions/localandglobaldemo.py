#Global Var
x=123

def display():
    x=166
    print(x)
    print(globals()['x'])

z = display
z()
z()
z()

