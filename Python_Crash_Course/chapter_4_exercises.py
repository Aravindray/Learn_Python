# Author: Aravind Date: Fri, 13/9 2024

#4-1, 4-11
pizzas = ['Margherita', 'New York-style', 'Neapolitan']
for pizza in pizzas:
    # print(pizza)
    print(f'I like {pizza} pizza')

print()
print(f"I love to eat pizza everyday, The {pizzas[0]} pizza made my day.")
print(f"And Wow, I love the thin crust and foldable pizza like {pizzas[1]}.")
print(f"Who doesn't love mozzarella cheese I also love {pizzas[2]} pizza which full of mozzarella.")
print('I really love pizza!')

friend_pizzas = pizzas[:]
pizzas.append('Chicago')
friend_pizzas.append('Detroit')

print('\nMy favorite pizzas are:')
for pizza in pizzas:
    print(f'\t{pizza}')

print('\nMy friend\'s favorite pizzas are:')
for pizza in friend_pizzas:
    print(f'\t{pizza}')

#4-2
print()
animals = ['goat', 'sheep', 'cow']
for animal in animals:
    # print(animal)
    print(f'A {animal} would make a great pet.')
print('Any of these animals would make a great pet!')

#4-3
print()
for number in range(1, 21):
    print(number)

#4-4
print()
one_million = [x for x in range(1, 1000001)]
# for number in one_million:
#     print(number)

#4-5
print()
print(f"The minimum value of the one_million list is {min(one_million)}")
print(f"The maximum value of the one_million list is {max(one_million)}")
print(f'The sum of one_million list is {sum(one_million)}')

#4-6
print()
odd_numbers = [x for x in range(1, 20, 2)]
for number in odd_numbers:
    print(number)

#4-7, 4-10
print()
multiple_threes = [x*3 for x in range(1, 11)]
for number in multiple_threes:
    print(number)

print()
print(f"The first three items in the list are: {multiple_threes[:3]}")
middle_index = (len(multiple_threes)//2) - 1
print(f"Three items from the middle of the list are: "
      f"{multiple_threes[middle_index:middle_index+3]}")
print(f"The last three items in the list are: {multiple_threes[-3:]}")

#4-8, 4-9
print()
cubes = [x**3 for x in range(1,11)]
for number in cubes:
    print(number)

#4-12
print()
my_foods = ['pizza', 'falafel', 'carrot cake']
print('My favorite foods are:')
for food in my_foods:
    print(f'\t{food}')

print()
friend_foods = my_foods[:]
friend_foods.append('Ice cream')
print('My friend\'s favorite foods are:')
for food in friend_foods:
    print(f'\t{food}')

#4-13
print()
buffets = ('salad', 'bread rolls', 'pasta', 'roasted meats', 'dessert')
print('Menu')
for food in buffets:
    print(food)
# buffets[0] = 'veg salad'

print()
buffets = ('veg salad', 'PB&J', 'pasta', 'cheese potato', 'dessert')
print("Revised Menu")
for food in buffets:
    print(food)
