import re

s = 'Python is a good lang, every1 should learn Python, I like Python'
sub ='Python'
flag=False
pos=-1

count=0
while True:
    pos=s.find(sub,pos+1,len(s))
    if pos == -1:
        break
    print("Found the ",sub," at position ", pos)
    count+=1
    flag=True

if flag == False:
    print("Not Found")
else:
    print(sub, " Found ",count, " Times" )

