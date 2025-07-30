# Calculate the sum and average of the digits present in a string
# Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.
#
# Given:
#
# str1 = "PYnative29@#8496"
# Expected Outcome:
#
# Sum is: 38 Average is  6.333333333333333

def excercise_09(str_x):
    sum = 0
    c = 0
    for i in str_x:
        if i.isdigit():
            sum += int(i)
            c+=1
    return f"Sum is: {sum} Average is  {sum/c}"

str1 = "PYnative29@#8496"

solution = excercise_09(str1)

print(solution)
