import re

regex = r'\b[A-Za-z0-9./%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def checkEmail(email):

    if(re.fullmatch(regex,email)):
        print('Valid')
    else:
        print('In Valid')

email='shankkalra@gmail.com'
checkEmail(email)