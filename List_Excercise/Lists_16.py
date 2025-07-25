# Flatten Nested List
# Write a function to flatten a list of lists into a single, non-nested list. (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4]).
#
# Given:
#
# list_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
# Expected Output:
#
# [1, 2, 3, 4, 5, 6, 7]
List_of_lists = [[1, 2], [3, 4], [5, 6, 7]]
def flatten_list(list_x):

    return [ii for i in list_x for ii in i]

print(f"Flattened List: {flatten_list(List_of_lists)}")
