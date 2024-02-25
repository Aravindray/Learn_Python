'''Is it possible to store the instance of a class in a list? Let's Explore'''
from students_twelve import Student
import pickle
import sys

class Section:
    '''This class store the object of another class and perform some basic list operation'''
    def __init__(self):
        '''Lets store the object of class student in the form of list, to do so let's initialize an empty list'''
        self.records = list()
   
    def file_import(self,source):
        '''Lets open the binary file of student object and store it in list'''
        self.records = list()
        with open(source,'rb') as file:
            try:
                while True:
                    student = pickle.load(file)
                    self.records.append(student)
            except EOFError:
                pass

    def lst_export(self,destination):
        '''This method export the list self records into a binary file and store it in destination'''
        with open(destination,'wb') as file:
            for student in self.records:
                pickle.dump(student, file)
   
    def linear_search(self,search,key):
        '''This method perform linear search if the list is not sorted'''
        if not (search == 'roll_number' or search == 'name' or search == 'mark'):
            print('Invalid a argument for sorting')
            sys.exit()
        for i, record in enumerate(self.records):
            if search == 'roll_number' and record.roll_number == key:
                return i
            elif search == 'name' and record.name == key:
                return i
            elif search == 'mark' and record.mark == key:
                return i
        return -1

    def insertion_sort(self,based_on):
        '''This method sort the list based on the given object attribute'''
        length_of_list = len(self.records)

        if based_on == 'roll_number':
            for i in range(1,length_of_list):
                temp = self.records[i]
                j = i - 1
                while j >= 0 and temp.roll_number < self.records[j].roll_number:
                    self.records[j+1] = self.records[j]
                    j = j - 1
                self.records[j+1] = temp
            print('sorted')

        elif based_on == 'name':
            for i in range(1,length_of_list):
                temp = self.records[i]
                j = i - 1
                while j >= 0 and temp.name < self.records[j].name:
                    self.records[j+1] = self.records[j]
                    j = j - 1
                self.records[j+1] = temp
            print('sorted')

        elif based_on == 'mark':
            for i in range(1,length_of_list):
                temp = self.records[i]
                j = i - 1
                while j >= 0 and temp.mark < self.records[j].mark:
                    self.records[j+1] = self.records[j]
                    j = j - 1
                self.records[j+1] = temp
            print('sorted')
        
        else:
            print('Invalid a argument for sorting')
            sys.exit()

    def is_sorted(self, based_on):
        '''This method will check whether the list is sorted or not based on the given type and return True or False'''
        if not (based_on == 'roll_number' or based_on == 'name' or based_on == 'mark'):
            print('Invalid a argument for sorting')
            sys.exit()
        length_of_list = len(self.records)
        for i in range(1,length_of_list):
            if based_on == 'roll_number' and self.records[i].roll_number < self.records[i-1].roll_number:
                return False
            elif based_on == 'name' and self.records[i].name < self.records[i-1].name:
                return False
            elif based_on == 'mark' and self.records[i].mark < self.records[i-1].mark:
                return False
        return True

    def binary_search(self,search,key):
        '''This method accept 2 arguments where search is for type of search and key is for what to search
        before binary search let's check whether the list is sorted or not'''
        # Binary Search
        self.insertion_sort(search)
        if search == 'roll_number':
            start = 0
            end = len(self.records) - 1
            while start <= end:
                mid = (start + end) // 2
                if key < self.records[mid].roll_number:
                    end = mid - 1
                elif key > self.records[mid].roll_number:
                    start = mid + 1
                elif key == self.records[mid].roll_number:
                    return mid
            return -1
        elif search == 'name':
            start = 0
            end = len(self.records) - 1
            while start <= end:
                mid = (start + end) // 2
                if key < self.records[mid].name:
                    end = mid - 1
                elif key > self.records[mid].name:
                    start = mid + 1
                elif key == self.records[mid].name:
                    return mid
            return -1
        elif search == 'mark':
            start = 0
            end = len(self.records) - 1
            while start <= end:
                mid = (start + end) // 2
                if key < self.records[mid].mark:
                    end = mid - 1
                elif key > self.records[mid].mark:
                    start = mid + 1
                elif key == self.records[mid].mark:
                    return mid
            return -1
        else:
            print('Invalid a argument for search')
            sys.exit()

    def __str__(self):
        '''This is how it will print'''
        empty_string = ''
        for student in self.records:
            empty_string += Student.__str__(student) + '\n'
        return empty_string
