list1 = [1,2,34,5,6,"ab",23,"rr",566]

def printGreaterThanSixValues(list1):
    for items in list1:
        if type(items) == int and items >=6:
            print(items)

val = printGreaterThanSixValues(list1)

