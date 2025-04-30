
prime_lis = []

for i in range(1,21):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_lis.append(i)

for i in prime_lis[1::2]:
    print(i, end = ",")
