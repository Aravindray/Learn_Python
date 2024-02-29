'''This module is queue from data structure I'''

class Queue:
    '''Queue class have enqueue and dequeue methods'''
    def __init__(self):
        '''This method initialize the empty list'''
        self.que = list()
    
    def enqueue(self, value):
        '''This method insert new value in rare'''
        self.que.append(value)
    
    def is_empty(self):
        '''Return True if list is empty or False otherwise'''
        return len(self.que) == 0

    def dequeue(self):
        '''FIFO structure will remove first/front element from a queue'''
        if not(self.is_empty()):
            return self.que.pop(0)
        else:
            print('Underflow!! Queue is empty')
            return None
        
    def front(self):
        '''This method fetch first/front value from a queue'''
        if not(self.is_empty()):
            return self.que[0]
        else:
            print('Queue is empty')
            return None
    
    def size(self):
        '''Return the length of the queue'''
        if not(self.is_empty()):
            return len(self.que)
        else:
            print('Queue is empty')
            return None

    def __str__(self):
        '''This will represent each element from queue'''
        string = str()
        for element in self.que:
            string += element + ' '
        return string
