#  Accept any three string from one input() call
# Write a program to take three names as input from the user in a single call to the input() function.
#
# See: Get multiple inputs from a user in one line
#
# Show Hint
# Expected Output
#
# Enter three string Emma Jessa Kelly
# Name1: Emma
# Name2: Jessa
# Name3: Kelly

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
