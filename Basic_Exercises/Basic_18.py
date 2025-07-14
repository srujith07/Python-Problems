# Check if a given year is a leap year
# A leap year is a year in the Gregorian calendar that contains an extra day, making it 366 days long instead of the usual 365. This extra day, February 29th, is added to keep the calendar synchronized with the Earth’s revolution around the Sun.
#
# Rules for leap years: a year is a leap year if it’s divisible by 4, unless it’s also divisible by 100 but not by 400.
#
# Write a code find if a given year is a leap year.
#
# Given:
#
# year1 = 2020
# # Output True
#
# year2 = 2025
# # Output False



def excercise_18(year):
    if year % 4 == 0 :
        if year % 100 == 0:
            if year %400 == 0:
                return "True"
            else:
                return "False"
        else:
            return "True"
    else:
        return "False"


year = int(input("Enter an year to check if its a Leap Year : "))



solution = excercise_18(year)

print(solution)


if year % 4 == 0 :
    if year % 100 == 0:
        if year %400 == 0:
            print("True")
        else:
            print("False")
    else:
        print("True")
else:
    print("False")
