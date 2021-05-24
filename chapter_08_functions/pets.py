# pets.py
# Positional Arguments
# When you call a function, Python must match each argument in the function 
# call with a parameter in the function definition.
def describe_pet(animal_type, pet_name):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('cat', 'mimi')
# Multiple Function Calls
# Order Matters in Positional Arguments
describe_pet('dog', 'hans')

# Keyword Arguments
# A keyword argument is a name-value pair that you pass to a function.
# The order of keyword arguments doesn’t matter because Python 
# knows where each value should go. T
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# Default Values
def describe_pet(pet_name, animal_type='dog'):
	"""Display information about a pet."""
	print("\nI have a " + animal_type + ".")
	print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hans')