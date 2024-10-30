'''Blueprint for Bank account'''

class Account:
    '''Represent bank user account'''
    def __init__(self, username, amount, password):
        '''Instantiate an object with username, opening amount and password'''
        self.username = username
        self.amount = int(amount)
        self.password = password

    def deposit(self, deposit_amount, password):
        '''Deposit an amount to account balance'''
        if password != self.password:
            return None
        if deposit_amount < 0:
            print('You can\'t deposit negative number in your account')
            return None

        self.amount += deposit_amount
        return self.get_balance(password)

    def get_balance(self, password):
        '''Get and return users balance'''
        if password != self.password:
            return None

        return self.amount

    def withdraw(self, withdraw_amount, password):
        '''Withdraw an amount from users current balance'''
        if password != self.password:
            return None
        if withdraw_amount < 0:
            print("You can't withdraw an negative number")
            return None
        if withdraw_amount > self.amount:
            print("Insufficient balance")
            return None

        self.amount -= withdraw_amount
        print('Amount debited')
        return self.get_balance(password)

    def get_details(self, password):
        '''prints about users account details'''
        if password != self.password:
            print('Invalid password')
        else:
            print('****Your Details****')
            print(f'     Name: {self.username}')
            print(f'     Balance: {self.amount}')
            print(f'     Password: {self.password}')
            print()

    def to_dict(self):
        '''Represent the data into dict'''
        user = {
            'username': self.username,
            'balance': self.get_balance(self.password),
            'password': self.password
        }
        return user
