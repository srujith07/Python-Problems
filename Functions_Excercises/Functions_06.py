# Create a recursive function
# Write a program to create a recursive function that calculates the sum of numbers from 0 to 10.
#
# A recursive function is a function that calls itself repeatedly.
#
# Expected Output:
#
# 55

def excercise_06(number_x):
    if number_x == 1:
        return 1

    return number_x + excercise_06(number_x-1)

solution = excercise_06(10)

print(solution)
