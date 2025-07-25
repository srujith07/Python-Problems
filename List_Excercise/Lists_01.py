# Perform Basic List Operations
# Given:
#
# my_list = [10, 20, 30, 40, 50]
# Perform following operations on given list
#
# Access Elements: Print the third element.
# List Length: Print the number of elements in the list
# Check if Empty: Write a code to check is list empty.
# Expected Output:
#
# Initial list: [10, 20, 30, 40, 50]
#
# Third item:  30
# Length of the list: 5
# list is not empty

my_list = [10, 20, 30, 40, 50]

print(f"Initial list: {my_list}")
print(f"Third item: {my_list[2]}")
print(f"Third item: {len(my_list)}")
print(f"List not empty" if my_list else f"List is empty")
