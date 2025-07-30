# Modify Nested Dictionary
# In the below dictionary, change name to ‘Jessa’.
#
# Given:
#
# nested_student_dict = {
#     "class": {
#         "student": {
#             "name": "Mike",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }
# Expected Output:
#
# nested_student_dict = {
#     "class": {
#         "student": {
#             "name": "Jessa",
#             "marks": {
#                 "physics": 70,
#                 "history": 80
#             }
#         }
#     }
# }

nested_student_dict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
print(f"Nested dictionary: {nested_student_dict}")
nested_student_dict['class']['student']['name'] = 'Jessa'

print(f"Dict after modification: {nested_student_dict}")
