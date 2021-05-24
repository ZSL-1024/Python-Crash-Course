# Excercise 4-13
five_simple_foods = ('fried rice', 'noodles', 'dumplings', 'soup', 'hot pot')
print("Original Menu:")
for food in five_simple_foods:
    print(food)

# Intentional error
# five_simple_foods[0] = 'congee'

five_simple_foods = ('fried rice', 'noodles', 'dumplings', 'congee', 'fried noodles')
print("\nRevised Menu:")
for food in five_simple_foods:
    print(food)

