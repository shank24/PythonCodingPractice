#list of mixed format numbers
numbers = [7,22,4,5,99.7,'3','5']

#convert numbers to integers using expression
print(list((int(n) for n in numbers)))

name_list = ['Adam','Cherry']

uppercase = (name.upper() for name in name_list)
print(list(uppercase))

#breaking it up
uppercased = (name.upper() for name in name_list)
rev_uppercase = (name[::-1] for name in uppercased)
print(list(rev_uppercase))