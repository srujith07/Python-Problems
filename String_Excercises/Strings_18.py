# Replace each special symbol with # in the following string
# Given:
#
# str1 = '/*Jon is @developer & musician!!'
# Expected Output:

##Jon is #developer # musician##

def excercise_18(str_x):
    result = ""
    for i in str_x:
        if i.isalpha() or i == " " or i.isdigit():
            result+=i
        else:
            result+="#"

    return result
str1 = '/*Jon is @developer & musician!!'

solution = excercise_18(str1)

print(solution)
