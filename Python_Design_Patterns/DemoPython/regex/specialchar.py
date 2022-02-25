import re

str = 'Take  1 up 1-3-2019  One 23 idea. One idea 45 at a time Only 03-03-2020'

#Carat Symbol - At the beginning of the string
result = re.search(r'^O\w',str)
print(result)

result = re.search(r'^T\w*',str)
print(result.group())

result = re.search(r'[a-z]\w*',str)
print(result.group())
