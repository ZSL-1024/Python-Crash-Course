# 6-3
glossary = {
	'string': 'A series of characters.',
	'comment': 'A note in a program that the Python interpreter ignores.',
	'list': 'A collection of items in a particular order.',
	'loop': 'Work through a collection of items, one at a time.',
	'dictionary': 'A collection of key-value pairs.',
	'key': 'The first item in a key-value pair in a dictionary.',
    'value': 'An item associated with a key in a dictionary.',
    'conditional test': 'A comparison between two values.',
    'float': 'A numerical value with a decimal component.',
    'boolean expression': 'An expression that evaluates to True or False.',
	'set': 'A set is similar to a list except that each item in the set must be unique',
	}

for term, meaning in glossary.items():
	print(term.title() + ": " + meaning)