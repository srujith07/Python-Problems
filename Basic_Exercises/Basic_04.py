# Remove first n characters from a string
# Write a Python code to remove characters from a string from 0 to n and return a new string.



# my_str = str(input("Enter your string:- "))
# re_num = int(input("Enter number of charectors to remove:- "))
#
# print (my_str[re_num:])

def excercise_1(word, n):

    return word[n:]

print("Removing characters from a string")
print(excercise_1("pynative", 4))
# output 'tive' first four characters are removed

print(excercise_1("pynative", 2))
# output 'native'
