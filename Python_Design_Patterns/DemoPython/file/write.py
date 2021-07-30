#This opens the file for writing
f = open('myfile1.txt','w')

print('Enter Text, Type #, when done')
s=''
while s!='#':
    s=input()
    f.write(s+'\n')

f.close()

