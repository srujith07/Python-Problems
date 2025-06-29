

#Method 1
data = []
print("Enter Names below: \n")

while True:
    inp = input()

    if inp:
        data.append(inp)
    else:
        break

for i in range(len(data)):
    print(f"Name {i+1}: {data[i]}")

# Method 2

# name_1, name_2,name_3 = input("Enter names here: ").split()
#
# print(name_1,name_2,name_3)
