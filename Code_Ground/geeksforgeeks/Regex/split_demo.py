import re

str='Take 1 up 2 one 3 idea, 4 one 5 idea, 6 One'
res=re.split(r'\d+',str)
print(res)

res = re.findall(r'one',str,flags=re.I)
print(res)
print(len(res))
replace = re.sub(r'\o\w\w','two',str, flags=re.I)
print(replace)