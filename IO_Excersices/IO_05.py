# Accept a list of 5 float numbers as an input from the user
# Refer:
#
# Take list as a input in Python.
# Python list
# Expected Output:
#
# [78.6, 78.6, 85.3, 1.2, 3.5]





def excercise_05(n):
    list_numbers = []
    for i in range(1,n+1):
        a = float(input(f"Enter value number {i}: "))
        list_numbers.append(a)

    return list_numbers

solution = excercise_05(5)

print(solution)
