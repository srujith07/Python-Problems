# Create a new string made of the first, middle, and last characters of each input string
# Given two strings, s1 and s2, write a program to return a new string made of s1 and s2’s first, middle, and last characters.
#
# Given:
#
# s1 = "America"
# s2 = "Japan"
# Expected Output:
#
# AJrpan

def excercise_03(str_x,str_y):
    x_mdx = len(str_x)//2
    y_mdx = len(str_y)//2

    fs = str_x[0]+str_y[0]
    mids = str_x[x_mdx]+str_y[y_mdx]
    ls = str_x[-1]+str_y[-1]

    return f"{fs}{mids}{ls}"
s1 = "America"
s2 = "Japan"
solution = excercise_03(s1,s2)

print(solution)

