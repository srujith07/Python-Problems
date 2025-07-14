# Capitalize the first letter of each word in a string
# Expected Output:
#
# str1 = "pynative.com is for python lovers"
# Output Pynative.com Is For Python Lovers

str1 = "pynative.com is for python lovers"

def excercise_22(str_x):
    result = ""
    str_list = str_x.split()

    for i in str_list:
        result+= i.capitalize() + " "

    return result

solution = excercise_22(str1)

print(solution)


ns = []
for i in str1.split():
    te = i[0].upper()+i[1:]
    ns.append(te)

for i in ns:
    print(i, end=" ")



