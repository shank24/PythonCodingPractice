try:
    num = int (input('Enter a number'))
    assert num%2==0,'Odd Number'
except AssertionError as object:
    print(object)

