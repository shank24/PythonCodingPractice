from threading import *
from time import *

class Producer:
    def __init__(self):
        self.prodList = []
        self.ordersplaced = False

    def produce(self):
        for i in range(1,5):
            self.prodList.append("Product"+str(i))
            sleep(1)
            print('Item Added')
        self.ordersplaced = True

class Consumer:
    def __init__(self,prod):
        self.prod=prod

    def consume(self):
        while self.prod.ordersplaced == False:
            sleep(0.2)

        print('Orders Shipped',  self.prod.prodList)


p=Producer()
c=Consumer(p)

t1=Thread(target=p.produce)
t2=Thread(target=c.consume)

t1.start()
t2.start()

