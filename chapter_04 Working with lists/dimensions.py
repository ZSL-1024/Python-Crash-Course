# Defining a Tuple
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Looping Through All Values in a Tuple
for dimension in dimensions:
	print(dimension)

# Writing over a Tuple
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)

dimensions = (400, 100)
print("\nModified dimension:")
for dimension in dimensions:
	print(dimension)
