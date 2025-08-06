# Find Common Elements in Two Lists
# list1 = [10, 20, 30, 40] and list2 = [30, 40, 50, 60], find the common elements using sets.
#
# Given:
#
# list1 = [10, 20, 30, 40]
# list2 = [30, 40, 50, 60]
# Expected Output:
#
# {40, 30}

list1 = [10, 20, 30, 40]
list2 = [30, 40, 50, 60]

list1 = set(list1)
list2 = set(list2)
print(list1.intersection(list2))
