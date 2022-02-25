
class OverTheLimitException(Exception):
    def __init__(self,msg):
        self.msg=msg


def withdraw(amount):
    if(amount>500):
        raise OverTheLimitException('You cannot withdraw more than 500$ PDay')


withdraw(600)

