pets = []

pet = {
	'name': 'mimi', 
	'owner': 'john',
	'animal type': 'cat', 
    'weight': 4,
    'eats': 'fish',
	}
pets.append(pet)

pet = {
	'name': 'gigi', 
	'owner': 'eric',
	'animal type': 'dog', 
    'weight': 10,
    'eats': 'meat',
	}
pets.append(pet)

pet = {
	'name': 'kiki', 
	'owner': 'sarah',
	'animal type': 'rabbit', 
    'weight': 2,
    'eats': 'grass',
	}
pets.append(pet)

for pet in pets:
	print("\nHere's what I know about " + pet['name'].title() + ":")
	for key, value in pet.items():
		print("\t" + key + ": " + str(value))