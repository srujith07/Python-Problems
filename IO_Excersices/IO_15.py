# Padding with Zeros
# Ask the user for a number. Print this number padded with leading zeros to a width of 5.
#
# For example, if the input is 12, the output should be “00012“

n = int(input("Enter number : "))

l = 5 - len( str( n  )  )

for i in range(l):
    print(0,end ="")

print(n)
