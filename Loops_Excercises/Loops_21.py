

# Flatten a nested list using loops
# Write a program to flatten a nested list using loops.
#
# Given:
#
# nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]
#
# # write function 'flatten_list' to flatten a nested list
# flattened = flatten_list(nested_list)
# print("Flattened list:", flattened)


nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

n_list = []

for i in nested_list:

    if isinstance(i , list):
        for j in i:
            n_list.append(j)
    
    elif not isinstance(i , list):
        n_list.append(i)


print(n_list)
