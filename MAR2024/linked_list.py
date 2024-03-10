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

    def insert_end(self, value):
        '''This method insert the element in last of the linked list'''
        if self.head is None:
            self.head = Node(value)
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(value)

    def delete_end(self):
        '''Delete last element in the linked list'''
        if self.head is None:
            print('Linked list if underflow')
            return None
        current = self.head
        previous = None
        while current.next is not None:
            previous = current
            current = current.next
        value = current.data
        previous.next = None
        del current
        print(f'last value {value} is deleted')
        return value

    def find_value(self, node_number):
        '''This method find the number by given node number position'''
        if self.head is None:
            print('linked list is empty')
            return None
        elif node_number == 1:
            value = self.head.data
            print(f'value found in the given node {node_number} is {value}')
            return value
        current = self.head
        for _ in range(1, node_number):
            current = current.next
        value = current.data
        print(f'value found in the given node {node_number} is {value}')
        return value

    def reverse(self):
        '''This method reverse the linked list'''
        data_lst = list()
        current = self.head
        while current.next is not None:
            data_lst.append(current.data)
            current = current.next
        data_lst.append(current.data)
        self.head = None
        for data in data_lst:
            self.insert_begin(data)

    def reverse_display(self):
        '''Just display the reverse order of linked list'''
        data_lst = list()
        current = self.head
        while current.next is not None:
            data_lst.append(current.data)
            current = current.next
        data_lst.append(current.data)
        data_lst.reverse()
        result = str()
        for i in range(len(data_lst)-1):
            result += str(data_lst[i]) + '→'
        result += str(data_lst[-1])
        print(result)

    def divide_list(self):
        '''divide the linked list into odd and even'''
        even_tuple = list()
        odd_tuple = list()
        data_lst = list()
        current = self.head
        while current.next is not None:
            data_lst.append(current.data)
            current = current.next
        data_lst.append(current.data)
        for i, data in enumerate(data_lst):
            if i % 2 == 0:
                even_tuple.append(data)
            else:
                odd_tuple.append(data)
        return tuple(even_tuple), tuple(odd_tuple)

    def __iter__(self):
        '''Iterate through linked list'''
        current = self.head
        while current is not None:
            yield current
            current = current.next
        

    def __str__(self):
        '''This method returns the string representation of linked list a→b→c'''
        result = str()
        current = self.head
        while current.next is not None:
            result += str(current.data) + '→'
            current = current.next
        result += str(current.data)
        return result
