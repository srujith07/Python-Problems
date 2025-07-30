#Split a string on hyphens
# Write a program to split a given string on hyphens and display each substring.
#
# Given:
#
# str1 = Emma-is-a-data-scientist
# Expected Output:
#
# Displaying each substring
#
# Emma
# is
# a
# data
# scientist

def excercise_13(str_x):
    result = ""
    str_x = str_x.split("-")

    for i in str_x:
        result+=i +'\n'
    return result
str1 = "Emma-is-a-data-scientist"
sollution = excercise_13(str1)
print(sollution)
