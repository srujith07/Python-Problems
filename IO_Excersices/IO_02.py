# Format Output String
# Write a program to display four string “My, “Name“, “Is“, “James” as “My**Name**Is**James“.
#
# Use the print() function to format the given words in the specified format. Display the ** separator between each string.
#
# Given:
#
# str1 = 'My'
# str2 = 'Name'
# str3 = 'Is'
# str4 = 'James'
# Expected Output:
#
# For example: print('your code') should display My**Name**Is**James
wrd_01 = input("Enter First Word: ")
wrd_02 = input("Enter Second Word: ")
wrd_03 = input("Enter Third Word: ")

def excercise_02(wrd_x,wrd_y,wrd_z):
    print(wrd_x,wrd_y,wrd_z, sep="**")


excercise_02(wrd_01,wrd_02,wrd_03)
