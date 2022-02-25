from datetime import date
import time

#Performance Time
start_time = time.perf_counter()

lst=[]

d1=date(2016,8,12)
d2=date(2017,8,12)
d3=date(2015,8,12)

lst.append(d1)
lst.append(d2)
lst.append(d3)

lst.sort()

#time.sleep(3)
for x in lst:
    print(x)


end_time = time.perf_counter()

print('Execution Time', end_time-start_time)