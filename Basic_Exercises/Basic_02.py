# Exercise 2:
# Python code to iterate through the first 10 numbers and, in each iteration, print the sum of the current and previous number.
#
# Expected Output:
#
# Printing current and previous number sum in a range(10)
# Current Number 0 Previous Number  0  Sum:  0
# Current Number 1 Previous Number  0  Sum:  1
# Current Number 2 Previous Number  1  Sum:  3
# Current Number 3 Previous Number  2  Sum:  5
# Current Number 4 Previous Number  3  Sum:  7
# Current Number 5 Previous Number  4  Sum:  9
# Current Number 6 Previous Number  5  Sum:  11
# Current Number 7 Previous Number  6  Sum:  13
# Current Number 8 Previous Number  7  Sum:  15
# Current Number 9 Previous Number  8  Sum:  17

# Regular Method

for i in range(11):
    pv_num = i - 1
    sm = i+pv_num

    if pv_num < 0:
        pv_num,sm = 0,0

    print (f"Current Number {i}  Previous Number  {pv_num}  Sum:  {sm}" )

# Functions


def excercise_2():

    print("Printing current and previous number sum in a range(10)")
    result = ""
    for i in range(11):
        cur = i
        pv_num = i -1
        sum = cur+pv_num
        if pv_num < 0:
            pv_num = 0
            sum = 0

        result += f"Current Number {cur}  Previous Number  {pv_num}  Sum:  {sum}" + '\n'

        return result

solution = excercise_2()

print(solution)
