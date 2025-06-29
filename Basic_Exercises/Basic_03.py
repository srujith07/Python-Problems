
#method 1

my_str = "Pynative"

c = 0

for i in my_str:

    if c % 2 == 0:
        print(i)

    c = c+1


# method 2 

str_len = len(my_str)

for i in range(str_len):
    if i % 2 == 0:
        print(my_str[i])
