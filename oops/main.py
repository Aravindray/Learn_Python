'''Main module to create and store bank users'''

import json
from pathlib import Path
from accounts import Account

# ToDo - Need to create a new user and populate it to members.json
# ToDo - Need to delete an existing user from the members.json

class Bank:
    '''Create a bank class which handel accounts class also know as composition'''
    def __init__(self) -> None:
        '''class instantiation'''
        path = Path('members.json')
        content = path.read_text(encoding='utf-8')
        if content:
            self.json_dict = json.loads(content)
        else:
            self.json_dict = {}
        self.members_dict = {}
        self.user_account_number = len(self.json_dict)

    def create_account(self, username, opening_balance, password):
        '''Create a new user account and store it in members class'''
        balance = int(opening_balance)
        o_account = Account(username, balance, password)
        self.members_dict[self.user_account_number] = o_account
        dict_serializer = {key: acc.to_dict() for key, acc in self.members_dict.items()}
        self.json_dict.update(dict_serializer)
        write_content = json.dumps(self.json_dict)
        path = Path('members.json')
        path.write_text(write_content, encoding='utf-8')
        print(f'Account Created for {username}')
        self.user_account_number += 1
        return f'{self.user_account_number-1}'

if __name__ == '__main__':
    o_bank = Bank()
    # account_num = o_bank.create_account('Joe', 100, "Joe'sPassword")
    # print(f'Joe\'s account number is {account_num}')

    # account_num = o_bank.create_account('Mary', 54321, "Mary'sPassword")
    # print(f'Mary\'s account number is {account_num}')

    # account_num = o_bank.create_account('Aravind', 100, "Aravind'sPassword")
    # print(f'Aravind\'s account number is {account_num}')

    # account_num = o_bank.create_account('Ray', 54321, "Ray'sPassword")
    # print(f'Ray\'s account number is {account_num}')

    account_num = o_bank.create_account('Raj', 54321, "Raj'sPassword")
    print(f'Raj\'s account number is {account_num}')
