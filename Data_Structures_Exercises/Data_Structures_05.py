# Paired Elements from Two Lists as a Set
# Write a code to create a Python set such that it shows the element from both lists in a pair.
#
# Given:
#
# first_list = [2, 3, 4, 5, 6, 7, 8]
# second_list = [4, 9, 16, 25, 36, 49, 64]
# Expected Output:
#
# Result is  {(6, 36), (8, 64), (4, 16), (5, 25), (3, 9), (7, 49), (2, 4)}

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

sq_set = set()

for i in first_list:

    if (i**2) in second_list:

        sq_set.add((i,i**2))

print("Result is ",sq_set)
