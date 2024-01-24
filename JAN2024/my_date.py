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
            currentYear = [31, 29, 31, 30,  31, 30, 31, 31,  30, 31,  30, 31]
        else:
            currentYear = [31, 28, 31, 30,  31, 30, 31, 31,  30, 31,  30, 31]

        if (day > 0 and day <= currentYear[self.month - 1]):
            return day
        else:
            print('Invalid value for day')
            sys.exit()

    def add_day(self,day):
        '''Add new day into class object'''
        self.day = self.checkDay(day)

    def add_month(self,month):
        '''Add new month into class object'''
        if month > 0 and month <= 12:
            self.month = month
        else:
            print('Invalid value for month')
            sys.exit()

    def add_year(self,year):
        '''Add new year in the class object'''
        if year > 1900:
            self.year = year
        else:
            print('Invalid value for year. Year should be greater than 1900')
            sys.exit()

    def weekdays(self):
        '''To return the week day like Monday to Sunday with respect to given date'''
        pass

    def diff_dates(self):
        '''To find difference between two dates in terms of the years, months, and days.'''
        pass

    def future_date(self, fdays = 0, fweeks = 0, fmonths = 0, fyears = 0):
        '''To find a future date after a given number of days, weeks, months and years.'''

        nday = self.day
        nmonth = self.month
        nyear = self.year

        if fdays >= 1:

            for i in range(1,fdays+1):
        
                if nyear % 400 == 0 or (nyear % 4 == 0 and nyear % 100 != 0):
                    month_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                else:
                    month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                
                nday += 1

                if nday > month_days[nmonth]:
                    nmonth += 1
                    nday = 1
                    if nmonth > 12:
                        nmonth = 1
                        nyear += 1
                        nday = 1

        if fweeks >= 1:

            fweeks = fweeks * 7
            
            for i in range(1,fweeks+1):
        
                if nyear % 400 == 0 or (nyear % 4 == 0 and nyear % 100 != 0):
                    month_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                else:
                    month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                
                nday += 1

                if nday > month_days[nmonth]:
                    nmonth += 1
                    nday = 1
                    if nmonth > 12:
                        nmonth = 1
                        nyear += 1
                        nday = 1

        if fmonths >= 1:

            for i in range(1,fmonths+1):
                nmonth += 1

                if nmonth > 12:
                    nyear += 1
                    nmonth = 1

        if fyears >= 1:
             
            nyear += fyears

        if nday <= 9:
            nday = '0' + str(nday)
        if nmonth <= 9:
            nmonth = '0' + str(nmonth)

        print(f'{nday}-{nmonth}-{nyear}')

    def past_date(self, fdays = 0, fweeks = 0, fmonths = 0, fyears = 0):
        '''To find a date in the past before a give number of days, weeks, months and years.'''
        pass

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
