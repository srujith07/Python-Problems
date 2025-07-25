# Remove Duplicates from list
# Write a function that takes a list with duplicate elements and returns a new list with only unique elements.
#
# Given: list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]
#
# Expected Output:
#
# [1, 2, 3, 4, 5]

list_with_duplicates = [1, 2, 2, 3, 1, 4, 5, 4]

set_list = set(list_with_duplicates)

res = list(set_list)

print(res)
