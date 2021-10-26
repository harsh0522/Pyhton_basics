# # Given a positive integer, write a program to recursively apply the following formula:
 
# # 1. If the number is odd, then multiply it by 3 & add 1.
# # 2. If the number is even, then divide it by 2.
 
# # collatz(7) -> [7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
# # collatz(26) -> [26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
 
# # Notes: The function receives an integer and must return a list of integers.


b=[]
def collatz(a):
    
    if a < 0:
        return "no is not positiv"
    elif a%2!=0:
        if a == 1:
            b.append(int(a))
            return "Harsh"
        b.append(int(a))
        return collatz(a*3+1)
    else:
        b.append(int(a))
        return collatz(a/2)
    
a = int(input('enter number '))
print(collatz(a))
print(b)

import matplotlib.pyplot as plt
plt.plot(b)
plt.show()
#harsh







