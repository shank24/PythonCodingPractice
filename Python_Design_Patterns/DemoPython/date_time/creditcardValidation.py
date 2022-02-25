from datetime import *

def validateCard(expdate):
    if expdate>datetime.now().date():
        return 'Valid'
    else:
        return 'Expired'

print(validateCard(date(2018,2,2)))