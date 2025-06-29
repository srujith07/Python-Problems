num = 9876543210

num = str(num)

lar = 0

smal = 0

for i in num:

    if int(i) > lar:
        lar = int(i)


    if int(i) < smal:
        smal = int(i)


print(lar, smal  )
