# 6-11
cities = {
	'guangzhou': {
		'country': 'china',
		'population': 123123123,
		'located in': 'guangdong province',
		},
	'suzhou': {
		'country': 'china',
		'population': 56123123,
		'located in': 'jiangsu province',
		},
	'xian': {
		'country': 'china',
		'population': 7823123,
		'located in': 'shanxi province',
		},	
	}

for city, city_info in cities.items():
	country = city_info['country'].title()
	population = city_info['population']
	fact = city_info['located in'].title()

	print("\n" + city.title() + " is in " + country + ".")
	print(" It has a population of about " + str(population) + ".")
	print(" And located in " + fact.title() + ".")
