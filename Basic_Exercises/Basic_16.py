
n = int(input("Enter number to check if its palindrome: "))

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
