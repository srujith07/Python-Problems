income = int(input("Enter your income: "))

tax = 0

if income <= 10000:
    tax = 0

elif income > 10000 and income <= 20000:

    tax += (income - 10000)*10/100

elif income > 20000:
    tax += 10000*10/100
    tax += (income-20000)*20/100


print("Salary :", income)
print("Tax: ",tax)

print("Net Salary after Tax :",income - tax )
