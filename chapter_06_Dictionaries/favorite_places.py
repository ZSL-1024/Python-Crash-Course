# 6-9
favorite_places = {
	'john': ['paris', 'hawaii', 'tokyo'],
	'victor': ['iceland', 'newyork'],
	'sarah': ['los angels', 'florida', 'africa']
}

for name, places in favorite_places.items():
	print("\n" + name.title() + " likes the following places:")
	for place in places:
		print("- " + place.title())
