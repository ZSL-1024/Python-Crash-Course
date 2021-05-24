# sandwiches.py 8-12
def make_sandwich(items):
	"""Summarize the pizza we are about to make."""
	print("\nMaking a sandwich with the following items:")
	for item in items:
		print("- " + item)
	print("Your sandwich is ready!")

items = ['turkey ham', 'apple slices', 'honey mustard']		
make_sandwich(items)

items = ['ham', 'tomato']
make_sandwich(items)

items = ['chicken', 'lettuce', 'cheese']
make_sandwich(items)