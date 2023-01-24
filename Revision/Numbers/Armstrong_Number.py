def armstrong_number(number):
    actual=number

    val=0
    while number!=0:
        r=number%10;
        val = val+pow(r,3)
        number/=10
    if val == actual:
        print('Yes')
    else:
        print('No')

num=int(input('Enter a number'))
armstrong_number(num)