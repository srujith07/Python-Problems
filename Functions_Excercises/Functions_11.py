
# Create a function with keyword arguments
# The exercise requires you to create a function that can accept any number of keyword arguments. A keyword argument is where you specify the name of the argument along with its value (e.g., name="Alice", age=30). Inside the function, you need to access these arguments and print them in a key-value format.
#
# Create a function print_info(**kwargs) that accepts keyword arguments and prints the key-value pairs. Call it with different keyword arguments

def print_info(**kwargs):
    result = ""
    for i,j in kwargs.items():
        result+=str(i) + " " + str(j) +'\n'

    return  result

solution = print_info(name="Alice", age=30, city = "Hyderabad")

print(solution)
