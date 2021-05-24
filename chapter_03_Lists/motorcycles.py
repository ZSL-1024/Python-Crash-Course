# Modifying Elements in a List

motorcycles = ['honda', 'yamaha', 'suzuki']

print(motorcycles)

motorcycles[0] = 'ducati'

print(motorcycles)

# Adding Elements to a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print("\t")
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

# Inserting Elements into a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print("\t")
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing Elements from a List

motorcycles = ['honda', 'yamaha', 'suzuki']
print("\t")
print(motorcycles)

del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method

motorcycles = ['honda', 'yamaha', 'suzuki']
print("\t")
print(motorcycles)

popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()
print("\t")
print("The last motorcycle I owned was a " + last_owned.title() + ".")


# Popping Items from any Position in a List

motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print("\t")
print('The first motorcycle I owned was a ' + first_owned.title() + '.')

# Removing an Item by Value

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print('\t')
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print('\t')
print(motorcycles)
too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print("\nA " + too_expensive + " is too expensive for me.")

