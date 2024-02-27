'''This module comes under data structure and algorithms'''

class Stack:
    '''This is Last In First Out (LIFO) method'''
    def __init__(self):
        '''An empty list will initialized'''
        self.stk = list()

    def push(self, value):
        '''Push method add new element on the top of the stack'''
        self.stk.append(value)
    
    def is_empty(self):
        '''It return True if length is 0 and False otherwise'''
        return len(self.stk) == 0
    
    def pop(self):
        '''Pop method will delete the top value from the stack'''
        if not(self.is_empty()):
            return self.stk.pop()
        else:
            print('Stack underflow')
            return None
    
    def top(self):
        '''Top method fetch the top value from the stack'''
        return self.stk[-1]
    
    def __str__(self):
        '''A list will be printed with tab spaces'''
        empty_stk = ''
        for element in self.stk:
            empty_stk += str(element) + '\t'
        return empty_stk
