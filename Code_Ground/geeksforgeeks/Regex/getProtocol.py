import re

URL='https://www.geeksforgeeks.org/courses'

#protocol
obj1=re.findall(r'(\w+)://',URL)
print(obj1)

#hostname
obj2=re.findall(r'://www.([\w\-\.]+)',URL)
print(obj2)

url='www:localhost:4040/abc_file'
obj3=re.findall(r'www:([\w\.\-]+)(:(\d+))?', url)
print(obj3)
