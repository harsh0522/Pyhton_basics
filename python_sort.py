# sort() method = used with lists
# sorted(iterables) function = used with iterables

# students = ["squidward","Sandy", "patrik", "Spongebob","Mr.Krabs"]
# students.sort()
# for i in students:
#     print(i)

# students.sort(reverse=True)
#here tuples cannot used sort() method instead we use sorted() function
# students = ("squidward","Sandy", "patrik", "Spongebob","Mr.Krabs")
# sorted_student = sorted(students)

# for i in sorted_student:
#     print(i)
###################################################################


#list of tuples
# students = [("Squidward", "F", 60),
#             ("Sandy", "A", 33),
#             ("Patrick","D", 36),
#             ("Spongebob","B", 20),
#             ("Mr.Krabs","C", 78)]

#now if we want to sort by second argument that is grade we will do like this
# grade = lambda grades:grades[1]
# ages = lambda ages:ages[2]
# students.sort(key=ages)
# for i in students:
#     print(i)

##########################################
# now if we have tuples of tuples 


students = (("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick","D", 36),
            ("Spongebob","B", 20),
            ("Mr.Krabs","C", 78))


# sorted_students = sorted(students)
# for i in sorted_students:
#     print(i)


#sorting tuples of tuples by second column
grade = lambda grade:grade[1]
students_sorted = sorted(students,key=grade)
for i in students_sorted:
    print(i)



