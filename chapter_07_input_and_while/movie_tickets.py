# 7-5 movie_tickets.py
prompt = "How old are you? "
prompt += "\nEnter 'quit' when you are finished."

while True:
	age = input(prompt)
	if age == 'quit':
		break
	age = int(age)

	if age < 3:
		print("\tYou get in free.")
	elif age < 13:
		print("\tYour ticket is $10.")
	elif age > 12:
		print("\tYour ticket is $15.")

