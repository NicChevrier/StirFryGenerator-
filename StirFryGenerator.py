import random

# List of ingredients
noodles = ['udon', 'ramen', 'soba']
sauces = ['teriyaki', 'hoisin', 'oyster', 'sweet and sour']
veggies = ['bell peppers', 'carrots', 'mushrooms', 'snap peas', 'bok choy']
proteins = ['chicken', 'beef', 'tofu']

# Generate a stir fry
noodle = random.choice(noodles)
sauce = random.choice(sauces)
veggie = random.choice(veggies)
protein = random.choice(proteins)

# Print the stir fry
print(f'Your stir fry is made with {noodle} noodles, {sauce} sauce, {veggie} and {protein}.')
