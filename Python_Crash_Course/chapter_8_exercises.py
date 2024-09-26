'''This module hold chapter 8 exercises'''
# Author: Aravind Date: Thu, 19/9 2024
# 8-17
# 8-1
def display_message():
    '''This function will print a simple statement.'''
    print()
    print('In this I am going to learn about the python functions.')

display_message()

# 8-2
def favorite_book(title):
    '''This function will get and print the favorite book.'''
    print()
    print(f'One of my favorite books is {title.title()}.')

favorite_book('Python Crash Course E3')

# 8-3, 8-4
def make_shirt(size='large', msg='I love Python'):
    '''This function will accept the size and message and print it.'''
    print()
    print(f'The "{msg}" message will be printed in your {size.title()} size T-shirt.')

make_shirt()
make_shirt('Medium', 'Hello World!')
make_shirt(msg='You\'re a Programmer', size='Extra Large')

# 8-5
def describe_city(city, country='America'):
    '''This function will accept city and country and print it.'''
    print()
    print(f'{city.title()} is in {country.title()}')

describe_city('Indiana')
describe_city('Salem', 'india')
describe_city('tokyo', 'japan')

# 8-6
def city_country(city, country):
    '''This function accept city, country and return a string representation.'''
    print()
    return f"{city.title()}, {country.title()}"

one = city_country('Paris', 'France')
print(one)
two = city_country('Shanghai', 'china')
print(two)
three = city_country('Dubai', 'Emirates')
print(three)

# 8-7, 8-8
def make_album(name, title, no_of_songs=None):
    '''This function will return the dictionary of album'''
    print()
    album = {}
    album['artist'] = name.lower()
    album['title'] = title.lower()
    if no_of_songs:
        album['song count'] = no_of_songs
    return album

imagine_dragons = make_album('imagine dragons', 'evolve')
print(imagine_dragons)
whitney_houston = make_album('whitney houston', 'my love is your love', 13)
print(whitney_houston)
madonna = make_album('madonna', 'ray of light', 13)
print(madonna)

while True:
    print('\nPress "q" to quit the loop')
    name = input('Enter the artist name: ')
    if name == 'q':
        break
    album_title = input('Enter the album title: ')
    if album_title == 'q':
        break
    question = input('Do you want to add song count (y / n): ')
    if question == 'y':
        song_count = int(input(f'Enter the song count of {album_title.title()} album: '))
        album = make_album(name, album_title, song_count)
        print(album)
        continue
    album = make_album(name, album_title)
    print(album)

# 8-9
def show_messages(lists):
    print()
    '''This function will print every element in a given list'''
    for element in lists:
        print(element)

# 8-10, 8-11
def send_messages(lists: list, empty_list: list) -> None:
    '''This function will print and move elements from one list to another'''
    print()
    while lists:
        msg = lists.pop(0)
        print(f'{msg.title()}')
        empty_list.append(msg)

messages: list[str] = ['hello', 'hi', 'welcome', 'goodbye', 'bye', 'take care']
show_messages(messages)
sent_messages: list[str] = []
send_messages(messages[:], sent_messages)

print('Original List:')
print(messages)
print('Moved Message List:')
print(sent_messages)

# 8-12
def make_sandwich(*args):
    '''This function accept as many arguments and print it'''
    print()
    print('Here are the items that you wanted for your sandwich:')
    for item in args:
        print(f'- {item.title()}')
    
make_sandwich('tomato', 'fried chicken', 'pickle', 'olives')
make_sandwich('veggie patty', 'tomato', 'pickle', 'coconut', 'chocolate')
make_sandwich('veggie patty', 'oregano')

# 8-13
def build_profile(first, last, **user_info):
    '''This function build and return dictionary of user detail'''
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

about_me = build_profile('aravind', 'ray', age=25, degree='b.e ece',location='earth')
print(about_me)

# 8-14
def make_car(manufacturer: str, model: str, **cars) -> dict:
    '''This function will accept arbitrary kwargs and return dictionary'''
    cars['manufacturer'] = manufacturer
    cars['model'] = model
    return cars

my_car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(my_car)
