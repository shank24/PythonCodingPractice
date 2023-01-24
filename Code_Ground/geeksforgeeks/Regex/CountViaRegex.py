import re

string = "ThisIsGeeksforGeeks!, 123"

#Creating seperate lists of using the re.findall()

uppercase_char= re.findall("[A-Z]",string)
lowercase_char= re.findall("[a-z]",string)
numerical_char= re.findall("[0-9]",string)
special_char= re.findall("[, .!?]",string)

print('Upper', len(uppercase_char))
print('Lower', len(lowercase_char))
print('Numeric', len(numerical_char))
print('Special', len(special_char))
