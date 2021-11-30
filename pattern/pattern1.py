# *****
# *****
# *****
# *****
# *****



def pattern1(n):
    for row in range(1,n+1):
        for col in range(0,row):
            print("*",end=' ')
        print()

pattern1(5)