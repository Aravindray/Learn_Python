# Author: Aravind Date: Sat, 14/9 2024
#5-12
#5-1, 5-2
favorite_color = 'red'
if favorite_color == 'green':
    print('I think your favorite color is green')

if favorite_color == 'blue':
    print('I think your favorite color is blue')

if favorite_color == 'red':
    print('I think your favorite color is red')

name = 'John'

if name.lower() == 'peter':
    print('Hey Peter, Welcome back!')

if name.lower() == 'john':
    print('Hi John, Welcome back')

jersey_number = 0

if jersey_number <= 10:
    print('Yes, It\'s less than 10.')

my_favorite_color = 'all'
my_favorite_number = 1
your_favorite_color = 'all'
your_favorite_number = 2

if my_favorite_color == your_favorite_color and \
    my_favorite_number == your_favorite_number:
    print('We are twins!')

if my_favorite_color == your_favorite_color or \
    my_favorite_number == your_favorite_number:
    print('We have similar taste!')

foods = ['pizza', 'pasta', 'burger', 'salad', 'ice cream']
if 'ice cream' in foods:
    print("Yes, It's available.")

if 'dosa' not in foods:
    print("Yes, It's not available")

#5-3
print()
alien_0_color = 'yellow'

if alien_0_color == 'green':
    print('You just earn 5 points')

alien_1_color = 'green'

if alien_1_color == 'green':
    print('You just earn 5 points')

#5-4
print()
if alien_0_color == 'green':
    print('You just earn 5 points')
else:
    print('You just earn 10 points')

#5-5
print()
if alien_1_color == 'green':
    print('You just earn 5 points')
else:
    print('You just earn 10 points')

#5-6
print()
age = 26

if age < 2:
    print("You're a baby.")
elif age < 4:
    print("You're a toddler.")
elif age < 13:
    print("You're a kid.")
elif age < 20:
    print("You're a teenager.")
elif age < 65:
    print("You're a adult.")
else:
    print("You're a elder person.")

#5-7
print()
favorite_fruits = ['apple', 'banana', 'orange', 'watermelon', 'graph', 'pomegranate', 'jackfruit']

if 'apple' in favorite_fruits:
    print("You really like apples!")

if 'durian' in favorite_fruits:
    print('You REALLY like "durian"!')

if 'graph' in favorite_fruits:
    print('You really like graphs!')

if 'mango' in favorite_fruits:
    print('You really like mangoes!')

if 'papaya' in favorite_fruits:
    print('You really like papayas!')

#5-8, 5-9
print()
users = ['admin', 'aravind', 'ray', 'john', 'bill', 'dan']
# users = []

if users:
    for user in users:
        if user == 'admin':
            print(f"Hello {user.title()}, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print('We need to find some users!')

# Date: Wed, 18/9 2024

#5-10
print()
current_users = ['CodeCrafter', 'PixelPioneer', 'ScriptSage', 'ByteBender', 'TechTrekker']
new_users = ['QuantumQuester', 'DataDynamo', 'CyberScribe', 'NexusNavigator', 'ByteBender', 'PixelPioneer']
lowercase_current_users = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in lowercase_current_users:
        print('Username is already available, Try different username!')
    else:
        print('Username is available.')

#5-11
print()
ordinal_numbers = list(range(1,10))
for number in ordinal_numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
