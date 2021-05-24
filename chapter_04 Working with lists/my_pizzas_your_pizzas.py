# Excercise 4-11
favorite_pizzas = ['pepperoni', 'hawaiian', 'veggie']
for pizza in favorite_pizzas:
	print("I like " + pizza + " pizza.\n")

print("I really love pizza!")

# make a copy
friend_pizzas = favorite_pizzas[:]

favorite_pizzas.append('seafood')
friend_pizzas.append('pesto')

print("My favorite pizzas are:")
for pizza in favorite_pizzas:
	print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)