'''This module is for doubly linked list'''
from node import DoubleNode

class DoublyLinkedList:
    '''This class hold the element with 2 way communication manner'''
    def __init__(self):
        '''This will constructed with empty list'''
        self.head = None
    
    def insert_begin(self, value):
        '''Insert the new element in the beginning of the list'''
        if self.head is None:
            self.head = DoubleNode(value)
            print('Value inserted at beginning')
        else:
            temp = DoubleNode(value)
            temp.next = self.head
            self.head.previous = temp
            self.head = temp
            print('Value inserted at beginning')

    def insert_end(self, value):
        '''Insert the new element in the end of the list'''
        if self.head is None:
            self.head = DoubleNode(value)
            print('Value inserted at end')
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            temp = DoubleNode(value)
            current.next = temp
            temp.previous = current
            print('Value inserted at end')
    
    def delete_begin(self):
        '''Delete the first element in the list'''
        if self.head is None:
            print('Doubly linked list is underflow!!')
            return None
        temp = self.head
        self.head = self.head.next
        value = temp.data
        del temp
        print(f'First value {value} is deleted from the list')
        return value

    def delete_end(self):
        '''Delete the last element in the list'''
        if self.head is None:
            print('Doubly linked list is underflow!!')
            return None
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next
        previous.next = None
        value = current.data
        del current
        print(f'Last value {value} is deleted from the list')
        return value
    
    def delete_value(self, value):
        '''Delete the given value from the linked list'''
        if self.head is None:
            print('List is empty')
            return None
        current = self.head
        previous = None
        while current.data != value:
            if current.next is not None:
                previous = current
                current = current.next
            else:
                print(f'Value {value} is not in the list')
                return None
        if current.next is None:
            previous.next = None
            value = current.data
            del current
            print(f'{value} deleted from the list')
            return value
        temp = current.next
        previous.next = temp
        temp.previous = previous
        value = current.data
        print(f'{value} deleted from the list')
        return value
    
    def __str__(self):
        '''String representation of doubly linked list Previous:Data:Next'''
        result = str()
        current = self.head
        while current.next is not None:
            result += str(current.data) + '→'
            current = current.next
        result += str(current.data)
        return result
