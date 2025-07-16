# Modifies global variable
# Define a global variable global_var = 10. Write a function that modifies a global variable value.

global_var = 10

def excercise_12():

    global global_var

    global_var = 25

    return f"Global Var Inside the Function {global_var}"

solution = excercise_12()
print(solution)

print(f"Global Var Outside the Function {global_var}")
