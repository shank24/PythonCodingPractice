from threading import *

def displayNumber():
    i=0
    print(current_thread().getName())
    while i<=10:
        print(i)
        i+=1


#Main thread here
print(current_thread().getName())
t=Thread(target=displayNumber)

t.start()