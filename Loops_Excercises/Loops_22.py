
# Find largest and smallest digit in a number
# Write a program in Python identifies the digit with the highest value and the digit with the lowest value within that number.
#
# Input:
#
# num1 = 9876543210
# num2 = -5082


num = -5082

if num < 0:
    num-=num + num
print(num)

num = str(num)

lar = 0

smal = 0

for i in num:

    if int(i) > lar:
        lar = int(i)


    if int(i) < smal:
        smal = int(i)


print(lar, smal  )
