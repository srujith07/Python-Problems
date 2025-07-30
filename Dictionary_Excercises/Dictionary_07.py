# Access Nested Dictionary
# Given a nested dictionary {'person': {'name': 'Alice', 'age': 30}}, print Alice’s age.
#
# Given:
#
# data = {'person': {'name': 'Alice', 'age': 30}}
# Expected Output:
#
# Alice's age is: 30

nested_person_dict = {'person': {'name': 'Alice', 'age': 30}}
print(f"Nested dictionary: {nested_person_dict}")


alices_age = nested_person_dict['person']['age']

print(f"Alice's age is: {alices_age}")
