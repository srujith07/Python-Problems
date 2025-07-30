# Find all occurrences of a substring in a given string by ignoring the case
# Write a program to find all occurrences of “USA” in a given string ignoring the case.
#
# Given:
#
# str1 = "Welcome to USA. usa awesome, isn't it?"
# Expected Outcome:
#
# The USA count is: 2

str1 = "Welcome to USA. usa awesome, isn't it?"

def excercice_08(str_x):
    check_str = "usa"
    str_x = str_x.lower()
    count = str_x.count(check_str)

    return  f"The USA count is: {count}"

solution = excercice_08(str1)
print(solution)
