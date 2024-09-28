'''This module will hold chapter 10 Try it yourself exercises'''
# Author: Aravind Date: Sat, 28/9 2024
from pathlib import Path
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
"""
# 10-6
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

# 10-7 Not descriptive so skipped
