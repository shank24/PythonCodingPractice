math=int(input('Enter Marks in Math'))
phy=int(input('Enter Marks in Physics'))
chem=int(input('Enter Marks in Chemistry'))

average = (math+phy+chem)/3

if (math<35 or phy <35 or chem<35):
    print("Student is Failed in Exam")
elif average<=59:
    print("Grade Is C")
elif average<=69:
    print("Grade Is B")
else:
    print("Grade is A")


