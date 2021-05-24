# ex 9-7 admin.py
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


class Admin(User):
	"""A user with administrative privileges."""

	def __init__(self, first_name, last_name, username, email, location, major):
		super().__init__(first_name, last_name, username, email, location, major)
		self.first_name = first_name
		self.last_name = last_name
		self.username = username
		self.email = email
		self.location = location
		self.major = major
		self.privileges = Privileges()


class Privileges():
	"""docstring for Privileges"""
	def __init__(self, privileges=[]):
		self.privileges = privileges
		

	def show_privileges(self):
		"""Print a lsit of privileges that a administrator has"""
		print("\nPrivileges: ")
		if self.privileges:
			for privilege in self.privileges:
				print("- " + privilege)
		else:
			print("- This user has no privileges.")


steve = Admin('steve', 'zhuang', 'steve_z', 'steve_z@gggcom', 
					'guangzhou', 'SDE')
steve.describe_user()

steve.privileges.show_privileges()

print("\nAdding privileges:")
steve.privileges.privileges = ['can add post', 'can delete post', 'can ban user']
steve.privileges.show_privileges()

