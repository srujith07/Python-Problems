# Exercise 2: Perform dictionary operations
# Given:
#
# my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
# Perform following operations on given dictionary
#
# Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
# Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
# Check if Key Exists in the dictionary
# Expected Output:
#
# Original dictionary: {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
#
# Updated dictionary after removing 'profession': {'name': 'Alice', 'age': 35, 'city': 'New York'}
#
# Printing all key-value pairs:
# name: Alice
# age: 35
# city: New York
#
# Does 'age' exist? True

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

print(f"Original dictionary: {my_dict}")

# Remove the 'model' key-value pair using del
del my_dict['profession']
print(f"Updated dictionary after removing 'profession': {my_dict}")

print("Printing all key-value pairs:")
for key, value in my_dict.items():
  print(f"{key}: {value}")



key1 = 'age'
print(f"Does '{key1}' exists ? : {key1 in my_dict.keys()}")
