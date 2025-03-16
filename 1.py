#`Exercise 1: Calculate the multiplication and sum of two numbers
#`Given two integer numbers, write a Python code to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.
#`
#`Given 1:
#`
#`number1 = 20
#`number2 = 30
#`Expected Output:
#`
#`The result is 600
#`Given 2:
#`
#`number1 = 40
#`number2 = 30
#`Expected Output:
#`
#`The result is 70

num_1 = int(input("Enter Number 1 value : "))
num_2 = int(input("Enter Number 2 value : "))

if ( num_1 * num_2 ) >= 1000:
    print (num_1 + num_2 )
else:
    print( num_1*num_2 )
