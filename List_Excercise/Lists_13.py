# Remove all occurrences of a specific item from a list
# Given a Python list, write a program to remove all occurrences of item 20.
#
# Given:
#
# list1 = [5, 20, 15, 20, 25, 50, 20]
# Expected output: [5, 15, 25, 50]

list1 = [5, 20, 15, 20, 25, 50, 20]

def remove_value(list_x, val_x):
    res = []
    for i in list_x:
        if i != val_x:
            res.append(i)

    return res

print(remove_value(list1,20))
