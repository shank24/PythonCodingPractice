class Car:
    def __init__(self,make,year):
        self.make=make
        self.year=year


    class Engine:
        def __init__(self,number):
            self.number=number
        def start(self):
            print('Engine Started')



c1=Car('BMW',2018)
e=c1.Engine(123)
e.start()



