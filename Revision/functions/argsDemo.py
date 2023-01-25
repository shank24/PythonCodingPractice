def myfun(x, *args, **kwargs):
    print(x)
    for each_arg in args:
        print(each_arg)
    for k,v in kwargs.items():
        print(k,v)

myfun(1,2,3,4,'d',name="Tola",sal=130)