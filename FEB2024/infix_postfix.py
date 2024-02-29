'''This module convert infix expression to postfix expression basics'''

from stack import Stack
from postfix_evaluate import postfix_eval

# user_input = input('Enter the infix expression: ')

def infix_postfix(array):
    '''This function convert infix expression to postfix expression'''
    stk = Stack()
    postfix = ''
    precedence = {'+':1, '-':1, '*':2, '/':2}
    numbers = '0123456789'
    for arr in array:
        # print('for each iteration postfix',postfix)
        # print('for each iteration stk',stk)
        if arr == '(':
            stk.push(arr)
            # print('if (',stk)
        elif arr in numbers:
            postfix += arr
        elif arr in precedence:
            top = stk.top()
            if stk.is_empty():
                stk.push(arr)
                # print('while empty',stk)
            elif top == '(':
                stk.push(arr)
                # print('if top is (',stk)
            elif precedence[arr] > precedence[top]:
                stk.push(arr)
                # print('while precedence:',stk)
            else:
                while top != '(' and not(stk.is_empty()) and precedence[arr] <= precedence[top]:
                    value = stk.pop()
                    postfix += value
                    top = stk.top()
                stk.push(arr)
        elif arr == ')':
            # print('if arr is )')
            top = stk.top()
            while top != '(':
                # print('if ) top is',top)
                value = stk.pop()
                # print('if )',value)
                postfix += value
                # print('if )',postfix)
                top = stk.top()
            # print('before stk pop:',stk)
            stk.pop()
            # print('after stk pop:',stk)
    while not(stk.is_empty()):
        value_out = stk.pop()
        postfix += value_out
    return postfix

# result = infix_postfix(user_input)
# print('conversion of infix to postfix',result)

# infix_result = eval(user_input)
# print('Given infix expression result:',infix_result)
# postfix_result = postfix_eval(result)
# print('Converted postfix expression result:',postfix_result)
