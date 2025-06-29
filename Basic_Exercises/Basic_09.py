given_num = int(input("Enter the number to check: "))

given_num = str(given_num)

print("original number",given_num)

if given_num == given_num[::-1]:
    print("Yes. given number is palindrome number")

else:
    print("No. given number is not palindrome number")
