urls = {
    'Google': 'http://google.com',
    'Pluralsight':'http://pluralsight.com'
}

print(urls['Google'])

d = dict(golden = 123, indigo = 234, seashell = 989)
e = d.copy()
print(e)
f=dict(e)

g=dict(wheat=888, khaki=545, crimson=343)
f.update(g)
print(f)

for key in f:
    print(key, "==>",  f[key])

#Only Values
for value in f.values():
    print(value)


#Only keys
for key in f.keys():
    print(key)

print('golden' in f)

print('diamond' not in f)

#Note - Keys are immutable and values are mutable.
