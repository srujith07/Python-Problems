# Find the last position of a given substring
# Write a program to find the last position of a substring “Emma” in a given string.
#
# Given:
#
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# Expected Output:
#
# Last occurrence of Emma starts at index 43

def excercise_12(str_x):
    c= 0
    idx_emma = []
    for i in range(0,len(str_x)):
        if str_x[i:i+4] == "Emma":
            idx_emma.append(c)
        c+=1
    return f"Last occurrence of Emma starts at index: {idx_emma[-1]}"
str1 = "Emma is a data scientist who knows Python. Emma works at google."

solution = excercise_12(str1)

print(solution)

str1 = "Emma is a data scientist who knows Python. Emma works at google."


index = str1.rfind("Emma")
print("Last occurrence of Emma starts at index:", index)
