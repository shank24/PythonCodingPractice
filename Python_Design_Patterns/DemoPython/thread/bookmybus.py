from threading import *

class BookMyBus:

    def __init__(self,availSeats):
        self.availSeats=availSeats
        #self.lock=Lock()
        self.lock=Semaphore()

    def buy(self,seatsReq):
        self.lock.acquire()
        print('Total Seats Available',self.availSeats)
        if(self.availSeats>=seatsReq):
            print(current_thread().getName())
            print('Confirming a Seat')
            print('Processing the payment')
            print('Printing the Ticket')
            self.availSeats-=seatsReq
        else:
            print('No seats available')
        self.lock.release()

obj=BookMyBus(10)

t1=Thread(target=obj.buy,args=(3,))
t2=Thread(target=obj.buy,args=(4,))
t3=Thread(target=obj.buy,args=(3,))

t1.start()
t2.start()
t3.start()