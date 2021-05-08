import types


class Strategy:
    '''The Strategy Pattern Class'''

    def __init__(self, function=None):
        self.name = "Default Strategy"

        # If a reference to a function is provided, replace the execute() method with the given function
        if function:
            self.execute = types.MethodType(function, self)

    def execute(self):  # This gets replaced by another version, if another strategy is provided.
        print("{} is used".format(self.name))


# Replacement method

def strategy_one(self):
    print("{} is used to execute method 1 ".format(self.name))


def strategy_two(self):
    print("{} is used to execute method 2 ".format(self.name))

#Let's create our default strategy
s0 = Strategy()

#Let's execute our default strategy
s0.execute()

#Let's create the first version of our default strategy
s1 = Strategy(strategy_one)

#Let's set its name
s1.name = "Strategy One"
s1.execute()

s2 = Strategy(strategy_two)
s2.name = "Strategy Two"
s2.execute()
