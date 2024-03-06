'''This module is for circular linked list'''
from node import DoubleNode

class CircularLinkedList:
    '''This class hold the node with circular connections'''
    def __init__(self):
        '''Object constructed with empty head'''
        self.head = None

    def insert_begin(self, value):
        '''New element will be inserted in beginning of the list'''

    def insert_end(self, value):
        '''New element will be inserted in end of the list'''

    def delete_begin(self):
        '''First element from the list will be deleted'''

    def delete_end(self):
        '''Last element from the list will be deleted'''

    def delete_value(self, value):
        '''If the given value available in the list, first occurrence will be deleted 
        else return None'''

    def __str__(self):
        '''String representation of circular linked list will be printed a→b→c'''
