class Borg:
    '''Borg  class making class attribute global '''
    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state  # Make it an attribute _dictionary


class Singleton(Borg):  # Inherits from Borg Class
    ''' This class now shares all its attributes among its various instances'''

    # This essentially makes the singleton objects an object-oriented global _variable_rx

    def __init__(self, **kwargs):
        Borg.__init__(self)
        # Update the attribute dictionary by inserting a new key-value pair.
        self._shared_state.update(kwargs)

    def __str__(self):
        # Returns the attribute dictionary for printing
        return str(self._shared_state)


#Let's create a singleton object and add our first acronym
x = Singleton(HTTP="Hyper Text Transfer Protocol")
print(x)

#Let's create another singleton object and if it refers to the same attribute dictionary by adding another acronym
y= Singleton(SNMP = "Simple Network Management Protocol")
print(y)