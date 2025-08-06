# Filter Tuples
# Write a code to filter out students with scores less than 90 from a given a list of tuples.
#
# Given:
#
# students = [('Alice', 85), ('Bob', 92), ('Charlie', 78),('David', 95)]
# Expected Output:
#
# Students with scores 90 or above: [('Bob', 92), ('David', 95)]

students = [('Alice', 85), ('Bob', 92), ('Charlie', 78),('David', 95)]

new_students = [i for i in students if i[1] > 90]

print(new_students)
