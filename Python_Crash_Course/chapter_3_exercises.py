# Author: Aravind Date: Mon, 09/9 2024

#3-1
print()
names = ['Aravind', 'Raj', 'Ray', 'Python']
print(names[0].title())
print(names[1].title())
print(names[2].title())
print(names[3].title())

#3-2
print()
print(f"Hey {names[0].title()}, How are you?")
print(f"Hey {names[1].title()}, How are you?")
print(f"Hey {names[2].title()}, How are you?")
print(f"Hey {names[3].title()}, How are you?")

#3-3
print()
fav_trans = ['Motorcycle', 'Car', 'Boat', 'Airplane', 'Bus', 'Train']
print(f'I would like to own a Honda {fav_trans[0].lower()}.')
print(f'I would like to own a BMW {fav_trans[1].lower()}.')
print(f'I would like to own a Boston Whaler {fav_trans[2].lower()}.')
print(f'I would like to own a Boeing {fav_trans[3].lower()}.')
print(f'I would like to own a Volkswagen {fav_trans[4].lower()}.')
print(f'I would like to own a Lionel {fav_trans[5].lower()}.')

#3-4
print()
guests = ['Dad', 'Mom', 'Sister']
print(f'Hey! Hello {guests[0]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[1]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[2]}, I would like to invite you for next week friday dinner to my house')

#3-5
print()
old_guest = 'Sister'
new_guest = 'Nephew-1'
guests.remove(old_guest)
print(f"Hello {guests[0]}, It's a shame that {old_guest} won't make it as per plan, so I am inviting {new_guest}.")
print(f"Hello {guests[1]}, It's a shame that {old_guest} won't make it as per plan, so I am inviting {new_guest}.")
guests.append(new_guest)
print(f'Hey! Hello {guests[0]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[1]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[2]}, I would like to invite you for next week friday dinner to my house')

#3-6
print()
print(f'Hey! Hello {guests[0]}, I would like to let you know that I have found new bigger table for 6 people')
print(f'Hey! Hello {guests[1]}, I would like to let you know that I have found new bigger table for 6 people')
print(f'Hey! Hello {guests[2]}, I would like to let you know that I have found new bigger table for 6 people')
guests.insert(0, 'Ray')
guests.insert(3, 'Uncle')
guests.append('Nephew-2')
print(f'Hey! Hello {guests[0]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[1]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[2]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[3]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[4]}, I would like to invite you for next week friday dinner to my house')
print(f'Hey! Hello {guests[5]}, I would like to invite you for next week friday dinner to my house')

#3-7
print()
sry_1 = guests.pop()
print(f"Hey {sry_1}, I am so sorry, Just now I received the message that new table will not delivered as per schedule again soo sorry, Now I have only 2 extra seats, so again sorry to cancel the dinner party.")
sry_2 = guests.pop()
print(f"Hey {sry_2}, I am so sorry, Just now I received the message that new table will not delivered as per schedule again soo sorry, Now I have only 2 extra seats, so again sorry to cancel the dinner party.")
sry_3 = guests.pop()
print(f"Hey {sry_3}, I am so sorry, Just now I received the message that new table will not delivered as per schedule again soo sorry, Now I have only 2 extra seats, so again sorry to cancel the dinner party.")
sry_4 = guests.pop(0)
print(f"Hey {sry_4}, I am so sorry, Just now I received the message that new table will not delivered as per schedule again soo sorry, Now I have only 2 extra seats, so again sorry to cancel the dinner party.")
print(f"Hey {guests[0]}, I have a update that new table won't be arrived at time so I am only going to invite you and {guests[1]} only, so don't forgot to visit next friday")
print(f"Hey {guests[1]}, I have a update that new table won't be arrived at time so I am only going to invite you and {guests[0]} only, so don't forgot to visit next friday")

del guests[0]
del guests[0]

print('Empty guests')
print(guests)

#3-8
print()
locations = ['USA', 'Japan', 'Christmas Island', 'Italy', 'Spain', 'Turkey', 'Caribbean']
print(locations)
print(sorted(locations))
print(locations)
print(sorted(locations, reverse=True))
print(locations)
locations.reverse()
print(locations)
locations.reverse()
print(locations)
locations.sort()
print(locations)
locations.sort(reverse=True)
print(locations)

#3-9
print()
new_guests = ['Dad', 'Mom', 'Sister', 'Uncle', 'Nephews']
print(f"Total {len(new_guests)} guests are invited")

#3-10
print()
rivers = ['Jordan', 'Euphrates', 'Tigris', 'Nile', 'Jabbok', 'Missouri']
print(f'Total rivers are - {len(rivers)}')
print(f'Rivers in ascending order {sorted(rivers)}')
print(f'Rivers in descending order {sorted(rivers)}')
print("Let's add new river at the end of list")
rivers.append('Thames')
print(f"Now the total length of rivers are - {len(rivers)}")
print("Let's insert a new river in middle of the list")
rivers.insert(3, 'Murray')
print(f'{rivers} and it\'s total length now are - {len(rivers)}')
print('Let\'s delete on using pop()')
deleted = rivers.pop()
print(f"deleted river is {deleted}")
print(f'Now rivers are {rivers}')
print('Now delete one river using del statement')
del rivers[3]
print(f"Rivers after deleted {rivers}")
print('Let\'s reverse the list appearance')
rivers.reverse()
print(f'reversed rivers {rivers}')
print("Let's sort the rivers ascending using sort()")
rivers.sort()
print(rivers)
print("Let's sort the rivers descending using sort()")
rivers.sort(reverse=True)
print(rivers)
print("Let's delete one using pop(index)")
new_deleted = rivers.pop(2)
print(f'"{new_deleted} river" is now deleted')
print(rivers)
# append, modify, remove, accessing one
print('Let\'s add new river at the end')
rivers.append('Orinoco')
print(rivers)
print('Let\'s modify the last one')
rivers[-1] = 'Saint Lawrence'
print(rivers)
remove_this = 'Saint Lawrence'
print('Let\'s remove this river')
rivers.remove(remove_this)
print(rivers)
print(f'{rivers[1]} river is located in northeastern africa.')

#3-11 (Intentional Error)
hall_things = ['TV', 'Sofa', 'Table', 'AC', 'Photos']
print(hall_things[5])
