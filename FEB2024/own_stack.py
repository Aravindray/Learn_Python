class Stack:

    def __init__(self, size):
        '''Objective: To initialize data members of object of type Stack
        Input Parameters:
            self (implicit parameter) - Object of type stack
            size - numeric (number of element in stack)
        Return Value: None'''
        self.stack_size = size
        self.values = [None for i in range(self.stack_size)]
        self.top = -1

    def is_full(self):
        '''Objective: To determine if the stack is full
        Input Parameter:
            self (implicit parameter) - Object of the type Stack
        Return Value: True if the stack is full else False'''
        return (self.top + 1) == self.stack_size
    
    def is_empty(self):
        '''Objective: To determine if the stack is empty
        Input Parameter:
            Self (Implicit Parameter) - Object of type stack
        Return Value: True if the stack is empty else False'''
        return self.top == -1
    
    def push(self, element):
        '''Objective: To put an element on top of the stack
        Input Parameter:
            self (implicit parameter) - Object of type stack
            element - value to be inserted
        Return Value: None'''
        if self.is_empty():
            self.values[0] = element
            self.inc_size()
        elif self.top + 1 < self.stack_size:
            self.values[self.top + 1] = element
            self.inc_size()
        else:
            print('Stack is overflow')

    def pop(self):
        '''Objective: To remove an element from the top of stack
        Input parameter:
            self (implicit parameter) - Object of type stack
        Return Value: Top element of the stack if stack is not empty else None'''
        if self.is_empty():
            print('Stack underflow')
            return None
        else:
            popped = self.top_element()
            self.values[self.top] = None
            self.top -= 1
            return popped


    def top_element(self):
        '''Objective: To return top element of the stack
        Input parameter:
            self (implicit parameter) - Object of type stack
        Return Value: top element of the stack if stack is not empty else None'''
        if self.is_empty():
            print('Stack is empty')
            return None
        else:
            return self.values[self.top]

    def inc_size(self):
        '''Once the element added it will increase the size by one'''
        self.top += 1

    def size(self):
        '''Objective: To return no of element in the stack
        Input Parameter:
            self (implicit parameter) - Object of type stack
        Return Value: number of elements in stack - numeric'''
        return self.top + 1

    def __str__(self):
        '''This will print'''
        string = str()
        for element in self.values:
            string += str(element) + ' '
        return string
    