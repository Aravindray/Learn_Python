'''Author: Aravind Date: Tue 01/10 2024'''
from city_fun import display_city_status

def test_city_country():
    '''test city and country'''
    result = display_city_status('santiago', 'chile')
    assert result == 'Santiago, Chile'

def test_city_country_population():
    '''test city, country and population'''
    result = display_city_status('santiago', 'chile', 5000000)
    assert result == 'Santiago, Chile - Population 5000000'
