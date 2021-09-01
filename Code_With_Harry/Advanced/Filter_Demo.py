#Filter
list_1 = [1, 2, 3, 4, 5, 6,7,8,9]

def is_Greater(num):
    return num > 5

gr_than_5 = filter(is_Greater,list_1)

print (gr_than_5)


#Reduce

from functools import reduce

list_2 = [1, 2, 3, 4, 5]

num = reduce(lambda x,y:x*y,list_2)

print (num)
