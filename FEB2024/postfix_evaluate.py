'''This module check the postfix expression and perform calculation'''
from stack import Stack

def postfix_eval(array):
    stk = Stack()
    operators = ['+', '-', '*', '/']
    for ui in array:
        if ui not in operators:
            stk.push(ui)
        elif ui in operators:
            operand2 = stk.pop()
            operand1 = stk.pop()
            result = str(eval(operand1 + ui + operand2))
            stk.push(result)
    return stk
