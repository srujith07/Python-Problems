#  Print all prime numbers within a range
# Note: A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11)
#
# A Prime Number is a natural number greater than 1 that cannot be made by multiplying other whole numbers.
#
# Examples:
#
# 6 is not a prime number because it can be made by 2×3 = 6
# 37 is a prime number because no other whole numbers multiply to make it.

start = int(input("Enter start value: "))

end = int(input("Enter end value: "))

for i in range(start,end+1):
    is_prime = True
    for j in range(2,i):
        if (i%j) == 0:
            is_prime = False
            break
    if is_prime:
        print(i)




