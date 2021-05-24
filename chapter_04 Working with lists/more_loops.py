# Excercise 4-12
# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("my favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Adding a new food to each list
my_foods.append('cannoli')
friend_foods.append('ice cream')

print("\nmy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)
print('\n')

# Adding for loop to print each list of foods
for food in my_foods:
	print(food)

print('\n')
for food in friend_foods:
	print(food)