# Append new string in the middle of a given string
# Given two strings, s1 and s2. Write a program to create a new string s3 by appending s2 in the middle of s1.
#
# Given:
#
# s1 = "Ault"
# s2 = "Kelly"
# Expected Output:
#
# AuKellylt

s1 = "Ault"
s2 = "Kelly"

def excercise_02(str_x,str_y):
    m_idx = len(str_x)//2

    return f"{str_x[:m_idx]}{str_y}{str_x[m_idx:]}"

solution = excercise_02(s1,s2)

print(solution)
