locations = ['paris', 'scotland','tokyo','singapore','beijing']

print("Here is the original list:")
print(locations)

print("\nHere is the sorted list:")
print(sorted(locations))

print("\nHere is the original list again:")
print(locations)

print("\nHere is the sorted list in reverse:")
print(sorted(locations, reverse=True))

print("\nHere is the original list again:")
print(locations)

print("\nReverse:")
locations.reverse()
print(locations)

print("\nOriginal:")
locations.reverse()
print(locations)

print("\nAlphabetical:")
locations.sort()
print(locations)

print("\nReverse Alphabetical:")
locations.sort(reverse=True)
print(locations)