# EX 9-4 number_served.py
class Restaurant():
	"""docstring for Restaurant"""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize the restaurant."""
		self.restaurant_name = restaurant_name.title()
		self.cuisine_type = cuisine_type
		self.number_served = 0


	def describe_restaurant(self):
		"""Display a summary of the restaurant."""
		msg = self.restaurant_name + " serves wonderful " + self.cuisine_type + "."
		print("\n" + msg)


	def open_restaurant(self):
		"""Display a message that the restaurant is open."""
		msg = self.restaurant_name + " is open. Come on in."
		print("\n" + msg)


	def set_number_served(self, number_served):
		"""Set the number of customers that have been served."""
		self.number_served = number_served


	def increment_number_served(self, additional_served):
		"""Incerement the number of customers that who've been served."""
		self.number_served += additional_served



restaurant = Restaurant('the hang bang', 'shanghai')
restaurant.describe_restaurant()

print("\nNumber served: " + str(restaurant.number_served))
restaurant.number_served = 222
print("\nNumber served: " + str(restaurant.number_served))

restaurant.set_number_served(777)
print("\nNumber served: " + str(restaurant.number_served))

restaurant.increment_number_served(555)
print("\nNumber served: " + str(restaurant.number_served))
