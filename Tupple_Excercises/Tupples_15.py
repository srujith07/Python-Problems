# Map Tuples
# Given a tuple of numbers, create a new tuple where each number is squared.
#
# Given:
#
# t = (1, 2, 3, 4)
# Expected Output:
#
# Original tuple: (1, 2, 3, 4)
# Squared tuple:  (1, 4, 9, 16)


t = (1, 2, 3, 4)

print(f"Original tuple: {t}")
new_tup = tuple(map (lambda x: x**2 ,t))
print(f"Squared tuple: {new_tup}")
