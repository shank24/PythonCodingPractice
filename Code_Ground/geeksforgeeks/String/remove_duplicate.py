str='abcabcabc'

temp=[]
for s in str:
    if s not in temp:
        temp.append(s)

print(''.join(temp))