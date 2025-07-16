#
# Call Function using both positional and keyword arguments
# Define a function describe_pet(animal_type, pet_name) that prints a description of a pet. Call this function using both positional and keyword arguments.
#

def describe_pet(animal_type, pet_name):

    return f"My pet name is {pet_name}, It is a {animal_type}."


solution = describe_pet("Dog","Pinky")

print(solution)

solution = describe_pet(pet_name="Pinky",animal_type="Dog")

print(solution)
