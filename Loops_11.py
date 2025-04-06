start = int(input("Enter start value: "))

end = int(input("Enter end value: "))

for i in range(start,end+1):
    is_prime = True
    for j in range(2,i):
        if (i%j) == 0:
            is_prime = False
            break
    if is_prime:
        print(i)




