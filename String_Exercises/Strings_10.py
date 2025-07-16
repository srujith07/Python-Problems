# Write a program to count occurrences of all characters within a string
# Given:
#
# str1 = "Apple"
# Expected Outcome:
#
# {'A': 1, 'p': 2, 'l': 1, 'e': 1}

def excercise_10(str_x):
    count_dict = {}
    for i in str_x:
        count_dict[i] = str_x.count(i)

    return count_dict
str1 = "Apple"
solution = excercise_10(str1)
print(solution)
