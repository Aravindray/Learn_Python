# This script is about Bank and Account
import sys

class Account:
    '''This class is perform basic interest calculation'''
    def __init__(self,name,account_number,account_type,amount_deposited):
        '''This is a class constructor with name, account_type - string
        account_number, amount_deposited - number'''
        self.name = name
        self.account_number = account_number
        self.account_type = account_type
        self.amount_deposited = amount_deposited
    
    def get_name(self):
        '''This will return account holder name'''
        return self.name
    
    def get_account_number(self):
        '''This will return account number'''
        return self.account_number
    
    def get_account_type(self):
        '''This will return account type'''
        return self.account_type
    
    def get_amount_deposited(self):
        '''This will return deposited amount'''
        return self.amount_deposited
    
    def set_name(self,new_name):
        '''This will return account holder name'''
        self.name = new_name
    
    def set_account_number(self,new_number):
        '''This will return account number'''
        self.account_number = new_number
    
    def set_account_type(self,new_type):
        '''This will return account type'''
        self.account_type = new_type
    
    def set_amount_deposited(self,new_amount):
        '''This will return deposited amount'''
        self.amount_deposited += new_amount

    def __str__(self):
        '''This will print'''
        return f'Name: {self.get_name()}\nAccount Number: {self.get_account_number()}\nAccount Type: {self.get_account_type()}\nAmount Deposited: {self.get_amount_deposited()}'
    
class Saving(Account):
    '''This class have minimum deposited amount as a class data attribute and property interest calculator as method'''
    minimum_deposit_amount = 2000
    def __init__(self,name,account_number,account_type,amount_deposited):
        '''This is a class constructor with minimum deposit amount'''
        if account_type == 'Saving' or account_type == 'saving':
            super().__init__(name,account_number,account_type,amount_deposited)
            self.minimum_deposit_amount = Saving.get_minimum_deposit_amount()
        else:
            print('Invalid account type!')
            sys.exit()

    @staticmethod
    def get_minimum_deposit_amount():
        '''This will return minium deposit amount'''
        return Saving.minimum_deposit_amount
    
    def property_interest(self):
        '''This method calculate interest'''
        principal_amount = float(input('Enter the principal amount: '))
        interest_rate = float(input('Enter the interest rate as %: '))
        duration = float(input('Enter the period as year: '))
        interest_amount = interest_rate / 100
        simple_interest = principal_amount * interest_amount * duration
        return simple_interest

    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nMinimum Deposit Amount for Savings Account is: {Saving.get_minimum_deposit_amount()}'

class Current(Account):
    '''This class have minimum deposited amount as a class data attribute'''
    minimum_deposit_amount = 10000
    def __init__(self,name,account_number,account_type,amount_deposited):
        '''This is a class constructor with minimum deposit amount'''
        if account_type == 'Current' or account_type == 'current':
            super().__init__(name,account_number,account_type,amount_deposited)
            self.minimum_deposit_amount = Current.get_minimum_deposit_amount()
        else:
            print('Invalid Account Type!')
            sys.exit()

    @staticmethod
    def get_minimum_deposit_amount():
        '''This method return the class attribute minimum deposit amount'''
        return Current.minimum_deposit_amount

    def __str__(self):
        '''This will print'''
        return f'{super().__str__()}\nMinimum Deposit Amount for Current Account is: {Current.get_minimum_deposit_amount()}'
