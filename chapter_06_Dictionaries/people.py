# 6-7
person_1 = {
	'first_name': 'victor', 
	'last_name': 'chen', 
	'age': 20, 
	'city': 'Jersey City'
	}

person_2 = {
	'first_name': 'yu', 
	'last_name': 'zhang', 
	'age': 19, 
	'city': 'Newyork City'
	}

person_3 = {
	'first_name': 'zi', 
	'last_name': 'zhuang', 
	'age': 24, 
	'city': 'Guangzhou'
	}

people = [person_1, person_2, person_3]

for person in people:
	name = person['first_name'].title() + " " + person['last_name'].title()
	age = str(person['age'])
	city = person['city'].title()

	print(name + ", of " + city + ", is " + age + " years old.")

# 参考答案
people = []

person = {
	'first_name': 'victor', 
	'last_name': 'chen', 
	'age': 20, 
	'city': 'Jersey City'
	}
people.append(person)

person = {
	'first_name': 'yu', 
	'last_name': 'zhang', 
	'age': 19, 
	'city': 'Newyork City'
	}
people.append(person)

person = {
	'first_name': 'zi', 
	'last_name': 'zhuang', 
	'age': 24, 
	'city': 'Guangzhou'
	}
people.append(person)

for person in people:
	name = person['first_name'].title() + " " + person['last_name'].title()
	age = str(person['age'])
	city = person['city'].title()

	print(name + ", of " + city + ", is " + age + " years old.")

