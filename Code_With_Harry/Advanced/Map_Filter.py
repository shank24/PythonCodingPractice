numbers  = ["1", "2", "3", "4", "5", "6", "7"]

for item in range(len(numbers)):
    numbers[item] =int(numbers[item])

numbers[0] = numbers[0] + 2
print(numbers[0])

#Map Demo
number = list(map(int, numbers))

print(number)

