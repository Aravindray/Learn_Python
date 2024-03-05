'''This module hold the linked list structure'''
from node import Node

class LinkedList:
    '''This class holds the node as a linked list'''
    def __init__(self):
        '''This method construct the linked list class with empty head parameter'''
        self.head = None

    def insert(self, value):
        '''Objective: To add the new value in the linked list in sorted manner'''
        if self.head is None:
            self.head = Node(value)
        elif value < self.head.data:
            temp = Node(value)
            temp.next = self.head
            self.head = temp
        else:
            current = self.head
            previous = None
            while value > current.data:
                if current.next is not None:
                    previous = current
                    current = current.next
                else:
                    temp = Node(value)
                    current.next = temp
                    return 'value added'
            another_temp = Node(value)
            another_temp.next = current
            previous.next = another_temp

    def delete(self, value):
        '''Objective: To remove the element from the linked list'''
        if self.head is None:
            print('Linked List is empty')
            return None
        elif value == self.head.data:
            temp = self.head
            out_value = self.head.data
            self.head = self.head.next
            del temp
            print(f'{out_value} is deleted from a linked list')
            return out_value
        else:
            current = self.head
            previous = None
            while value != current.data:
                previous = current
                current = current.next
            previous.next = current.next
            out_value = current.data
            del current
            print(f'{out_value} is deleted from a linked list')
            return out_value

    def insert_begin(self, value):
        '''Objective: To insert the value in the beginning of the liked list'''
        if self.head is None:
            self.head = Node(value)
        else:
            temp = Node(value)
            temp.next = self.head
            self.head = temp

    def delete_begin(self):
        '''Objective: Delete the first element/node in the linked list'''
        if self.head is None:
            print('Linked list is empty!!')
            return None
        temp = self.head
        value = self.head.data
        self.head = self.head.next
        del temp
        print('First element from the linked list is deleted!')
        return value

    def __str__(self):
        '''This method returns the string representation of linked list a→b→c'''
        result = str()
        current = self.head
        while current.next is not None:
            result += str(current.data) + '→'
            current = current.next
        result += str(current.data)
        return result
