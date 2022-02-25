from datetime import *


class Event:

    def __init__(self, startTime, endTime):
        self.startime = startTime
        self.endtime = endTime
        self.venue = []

    def addVenue(self,venue):
        self.venue.append(venue)

class Venue:
    def __init__(self, name):
        self.name = name
        self.address = []


    def addAddress(self,address):
        self.address.append(address)


class Address:
    def __init__(self, street, city, state, country):
        self.street = street
        self.city = city
        self.state = state
        self.country = country

e= Event(time(9,30), time(11,30))
a= Address('North Side Street', 'Toronto', 'Ontario', 'Canada')
v= Venue('State Avenue Park')

e.addVenue(v)
v.addAddress(a)

for eachVenue in e.venue:
    print(eachVenue.name)
    for eachAddress in v.address:
        print(eachAddress.street)
        print(eachAddress.city)
        print(eachAddress.state)
        print(eachAddress.country)


