#Exercise 1A: Create a string made of the first, middle and last character
# Write a program to create a new string made of an input string’s first, middle, and last character.
#
# Given:
#
# str1 = "James"
# Expected Output:
#
# Jms

def excercise_01A(str_x):
    m_idx = len(str_x)//2

    return f"{str_x[0]}{str_x[m_idx]}{str_x[-1]}"

solution = excercise_01A("James")
print(solution)

def excercise_01B(str_x):

    m_idx = len(str_x) // 2

    return f"{str_x[m_idx-1]}{str_x[m_idx]}{str_x[m_idx+1]}"

solution = excercise_01B("JaSonAy")

print(solution)
