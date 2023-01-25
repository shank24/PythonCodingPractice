word=raw_input('Enter a word')
vowels = {'a','i','e','o','u'}
result = {}

for c in word:
    if c in vowels:
        result[c] = result.get(c, 0) + 1
for k,v in result.items():
    print('{}={} times'.format(k,v))
    #print(k,"is present :" , v , " Times")