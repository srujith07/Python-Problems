# Check if the first and last numbers of a list are the same
# Write a code to return True if the list’s first and last numbers are the same. If the numbers are different, return False.
#
# Given:
#
# numbers_x = [10, 20, 30, 40, 10]
# # output True
#
# numbers_y = [75, 65, 35, 75, 30]
# # Output False

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


if numbers_x[0] == numbers_x[::-1][0]:
    print("Result is True")
else:
    print("Result is False")

if numbers_y[0] == numbers_y[::-1][0]:
    print("Result is True")
else:
    print("Result is False")

def excercise_5(list_x):

    if list_x[0] == list_x[-1]:
        return True
    else:
        return False

solution = excercise_5(numbers_x)
print(solution)
solution = excercise_5(numbers_y)
print(solution)
