import os,sys

if os.path.isfile("1myfile.txt"):
    f=open("myfile.txt",'r')
    s=f.read()
    print(s)
    f.close()
else:
    print('File Is Not present')
    sys.exit()

