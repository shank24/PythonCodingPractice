from abc import abstractmethod,ABC

#If all the class have abstract method, then we call that class as
#Interfaces

class BMW(ABC):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def drive(self):
        pass

class ThreeSeries(BMW):

    def __init__(self, cruiseControlEnabled, make, model, year):
        BMW.__init__(self, make, model, year)
        self.cruiseControlEnabled = cruiseControlEnabled

    def display(self):
        print(self.cruiseControlEnabled)

    def start(self):
        super().start()
        print("Button Start")

    def stop(self):
        super().stop()
        print("Button Stop")

    def drive(self):
        print('In Three Series')


class FiveSeries(BMW):

    def __init__(self, parkingAssistEnabled, make, model, year):
        super().__init__(make, model, year)
        self.parkingAssistEnabled = parkingAssistEnabled

    def display(self):
        print(self.parkingAssistEnabled)

    def start(self):
        super().start()
        print("Remote Start")

    def stop(self):
        super().stop()
        print("Remote Stop")

    def drive(self):
        print('In Five Series')


threeSeries = ThreeSeries(True, 'BMW', '328i', '2018')
print(threeSeries.cruiseControlEnabled)
print(threeSeries.make)
print(threeSeries.model)
print(threeSeries.year)

threeSeries.start()
threeSeries.stop()
threeSeries.display()

fiveSeries = FiveSeries(True, 'Audi', '440i', '2020')
print(fiveSeries.parkingAssistEnabled)
print(fiveSeries.make)
print(fiveSeries.model)
print(fiveSeries.year)

fiveSeries.start()
fiveSeries.stop()
fiveSeries.display()