import re

def check(str, pattern):

    if re.search(pattern, str):
        print ("Valid")
    else:
        print("Invalid")

# driver Code
pattern = re.compile('^[12349]+$')
check('2134',pattern)
check('4213',pattern)
check('231',pattern)
check('9231',pattern)
