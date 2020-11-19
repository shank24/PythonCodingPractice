n=int(input().strip())

if n%2==0:
    if n in range(2,6):
        print('Not Weird')
elif(n>=6 and n<=20)):
    print('Not Weird')
elif((n%2==0) and (n>20)):
    print('Not Weird')
elif((n%2!=0)):
    print('Weird')

def dictionary():
    check = {True: "Not Weird", False: "Weird"}
    print(check[
              n % 2 == 0 and (
                      n in range(2, 6) or
                      n > 20)
              ])

dictionary()

def simpleway():
    if n % 2 == 0 and (n in range(2, 6) or n > 20):
        print
        "Not",
    print
    "Weird"


simpleway()