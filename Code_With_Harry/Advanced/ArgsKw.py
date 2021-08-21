
def function_name_print(a,b,c,d):
    print(a,b,c,d)

#function_name_print('A','B','C','D')


def funargs(normal, *args):
    print(normal)
    print(type(args))
    for item in args:
        print(item)


val = ['A','B','C','D']
normal = "Strings"

funargs(normal,*val)

