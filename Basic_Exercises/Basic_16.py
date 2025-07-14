# Check Palindrome Number
# A palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.
#
# Write a code to check if given number is palindrome.
#
#
# n = 4664

def excercise_16(number_x):
    temp = number_x
    rev = 0
    while number_x > 0:
        rm = number_x % 10

        rev = (rev*10) + rm

        number_x = number_x // 10

    if rev == temp:
        return "Given number is Palindrome"
    else:
        return "Given number is Not a Palindrome"

solution = excercise_16(n)

print(solution)

# Method 1

# n = str(n)
#
# if n == n[::-1]:
#     print("Given number is palindrome")
# else:
#     print("Given number is not a palindrome")

# Method 2
on = n
ns = ""
while n > 0 :
    ns += str(n%10)
    n = n //10
if ns == str(on):
    print("Given number is palindrome")
else:
    print("Given number is not a palindrome")
