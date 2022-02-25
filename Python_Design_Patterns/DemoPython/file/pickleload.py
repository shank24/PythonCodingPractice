import pickle
f=open('student.dat','rb')
#Deserialized Object
obj=pickle.load(f)
obj.display()
f.close()