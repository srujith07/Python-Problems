# Create a recursive function
# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself repeatedly.
#
# Expected Output:
#
# 55
def my_func(no):
    if no == 0:
        return 1
    else:
        return no * my_func(no-1)

a = my_func(5)

print(a)

