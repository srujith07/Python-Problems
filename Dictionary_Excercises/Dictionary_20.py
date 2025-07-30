# Check if All Values are Unique
# Write a function that takes a dictionary and returns True if all values in the dictionary are unique, False otherwise.
#
# Given:
#
# dict1 = {'a': 1, 'b': 2, 'c': 3}             # All values unique
# dict2 = {'x': 10, 'y': 20, 'z': 10}          # Value 10 is duplicated
# dict3 = {} # Empty dictionary (all values are vacuously unique)
# Expected Output:
#
# Dictionary: {'a': 1, 'b': 2, 'c': 3} -> All values unique? True
# Dictionary: {'x': 10, 'y': 20, 'z': 10} -> All values unique? False
# Dictionary: {} -> All values unique? True
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'x': 10, 'y': 20, 'z': 10}

dict3 = {}

def is_unique(dict_x):
    new_dict = {i for i in dict_x.values()}
    if len(new_dict) == len(dict_x):
        return True
    else:
        return False



print(f"Dictionary: {dict1} -> All values unique? {is_unique(dict1)} ")
print(f"Dictionary: {dict2} -> All values unique? {is_unique(dict2)} ")
print(f"Dictionary: {dict3} -> All values unique? {is_unique(dict3)} ")

