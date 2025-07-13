# Check Palindrome Number
# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
#
# Expected Output:
#
# original number 121
# Yes. given number is palindrome number
#
# original number 125
# No. given number is not palindrome number


def excercise_9(number_x):
    temp = number_x
    rev = 0
    while number_x > 0:
        rm = number_x % 10

        rev = (rev*10) + rm

        number_x = number_x // 10

    if rev == temp:
        return True
    else:
        return False

solution = excercise_9(121)

print(solution)




# given_num = int(input("Enter the number to check: "))
#
# given_num = str(given_num)
#
# print("original number",given_num)
#
# if given_num == given_num[::-1]:
#     print("Yes. given number is palindrome number")
#
# else:
#     print("No. given number is not palindrome number")
