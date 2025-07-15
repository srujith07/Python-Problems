# Check File is Empty or Not
# Write a program to check if the given file is empty or not

with open("test.txt", 'r') as test_file:
    if test_file.read():
        print("Files is not empty")
    else:
        print("File is empty")
