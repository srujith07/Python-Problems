# Print Reverse Number Pattern
# Expected Output:
#
# 1 1 1 1 1
# 2 2 2 2
# 3 3 3
# 4 4
# 5


n = 6

def excercise_20(num_x):

    result = ""

    for i in range(1,num_x):
        result += (str(i)+ " ") * (num_x - i) + '\n'

    return result

solution = excercise_20(n)

print(solution)


for i in range(1,n):
    print((str(i) + " ")*(n-i))
