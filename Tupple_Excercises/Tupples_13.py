# Removing Duplicates from Tuple
# # Write a code to create a new tuple with only unique elements.
# #
# # Given:
# #
# # my_tuple = (1, 2, 2, 3, 4, 4, 5)
# # Expected Output:
# #
# # Original tuple with duplicates: (1, 2, 2, 3, 4, 4, 5)
# # Tuple with unique elements: (1, 2, 3, 4, 5)

my_tuple = (1, 2, 2, 3, 4, 4, 5)

tuple_set = set(my_tuple)
print(f"Original tuple with duplicates: {my_tuple}")
og_tuple = tuple(tuple_set)
print(f"Tuple without duplicates {og_tuple}")
