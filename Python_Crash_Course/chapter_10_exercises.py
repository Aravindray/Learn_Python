'''This module will hold chapter 10 Try it yourself exercises'''
# Author: Aravind Date: Sat, 28/9 2024
from pathlib import Path
import json

# 10-1, 10-2
print('Using read_text()')
path = Path('learning_python.txt')
contents = path.read_text().rstrip()
print(contents)

print()
print('Using splitlines()')
lines = contents.splitlines()
for line in lines:
    line = line.replace('Python', 'JavaScript')
    print(line)

# 10-3
print()
for line in contents.splitlines():
    print(line)

# 10-4
print()
user_input = input('Enter you name: ')
path = Path('guest.txt')
path.write_text(user_input)

# 10-5
print()
names = ''
while True:
    user_input = input('Enter your name\nEnter "q" to quit: ')
    if user_input == 'q':
        break
    names += user_input + '\n'

path = Path('guest_book.txt')
path.write_text(names)

# 10-6, 10-7
print('Enter "q" for quit the program')
while True:
    first_number = input('Enter the first number: ')
    if first_number == 'q':
        break
    second_number = input('Enter the second number: ')
    if second_number == 'q':
        break
    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print('We can\'t convert string to integer, Make sure to enter the integer')
    else:
        print(answer)

# 10-8, 10-9
path = Path('cars.txt')
try:
    contents = path.read_text().rstrip()
except FileNotFoundError:
    print(f'Your file {path} not exists in the current directory')
else:
    print(contents)

bike_path = Path('bikes.txt')
try:
    contents = bike_path.read_text().rstrip()
except FileNotFoundError:
    pass
else:
    print(contents)

# 10-10
path = Path('reviews.txt')
contents = path.read_text(encoding='utf-8')
lines = contents.splitlines()
counter = 0
for line in lines:
    result = line.lower().count('the ')
    counter += result

print(f'The world "the" appears {counter} times.')

# 10-11, 10-12

def store_fav_number(path: Path) -> None:
    '''Get favorite number of user and store it'''
    fav_num = int(input('Enter your favorite number? '))
    con_fav_num = json.dumps(fav_num)
    path.write_text(con_fav_num)
    print('Favorite number stored')

def get_fav_number(path: Path) -> int:
    '''Retrieve favorite number of user and return it'''
    if path.exists():
        con_fav_num = path.read_text()
        fav_num = json.loads(con_fav_num)
        return fav_num
    else:
        return None

def display_fav_number(path: Path) -> None:
    '''If fav number available it displays it 
    or it will ask user to enter their fav number
    '''
    fav_num = get_fav_number(path)
    if fav_num:
        print(f'I know your favorite number! It\'s {fav_num}.')
    else:
        store_fav_number(path)

file_path = Path('fav_num.json')
display_fav_number(file_path)

# 10-13, 10-14

def get_stored_username(path: Path) -> str:
    '''Get stored username if available'''
    if path.exists():
        contents = path.read_text()
        user_detail = json.loads(contents)
        return user_detail
    return None

def get_new_username(path: Path) -> dict:
    '''Prompt for a new user'''
    user_detail = {}
    first_name = input('Enter your first name: ')
    last_name = input('Enter your last name: ')
    age = int(input('What is your age? '))
    username = input('Enter your username: ')
    user_detail['username'] = username
    user_detail['age'] = age
    user_detail['first_name'] = first_name
    user_detail['last_name'] = last_name
    contents = json.dumps(user_detail)
    path.write_text(contents)
    return contents

def greet_user() -> None:
    '''Greet user by name'''
    path = Path('user_details.json')
    user_detail = get_stored_username(path)
    if user_detail:
        message = f'Is this your username "{user_detail['username']}" - Y/N: '
        verify = input(message)
        if verify == 'Y':
            print(f'Welcome back {user_detail['first_name']} {user_detail['last_name']}!')
        else:
            user_detail = get_new_username(path)
    else:
        user_detail = get_new_username(path)
        print(f'We will remember you when you come back, {user_detail}!')

greet_user()
