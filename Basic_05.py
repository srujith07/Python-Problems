numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


if numbers_x[0] == numbers_x[::-1][0]:
    print("Result is true")
else:
    print("Result is false")

if numbers_y[0] == numbers_y[::-1][0]:
    print("Result is true")
else:
    print("Result is false")
