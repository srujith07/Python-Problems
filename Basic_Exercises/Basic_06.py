# Display numbers divisible by 5
# Write a Python code to display numbers from a list divisible by 5
# 
# Expected Output:
# 
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55
lis = [10, 20, 33, 46, 55]

print("Given list is",lis)

print (  "Divisible by 5"  )

for i in lis:
    if i % 5 == 0:
        print(i)

def excercise_6(list_x):
    result = "Divisible by 5" + '\n'

    for i in list_x:
        if i % 5 == 0:
            result += str(i) + '\n'

    return  result

solution = excercise_6(lis)

print(solution)
