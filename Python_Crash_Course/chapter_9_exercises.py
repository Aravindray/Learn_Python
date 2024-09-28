'''Python Crash Course - Exercise 9 - Try it Yourself'''
# Author: Aravind Date: Thu, 26/9 2024
import random
from restaurant import Restaurant

# 9-2, 9-5
class User:
    '''Stores about a user'''
    login_attempt = 0

    def __init__(self, first_name: str,
                 last_name: str,
                 email: str,
                 dob: str) -> None:
        '''Class Constructor'''
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.dob = dob

    def describe_user(self):
        '''Describe about the user'''
        print(f"\nName: {self.first_name.title()} {self.last_name.title()}"
              f"\nEmail: {self.email}\nDOB: {self.dob}")

    def greet_user(self):
        '''Greet user with Hello'''
        print(f'Hello {self.first_name.title()} {self.last_name.title()}!')

    def increment_login_attempt(self):
        '''Increase the class attribute by 1'''
        self.login_attempt += 1

    def reset_login_attempt(self):
        '''Reset the login attempt to 0'''
        self.login_attempt = 0

u1 = User('aravind', 'ray', 'admin@admin.com', '23-12-2004')
u2 = User('rock', 'star', 'rock@admin.com', '18-04-2010')
u3 = User('daniel', '', 'nothing@nothing.admin', '06-08-2005')

u1.describe_user()
u1.greet_user()

u2.describe_user()
u2.greet_user()

u3.describe_user()
u3.greet_user()

print(u1.login_attempt)
u1.increment_login_attempt()
u1.increment_login_attempt()
u1.increment_login_attempt()
print(u1.login_attempt)
u1.reset_login_attempt()
print(u1.login_attempt)

# 9-8
class Privilege:
    '''Will store about privilege'''
    privileges = ['can add post', 'can delete post', 'can ban user', 'can create channel', 'can delete server']

    def show_privileges(self):
        '''will display all privileges'''
        print('Admin Privileges:')
        for privilege in self.privileges:
            print(f'- {privilege}')

# 9-7, 9-8
class Admin(User):
    '''An extended version of user for admin'''
    privileges = Privilege()

a1 = Admin('Aravind', 'ray', 'admin@admin.com', '16-05-1999')
a1.describe_user()
a1.privileges.show_privileges()

# 9-9 Check electric_car.py file

# 9-10

restaurant4 = Restaurant('Erato', 'Greek')
restaurant4.describe_restaurant()

# 9-11, 9-12 - Skipped

# 9-13
class Die:
    '''An digital Die'''
    sides = 6

    def roll_die(self):
        '''Print a random number between 1 to no of sides die has'''
        print('Die landed in:')
        print(f'{random.randint(1, self.sides)}')

d1 = Die()
for _ in range(1,11):
    d1.roll_die()

print()
d2 = Die()
d2.sides = 10
for _ in range(1,11):
    d2.roll_die()

print()
d3 = Die()
d3.sides = 20
for _ in range(1,11):
    d3.roll_die()

# 9-14

numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
letters = ('a', 'b', 'c', 'd', 'e')
lottery_number = '5648'
lottery_letters = 'acdb'

generated_lottery_numbers = ''.join(random.sample(numbers, k=4))

if generated_lottery_numbers == lottery_number:
    print('You won the lottery')
else:
    print(f'Your number {generated_lottery_numbers} didn\'t match the lottery {lottery_number}')

generated_lottery_letters = ''.join(random.sample(letters, k=4))

if generated_lottery_letters == lottery_letters:
    print('You won the lottery')
else:
    print(f'Your number {generated_lottery_letters} didn\'t match the lottery {lottery_letters}')

# 9-15
letter_counter = 0
while True:
    generated_lottery_letters = ''.join(random.sample(letters, k=4))
    letter_counter += 1
    if generated_lottery_letters == lottery_letters:
        print('You\'re letter matches! You have won the lottery price!')
        break

print(f'You won "1" in {letter_counter} attempt')

number_counter = 0
while True:
    generated_lottery_numbers = ''.join(random.sample(numbers, k=4))
    number_counter += 1
    if generated_lottery_numbers == lottery_number:
        print('You\'re number matches! You have won the lottery price!')
        break

print(f'You won "1" in {number_counter} attempt')
