given_num = int(input("Enter the range of fibonacci series: "))

current = 0
start = 1

for i in range(given_num):
    print(current, current+start)
    current += current + start
