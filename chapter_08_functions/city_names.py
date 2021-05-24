# 8-6
def city_country(city, country):
	"""Retrun a string of a city and its country"""
	return(city.title() + ', ' + country.title())

city = city_country('beijing', 'china')
print(city)

city = city_country('newyork city', 'united states')
print(city)

city = city_country('santiago', 'chile')
print(city)
