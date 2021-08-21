import time


k=0

start_time = time.time()
while k<5:
    print("Shank 123")
    k+=1
print(time.time() -start_time)

start_time1 = time.time()
for i in range(5):
    print("Shank")

print(time.time() -start_time1)
