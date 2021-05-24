# pets.py
# Removing All Instances of Specific Values from a List

pets = ['dog', 'cat', 'goldfish', 'cat', 'dog', 'cat', 'rabbit']
print(pets)

while 'cat' in pets:
	pets.remove('cat')

print(pets)
