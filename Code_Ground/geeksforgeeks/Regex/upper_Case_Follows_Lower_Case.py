import re

def match(text):

    pattern = re.compile('[A-Z]+[a-z]+$')
    if (re.search(pattern, text)):
        return 'Yes'
    else:
        return 'No'

# Driver Function
print(match("Geeks"))
print(match("geeksforGeeks"))
print(match("geeks"))