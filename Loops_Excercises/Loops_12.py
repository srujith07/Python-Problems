# Display Fibonacci series up to 10 terms
# Have you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.
#
# For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
#
# Expected output:
#
# Fibonacci sequence:
# 0  1  1  2  3  5  8  13  21  34

given_num = int(input("Enter the range of fibonacci series: "))

prev = 0

curr = 1

print(prev, curr, end=" ")

for i in range(given_num-2):
    fabi = prev+curr
    print(fabi, end=" ")
    prev = curr
    curr = fabi
