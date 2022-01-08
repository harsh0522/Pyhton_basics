#slicing = create  a substring by extracting elements from another string
           #indexing[] or slicing()
        #    [start:stop:step]
        #slicing() ------> It will create a slice object

# name = "Bro Code"
# first_name  = name[0:3]
# first_name  = name[:3]
# last_name = name[4:]
# print(first_name)
# print(last_name)
# funky_name = name[::3]
# print(funky_name)
# reversed_name = name[::-1]
# print(reversed_name)

########SLICE FUNCTION#############
website = "http://google.com"
website2 = "http://wikipedia.com"
slice = slice(7,-4) 
print(website[slice])
print(website2[slice])