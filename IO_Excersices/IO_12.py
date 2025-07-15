# Interactive Menu
# Create a simple interactive menu with options like “1. Say Hello”, “2. Calculate Square”, “3. Exit”. Based on the user’s input, perform the corresponding action

while True:

    print("1. Say Hello ")
    print("2. Caluculate Square  ")
    print("2. Exit ")

    inp = int(input ( "Enter Your choice: ") )

    if inp == 1:
        print( "Hello How are you ?" )
        break
    elif inp == 2:
        nm = int( input( "Enter a number to get its square: "  )   )

        print( nm **2)
        break
    elif inp == 3:
        print("Exiting")
        break
