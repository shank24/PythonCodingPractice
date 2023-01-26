import pickle,Student

f=open("student.dat","wb")
s=Student.Student('John',123)
pickle.dump(s,f)
f.close()