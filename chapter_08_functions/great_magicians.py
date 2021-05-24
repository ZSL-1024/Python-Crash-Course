# 8-10 great_magicians.py
def show_magicians(names):
	"""Rrint the name of each magician in the list."""
	for name in names:
		print(name.title())

def make_great(names):
	"""Add 'the Great!' to each magician's name."""
	# Build a new list to hold the great magicians.
	great_magicians = []

	# Make each magician great, and add it to great_magicians.
	while names:
		name = names.pop()
		great_magician = name + ' the Great'
		great_magicians.append(great_magician)

	# Add the great magicians back into magicians.
	for great_magician in great_magicians:
		names.append(great_magician)

	return names


names = ['david', 'harry', 'teller']
show_magicians(names)

print("\nGreat magicians:")
great_magicians = make_great(names[:])
show_magicians(great_magicians)

print("\nOriginal magicians:")
show_magicians(names)