row = int(input("Enter size of pattren: "))

print_str = ""
for i in range(1,row+1):
    print_str += str(i) + " "
    print(print_str)


for i in range (1, row+1):
    for j in range(1,i+1):
        print(j, end= " ")
    print()
