# ***********************************
# if __name__ == '__main__'
# ***********************************
#  Python interpreter sets "special variables", one of which is __name__
#  Python will assign the __name__ variable a value of '__main__' if it's
#  the initial module being run

# import module2

# print(__name__)
# print(module2.__name__)

def hello():
    print("hello1")

if __name__ == '__main__':
    hello()
else:
    print("running other module indirectly")