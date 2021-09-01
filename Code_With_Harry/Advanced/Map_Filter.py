numbers  = ["1", "2", "3", "4", "5", "6", "7"]

for item in range(len(numbers)):
    numbers[item] =int(numbers[item])

numbers[0] = numbers[0] + 2
print(numbers[0])

#Map Demo
number = list(map(int, numbers))

print(number)

# def squ(a):
#     return a*a
    
# num = [1,2,3,4,5,6,7,8,9,10]
# square = list(map(squ, num))

# print(square)


# #lambda Function
# num = [1,2,3,4,5,6,7,8,9,10]
# square = list(map(lambda x: x*x, num))

# print(square)


#

def square(a):
    return a*a

def cube(a):
    return a*a*a


func = [square,cube]
num = [1,2,3,4,5,6,7,8,9,10]

for i in range(5):
    val = list(map(lambda x: x(i), func))
    print (val)