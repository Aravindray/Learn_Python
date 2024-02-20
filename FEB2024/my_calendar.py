# This is test my knowledge to create a new calendar based on previous module that I created as my_date (JAN2024) and my_time (FEB2024)

# for adding days I used days to years but recommended method is add years to days (smaller unit to higher unit - I used).
# for subtracting days I used days to years which is the recommended method (smaller unit to higher unit - I used).


'''This is the module for calendar'''
import sys

class Calendar:
    '''This class comprise day, month, year, hour, minute and second'''
    def __init__(self,day=1,month=1,year=2024,hour=0,minute=0,second=0):
        '''This is a class constructor'''
        if month >= 1 and month <= 12:
            self.month = month
        else:
            print('Enter month is invalid it should be between 1 to 12')
            sys.exit()
        if year >= 1000 and year<= 9999:
            self.year = year
        else:
            print('Entered year is invalid accept range between 1000 to 9999')
            sys.exit()
        if day >= 1 and day <= self.check_year(self.year,self.month):
            self.day = day
        else:
            print('Entered day is invalid!\n1. Check whether the day within the range of 1 to 29/30/31 respective to provided month\n2.Or you may entered 30 days in non leap year in february month')
            sys.exit()
        if hour >= 0 and hour <= 23:
            self.hour = hour
        else:
            print('Hours should be range of 0 to 23')
            sys.exit()
        if minute >= 0 and minute <= 59:
            self.minute = minute
        else:
            print('Minute should be range of 1 to 59')
            sys.exit()
        if second >= 0 and second <= 59:
            self.second = second
        else:
            print('Second should be range of 1 to 59')
            sys.exit()

    def check_year(self,new_year=None,new_month=None):
        '''This will check whether the given year is leap year or not and return respective days available in the month'''
        if new_year % 400 == 0 or (new_year % 4 == 0 and new_year % 100 != 0):
            months_days = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            return months_days[new_month]
        else:
            months_days = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
            return months_days[new_month]
        
    def get_day(self):
        '''This will return day of an object'''
        return f'Day: {self.day}'
    
    def get_month(self):
        '''This will return month of an object'''
        return f'month: {self.month}'
    
    def get_year(self):
        '''This will return year of an object'''
        return f'year: {self.year}'
    
    def get_hour(self):
        '''This will return hour of an object'''
        return f'hour: {self.hour}'
    
    def get_minute(self):
        '''This will return minute of an object'''
        return f'minute: {self.minute}'
    
    def get_second(self):
        '''This will return second of an object'''
        return f'second: {self.second}'
    
    def __sub__(self,other):
        '''This will sub 2 dates and return new date possibly with decreased day/month/year/hour/minute/seconds'''
        day_counter = 0
        seconds_counter = 0
        day_checker = True
        day_diff = 0
        month_checker = True
        month_diff = 0
        if isinstance(other,Calendar):
            if self.__lt__(other):
                min_date = Calendar(self.day,self.month,self.year,self.hour,self.minute,self.second)
                max_date = Calendar(other.day,other.month,other.year,other.hour,other.minute,other.second)
            else:
                max_date = Calendar(self.day,self.month,self.year,self.hour,self.minute,self.second)
                min_date = Calendar(other.day,other.month,other.year,other.hour,other.minute,other.second)

            while True:

                if min_date.day == max_date.day and min_date.month == max_date.month and min_date.year == max_date.year:
                    break

                min_date.day += 1
                day_counter += 1
                if min_date.day > min_date.check_year(min_date.year,min_date.month):
                    min_date.month += 1
                    if min_date.month > 12:
                        min_date.year += 1
                        min_date.month = 1
                    min_date.day = 1
                
                if day_checker:
                    if min_date.day == max_date.day:
                        day_diff = day_counter
                        day_checker = False

                if month_checker:
                    if min_date.month == max_date.month and min_date.day == max_date.day:
                        month_diff = day_counter
                        month_checker = False
                    
            while True:
                if min_date.second == max_date.second and min_date.minute == max_date.minute and min_date.hour == max_date.hour:
                    break

                min_date.second += 1
                seconds_counter += 1
                if min_date.second > 59:
                    min_date.minute += 1
                    if min_date.minute > 59:
                        min_date.hour += 1
                        min_date.minute = 0
                    min_date.second = 0
            
            result_year = day_counter // 365
            result_month = month_diff // 30
            result_day = day_diff
            result_hour = seconds_counter // 3600
            result_minute = (seconds_counter - result_hour * 3600) // 60
            result_second = seconds_counter - result_hour * 3600 - result_minute * 60
            
            return f'Total difference is {result_year} year {result_month} month {result_day} days (or total {day_counter} days) {result_hour} hours {result_minute} minute {result_second} second'
        else:
            print('Both must be same data type')
            sys.exit()

    def __eq__(self,other):
        '''This will compare the equality of 2 dates and return True or False'''
        if isinstance(other,Calendar):
            if self.year == other.year and self.month == other.month and self.day == other.day:
                return True
            return False
        else:
            print('To perform both must be same data type or same object')
            sys.exit()

    def __ne__(self,other):
        '''This class will compare the not equality of 2 dates and return True if both are not equal else return False'''
        if isinstance(other,Calendar):
            if self.year != other.year and self.month != other.month and self.day != other.day:
                return True
            return False
        else:
            print('To perform both must be same data type or same object')
            sys.exit()

    def __lt__(self,other):
        '''This will compare 2 dates and return True or False'''
        if isinstance(other,Calendar):
            if self.year < other.year:
                return True
            elif self.year == other.year and self.month < other.month:
                return True
            elif self.year == other.year and self.month == other.month and self.day < other.day:
                return True
            elif self.year == other.year and self.month == other.month and self.day == other.day and self.hour < other.hour:
                return True
            elif self.year == other.year and self.month == other.month and self.day == other.day and self.hour == other.hour and self.minute < other.minute:
                return True
            elif self.year == other.year and self.month == other.month and self.day == other.day and self.hour == other.hour and self.minute == other.minute and self.second < other.second:
                return True
            else:
                return False
        else:
            print('Only able to sort if both are same data type or same object')
            sys.exit()
    

    def add(self,add_day=0,add_month=0,add_year=0,add_hour=0,add_minute=0,add_second=0):
        '''This will add the given parameter and return new date'''

        if add_day >= 1:
            for i in range(1,add_day+1):
                self.day += 1
                if self.day > self.check_year(self.year,self.month):
                    self.month += 1
                    if self.month > 12:
                        self.year += 1
                        self.month = 1
                    self.day = 1

        if add_month >= 1:
            for i in range(1,add_month+1):
                self.month += 1
                if self.month > 12:
                    self.year += 1
                    self.month = 1

        if add_year >= 1:
            self.year += add_year

        if add_second >= 1:
            for i in range(1,add_second+1):
                self.second += 1
                if self.second > 59:
                    self.minute += 1
                    if self.minute > 59:
                        self.hour += 1
                        if self.hour > 23:
                            self.day += 1
                            if self.day > self.check_year(self.year,self.month):
                                self.month += 1
                                if self.month > 12:
                                    self.year += 1
                                    self.month = 1
                                self.day = 1
                            self.hour = 0
                        self.minute = 0
                    self.second = 0

        if add_minute >= 1:
            for i in range(1,add_minute+1):
                self.minute += 1
                if self.minute > 59:
                    self.hour += 1
                    if self.hour > 23:
                        self.day += 1
                        if self.day > self.check_year(self.year,self.month):
                            self.month += 1
                            if self.month > 12:
                                self.year += 1
                                self.month = 1
                            self.day = 1
                        self.hour = 0
                    self.minute = 0

        if add_hour >= 1:
            for i in range(1,add_hour+1):
                self.hour += 1
                if self.hour > 23:
                    self.day += 1
                    if self.day > self.check_year(self.year,self.month):
                        self.month += 1
                        if self.month > 12:
                            self.year += 1
                            self.month = 1
                        self.day = 1
                    self.hour = 0

    def sub(self,sub_day=0,sub_month=0,sub_year=0,sub_hour=0,sub_minute=0,sub_second=0):
        '''This will subtract the given parameter and return new date'''
        if sub_day >= 1:
            for _ in range(1,sub_day+1):
                self.day -= 1
                if self.day < 1:
                    self.month -= 1
                    if self.month < 1:
                        self.year -= 1
                        self.month = 12
                    self.day = self.check_year(self.year,self.month)
        
        if sub_month >= 1:
            for _ in range(1,sub_month+1):
                self.month -= 1
                if self.month < 1:
                    self.year -= 1
                    self.month = 12

        if sub_year >= 1:
            self.year -= sub_year

        if sub_second >= 1:
            for _ in range(1,sub_second+1):
                self.second -= 1
                if self.second < 0:
                    self.minute -= 1
                    if self.minute < 0:
                        self.hour -= 1
                        if self.hour < 0:
                            self.day -= 1
                            if self.day < 1:
                                self.month -= 1
                                if self.month < 1:
                                    self.year -= 1
                                    self.month = 12
                                self.day = self.check_year(self.year,self.month)
                            self.hour = 23
                        self.minute = 59
                    self.second = 59
        
        if sub_minute >= 1:
            for _ in range(1,sub_minute+1):
                self.minute -= 1
                if self.minute < 0:
                    self.hour -= 1
                    if self.hour < 0:
                        self.day -= 1
                        if self.day < 1:
                            self.month -= 1
                            if self.month < 1:
                                self.year -= 1
                                self.month = 12
                            self.day = self.check_year(self.year,self.month)
                        self.hour = 23
                    self.minute = 59

        if sub_hour >= 1:
            for _ in range(1,sub_hour+1):
                self.hour -= 1
                if self.hour < 0:
                    self.day -= 1
                    if self.day < 1:
                        self.month -= 1
                        if self.month < 1:
                            self.year -= 1
                            self.month = 12
                        self.day = self.check_year(self.year,self.month)
                    self.hour = 23

    def set_day(self,new_day):
        '''This will update new day of an object'''
        if new_day >= 1 and new_day <= self.check_year(self.year,self.month):
            self.day = new_day
        else:
            print('Enter day is not valid')
            sys.exit()
    
    def set_month(self,new_month):
        '''This will update new month of an object'''
        if new_month >= 1 and new_month <= 12:
            if self.day >= 1 and self.day <= self.check_year(self.year,new_month):
                self.month = new_month
            else:
                print(f'There is no {self.day} days in the given month - {new_month}')
                sys.exit()
        else:
            print('Entered month is not in range')
            sys.exit()
    
    def set_year(self,new_year):
        '''This will update new year of an object'''
        if self.day >= 1 and self.day <= self.check_year(new_year,self.month):
            self.year = new_year
        else:
            print(f'Invalid year for given day and month {self.day} and {self.month}')
            sys.exit()

    def set_hour(self,new_hour):
        '''This will update new hour of an object'''
        if new_hour >= 0 and new_hour <= 23:
            self.hour = new_hour
        else:
            print('Entered hour is out of range')
            sys.exit()

    def set_minute(self,new_minute):
        '''This will update new minute of an object'''
        if new_minute >= 0 and new_minute <= 59:
            self.minute = new_minute
        else:
            print('Entered minute is out of range')
            sys.exit()
    
    def set_second(self,new_second):
        '''This will update new second of an object'''
        if new_second >= 0 and new_second <= 59:
            self.second = new_second
        else:
            print('Entered second is out of range')
            sys.exit()
    
    def __str__(self):
        '''This will print'''
        if self.day <= 9: day = '0' + str(self.day)
        else: day = self.day
        if self.month <= 9: month = '0' + str(self.month)
        else: month = self.month
        if self.year <= 9: year = '0' + str(self.year)
        else: year = self.year
        if self.hour <= 9: hour = '0' + str(self.hour)
        else: hour = self.hour
        if self.minute <= 9: minute = '0' + str(self.minute)
        else: minute = self.minute
        if self.second <= 9: second = '0' + str(self.second) 
        else: second = self.second
        return f'{day}/{month}/{year} {hour}:{minute}:{second}' # DD/MM/YYYY HH:MM:SS

dates = [Calendar(15,5,1999), Calendar(21,12,2015), Calendar(30,12,2015), Calendar(11,1,1888)]
dates.sort()
for date in dates:
    print(date)
