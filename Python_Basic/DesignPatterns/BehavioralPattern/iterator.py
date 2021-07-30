def count_to(count):
    '''Our Iterator implementation'''

    #Our list
    number_in_german = ["eins","iwei","drei","vier","funf"]

    #Our built-in iterator
    #Create a tuple such as (1, "eins")
    iterator = zip(range(count),number_in_german)

    #Iterate through our iterable list
    #Extract the German NumPy
    #Put them in a generator called number

    for position, number in iterator:

        #Returns a 'generator' containing numbers in German
        yield number

#Let's test the generator returned by our iterator
for num in count_to(5):
    print("{}".format(num))

