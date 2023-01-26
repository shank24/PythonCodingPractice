try:

    a=int(input('Enter a number'))
    b=int(input('Enter a number'))
    c=a/b
    print (c)
except ZeroDivisionError:
    print ('Division Error Handled')
    print('Please Enter Non-Zero Number')