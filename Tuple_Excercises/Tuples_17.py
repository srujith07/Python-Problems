# Sort a tuple of tuples by 2nd item
# Given:
#
# tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# Expected output:
#
# (Sorted tuple by 2nd item: (('c', 11), ('a', 23), ('d', 29), ('b', 37))


tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))

num_tup = [i[1] for i in tuple1]
num_tup.sort()
print(num_tup)
new_list =[]
for i in num_tup:
    for j in tuple1:
        if i == j[1]:
            new_list.append(j)

print(new_list)
