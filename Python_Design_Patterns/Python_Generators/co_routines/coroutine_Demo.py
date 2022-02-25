

def coroutine_example():
    while True:
        x = yield
        print(x)


c = coroutine_example()
c.next()
c.send(10)
