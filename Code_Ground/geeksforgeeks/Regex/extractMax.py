import re

def extractMax(input):

    numbers = re.findall('\d+',input)

    numbers = map(int,numbers)
    print(max(numbers))

input = '100klh564abc365bg'
extractMax(input)