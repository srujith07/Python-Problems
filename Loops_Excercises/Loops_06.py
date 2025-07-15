# Count the total number of digits in a number
# Write a Python program to count the total number of digits in a number using a while loop.
#
# For example, the number is 75869, so the output should be 5.


data = input("Enter your Input here: ")

num_list = []

for i in data:
    if i.isdigit():
        num_list.append(i)

print(len(num_list))
