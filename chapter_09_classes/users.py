# EX 9-3 users.py
class User():
	"""A class representing User profile."""

	def __init__(self, first_name, last_name, username, email, location, major):
		"""Initialize user attributes."""
		self.first_name = first_name.title()
		self.last_name = last_name.title()
		self.username = username
		self.email = email
		self.location = location.title()
		self.major = major


	def describe_user(self):
		"""Summarize the user's information."""
		print("\n" + self.first_name + " " + self.last_name)
		print(" Username: " + self.username)
		print(" Emial: " + self.email)
		print(" Location: " + self.location)
		print(" Major: " + self.major)


	def greet_user(self):
		"""Display a personalized greeting to the user."""
		print("\nWelcome back, " + self.username + "!")

# Create several instances
victor = User('victor', 'chen', 'v_chen', 'v_chen@asdasd.com', 
				'jersey city', 'math')
victor.describe_user()
victor.greet_user()

william = User('william', 'matthew', 'w_matthew', 'w_matthew@qq.com', 
				'jersey city', 'IT')
william.describe_user()
william.greet_user()


