from typing import Pattern


# pattern2

# *
# **
# ***
# ****
# *****

def pattern2(n):
    for row in range(0,n+1):
        for col in range(0,row):
            print("*",end='')
        print()

pattern2(5)
