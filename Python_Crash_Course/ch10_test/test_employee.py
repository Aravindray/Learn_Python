'''Exercise 11-3'''
import pytest
from employee import Employee

@pytest.fixture
def employee():
    '''It create employee instance'''
    create_employee = Employee('Aravindraj', 'G', 500000)
    return create_employee

def test_give_default_raise(employee):
    '''Raise default amount to annual salary'''
    employee.give_rise()
    assert employee.annual_salary == 505000

def test_give_custom_raise(employee):
    '''Raise custom amount to annual salary'''
    employee.give_rise(100000)
    assert employee.annual_salary == 600000
