# Print Alternate Prime Numbers till 20
# A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11).
#
# For example:
#
# All prime numbers from 1 to 20: 2, 3, 5, 7, 11, 13, 17, 19
#
# Alternate prime numbers from 1 to 20:
# 2, 5, 11, 17


def excercise_19(range_x):
    result = ""
    prime_list = []
    for i in range(2, range_x):
        for j in range(2,i):
            if i %j == 0:
                break
        else:
            prime_list.append(i)

    return  prime_list[::2]

solution = excercise_19(20)

print(solution)

prime_lis = []

for i in range(1,21):
    for j in range(2,i):
        if i % j == 0:
            break
    else:
        prime_lis.append(i)
c = 0
for i in prime_lis[1::2]:
    print((str(i) +",") if c < len(prime_lis[1::2])-1 else (i), end = "")
    c+= 1
