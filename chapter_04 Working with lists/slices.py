# Excercise 4-10
cubes = []
for number in range(1,11):
	cube = number**3
	cubes.append(cube)

for cube in cubes:
	print(cube)

print(cubes)

print("\nThe first three items in the list are:")
print(cubes[:3])

print("\nThree items from the middle of the list are:")
print(cubes[3:6])

print("\nThe last three items in the list are:")
print(cubes[-3:])

print("\nThe reverse list is:")
print(cubes[::-1])