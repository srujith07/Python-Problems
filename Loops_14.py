
# Method 1

n = int(input("Enter number to reverse : "))

print(str(n)[::-1])

# Method 2

while n > 0 :
    print(n%10, end = "")
    n = n //10
