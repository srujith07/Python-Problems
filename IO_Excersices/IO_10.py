# Read Line Number 4 from File

# Read Specific Lines From a File in Python
# Python read file
# Create a test.txt file and add the below content to it.
#
# test.txt file:
#
# line1
# line2
# line3
# line4
# line5
# line6
# line7

with open("test.txt", "r") as test_file:
    lines = test_file.readlines()

    print(lines[3])
