str1='13.3.4'
str2='13.3.5'

x1 = [x for x in str1.split('.')]
x2 = [y for y in str2.split('.')]

Flag=False
for i in range(len(x1)):
    if x1[i] >= x2[i]:
        Flag=True
    else:
        Flag=False


if(Flag):
    print('X1 is greater')
else:
    print('X2 is greater')