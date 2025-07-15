# Find the factorial of a given number
# Write a Python program to use for loop to find the factorial of a given number.
#
# The factorial (symbol: !) means multiplying all numbers from the chosen number down to 1.
#
# For example, a factorial of 5! is 5 × 4 × 3 × 2 × 1 = 120
#
# Expected output:
#
# 120

n = int(input("Enter number top find its factorial : "))
fact = 1
while n > 0 :
    fact = fact * n
    n = n-1

print(fact)

