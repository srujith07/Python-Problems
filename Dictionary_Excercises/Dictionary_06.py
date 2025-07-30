# Count Character Frequencies
# Given a string, create a dictionary where keys are characters and values are their frequencies in the string.
#
# Given:
#
# string1 = 'Jessa'
# Expected Output:
#
# Frequencies for 'Jessa': {'J': 1, 'e': 1, 's': 2, 'a': 1}

str_x = 'Jessa'
my_dict = {}
for i in str_x:
    if i in my_dict:
        my_dict[i]+=1
    else:
        my_dict[i] = 1

print(f"Frequencies for {str_x}: {my_dict}")
