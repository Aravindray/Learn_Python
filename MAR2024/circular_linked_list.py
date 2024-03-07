'''This module is for circular linked list'''
from node import Node

class CircularLinkedList:
    '''This class hold the node with circular connections'''
    def __init__(self):
        '''Object constructed with empty head'''
        self.last = None

    def insert_begin(self, value):
        '''New element will be inserted in beginning of the list'''
        if self.last is None:
            self.last = Node(value)
            print('Value inserted in beginning of the list')
        else:
            temp = Node(value)
            if self.last.next is None:
                temp.next = self.last
                self.last.next = temp
                print('Value inserted in beginning of the list')
            else:
                temp.next = self.last.next
                self.last.next = temp
                print('Value inserted in beginning of the list')


    def insert_end(self, value):
        '''New element will be inserted in end of the list'''
        if self.last is None:
            self.last = Node(value)
            print('Value inserted in end of the list')
        else:
            temp = Node(value)
            if self.last.next is None:
                self.last.next = temp
                temp.next = self.last
                self.last = temp
                print('Value inserted in end of the list')
            else:
                temp.next = self.last.next
                self.last.next = temp
                self.last = temp
                print('Value inserted in end of the list')

    def delete_begin(self):
        '''First element from the list will be deleted'''
        if self.last is None:
            print('List underflow!')
            return None
        elif self.last.next is None:
            value = self.last.data
            self.last = None
            print(f'First element {value} of the list is deleted.')
            return value
        else:
            value = None
            temp = self.last.next
            if temp.next == self.last:
                value = temp.data
                self.last.next = None
                del temp
                print(f'First element {value} from the list is deleted.')
                return value
            self.last.next = temp.next
            value = temp.data
            del temp
            print(f'First element {value} from the list is deleted.')
            return value

    def delete_end(self):
        '''Last element from the list will be deleted'''
        if self.last is None:
            print('list underflow')
            return None
        elif self.last.next is None:
            value = self.last.data
            self.last = None
            print(f'Last element {value} from the list is deleted.')
            return value
        else:
            current = self.last.next
            previous = None
            if current.next == self.last:
                temp = self.last
                value = temp.data
                current.next = None
                del temp
                self.last = current
                print(f'Last element {value} from the list is deleted')
                return value
            else:
                while current != self.last:
                    previous = current
                    current = current.next
                previous.next = self.last.next
                value = current.data
                del current
                self.last = previous
                print(f'Last element {value} from the list is deleted.')
                return value

    def delete_value(self, value):
        '''If the given value available in the list, first occurrence will be deleted else return None'''
        if self.last is None:
            print('List underflow')
            return None
        elif self.last.next is None:
            if value == self.last.data:
                result = self.last.data
                self.last = None
                print(f'{result} from the list is deleted')
                return result
            print('Value is not in the list')
            return None
        else:
            current = self.last.next
            if value == current.data:
                if current.next == self.last:
                    self.last.next = None
                    result = current.data
                    del current
                    print(f'{result} from the list is deleted')
                    return result
                self.last.next = current.next
                result = current.data
                del current
                print(f'{result} from the list is deleted')
                return result
            previous = None
            while current.data != value:
                previous = current
                current = current.next
            if current == self.last:
                result = self.delete_end()
                # previous.next = None
                # self.last = previous
                # value = current.data
                # del current
                print(f'{value} from the list is deleted')
                return value
            previous.next = current.next
            value = current.data
            del current
            print(f'{value} from the list is deleted')
            return value

    def __str__(self):
        '''String representation of circular linked list will be printed a→b→c'''
        result = str()
        if self.last is None:
            return 'List is empty'
        elif self.last.next is None:
            return str(self.last.data)
        else:
            head = self.last.next
            while head != self.last:
                result += str(head.data) + '→'
                head = head.next
            result += str(head.data)
            return result
