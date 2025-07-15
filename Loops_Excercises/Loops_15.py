# Print elements from a given list present at odd index positions
# Given:
#
# my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# Note: The list index always starts at 0
#
# Expected output:
#
# 20 40 60 80 100

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

list_len = len(my_list)

for i in range(list_len):
    if i % 2 != 0:
        print(my_list[i], end = " ")
print()
for i in my_list[1::2]:
    print(i, end = " ")
