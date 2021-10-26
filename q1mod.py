b=[]
def collatz(a):

    if a%2!=0:
        if a == 1:
            b.append(int(a))
            return None
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
#pythona