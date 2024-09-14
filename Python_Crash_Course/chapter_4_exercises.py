# Author: Aravind Date: Fri, 13/9 2024

#4-1
pizzas = ['Margherita', 'New York-style', 'Neapolitan']
for pizza in pizzas:
    # print(pizza)
    print(f'I like {pizza} pizza')
print(f"I love to eat pizza everyday, The {pizzas[0]} pizza made my day.")
print(f"And Wow, I love the thin crust and foldable pizza like {pizzas[1]}.")
print(f"Who doesn't love mozzarella cheese I also love {pizzas[2]} pizza which full of mozzarella.")
print('I really love pizza!')

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
print(f"The first three items in the list are: {multiple_threes[:3]}")
middle_index = (len(multiple_threes)//2) - 1
print(f"Three items from the middle of the list are:"
       "{multiple_threes[middle_index:middle_index+3]}")

#4-8, 4-9
print()
cubes = [x**3 for x in range(1,11)]
for number in cubes:
    print(number)
