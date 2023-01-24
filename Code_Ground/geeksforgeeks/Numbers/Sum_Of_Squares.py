def get_Sum_Squares(num):

    val=0
    while num!=0:
        val = val + pow(num,2)
        num = num-1
    return val

print(get_Sum_Squares(4))