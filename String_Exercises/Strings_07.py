# String characters balance Test
# Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter.
#
# Given:
#
# Case 1:
#
# s1 = "Yn"
# s2 = "PYnative"
# Expected Output:
#
# True
# Case 2:
#
# s1 = "Ynf"
# s2 = "PYnative"
# Expected Output:
#
# False

def excercise_07(s1,s2):
    result = True

    for i in s1:
        if i in s2:
            continue
        else:
            result = False
    return result

s1 = "Yn"
s2 = "PYnative"
solution = excercise_07(s1,s2)
print((solution))
s1 = "Ynf"
s2 = "PYnative"

solution = excercise_07(s1,s2)
print((solution))
