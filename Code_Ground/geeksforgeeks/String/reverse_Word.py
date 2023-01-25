str="You are awesome"

def iteration_Way(str):
    temp = str.split()
    result=[]
    i = len(temp)-1

    while(i>=0):
        result.append(temp[i])
        i=i-1
    return ' '.join(result)

def reversed_Word(str):
    str1=str.split(' ')
    return ' '.join(reversed(str1))

print(reversed_Word(str))
print(iteration_Way(str))
