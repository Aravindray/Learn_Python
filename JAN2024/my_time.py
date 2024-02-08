class MyTime:
    '''This class is for track time'''
    def __init__(self,hours,minutes,seconds):
        '''This is the class constructor'''
        assert hours >= 0 and hours <= 23
        self.hours = hours
        assert minutes >= 0 and minutes <= 59
        self.minutes = minutes
        assert seconds >= 0 and seconds <= 59
        self.seconds = seconds
    
    def change_hours(self,hours):
        '''This will update new hours'''
        assert hours >= 0 and hours <= 23
        self.hours = hours
    
    def change_minutes(self,minutes):
        '''This will update new minutes'''
        assert minutes >= 0 and minutes <= 59
        self.minutes = minutes
    
    def change_seconds(self,seconds):
        '''This will update new seconds'''
        assert seconds >= 0 and seconds <= 59
        self.seconds = seconds

    def get_hours(self):
        '''This will return hours HH'''
        return self.hours
    
    def get_minutes(self):
        '''This will return minutes MM'''
        return self.minutes
    
    def get_seconds(self):
        '''This will return seconds SS'''
        return self.seconds
    
    def add_new(self,new_hours = 0, new_minutes = 0, new_seconds = 0)
        ns = self.seconds + new_seconds
        if ns > 59:
            carry_minutes = new_seconds / 60
    
    def __str__(self):
        '''This will return for print statement'''
        if self.hours <= 9:
            hours = '0' + str(self.hours)
        else:
            hours = self.hours
        if self.minutes <= 9:
            minutes = '0' + str(self.minutes)
        else:
            minutes = self.minutes
        if self.seconds <= 9:
            seconds = '0' + str(self.seconds)
        else:
            seconds = self.seconds

        return f'{hours}:{minutes}:{seconds}'
