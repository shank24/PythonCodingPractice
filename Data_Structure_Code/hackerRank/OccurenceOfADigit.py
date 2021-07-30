#import fileinput

#inputData = ''

#for line in fileinput.input():
#    inputData += line

digit = int( input() )
n= int (input())


#Count the number of 2's digits in a single number
def codeHere(n,digit):
    # Use the function to return the solution.
    count = 0;
    while(n > 0 ):
        if(n % 10 == digit):
            count = count + 1
        n = n//10
    return count


#Count the number of 2's digits  between 0 and n
def numberOf2sinRange(n,digit):
    #Initialize Result
    count=0

    #Count 2's in every number from 2 to n
    for i in range(2 , n+1):
        count = count + codeHere(i,digit)
    return count


print(numberOf2sinRange(n,digit))
