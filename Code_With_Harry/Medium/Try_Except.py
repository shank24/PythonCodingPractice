#Exception demonstration
num1 = raw_input()
num2 = raw_input()

try:
    print("The sum is", int(num1)+int(num2))
except Exception as e:
    print(e)
    

print("Execution resumes")

Itemscart = 0

if Itemscart!=2:
    raise Exception("Itemscart Index Out of range")