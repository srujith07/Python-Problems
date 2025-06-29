given_number = int(input("Enter the number: "))

str_number = str(given_number)

final_str = ""

for i in str_number[::-1]:
    final_str+=i + " "

print(final_str)
