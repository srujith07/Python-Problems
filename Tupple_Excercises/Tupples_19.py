# Check if all items in the tuple are the same
# tuple1 = (45, 45, 45, 45)
# Expected output:
#
# True

tuple1 = (45, 45, 45, 45)

value = all(i == tuple1[0] for i in tuple1)
print(value)
