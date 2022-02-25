import time


k=0

start_time = time.time()
while k<5:
    print("Shank 123")
    k+=1
print("While Loop Ran In ", time.time() -start_time, "Seconds")

start_time1 = time.time()
for i in range(5):
    print("Shank")

print("For Loop Ran In ", time.time() -start_time1, "Seconds")

localtime = time.asctime(time.localtime(time.time()))
print(localtime)