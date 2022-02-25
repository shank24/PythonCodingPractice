from  datetime import *

d=date(2030,7,9)
print(d)

t=time(12,45)
print(t)

dt=datetime.combine(d,t)
print(dt)