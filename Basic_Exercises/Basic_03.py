
# Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.
#
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
#
# Expected Output:
#
# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t
# v

#method 1

my_str = "Pynative"

c = 0

for i in my_str:

    if c % 2 == 0:
        print(i)

    c = c+1


# method 2 

str_len = len(my_str)

for i in range(str_len):
    if i % 2 == 0:
        print(my_str[i])

str_in = "Pynative"
def excercise_3(str_in):
    str_length = len(str_in)
    result = ""
    for i in range(str_length):
        if i % 2 == 0:
            result+=str_in[i] + '\n'
    return result

solution = excercise_3(str_in)

print(solution)

