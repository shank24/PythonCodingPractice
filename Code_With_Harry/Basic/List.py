#List Demo
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


