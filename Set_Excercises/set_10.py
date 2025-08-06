# Check Superset
# Check if main_set = {10, 20, 30, 40} is a superset of subset_set = {10, 20}.
#
# Given:
#
# set1 = {10, 20}
# set2 = {10, 20, 30, 40}
# Expected Output:
#
# True

set1 = {10, 20}
set2 = {10, 20, 30, 40}

print(set2.issuperset(set1))
