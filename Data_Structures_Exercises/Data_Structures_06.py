#  Set Intersection and Removal
# Write a code to find the intersection (common) of two sets and remove those elements from the first set.
#
# See: Python Set
#
# Given:
#
# first_set = {23, 42, 65, 57, 78, 83, 29}
# second_set = {57, 83, 29, 67, 73, 43, 48}
# Expected Output:
#
# Intersection is  {57, 83, 29}
# First Set after removing common element  {65, 42, 78, 23}
#

first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
inter = first_set.intersection(second_set)
print("Intersection is ",inter)

for i in inter:
    first_set.remove(i)

print("First Set after removing common element ",first_set)


