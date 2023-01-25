def customgen(x,y):
    while x<y:
        yield x
        x+=1

res = customgen(10,20)
for i in res:print(i)