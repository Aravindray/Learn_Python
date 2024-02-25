# Chapter 12 - List Manipulation
import time

class Sorting:
    '''In this class I have implemented selection sort, bubble sort and Insertion sort technique'''
    def __init__(self,lst):
        '''This is class constructor with lst as list data type '''
        self.lst = lst

    def selection_sort(self):
        '''Selection Sorting'''
        length_of_lst = len(self.lst)
        for i in range(length_of_lst):
            mid_index = i
            for j in range(i,length_of_lst-1):
                if self.lst[mid_index] > self.lst[j+1]:
                    mid_index = j+1
            self.lst[i], self.lst[mid_index] = self.lst[mid_index], self.lst[i]

    def bubble_sort(self):
        '''Bubble Sorting from descending order'''
        length_of_lst = len(self.lst)
        for i in range(length_of_lst):
            swap = False
            for j in range(length_of_lst-1,i,-1):
                if self.lst[j] < self.lst[j-1]:
                    swap = True
                    self.lst[j], self.lst[j-1] = self.lst[j-1], self.lst[j]
            if swap == False:
                break

    def insertion_sort(self):
        '''insertion sorting'''
        length_of_lst = len(self.lst)
        for i in range(1,length_of_lst):
            temp = self.lst[i]
            j = i - 1
            while j >= 0 and self.lst[j] > temp:
                self.lst[j + 1] = self.lst[j]
                j = j - 1
            self.lst[j+1] = temp

    def __str__(self):
        '''This will return the lst'''
        return f'{self.lst}'
