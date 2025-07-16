# Find words with both alphabets and numbers
# Write a program to find words with both alphabets and numbers from an input string.
#
# Given:
#
# str1 = "Emma25 is Data scientist50 and AI Expert"
# Expected Output:
#
# Emma25
# scientist50

def excercise_17(str_x):
    result = ""
    wrds = []
    wrd_list = str_x.split()
    for i in wrd_list:
        for j in i:
            if j.isdigit():
                if i not in wrds:
                    wrds.append(i)
    for i in wrds:
        result+=i + '\n'
    return result

str1 = "Emma25 is Data scientist50 and AI Expert"
solution = excercise_17(str1)
print(solution)
