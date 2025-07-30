# Sort Dictionary by Values
# Sort a dictionary by its values and print the sorted dictionary (as an OrderedDict or by converting to a list of tuples).
#
# Given:
#
# my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
# Expected Output:
#
# Original dictionary: {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}
#
# Sorted by values (as OrderedDict):
# OrderedDict([('Jessa', 3), ('Kelly', 1), ('Jon', 2), ('Kerry', 4), ('Joy', 1)])



my_dict = {'Jessa': 3, 'Kelly': 1, 'Jon': 2, 'Kerry': 4, 'Joy': 1}

def get_value(item):
    return item[1]
new_dict = sorted(my_dict.items() , key=get_value)

print(new_dict)
