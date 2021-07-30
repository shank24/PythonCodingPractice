import time,datetime

epoch=time.time()
print(epoch)

#Getting Current Time
t=time.ctime(epoch)
print(t)

dt=datetime.datetime.today()
print('Current Date: {}/{}/{}'.format(dt.day, dt.month, dt.year) )
print('Current Time: {}:{}:{}'.format(dt.hour, dt.minute, dt.second))
