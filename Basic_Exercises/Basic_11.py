# Get each digit from a number in the reverse order.
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
#
# Given:
#
# number = 7536
# Output 6 3 5 7
#

given_number = 7536


def excercise_11(num_x):
    rev = ""
    while num_x > 0:
        rm = num_x % 10

        rev+= str(rm) + " "

        num_x = num_x//10

    return  rev

solution = excercise_11(given_number)

print(solution)



str_number = str(given_number)

final_str = ""

for i in str_number[::-1]:
    final_str+=i + " "

print(final_str)
