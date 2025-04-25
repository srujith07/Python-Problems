def my_func(no):
    if no == 0:
        return 1
    else:
        return no * my_func(no-1)

a = my_func(5)

print(a)

