'''
Step 1: Fist store the employee object in the list
Step 2: Sort the list using the bubble, insertion and selection sort algorithm
'''
from FEB2024.employee import Employee

object_list = list()

def file_list(file_name):
    '''This function will store the employee object in the list'''
    with open('employee_data.txt','r') as file:
        line = file.readline()
        while line != '':
            name, salary = line.split(',')
            emp = Employee(name,None,None,salary,None)
            object_list.append(emp)
            line = file.readline()

print(object_list)
