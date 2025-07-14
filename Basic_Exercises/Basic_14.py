# Print a downward half-pyramid pattern of stars
# * * * * *
# * * * *
# * * *
# * *
# *
# Refer:
#
# Print Pattern using for loop
# Nested loops in Python


n = 7

def excercise_14(size):

    result = ""

    for i in range(n,-1,-1):
        result+= ("* " * i ) +'\n'

    return  result

solution = excercise_14(n)

print(solution)

symbol = "* "

for i in range(n,0,-1):
    print(symbol*i)
