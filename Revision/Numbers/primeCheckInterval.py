

def isPrime(start, end):
    prime_list= []
    for i in range(start, end):
        if i == 0 or i == 1:
            continue
        else:
            for j in range(2, int(i/2)+1):
                if i % j == 0:
                    break
            else:
                prime_list.append(i)
    return prime_list

start=int(input('Enter a starting range'))
end=int(input('Enter an ending range'))
lst = isPrime(start, end)

if(len(lst) == 0):
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)
