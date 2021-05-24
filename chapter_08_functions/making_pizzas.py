# making_pizzas.py
# Importing an Entire Module
# import pizza
# Using as to Give a Function an Alias
from pizza import make_pizza as mp

# pizza.make_pizza('8','pepperoni')
# pizza.make_pizza('10','mushroom', 'green peppers', 'extra cheese')
mp('8','pepperoni')
mp('10','mushroom', 'green peppers', 'extra cheese')