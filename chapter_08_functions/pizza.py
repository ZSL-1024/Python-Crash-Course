# pizza.py
# Passing an Arbitrary Number of Arguments
# Mixing Positional and Arbitrary Arguments
def make_pizza(size, *toppings):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a " + str(size) + 
		  "-inches pizza with the following toppings:")
	for topping in toppings:
		print("- " + topping)

# make_pizza('8','pepperoni')
# make_pizza('10','mushroom', 'green peppers', 'extra cheese')
