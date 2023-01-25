#Iterative way

def iter_way(s):
    temp=s.split()
    res=''
    i=len(s)-1
    while i>=0:
        res=res+s[i]
        i=i-1
    return ''.join(res)

#Slicing
def slicing_str(s):
    return str[::-1]

#For Loop
def rev_str(s):
    str1=''
    for i in s:
        str1=i+str1
    return str1

def reverse_join(str):
    return ''.join(reversed(str))

str=raw_input('Enter a string')
print(slicing_str(str))
print(rev_str(str))
print(reverse_join(str))
print(iter_way(str))