# Removal all characters from a string except integers
# Given:
#
# str1 = 'I am 25 years and 10 months old'
# Expected Output:
#
# 2510

def excercise_16(str_x):
    result = ""

    for i in str_x:
        if i.isdigit():
            result+=i
    return int(result)
str1 = 'I am 25 years and 10 months old'
solution = excercise_16(str1)

print(solution)
