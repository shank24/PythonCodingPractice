lst = [20,30,40,255]
print(type(lst))
b=bytes(lst)
print(type(b))

#Values can be assign to bytearray, through the index, not on bytes.
#No slicing and repetition is allowed on both.

b1 = bytearray(lst)
print(type(b1))
b1[1]=23
