from threading import *
from time import sleep

class MyThread(Thread):

    def display(self):
        i=0
        print(current_thread().getName())
        sleep(1)
        while i<=10:
            print(i)
            i+=1

obj=MyThread()
t1=Thread(target=obj.display)
t1.start()

t2=Thread(target=obj.display)
t2.start()

t3=Thread(target=obj.display)
t3.start()
