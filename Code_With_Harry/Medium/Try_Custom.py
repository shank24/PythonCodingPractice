
try:
    with open('filelog.txt','r') as reader:
        reader.read()

except:
    print("Caught an excecption")



try:
    with open('filelog.txt','r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally:
    print('Cleaning up the resources')
