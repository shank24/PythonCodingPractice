class BMW:

    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        print('Starting the car')

    def stop(self):
        print('Stopping the car')



class ThreeSeries(BMW):

    def __init__(self,cruise,make,model,year):
        #super().__init__(make,model,year)
        BMW.__init__(self, make, model, year)
        self.cruise =cruise

    def start(self):
        #super().start()
        print('Button Start')

    def display(self):
        print(self.cruise)
        print(self.make)
        print(self.model)
        print(self.year)


class FiveSeries(BMW):

    def __init__(self, parking, make, model, year):
        BMW.__init__(self,make, model, year)
        self.parking = parking

    def display(self):
        print(self.parking)
        print(self.make)
        print(self.model)
        print(self.year)


thr=ThreeSeries(True,'BMW','324i','2018')
thr.display()
thr.start()
thr.stop()

fvr=FiveSeries(True,'BMW','325i','2018')
fvr.display()