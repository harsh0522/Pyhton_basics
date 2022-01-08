##  Question 1  ##
# Capital indexes
# Write a function named capital_indexes. The function takes a single parameter, 
# which is a string. Your function should return a list of all the indexes in the 
# string that have capital letters.
# For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].
# capital_indexes("Pranjal Pathak") -> [0, 8] captial_indexes("BrIjEsH K r") -> [0, 2, 4, 6, 8]
# a = []
# def capital_indexes(str):
#     for i,letter in enumerate(str):
#         if letter.isupper():
#             a.append(i)
#     return(a)

# CI = capital_indexes("HaRsh")
# print(CI)

# a = []
# def capita_indexes(str):
#     b=list(str.strip(" "))
#     print(b)
#     for i in range(0,len(b)):
#         if b[i] == b[i].islower():
#             print(b[i])

# ci = capita_indexes("HarsH")
# print(ci)

##Question 2
# Counting syllables
# Define a function named count that takes a single parameter. The parameter is a string.
# The string will contain a single word divided into syllables by hyphens, such as these:
# "ho-tel" "cat" "met-a-phor" "ter-min-a-tor"
# Your function should count the number of syllables and return it.
# For example, the call count("ho-tel") should return 2.

# def count(str):
#     a = str.split("-")
#     return len(a)

# b = count("cat")
# print(b)

##Question3
# Palindrome
# A string is a palindrome when it is the same when read backwards.
# For example, the string "bob" is a palindrome. So is "abba". 
# But the string "abcd" is not a palindrome, because "abcd" != "dcba".
# Write a function named palindrome that takes a single string as its parameter.
# Your function should return True if the string is a palindrome, and False otherwise.
# def pallindrome(str):
#     print(str[::-1])
#     if str == str[::-1]:
#         return True
#     else:
#         return False

# a = pallindrome("harsh")
# print(a)


##Question4
# Counting parameters
# Define a function param_count that takes a variable number of parameters. 
# The function should return the number of arguments it was called with.
# For example, param_count() should return 0, while param_count(2, 3, 4) should return 3.

# def param_count(*args):
#     return len(args)

# a = param_count()
# print(a) 

##Question5
# Type check Write a function named only_ints that takes two parameters. 
# Your function should return True if both parameters are integers, and False otherwise. 
# For example, calling only_ints(1, 2) should return True, 
# while calling only_ints("a", 1) should return False.
# def only_ints(a,b):
#     if type(a) == int and type(b) == int :
#         return True
#     else:
#         return False

# c = only_ints(1,"b")
# print(c)

##Question6
# Write a function named mid that takes a string as its parameter. 
# Your function should extract and return the middle letter. 
# If there is no middle letter, your function should return the empty string.
#For example, mid("abc") should return "b" and mid("aaaa") should return "".
# import math
# def mid(str):
#     if len(str)%2 != 0:
#         a = math.floor(len(str)/2)
#         #print(a)
#         return str[a]
#     else:
#         return " "

# b = mid("harsh")
# print(b)


##Question7
# Write a function named add_dots that takes a string and adds "." in between each letter. 
# For example, calling add_dots("test") should return the string "t.e.s.t".
# Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. 
# For example, calling remove_dots("t.e.s.t") should return "test".
# If both functions are correct, calling remove_dots(add_dots(string)) 
# should return back the original string for any string.

##Question8
# (You may assume that the input to add_dots does not itself contain any dots.)
# add_dots("Pankaj") -> "P.a.n.k.a.j" remove_dots("P.a.n.k.a.j") -> "Pankaj"
# remove_dots("P.E.K.K.A") -> "PEKKA" add_dots("PEKKA") -> "P.E.K.K.A"
# str1 = ""
# def add_dots(str):
#     a= list(str.strip("."))
#     b = len(a)-1
#     for i in range(1,len(a)+b):
#         if i%2 != 0:
#             a.insert(i,".")
    
#     return str1.join(a)
# a = add_dots("harmon")
# print(a)
# str2 = ""
# def remove_dots(str):
#     b = str.split(".")
#     return str2.join(b)
# b = remove_dots("h.a.r.m.o.n")
# print(b)

# aa = remove_dots(add_dots("ramramji"))
# print(aa)


##Question9
# Up and down
# Define a function named up_down that takes a single number as its parameter. 
# Your function return a tuple containing two numbers; the first should be one lower than the parameter, 
# and the second should be one higher.
# For example, calling up_down(5) should return (4, 6).
# def calling_up_down(n):
#     c = []
#     a = n-1
#     b = n+1
#     c.append(a)
#     c.append(b)
#     return tuple(c)

# a = calling_up_down(5)
# print(a)

# b=[]
# def calling_up_down(*n):
#     for i in n:
#         b.append(i)
#     return tuple(b)
# bb = calling_up_down(1,2,3,4,5,6)
# print(bb)

##Question10
# Define a function named convert that takes a list of numbers as its only parameter and 
# returns a list of each number converted to a string.
# For example, the call convert([1, 2, 3]) should return ["1", "2", "3"].
# lst1 = []
# def convert(lst):
#     for i in lst:
#         lst1.append(str(i))
#     return lst1
        
# qq = convert([1,2,3,4,"c"])
# print(qq)














































