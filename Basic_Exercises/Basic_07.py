# Find the number of occurrences of a substring in a string
# Write a Python code to find how often the substring “Emma” appears in the given string.
#
# Given:
#

str_x = "Emma is good developer. Emma is a writer"

# As i am in Learning proccess i have decided toi make this big by not solving this in 2 lines

def string_to_list(str_x):
    wrd = ""
    wrd_list = []
    for i in str_x:
        if i not in [" ", "."]:
            wrd+=i
        if i == " ":
            wrd_list.append(wrd)
            wrd=""
    if wrd:
        wrd_list.append(wrd)

    return wrd_list

#wrd_list = string_to_list(str_x)
# print(wrd_list)

def count_list_items(wrd_list):
    singluar_list = []

    for i in wrd_list:
        if i not in singluar_list:
            singluar_list.append(i)

    cnts = []

    for i in singluar_list:
        c = 0
        for j in wrd_list:
            if i == j:
                c+=1
        cnts.append(c)



    return singluar_list , cnts
#singular_list, list_count = count_list_items(wrd_list)

# print(singular_list)
# print(list_count)

def get_ordered_items(singular_list, list_count):
    order_index = []
    sort_count = sorted(list_count, reverse=True)
    chkd = []

    for val in sort_count:
        for idx in range(len(list_count)):
            if list_count[idx] == val and idx not in chkd:
                order_index.append(idx)
                chkd.append(idx)
                break

    return order_index

#ordered_idx= get_ordered_items(singular_list,list_count)
#
# print(ordered_idx)

def print_items_in_order(ordered_idx,singular_list, list_count):
    result = ""
    for i in ordered_idx:
        result += f"word {singular_list[i]} appeared {list_count[i]} times. \n"
    return result
# solution = print_items_in_order(ordered_idx,singular_list,list_count)

def excercise_7(str_x):

    wrd_list = string_to_list(str_x)
    singular_list, list_count = count_list_items(wrd_list)
    ordered_idx= get_ordered_items(singular_list,list_count)
    solution = print_items_in_order(ordered_idx,singular_list,list_count)

    return solution

solution = excercise_7(str_x)

print(solution)


# Without functions
# str_x = "Emma is good developer or developer. Emma is a writer"
#
# lis = []
#
# wrd = ""
#
# chkd = []
#
# for i in str_x:
#     if i == " ":
#         lis.append(wrd)
#         wrd = ""
#     if i != " " and i != ".":
#         wrd = wrd+i
#
# for i in lis:
#     if i not in chkd:
#         chkd.append(i)
#
#
# cnts = []
# for i in chkd:
#     c =  0
#     for j in lis:
#         if i == j:
#             c = c+1
#     cnts.append(c)
# #    print(i , c)
#
# print(chkd)
# print(cnts)
#
# mx_cnts = []
# mx_ind = 0
# for i in cnts:
#
#     if i is max(cnts):
#         mx_cnts.append(mx_ind)
#     mx_ind += 1
# print(mx_cnts)
#
# for i in mx_cnts:
#     print("word","'"+chkd[i]+"'","occured",cnts[i],"Times")
