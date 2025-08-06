# Remove Items From Set Simultaneously
# Write a Python program to remove items 10, 20, 30 from the following set at once.
#
# Given:
#
# set1 = {10, 20, 30, 40, 50}
# Expected output:
#
# {40, 50}

item_rem = 10,20,30

set1 = {10, 20, 30, 40, 50}
for i in item_rem:
    set1.discard(i)

print(set1)
