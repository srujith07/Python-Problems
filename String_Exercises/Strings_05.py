# Count all letters, digits, and special symbols from a given string
# Given:
#
# str1 = "P@#yn26at^&i5ve"
# Expected Outcome:
#
# Total counts of chars, digits, and symbols
#
# Chars = 8
# Digits = 3
# Symbol = 4

str1 = "P@#yn26at^&i5ve"

def excercise_05(str_x):
    chars = 0
    digits = 0
    symbols = 0

    for i in str_x:
        if i.isdigit():
            digits+=1
        elif i.isalpha():
            chars+=1
        else:
            symbols+=1
    return f"Total counts of chars, digits, and symbols \nChars = {chars} \nDigits = {digits}\nSymbols = {symbols}"

solution = excercise_05(str1)

print(solution)
