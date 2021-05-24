# 5-3
# Passing
alien_color = 'green'

if alien_color is 'green':
	print("You just earned 5 points.")

# Failing
alien_color = 'red'

if alien_color is 'green':
	print("\nYou just earned 5 points.")

# 5-4
# Running the if block
alien_color = 'green'

if alien_color is 'green':
	points = 5
else:
	points = 10

print("You just earned " + str(points) + " points.")
# Running the else block
alien_color = 'yellow'

if alien_color is 'green':
	points = 5
else:
	points = 10

print("\nYou just earned " + str(points) + " points.")

# 5-5
# Green 5
alien_color = 'green'

if alien_color is 'green':
	points = 5
elif alien_color is 'yellow':
	points = 10
else:
	points = 15

print("\nYou just earned " + str(points) + " points.")

# Yellow 10
alien_color = 'yellow'

if alien_color is 'green':
	points = 5
elif alien_color is 'yellow':
	points = 10
else:
	points = 15

print("\nYou just earned " + str(points) + " points.")

# Red 15
alien_color = 'red'

if alien_color is 'green':
	points = 5
elif alien_color is 'yellow':
	points = 10
else:
	points = 15

print("\nYou just earned " + str(points) + " points.")
