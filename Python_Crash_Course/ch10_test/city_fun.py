'''Exercise 11-1, 11-2'''
def display_city_status(city: str, country: str, population: int=None) -> str:
    '''Display city and It's country'''
    if population:
        formatted_text = f'{city}, {country} - Population {population}'
        return formatted_text.title()
    formatted_text = f'{city}, {country}'
    return formatted_text.title()
