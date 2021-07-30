class House(object): #The class being visited
    def accept(self,visitor):
        '''Interface to accept a visitor'''
        #Triggers the visiting operation!
        visitor.visit(self)

    def work_on_hvac(self, hvac_spec):
            print(self, "worked on by", hvac_spec) #Note that we may have a reference to the HVAC Specialist object in the house object

    def work_on_electricity(self, electrician):
        print(self, "worked on by", electrician) #Note that we may have a reference to the electrician object in the house object!

    def __str__(self):
            '''Simply return the class name when the House object is printed'''
            return self.__class__.__name__

class Visitor(object):
    '''Abstract visitor'''
    def __str__(self):
        '''Simply return the class name when the Visitor object is printed'''
        return self.__class__.__name__

class HvacSpecialist(Visitor): #Inherits from the parent class, Visitor
    '''Concrete visitor : HVAC Specialist'''
    def visit(self, house):
        house.work_on_hvac(self) #Note that the visitor now has a reference to the house object

class Electrician(Visitor): #Inherits from the parent class, Visitor
    '''Concrete visitor : Electrician'''
    def visit(self, house):
        house.work_on_electricity(self)  # Note that the visitor now has a reference to the house object

#Create on HVAC Special
hv = HvacSpecialist()

#Create an electrician
elec = Electrician()

#Create a House
home = House()

#Let's the accept the HVAC Specialist and work on the house by invoking the visit().
home.accept(hv)

#Let's the accept the Electrician and work on the house by invoking the visit().
home.accept(elec)