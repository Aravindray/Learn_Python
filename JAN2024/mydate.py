import sys
class MyDate:
    '''A simplest implement of date as a class'''

    def __init__(self, day = 1, month = 1, year = 2000):
        '''
        Objective: To initialize data members of object MyDate
        Input Parameters:
            self (implicit parameter) - object of type MyDate 
            day, month, year - int
        Return Value:
            None
        '''
        if not(isinstance(day,int) and isinstance(month,int) and isinstance(year,int)):
            print('Invalid data provided for date')
            sys.exit()
        
        if month > 0 and month <= 12:
            self.month = month
        else:
            print('Invalid value for month')
            sys.exit()
        
        if year > 1900:
            self.year = year
        else:
            print('Invalid value for year. Year should be greater than 1900')
            sys.exit()
        
        self.day = self.checkDay(day)

    def checkDay(self, day):
        '''
        Objective: To validate date component
        Input parameters:
            self(implicit parameter) - object of type MyDate
            day - int
        Return value:
            If validate True return day else return error message
        '''
        if self.year % 400 == 0 or (self.year % 100 != 0 and self.year % 4 == 0):
            currentYear = [31, 29, 31, 30,  31, 30,  31, 31,  30, 31,  30, 31]
        else:
            currentYear = [31, 28, 31, 30,  31, 30,  31, 31,  30, 31,  30, 31]

        if (day > 0 and day <= currentYear[self.month - 1]):
            return day
        else:
            print('Invalid value for day')
            sys.exit()

    def __str__(self):
        '''
        Objective: To return string representation of object
        Input parameter:
            self (implicit parameter) - Object of type MyDate
        Return value:
            string
        '''

        # Approach: use dd-mm-yyyy format

        if self.day <= 9:
            day = '0' + str(self.day)
        else:
            day = str(self.day)
        
        if self.month <= 9:
            month = '0' + str(self.month)
        else:
            month = str(self.month)
        
        return f'{day}-{month}-{str(self.year)}'
    
def main():
    today = MyDate(3,9,2004)
    print(today)
    defaultDate = MyDate()
    print(defaultDate)

if __name__ == '__main__':
    main()