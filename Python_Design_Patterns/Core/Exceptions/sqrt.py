def sqrt(x):
    '''
    Compute square roots using the method
    of Heron of Alexandria.

    Args:
    :param x: The number for which the square root is to be computed.
    :return: The square root of x.
    '''

    guess = x
    i = 0
    while guess * guess != x and i < 20:
        guess = (guess + x / guess) / 2.0
        i += 1
    return guess


def main():
    print(sqrt(9))
    print(sqrt(2))
    try:
        print(sqrt(-1))
    except ZeroDivisionError:
        print('Cannot Compute square root of a negative number')

    print('Program compiles fine')



if __name__ == '__main__':
    main()
