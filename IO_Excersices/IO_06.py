# Write all content of a file into a new file by skipping line number 5
# See:
#
# Python file handling
# Python Read file
# Python write file
# Create a test.txt file and add the below content to it.
#
# Given test.txt file:
#
# line1
# line2
# line3
# line4
# line5
# line6
# line7
# Expected Output: new_file.txt
#
# line1
# line2
# line3
# line4
# line6
# line7


with open ("test.txt", 'r') as test_file , open ("new_file.txt", 'w+') as new_file:
    line_count = 1

    for i in test_file:
        if  line_count!= 5:
            new_file.write(i)
        line_count+=1
    print("Copied content from from test.txt to new_filke.txt by skipping line number 5")

