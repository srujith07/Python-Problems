# Check if a user-entered string contains any digits using a for loop
# Expected Output:
#
# Enter a string: Pynative123Python
# The string contains at least one digit.
#
# Enter a string: PYnative
# The string does not contain any digits.


def excercise_21(str_x):
    for i in str_x:
        if i >= "0" and i <= "9":
            return "The string contains at least one digit."

    return "The string does not contain any digits."

solution_1 = excercise_21("Pynative123Python")

solution_2 = excercise_21("PYnative")

print(solution_1)
print(solution_2)



n = "Pynative123python"

print(any('0' <= i <= '9' for i in n))
