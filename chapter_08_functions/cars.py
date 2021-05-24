# 8-14 cars.py
def make_car(manufacturer, model, **options):
	"""Make a dictionary representing a car."""
	car_dict = {
		'manufacturer': manufacturer.title(),
		'model': model.title(),
		}
	for option, value in options.items():
		car_dict[option] = value

	return car_dict

my_modelY = make_car('tesle', 'modelY', color='grey', tow_package=True)
print(my_modelY)

my_accord = make_car('honda', 'accord', year=1991, color='white', headlights='popup')
print(my_accord)