'''This module hold section class and it's methods'''
import pickle
from students_twelve import Student

class Section:
    '''This section class can perform list manipulation operation which are students class objects'''
    def __init__(self):
        '''Objective: This class initialize the empty list of the object'''
        self.records = list()
    
    def read_list(self, source):
        '''This method reads the source file of students object and store it in class section object list'''
        self.records = list()
        f1 = open(source, 'rb')
        try:
            while True:
                student = pickle.load(f1)
                self.records.append(student)
        except EOFError:
            pass
        f1.close()

    def write_list(self, destination):
        '''This method will write the result of class section object into text file'''
        f = open(destination, 'wb')
        for student in self.records:
            pickle.dump(student)
        f.close()

    def insert_end(self,roll_no,name,mark):
        '''This method insert the new student object into list record if it not already present in the list'''
        student = Student(roll_no,name,mark)
        if student.roll_number not in [i.roll_number for i in self.records]:
            self.records.append(student)
            return 'record inserted successfully'
        return 'Student record already exists'
    
    def is_sorted(self):
        '''This method check whether the given list is ascending order based on the roll number'''
        for i in range(1,len(self.records)):
            if self.records[i].roll_number < self.records[i-1].roll_number:
                return False
        return True
    
    def binary_search(self, key):
        '''This is the binary search method based on the given key as of now user suppose to enter the key as roll number'''
        if not(self.is_sorted()):
            print('List is not sorted')
            return False
        start = 0
        end = len(self.records)-1
        while start <= end:
            mid = (start + end) // 2
            if key < self.records[mid].roll_number:
                end = mid -1
            elif key > self.records[mid].roll_number:
                start = mid + 1
            elif key == self.records[mid].roll_number:
                return True
        return False
    
    def liner_search(self, key):
        '''This method will helpful if the list is not shorted'''
        for student in self.records:
            if student.roll_number == key:
                return True
        return False
    
    def insertion_sort(self):
        '''As of now this method will sort the list based on the roll number'''
        length_lst = len(self.records)
        for i in range(1,length_lst):
            temp = self.records[i]
            j = i - 1
            while j >= 0 and temp.roll_number < self.records[j].roll_number:
                self.records[j+1] = self.records[j]
                j = i - 1
            self.records[j+1] = temp
        
    def sorted_insert(self,roll_no,name,mark):
        '''This method will add the new object in the list record on ascending order'''
        pass

    def delete(self, roll_no):
        '''This will delete the entry from a list record'''
        for i, r in enumerate(self.records):
            if r.roll_number == roll_no:
                del self.records[i]
                return 'Entry deleted'
        return 'Roll Number not in the list'

    def __str__(self):
        '''This method print'''
        string = ''
        for record in self.records:
            string += Student().__str__(record)
        print(string)
