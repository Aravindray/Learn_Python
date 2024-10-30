'''Main module to create and store bank users'''

import json
from accounts import Account

# ToDo - Need to create a new user and populate it to members.json
# ToDo - Need to delete an existing user from the members.json

o_joe = Account('Joe', 1000, 'JoesPassword')
o_joe.get_details('JoesPassword')
remaining_balance = o_joe.withdraw(50, 'JoesPassword')
print(f'Your remaining balance is - {remaining_balance}')
