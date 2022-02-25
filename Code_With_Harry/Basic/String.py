
str = "Shank is a good boy"
print(str)

#String slicing, excludes last character 
#prints 0 till 3 (Index)
print(str[0:4])

#prints whole string
print(str[0:78])

#prints string with the gap of 2, till 5 index
print(str[0:5:2])

#prints the whole string with the gap of 2
print(str[0::2])

#prints the whole string
print(str[::])

#prints the char from 0 till 4 index.
print(str[:5])

#prints the whole string.
print(str[0:])

#prints the whole string, with the gap of 1. [0:19:1] [Like this]
print(str[::])

print(len(str))


#Negative Indices

#Printing from backwards
print(str[-4:])
print(str[-4:-2])

#String Reverse 
print(str[::-1])

#String Reverse with 1 Char Gap 
print(str[::-2])

#String Reverse with 2 Char Gap 
print(str[::-3])


