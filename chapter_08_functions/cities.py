# 8-5 cities.py

def describe_city(name, country='china'):
	"""Display City Info"""
	print("\nThe City " + name.title() + " is in " + country.title() + ".")
	
describe_city('guangzhou')
describe_city("xi'an")	
describe_city('jersey city', 'united states')
