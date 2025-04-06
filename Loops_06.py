
data = input("Enter your Input here: ")

num_list = []

for i in data:
    if i.isdigit():
        num_list.append(i)

print(len(num_list))
