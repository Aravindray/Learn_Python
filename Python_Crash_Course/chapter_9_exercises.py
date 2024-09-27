'''Python Crash Course - Exercise 9 - Try it Yourself'''
# Author: Aravind Date: Thu, 26/9 2024

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
from restaurant import Restaurant

restaurant4 = Restaurant('Erato', 'Greek')
restaurant4.describe_restaurant()

# 9-11, 9-12 - Skipped
