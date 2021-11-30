# 3.  *****
#     ****
#     ***
#     **
#     *

def pattern3(n):
    for row in range(1,n+1):
        for col in range(6,row):
            print('*',end='')
        print()

pattern3(5)