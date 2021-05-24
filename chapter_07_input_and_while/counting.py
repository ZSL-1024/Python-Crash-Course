# The while Loop in Action
curren_number = 1
while curren_number <= 5:
	print(curren_number)
	curren_number +=1

# Using continue in a Loop
curren_number = 0
while curren_number < 10:
	curren_number += 1
	if curren_number % 2 == 0:
		continue

	print(curren_number)

# Avoiding Infinite Loops
x = 1
while x <= 5:
	print(x)
	x += 1