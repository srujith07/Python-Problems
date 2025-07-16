# Remove empty strings from a list of strings
# Given:
#
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# Expected Output:
#
# Original list of sting
# ['Emma', 'Jon', '', 'Kelly', None, 'Eric', '']
#
# After removing empty strings
# ['Emma', 'Jon', 'Kelly', 'Eric']

def excercise_14(list_x):
    new_list = []
    for i in list_x:
        if i:
            new_list.append(i)

    return new_list

list_x = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
solution = excercise_14(list_x)

print(solution)
