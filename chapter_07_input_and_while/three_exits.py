# 7-6 three_exits.py
prompt = "How old are you? "
prompt += "\nEnter 'quit' when you are finished."

# Use an active variable to control how long the loop runs.
active = True
while active:
	age = input(prompt)
	# Use a break statement to exit the loop when the user enters a 'quit' value.
	if age == 'quit':
		break
	age = int(age)

	if age < 3:
		print("\tYou get in free.")
	elif age < 13:
		print("\tYour ticket is $10.")
	elif age > 12:
		print("\tYour ticket is $15.")

