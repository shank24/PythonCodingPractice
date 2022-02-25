x=20
y=30
z=35

print(x==20 and y==30)
print(not (y==30 and z==32))

#BMI



def bmi(height,weight):
    height=height*0.4536
    return (weight/(height*height))

print(bmi(110,12))