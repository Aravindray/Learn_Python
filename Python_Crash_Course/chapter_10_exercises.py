'''This module will hold chapter 10 Try it yourself exercises'''
# Author: Aravind Date: Sat, 28/9 2024
from pathlib import Path
import json
"""
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

path = Path('reviews.txt')
contents = path.read_text(encoding='utf-8')
lines = contents.splitlines()
counter = 0
for line in lines:
    result = line.lower().count('the ')
    counter += result

print(f'The world "the" appears {counter} times.')
"""
# 10-11, 10-12

def store_fav_number(path: Path) -> None:
    '''Get favorite number of user and store it'''
    fav_num = int(input('Enter your favorite number? '))
    con_fav_num = json.dumps(fav_num)
    path.write_text(con_fav_num)
    print('Favorite number stored')

def get_fav_number(path: Path) -> int:
    '''Retrieve favorite number of user and return it'''
    con_fav_num = path.read_text()
    fav_num = json.loads(con_fav_num)
    return fav_num
