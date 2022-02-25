from threading import *

class EvenNumbers:
    def evencount(self):
        for i in range(2,101):
            print(i)
            i+=2

class OddNumbers:
    def oddcount(self):
        for i in range(1,100):
            print(i)
            i+=2


ev = EvenNumbers()
od = OddNumbers()

t1 = Thread(target=ev.evencount)
t2 = Thread(target=od.oddcount)

print(current_thread().getName())
for i in range(1,101):
    print(i)
    i+=1



t1.start()
t2.start()

