import pickle,student


f=open('student.dat','wb')
s=student.Student(123,'John',90)

#Serialized the file
pickle.dump(s,f)
f.close()