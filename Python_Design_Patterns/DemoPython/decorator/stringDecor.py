def decorfun(fun):
    def inner(name):
        result = fun(name)
        result += ", How are you"
        return result
    return inner

@decorfun
def hello(name):
    return "Hello "+name

print(hello("John"))
