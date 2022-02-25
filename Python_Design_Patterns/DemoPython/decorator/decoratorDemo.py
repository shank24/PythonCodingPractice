def decor(fun):
    def innerfun():
        result =fun()
        return result*2
    return innerfun

def num():
    return 5

res = decor(num)
print(res())

#Second Approach
#Name should be same, as it is defined as a deckor name
@decor
def num():
    return 6

print(num())

