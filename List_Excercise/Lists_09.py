# Create a copy of a list
# Create a copy of a list [10, 20, 30] and modify the copy.
# Print both the original and the copied list to demonstrate they are independent.

original_list = [10, 20, 30]
print("Original list initially:", original_list)


copied_list = original_list[:]


copied_list.append(40)
copied_list[0] = 100

print("Original list after modifying copy:", original_list)
print("Copied list after modification:", copied_list)

another_copy = list(original_list)
another_copy.append(50)
print("\nOriginal list after another_copy modification:", original_list)
print("Another copied list:", another_copy)

third_copy = original_list.copy()
third_copy[0] = 999
print("\nOriginal list after third_copy modification:", original_list)
print("Third copied list:", third_copy)
