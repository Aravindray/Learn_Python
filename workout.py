from FEB2024.own_stack import Stack

user_input = input('Enter the palindrome: ')

len_of_ui = len(user_input)

stk = Stack(len_of_ui)

for ui in user_input:
    stk.push(ui)

string = str()

for i in range(len_of_ui):
    value = stk.pop()
    string += value

if user_input == string:
    print(f'Given string {user_input} is "palindrome"')
else:
    print(f'Given string {user_input} is "not palindrome"')
