'''Chapter 11 Exercise'''
# Author: Aravind Date: Wed 02/10 2024

# 11-3
class Employee:
    '''
    Objective: To store first and last name of employee
    and salary details
    '''

    def __init__(self, first: str, last: str, annual_salary: int) -> None:
        '''Class constructor'''
        self.first_name = first
        self.last_name = last
        self.annual_salary = annual_salary

    def give_rise(self, raise_amount = 5000) -> None:
        '''Will rise employee salary'''
        self.annual_salary += raise_amount
