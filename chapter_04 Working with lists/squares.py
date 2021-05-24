# make a list of the first 10 square numbers 
# (that is, the square of each integer from 1 through 10).
squares = []
for value in range(1,11):
	square = value**2
	squares.append(square)

print(squares)

# more concisely
squares = []
for value in range(1,11):
	squares.append(value**2)

print(squares)

# Simple Statistics with a List of Numbers
digits = squares
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
squares = [value**2 for value in range(1,11)]
print(squares)