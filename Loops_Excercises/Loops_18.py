
# Print the following pattern
# Write a program to print the following start pattern using the for loop
#
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input("Enter size : "))

sym = "* "
for i in range(1, n+1):
    print(i*sym)
while n > 0:
    n = n-1
    print(n*sym)
