#F Strings

#Ist Way
f_name="Shanky"
l_name="Kalra"
#a = "This is %s %s"%(f_name,l_name)

#Second Way To
a = "This is {} {}"
b = a.format(f_name ,l_name)
print(b)


#F Strings
c = f"This is {f_name} {l_name}"
print(c)