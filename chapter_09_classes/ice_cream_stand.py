# ex 9-6 ice_cream_stand.py
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


class IceCreamStand(Restaurant):
	"""Repersent an ice cream stand, a specitic kind of restaurant."""

	def __init__(self, restaurant_name, cuisine_type='ice cream'):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = []


	def show_flavors(self):
		"""Display the flavors available."""
		print("\nWe have the following flavors available: ")
		for flavor in self.flavors:
			print("- " + flavor.title())


godiva = IceCreamStand('godiva')
godiva.flavors = ['chocolate', 'vanilla', 'strawberry']

godiva.describe_restaurant()
godiva.show_flavors()
		