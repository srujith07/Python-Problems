nested_list = [1, [2, 3], [4, 5, 6], 7, [8, 9]]

n_list = []

for i in nested_list:

    if isinstance(i , list):
        for j in i:
            n_list.append(j)
    
    elif not isinstance(i , list):
        n_list.append(i)


print(n_list)
