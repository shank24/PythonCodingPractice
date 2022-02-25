#Rule - Always use a comma after the first value in a tuple,
# else it will not be considered as tuple.

tpl=(40 ,50 ,40 ,"XYZ")
print(tpl[3])
print(tpl*3)
print(tpl.count(40))
print(tpl.index('XYZ'))

#Converting list to tuple

lst = [10,20,30,40]
print(type(lst))

tpl1 = tuple(lst)
print(type(tpl1))