import re

str='Take up one idea, one idea, One, Time'

res=re.findall('T..e',str)
print(res)

res=re.search('T..e',str)
print(res)
print(res.group())