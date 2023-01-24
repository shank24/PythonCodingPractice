#Datatypes Demo
grocery = ["Harpic", "Deo", "Perfume"]

print(grocery)
print(type(grocery))

#Looping in the loop
for i in grocery:
    print("Items ", i)

#Playing with numbers 
numbers = [1,5,8,2,3,9,10]
#If we run the method like reverse and sort, 
# it changes the original list
numbers.sort()
numbers.reverse()
print(numbers)
print(numbers[1:5])

#Extended Slice
print(numbers[::2])

print(numbers[::-1])

#Function
print(len(numbers))
print(min(numbers))
print(max(numbers))

numbers.append(99)
print(numbers)

numbers.insert(1,55)
print(numbers)

numbers.remove(5)
print(numbers)

numbers.pop()
print(numbers)

#Datatypes is Mutable - can change
numbers [1] = 67
print(numbers)

#Tuple is Immutable - cannot change
tp = (1,3,5,6,7,8,9,10,11,12,13,14,15)
print(tp)

#tp[1] = 45
#print(tp) - Cannot Change.

#Swapping 
a=10
b=12
a,b = b,a

print(a,b)
