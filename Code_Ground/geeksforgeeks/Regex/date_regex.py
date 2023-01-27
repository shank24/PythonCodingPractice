import re
str='24-12-1989 , 31-07-1993'

res = re.findall(r'\d{1,2}-\d{1,2}-\d{1,4}',str)
print(res)