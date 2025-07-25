# List Comprehension for Numbers
# Use list comprehension to create a new list containing only the numbers from a given list.
#
# Given:
#
# my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
# Expected Output:
#
# [1, 2, 3, 4, 5, 6]

my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]

new_list = [i  for i in my_list if isinstance(i, int) ]
print(new_list)
