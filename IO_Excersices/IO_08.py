# Format variables using string.format() method
# Write a program to use the string.format() method to format the following three variables according to the expected output.
#
# Given:
#
# totalMoney = 1000
# quantity = 3
# price = 450
# Expected Output:
#
# I have 1000 dollars so I can buy 3 football for 450.00 dollars.

totalMoney = 1000
quantity = 3
price = 450

print(f"I have {totalMoney} dollars so I can buy {quantity} football for {float(price)} dollars.")
