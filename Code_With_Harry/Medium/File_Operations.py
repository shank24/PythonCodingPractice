f = open("/home/shanky/Personal/Code/VS_Code_Python/shank1.txt")
print(f.tell())
print(f.readline())
#Reset the file pointer to Beginning
f.seek(0)
print(f.readline())
f.close()