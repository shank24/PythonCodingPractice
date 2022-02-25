import re

str = 'Take  1 up 1-3-2019  One 23 idea. One idea 45 at a time Only 03-03-2020'

#Find all subtring starts with o, followed by 3 chars

#\w - any alpha numeric char
result = re.search(r'o\w',str)
#print(result.group())

list=re.findall(r'o\w\w',str)
print(list,list.__len__())

#Matches from the beginning
result = re.match(r'T\w\w\w',str)
print(result.group())

result = re.sub(r'One','Two',str)
print(result)

#Quantifiers

#Here{1,2} returns minimum 1 char or 2 chars followed by O
result = re.findall(r'O\w{1,2}',str)
print(result)

#one or more
result = re.findall(r'O\w*',str)
print(result)

#Zero or One
result = re.findall(r'O\w?',str)
print(result)

#- + is for one or more and /d is for digits
result = re.split(r'\d+',str)
print(result)


#date extraction
result = re.findall(r'\d{1,2}-\d{1,2}-\d{4}' , str)
print(result)

