import re

#Specific char by number of len
str='Take up one idea, one idea, One'
result = re.search(r'o\w\w',str)
print(result.group())

#Digits
str1="Hi 123456 Hi"
res=re.search(r'\d{6}',str1)
print(res.group())


#Findall
res1=re.findall(r'\o\w\w',str)
print(res1)

#With IgnoreCase
pattern = re.compile(r'one', flags=re.I)
res1=re.search(pattern,str)
print(res1.group())

#Match
resm=re.match(r'T\w\w',str)
print(resm)

