
def function_name_print(a,b,c,d):
    print(a,b,c,d)

#function_name_print('A','B','C','D')


def funargs(normal, *args, **kwargs):
    print(normal)
    print(type(args))

    print("List")
    for item in args:
        print(item)

    print("Dictionary")
    for key,value in kwargs.items():
        print(key,value)


val = ['A','B','C','D']
normal = "Strings"
kw = {"Rohan":"Monitor", "Shank": "Coder"}

funargs(normal,*val,**kw)

