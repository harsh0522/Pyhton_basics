
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2) 

#def main():
    # print("enter the fib number: ",end=" ")
    # n = int(input())    
    # for i in range(0,n+1):
    #     print(fib(i),end=" ")

# if __name__ == "main()":
#      main()


n = int(input("enter the fib number: "))    
for i in range(0,n+1):
    print(fib(i),end=" ")
