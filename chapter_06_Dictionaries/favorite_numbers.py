# 6-2  6-10
favorite_numbers = {
	'david': [6, 9],
	'steve': [11, 22, 33],
	'john': [7, 23],
	'sarah': [5, 67]
	}

num = favorite_numbers['david']
print("David's favorite number is: " + str(num))

num = favorite_numbers['steve']
print("Steve's favorite number is: " + str(num))

num = favorite_numbers['john']
print("john's favorite number is: " + str(num))

num = favorite_numbers['sarah']
print("sarah's favorite number is: " + str(num))

for name, numbers in favorite_numbers.items():
	print("\n" + name.title() + "'s favorite numbers are: ")
	for num in numbers:
		print("  " + str(num))
