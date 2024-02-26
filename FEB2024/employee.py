'''This is the derived class of person'''
import sys
sys.path.append('d:\\Github\\Python\\JAN2024')
from my_calendar import Calendar
from person import Person


class Employee(Person):
    '''The class attributes are next_id and employee_count'''
    next_id = 1001
    employee_count = 0

    @staticmethod
    def inc_next_id():
        '''This method will increase the employee id whenever new employee is created'''
        Employee.next_id += 1
    
    @staticmethod
    def inc_employee_count():
        '''This will keep track of employee count'''
        Employee.employee_count += 1

    @staticmethod
    def dec_employee_count():
        '''This will decrease the employee count whenever the object or instance of class has deleted'''
        Employee.employee_count -= 1
    
    def __init__(self,name,dob,address,basic_salary,date_of_joining):
        '''The new object attributes are basic_salary and date_of_joining'''
        Person.__init__(self,name,dob,address)
        self.employee_id = Employee.next_id
        self.basic_salary = basic_salary
        self.date_of_joining = date_of_joining
        Employee.inc_next_id()
        Employee.inc_employee_count()

    def get_id(self):
        '''This will return the employee id'''
        return self.employee_id
    
    def get_salary(self):
        '''This will return employee current salary'''
        return self.basic_salary
    
    def get_date_of_joining(self):
        '''This will return date of joining of an employee'''
        return self.date_of_joining
    
    def revised_salary(self,new_salary):
        '''This will be employee new salary'''
        self.basic_salary = new_salary

    def __lt__(self, other):
        '''This will compare employees id and return True or False'''
        if isinstance(other, Employee):
            return self.get_id() < other.get_id()
        else:
            print('Both must be same data type')
            sys.exit()

    def __str__(self):
        '''This will print'''
        return f'{Person.__str__(self)}\nEmployee ID: {self.get_id()}\nEmployee Salary: {self.get_salary()}\nEmployee Joining date: {self.get_date_of_joining()}\n'
    
    def __del__(self):
        '''This will delete the employee count when user execute del method'''
        Person.__del__(self)
        Employee.dec_employee_count()
