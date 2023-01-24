def get_Sum_Squares(num):

    val=0
    for i in range(1,num+1):
        val = val + pow(i,3)
    return val

print(get_Sum_Squares(5))