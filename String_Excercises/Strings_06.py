# Create a mixed String using the following rules
# Given two strings, s1 and s2. Write a program to create a new string s3 made of the first char of s1, then the last char of s2, Next, the second char of s1 and second last char of s2, and so on. Any leftover chars go at the end of the result.
#
# Given:
#
# s1 = "Abc"
# s2 = "Xyz"
# Expected Output:
#
# AzbycX

s1 = "Abc"
s2 = "Xyz"

def excercise_06(s1,s2):
    result = ""
    length = len(s1) if len(s1) < len(s2) else len(s2)

    for i in range(length):
        result += s1[i] +s2[(length-1)-i]

    return result

solution = excercise_06(s1,s2)

print(solution)
