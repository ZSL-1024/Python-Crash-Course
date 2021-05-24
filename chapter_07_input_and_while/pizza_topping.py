# 7-4 pizza_topping.py
prompt = "\nWhat kind of topping would you like have on your pizza?"
prompt += "\nEnter 'quit' to end the program. \n"

while True:
	topping = input(prompt)

	if topping == 'quit':
		break
	else:
		print("\tI will add " + topping + " to your pizza.")