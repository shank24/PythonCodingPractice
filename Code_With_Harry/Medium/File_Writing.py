f = open("shank1.txt","a")
a = f.write("Learning Python\n")
print(a)

#Handle Read & Write Both
f = open("/home/shanky/Personal/Code/VS_Code_Python/shank1.txt","r+")
print(f.read())
f.write("Thanks!!")
f.close()

