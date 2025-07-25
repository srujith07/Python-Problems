# Combine two lists
# Combine given two lists into a single list and print it.
#
# Given:
#
# list_a = [1, 2]
# list_b = [3, 4]
# Expected Output:
#
# [1, 2, 3, 4]
list_a = [1, 2]
list_b = [3, 4]

list_a.extend(list_b)
print(list_a)
