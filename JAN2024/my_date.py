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
    
    def get_day(self):
        '''This function return the day of an object'''
        return self.day

    def get_month(self):
        '''This function return the month of an object'''
        return self.month

    def get_year(self):
        '''This function return the year of an object'''
        return self.year

    def weekdays(self):
        '''To return the week day like Monday to Sunday with respect to given date'''
        last_two_digit = str(self.year)
        last_two_digit = last_two_digit[2] + last_two_digit[3]
        last_two_digit = int(last_two_digit)

        Quarter = last_two_digit // 4

        month_table = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

        cal = self.day + month_table[self.month -1] + last_two_digit + Quarter

        if self.year >= 2000 and self.year <= 2099:
            cal -= 1


        final_remainder = cal % 7


        if final_remainder == 1:
            print('Sunday')
        elif final_remainder == 2:
            print('Monday')
        elif final_remainder == 3:
            print('Tuesday')
        elif final_remainder == 4:
            print('Wednesday')
        elif final_remainder == 5:
            print('Thursday')
        elif final_remainder == 6:
            print('Friday')
        elif final_remainder == 0:
            print('Saturday')
        else:
            print('Something is wrong')

    def __sub__(self, other):
        '''To find difference between two dates in terms of the years, months, and days.'''
        print('self',self)
        print('other',other)
        max_date = []
        min_date = []
        if isinstance(other, MyDate):
            if self.year >= other.year:
                if self.month >= other.month:
                    if self.day > other.day:
                        max_date = [self.day,self.month,self.year]
                        min_date = [other.day,other.month,other.year]
                    else:
                        max_date = [self.day,self.month,self.year]
                        min_date = [other.day,other.month,other.year]
                else:
                        max_date = [self.day,self.month,self.year]
                        min_date = [other.day,other.month,other.year]        
            else:
                min_date = [self.day,self.month,self.year]
                max_date = [other.day,other.month,other.year]

            def leap_year(lyear):
                if lyear % 400 == 0 or (lyear % 4 == 0 and lyear %100 != 0):
                    return [31, 29, 31, 30,  31, 30, 31, 31,  30, 31,  30, 31]
                else:
                    return [31, 28, 31, 30,  31, 30, 31, 31,  30, 31,  30, 31]

            print('Max Date',max_date)
            print('Min Date',min_date)

            rday = rmonth = ryear = 0

            while True:

                rday = max_date[0] - min_date[0]

                if rday > 0:
                    rmonth = max_date[1] - min_date[1]
                    if rmonth < 0:
                        max_date[2] -= 1
                        max_date[1] += 12
                    else:
                        ryear = max_date[2] - min_date[2]
                        break
                else:
                    leapYear = leap_year(max_date[2])
                    max_date[0] += leapYear[max_date[1] - 2]
                    max_date[1] -= 1
                    if max_date[0] < 1:
                        max_date[2] -= 1
                        max_date[1] += 12

            rweek = rday // 7

            print(f'difference of two dates is {ryear} years, {rmonth} months, {rweek} weeks or ({rday} days)')
        else:
            print('Invalid dates')
            sys.exit()

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
    
        new_day = self.day
        new_month = self.month
        new_year = self.year
        fweeks = fweeks * 7

        if fdays >= 1:

            for i in range(1,fdays+1):
        
                if new_year % 400 == 0 or (new_year % 4 == 0 and new_year % 100 != 0):
                    month_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                else:
                    month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

                new_day -= 1

                if new_day < 1:
                    new_month -= 1
                    if new_month < 1:
                        new_year -= 1
                        new_month = 12
                    new_day = month_days[new_month]

        if fweeks >= 1:

            for i in range(1,fweeks+1):
        
                if new_year % 400 == 0 or (new_year % 4 == 0 and new_year % 100 != 0):
                    month_days = {1:31, 2:29, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
                else:
                    month_days = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

                new_day -= 1

                if new_day < 1:
                    new_month -= 1
                    if new_month < 1:
                        new_year -= 1
                        new_month = 12
                    new_day = month_days[new_month]

        if fmonths >= 1:

            for i in range(1,fmonths+1):
                new_month -= 1
                if new_month < 1:
                    new_year -= 1
                    new_month = 12

        if fyears >= 1:

            new_year -= fyears

        if new_day <= 9:
            new_day = '0' + str(new_day)

        if new_month <= 9:
            new_month = '0' + str(new_month)

        print(f'{new_day}-{new_month}-{new_year}')

    def __eq__(self, other):
        '''This method will check'''
        if isinstance(other, MyDate):
            return (self.day == other.day and self.month == other.month and self.year == other.year)
        else:
            print('Can only perform if both are same data type')
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
