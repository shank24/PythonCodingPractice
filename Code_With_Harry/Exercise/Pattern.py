#Pattern Printing

one = int(input('Enter a Row'))
value = input('Type 1 or 0: ')
two = bool(value)


#Solution
if two == True:
    for i in range(1,one+1):
        for j in range(1,i+1):
            print("*")
        print()
elif two == False:
    for i in range(one,0,-1):
        for j in range(1,i+1):
            print("*")
        print()


