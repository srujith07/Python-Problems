given_num = int(input("Enter the range of fibonacci series: "))

prev = 0

curr = 1

print(prev, curr, end=" ")

for i in range(given_num-2):
    fabi = prev+curr
    print(fabi, end=" ")
    prev = curr
    curr = fabi
