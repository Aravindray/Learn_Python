# Author: Aravind Date: Thu, 19/9 2024

# 7-1
print()
rental_car = input('What kind of car you would like to rent? ')
print(f'Let me see if I can find you a {rental_car.title()}.')

# 7-2
print()
how_many = int(input('How many people are there in dinning group? '))
if how_many > 8:
    print('You guys will have to wait for a table.')
else:
    print('Your table is ready.')

# 7-3
print()
user_number = int(input('Enter a number: '))
if user_number % 10 == 0:
    print(f'Your number {user_number} is multiple of 10.')
else:
    print(f'No, Your number {user_number} is not multiple of 10.')

# 7-4
while True:
    message = "\nEnter your topping\n(enter "quit" to quit the program): "
    pizza_toping = input(message)
    if pizza_toping == 'quit':
        break
    print(f'You have added {pizza_toping} to your pizza.')

# 7-5, 7-6 iii
while True:
    message = '\nEnter your age\n[Press and return "q" anytime to quit the program]: '
    watcher_age = input(message)
    if watcher_age == 'q':
        break
    elif int(watcher_age) < 3:
        print('You can watch the movie freely!')
    elif int(watcher_age) >= 3 and int(watcher_age) < 12:
        print('It cost $10 for you.')
    else:
        print('It cost $15 for you.')

# 7-6 i
print()
user_input = input('Enter your age (return "q" to quit): ')
while user_input != 'q':
    if int(user_input) < 3:
        print('You can watch the movie freely!')
    elif int(user_input) >=3 and int(user_input) < 12:
        print('It cost $10 for you.')
    else:
        print('It cost $15 for you.')
    user_input = input('\nEnter your age (return "q" to quit): ')

# 7-6 ii
flag = True
while flag:
    user_input = input('\nEnter your age (return "q" to quit): ')
    if user_input == 'q':
        flag = False
    elif int(user_input) < 3:
        print('You can watch the movie freely!')
    elif int(user_input) >=3 and int(user_input) < 12:
        print('It cost $10 for you.')
    else:
        print('It cost $15 for you.')

# 7-7 skipped because already caused so many infinity loop

# 7-8, 7-9
sandwich_orders = [
    'pastrami',
    'tuna',
    'american',
    'bologna',
    'pastrami',
    'cheese',
    'chicken salad',
    'cuban',
    'pastrami',
    'egg',
    'fried chicken',
    'pastrami'
]
finished_sandwiches = []
print('Sorry, We are run out of "Pastrami Sandwich"!')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    sandwich_made = sandwich_orders.pop(0)
    print(f"I made your {sandwich_made} sandwich.")
    finished_sandwiches.append(sandwich_made)

print("These are the sandwiches that are made:")
for sandwich in finished_sandwiches:
    print(f'\t- {sandwich}')

# 7-10
response = {}

while True:
    print('\nEnter "q" to quit the program.')
    name = input('Enter your name: ')
    if name == 'q':
        break
    place = input('If you could visit one place in the world, where would you go?: ')
    if place == 'q':
        break
    response[name] = place
    again = input('Would you like to let another person respond? (yes / no): ')
    if again.lower() != 'yes':
        break
print()
for name, place in response.items():
    print(f"{name.title()} would like to visit {place.title()}.")
