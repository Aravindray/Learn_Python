'''Queue in form of linked'''
from node import Node

class LinkedQueue:
    '''Linked Queue insert the new element in rear and delete the front element as FIFO'''
    def __init__(self):
        '''This method constructed Linked queue object as None'''
        self.front = self.rear = None

    def enqueue(self, value):
        '''Insert the new element in queue rear'''
        if self.rear is None:
            self.rear = Node(value)
            self.front = self.rear
        else:
            self.rear.next = Node(value)
            self.rear = self.rear.next

    def dequeue(self):
        '''Delete first element in the queue front'''
        if self.front is None:
            print('Queue underflow!')
            return None
        temp = self.front
        value = temp.data
        self.front = self.front.next
        del temp
        print(f'First element {value} is deleted')
        return value

    def __str__(self):
        '''string represent of queue front←rear-1←rear'''
        result = str()
        current = self.front
        while current.next is not None:
            result += str(current.data) + '←'
            current = current.next
        result += str(current.data)
        return result

lq = LinkedQueue()
lq.enqueue(12)
lq.enqueue(13)
lq.enqueue(14)
print(lq)
