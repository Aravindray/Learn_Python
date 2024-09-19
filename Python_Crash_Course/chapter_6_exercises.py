# Author: Aravind Date: Wed, 18/9

#6-1, 6-7
aravind = {
    'first_name': 'aravind',
    'last_name': 'ray',
    'age': 25,
    'city': 'salem',
}

rks1 = {
    'first_name': 'selva',
    'last_name': 'mani',
    'age': 18,
    'city': 'tiruppur',
}

rks2 = {
    'first_name': 'rock',
    'last_name': 'star',
    'age': 14,
    'city': 'tiruppur',
}

people = [aravind, rks1, rks2]

for person in people:
    full_name = f'{person['first_name'].title()} {person['last_name'].title()}'
    about_me = f'Hi, This is {full_name}. I am {person['age']} year old and I live in {person['city'].title()}.'
    print(about_me)

#6-2, #6-10
favorite_numbers = {
    'ellen': [23, 89, 32],
    'rose': [1, 4, 34, 879],
    'emma': [54, 34, 4679],
    'selene': [8, 6548, 546, 78],
    'sonia': [98],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite number:")
    for number in numbers:
        print(f"\t- {number}")

#6-3, 6-4
glossaries = {
    'list': 'Is a collection of mutable datatype.',
    'dictionary': 'Is a collection of key-value pairs.',
    'string': 'Is a collection of characters.',
    'tuple': 'Is a collection of immutable datatype.',
    'set': 'Is a collection of unique datatype and order doesn\'t matter.',
    'boolean': 'It\'s either True or False.',
    'logical operator': 'and, or, not are logical operators.',
    'function': 'Is a block of code.',
    'class': 'It\'s a blueprint of objects attribute and behavior.',
    'module': 'It is a file with ends with .py extension.',
}

for key, value in glossaries.items():
    print(f'\n{key.title()}:\n\t{value}')

#6-5
print()
rivers = {
    'nile': 'egypt',
    'mississippi': 'America',
    'thames': 'england',
    'murray': 'australia',
    'danube': 'hungary',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print()
for river in rivers:
    print(f'The {river.title()}')

print()
for country in set(rivers.values()):
    print(country.title())

#6-6
print()
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'rust',
 'phil': 'python',
}

employees = ['jen', 'aravind', 'sarah', 'emma', 'edward', 'danial', 'phil', 'ray']
poll_users = list(favorite_languages.keys())

for employee in employees:
    if employee in poll_users:
        print(f'Thanks for the response!, {employee.title()}')
    else:
        print(f'Dear {employee.title()}, You are invited to take the favorite language poll')

#6-8 ignored, because 6-7 and 6-8 are same

#6-9
favorite_places = {
    'aravind': ['america', 'england', 'australia'],
    'dani': ['india', 'singapore'],
    'berry': ['america', 'germany', 'russia'],
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places:")
    for place in places:
        print(f"\t-{place.title()}")

#6-11
cities = {
    'new york city': {
        'country': 'america',
        'population': 8_260_000,
        'fact': 'World Trade Center located in New York City.',
    },
    'san francisco': {
        'country': 'america',
        'population': 788_478,
        'fact': 'Golden Gate Bridge is most famous in San Francisco.',
    },
    'paris': {
        'country': 'france',
        'population': 1_276_701,
        'fact': 'Eiffel Tower is most famous tourist spot in Paris.',
    },
}

for city, information in cities.items():
    print(f"\n{city.title()}:")
    for key, value in information.items():
        if key == 'country':
            print(f"\t{key.title()} - {value.title()}")
        else:
            print(f"\t{key.title()} - {value}")
