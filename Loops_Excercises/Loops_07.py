# Print the following pattern
# Write a Python program to print the reverse number pattern using a for loop.
#
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# Refer: Print patterns in Python


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
