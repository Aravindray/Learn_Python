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
    
    def add_new(self,new_hours = 0, new_minutes = 0, new_seconds = 0):
        assert not new_seconds < 0
        if new_seconds > 0:
            self.seconds += new_seconds
            if self.seconds > 59:
                carry_seconds = self.seconds % 60
                carry_minutes = self.seconds // 60
                self.minutes += carry_minutes
                if self.minutes > 59:
                    new_carry_minutes = self.minutes % 60
                    carry_hours = self.minutes // 60
                    self.hours += carry_hours
                    if self.hours > 23:
                        new_carry_hours = self.hours % 24
                        self.hours = new_carry_hours
                    self.minutes = new_carry_minutes
                self.seconds = carry_seconds
        assert not new_minutes < 0
        if new_minutes > 0:
            self.minutes += new_minutes
            if self.minutes > 59:
                carry_minutes = self.minutes % 60
                carry_hours = self.minutes // 60
                self.hours += carry_hours
                if self.hours > 59:
                    new_carry_hours = self.hours % 24
                    self.hours = new_carry_hours
                self.minutes = carry_minutes
        assert not new_hours < 0
        if new_hours > 0:
            self.hours += new_hours
            if self.hours > 23:
                carry_hours = self.hours % 24
                self.hours = carry_hours

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
