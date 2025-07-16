# Create an inner function
# Create a program with nested functions to perform an addition calculation as follows:
#
# Define an outer function that accepts two parameters, a and b.
# Inside this outer function, define an inner function that calculates the sum of a and b.
# The outer function should then add 5 to this sum.
# Finally, the outer function should return the resulting value.”
def ou_fun(a,b):
    def in_fun():
        return a + b
    return in_fun() + 5
a = ou_fun(4,5)

print(a)


