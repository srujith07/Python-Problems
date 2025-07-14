# Calculate income tax
# Calculate income tax for the given income by adhering to the rules below
#
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
# Expected Output:
#
# For example, suppose the income is 45000, and the income tax payable is
#
# 10000*0% + 10000*10%  + 25000*20% = $6000
income = 45000
def excercise_12(salary):

    tax = 0

    if salary <= 10000:
        return tax

    if (salary > 10000) and (salary < 20000):
        taxable = salary - 10000
        tax+= taxable * 10/10
        return tax
    if salary > 20000:
        taxable = salary - 20000

        tax += 10000 * 10/100 + taxable * 20/100
        return tax


solution = excercise_12(income)

print(solution )


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
