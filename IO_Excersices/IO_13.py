# Display Right-Aligned Output
# Ask the user for a word and a number. Print the word right-aligned in a field of width 20, followed by the number.
wrd = input( "Enter a word : "   )

nm = int( input( "Enter a anumber : "  ) )



print(f"{wrd:>20}{nm}")
