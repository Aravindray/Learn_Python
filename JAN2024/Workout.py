import sys

class Student:
    '''This class is to store students academic record and give percentage and division of a student'''

    def __init__(self, rollNum, name, stream, mark_list = None):
        '''This is the contractor of the object'''
        self.rollNum = rollNum
        self.name = name
        self.markList = mark_list
        if stream is 'C':
            self.stream = 'Commerce'
        elif stream is 'A':
            self.stream = 'Arts'
        elif stream is 'S':
            self.stream = 'Science'
        else:
            print('Allowed streams are A: Arts, C: Commerce, S: Science')
            sys.exit()
        self.percentage = self.percent()
        self.grades = self.grade_gen()
        self.division = self.divi()
        
    def set_marks(self):
        '''Get the marks for 5 subject from the user and return it as a list'''
        self.markList = []
        no_of_subject = int(input('Enter no of subjects that you want to enter the marks: '))
        assert no_of_subject > 0 and no_of_subject < 100
        for i in range(1,no_of_subject+1):
            enter_marks = float(input('Enter the mark of subject',i,': '))
            assert enter_marks > 0 and enter_marks <= 100
            self.markList.append(enter_marks)

    def get_stream(self):
        '''Display the student stream'''
        return self.stream

    def percent(self):
        '''Calculated the percentage of entered marks'''
        mrk_lst = self.markList
        percentage = (sum(mrk_lst) / len(mrk_lst)) * 100
        return percentage

    def grade_gen(self):
        '''Generate grades based on the entered marks by user'''
        grades = {}
        mrk_lst = self.markList
        for mrk in mrk_lst:
            if mrk >= 90:
                grades[mrk] = 'A'
            elif mrk < 90 and mrk >= 80:
                grades[mrk] = 'B'
            elif mrk < 80 and mrk >= 65:
                grades[mrk] = 'C'
            elif mrk < 65 and mrk >= 40:
                grades[mrk] = 'D'
            else:
                grades[mrk] = 'E'
        return grades

    def divi(self):
        '''Take the percentage and return the division'''
        percentage = self.percentage
        if percentage >= 60:
            return 'I'
        elif percentage < 60 and percentage >= 50:
            return 'II'
        elif percentage < 50 and percentage >= 35:
            return 'III'
        else:
            return 'Fail'

    def __str__(self):
        '''Return string representation of object'''
        return f'Name:{self.name}\nRoll Number:{self.rollNum}\nStream:{self.stream}\nMarks:{self.markList}\nAchieved Grades:{self.grades}\nAchieved Percentage:{self.percentage}\nAchieved Division:{self.division}'
