'''Exercise Module without using list append and pop method to make a queue'''

class Queue:
    '''Queue with out using append and pop methods'''
    def __init__(self, size):
        '''Objective: To initialize data members of a object of type queue
        Input Parameters:
            self (implicit parameter) - object of type queue
        Return Value: None'''
        self.qsize = size
        self.values = [None for i in range(self.qsize)]
        self.front, self.rear = -1, -1

    def enqueue(self, element):
        '''Objective: To insert an element at the rear end
        Input parameters:
            self (implicit parameter) - Object of type queue
            element - value to be inserted
        Return Value: None'''
        if self.is_full():
            print('Queue Overflow')
        else:
            if self.rear + 1 < self.qsize:
                self.values[self.rear+1] = element
                self.rear += 1
            self.front = 0

    def dequeue(self):
        '''Objective: To remove an element from the front of queue
        Input Parameter:
            self (implicit parameter) - Object of type queue
        return value: front element of the queue if queue is not empty else None'''
        if self.is_empty():
            print('Queue underflow')
            return None
        temp = self.values[self.front]
        for i in range(1, self.qsize):
            self.values[i-1] = self.values[i]
        self.rear -= 1
        self.values[-1] = None
        return temp

    def is_full(self):
        '''Objective: To determine whether the queue is full
        Input parameter:
            self (implicit parameter) - object of type queue
        Return Value: True if the queue is full else False'''
        return self.rear + 1 == self.qsize

    def is_empty(self):
        '''Objective: To determine whether the queue is empty
        Input parameter:
            self (implicit parameter) - Object of type queue
        Return Value: True if the queue is empty else False'''
        return self.rear == -1

    def front_element(self):
        '''Objective: To return element at the front of queue
        Input Parameter:
            self (implicit parameter) - Object of type queue
        Return Value: Front element of the queue if queue is not empty else None'''
        if self.is_empty():
            print('Queue is Empty')
            return None
        return self.values[self.front]

    def size(self):
        '''Objective: To return no of elements in the queue
        Input Parameter:
            self (implicit Parameter) - Object of type queue
        Return Value: Number of element is a queue - Numeric'''
        if self.is_empty():
            return 0
        return self.rear - self.front + 1

    def __str__(self):
        '''This will print'''
        string = str()
        for elements in self.values:
            string += str(elements) + ' '
        return string
