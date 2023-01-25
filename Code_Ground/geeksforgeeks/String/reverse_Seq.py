str="Python Is Good"

def reverse_Seq(str):
    temp=str.split(' ')
    res=[]
    i=0
    while i < len(temp):
        res.append(temp[i][::-1])
        i=i+1
    return ' '.join(res)



print(reverse_Seq(str))