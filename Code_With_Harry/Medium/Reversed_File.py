#Reversing the File

with open("/home/shanky/Personal/Code/VS_Code_Python/Code_With_Harry/Medium/shank.txt",'r') as reader:
    content = reader.readlines()
    with open("reversed.txt",'w') as writer:
        for line in reversed(content):
            writer.write(line)





