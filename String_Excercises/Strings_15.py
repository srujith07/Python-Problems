# Exercise 15: Remove special symbols / punctuation from a string
# Given:
#
# str1 = "/*Jon is @developer & musician"
# Expected Output:
#
# "Jon is developer musician"

def excercise_15(str_x):
    result = ""
    for i in str_x:
        t = i.lower()
        if t.isalpha() or i == " ":
            result+=i
    result = ' '.join(result.split())
    return result
str1 = "/*Jon is @developer & musician"

solution = excercise_15(str1)

print(solution)
