

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
