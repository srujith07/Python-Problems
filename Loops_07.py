row = int(input("Enter size of pattren: "))

for i in range(row,0,-1):
    for j in range(i,0,-1):
        print(j, end=" ")
    print(" ")

# Beginer Method

# row = int(input("Enter size of pattren: "))
# print_str = ""
# for i in range(row,0,-1):
#     print_str += str(i)
#
# for i in range(0,row):
#     for i in print_str[i:]:
#         print(i,end=" ")
#     print()
