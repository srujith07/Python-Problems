
n = int(input("Enter size : "))

sym = "* "
for i in range(1, n+1):
    print(i*sym)
while n > 0:
    n = n-1
    print(n*sym)
