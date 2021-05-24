# 7-8 deli.py
 # Make a list called sandwich_orders and fill it with the names of 
 # various sandwiches.
sandwich_orders = ['chicken', 'steak', 'tuna', 'shrimp', 'veggie']
# Then make an empty list called finished_sandwiches.
finished_sandwiches = []

# Loop through the list of sandwich orders and print a message for each order,
while sandwich_orders:
	current_sandwich = sandwich_orders.pop()

	print("I am working on your " + current_sandwich + " sandwich.")
	finished_sandwiches.append(current_sandwich)
print("\n")
# print a message listing each sandwich that was made.
for finished_sandwich in finished_sandwiches:
	print("I made your " + finished_sandwich + " sandwich.")