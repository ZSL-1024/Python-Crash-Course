# EX 9-1 Restaurant.py
class Restaurant():
	"""docstring for Restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize the restaurant."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type


	def describe_restaurant(self):
		"""Display a summary of the restaurant."""
		msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
		print("\n" + msg)


	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		msg = self.restaurant_name + " is open. Come on in."
		print("\n" + msg)

# Make an instance called restaurant from your class.
restaurant = Restaurant('the haidilao', 'hotpot')

# Print the two attributes individually, 
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# and then call both methods.
restaurant.describe_restaurant()
restaurant.open_restaurant()

# Three Restaurants
popeyes = Restaurant('popeyes louisiana kitchen', 'fried chicken')
popeyes.describe_restaurant()

shake_shack = Restaurant('shake shack', 'burgers')
shake_shack.describe_restaurant()

genki = Restaurant('genki sushi', 'sushi')
genki.describe_restaurant()
