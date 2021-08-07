
f = open("/home/shanky/Personal/Code/VS_Code_Python/Code_With_Harry/Medium/shank.txt")
print(f.readlines())

print(f.readline())
print(f.readline())
print(f.readline())

content = f.read()

print(content)

#Read Line-By-Line
for line in f:
    print(line)

f.close()

