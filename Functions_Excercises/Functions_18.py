# Create Higher-Order Function
# Write a function apply_operation(func, x, y) that takes a function func and two numbers x and y as arguments, and returns the result of calling func(x, y). Demonstrate its use with different functions (e.g., addition, subtraction).
#
# The exercise requires you to create a higher-order function, which is a function that can take other functions as arguments.

def apply_operation(func,x,y):

    return func(x,y)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

solution = apply_operation(add,5,10)

print(solution)
