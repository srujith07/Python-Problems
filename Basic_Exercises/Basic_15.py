# Get an int value of base raises to the power of exponent
# Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
#
# Note here exp is a non-negative integer, and the base is an integer.
#
# Expected output
#
# Case 1:
#
# base = 2
# exponent = 5
#
# 2 raises to the power of 5: 32 i.e.


base = 2

exponent = 5

def excercise_15(base, exponent):
    return f"{base} raises to the power of {exponent}: {base**exponent}"

solution = excercise_15(base=base,exponent=exponent)

print(solution)


value = base**exponent

print(f"{base} raises to the power of {exponent}: {value}")
