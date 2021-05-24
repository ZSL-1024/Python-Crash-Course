# ex 9-5 login_attempts.py
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
		self.login_attempts = 0


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


	def increment_login_attempts(self):
		"""Increment the value of login_attempts."""
		self.login_attempts +=1


	def reset_login_attempts(self):
		"""Reset login_attempts to 0."""
		self.login_attempts = 0

# Make an instance of the User class
victor = User('victor', 'chen', 'v_chen', 'v_chen@asdasd.com', 
				'jersey city', 'math')
victor.describe_user()
victor.greet_user()

# call increment_login_attempts() several times
print("\nMaking 3 login attempts...")
victor.increment_login_attempts()
victor.increment_login_attempts()
victor.increment_login_attempts()
# Print the value of login_attempts
print("  User login attempts: " + str(victor.login_attempts))

# then call reset_login_attempts().
print("Resetting login attempts...")
victor.reset_login_attempts()
print("  User login attempts: " + str(victor.login_attempts))
