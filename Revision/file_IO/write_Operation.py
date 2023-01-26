
#open the file
f = open("myfile.txt","w")
s=''
print ('Enter until #')
while s != '#':
    s = input()
    f.write(s+'\n')

f.close()