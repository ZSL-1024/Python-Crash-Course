# 7-9 no_pastrami.py
sandwich_orders = ['chicken', 'pastrami', 'steak', 'tuna', 'pastrami', 'shrimp', 'veggie', 'pastrami']
finished_sandwiches = []

# Add code near the beginning of your program to print a message 
# saying the deli has run out of pastrami
print("Sorry, we have run out of pastrami today.")

# And then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders
while 'pastrami' in sandwich_orders:
	sandwich_orders.remove('pastrami')

print('\n')

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print("I am working on your " + current_sandwich + " sandwich.")
	finished_sandwiches.append(current_sandwich)
print("\n")
for finished_sandwich in finished_sandwiches:
	print("I made your " + finished_sandwich + " sandwich.")

