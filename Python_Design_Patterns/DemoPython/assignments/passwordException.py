
try:
    pwd=input('Enter the password')
    if(len(pwd)<8):
        raise ValueError
except ValueError:
    print('The Password length does not meet the standard')



