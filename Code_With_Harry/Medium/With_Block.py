
with open("/home/shanky/Personal/Code/VS_Code_Python/shank1.txt") as f:
    a = f.read(4)
    print (a)

f = open("/home/shanky/Personal/Code/VS_Code_Python/shank1.txt", "rt")
print(f.readlines())
f.close()