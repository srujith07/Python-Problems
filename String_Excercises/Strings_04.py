# Arrange string characters such that lowercase letters should come first
# Given string contains a combination of the lower and upper case letters. Write a program to arrange the characters of a string so that all lowercase letters should come first.
#
# Given:
#
# str1 = PyNaTive
# Expected Output:
#
# yaivePNT

def excercise_04(str_x):
    lower = ""
    upper = ""
    for i in str_x:
        if (i >= "a") and (i <= "z"):
            lower +=i
        else:
            upper+=i

    return lower + upper

str1 = "PyNaTive"
solution = excercise_04(str1)
print(solution)
