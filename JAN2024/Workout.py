day = 15
month = 5
year = 1999

print('Given date',day,'-',month,'-',year)

last_two_digit = str(year)
last_two_digit = last_two_digit[2] + last_two_digit[3]
last_two_digit = int(last_two_digit)

print('last two digit',last_two_digit)

Quarter = last_two_digit // 4

print('Quarter',Quarter)

some_table = [1, 4, 4, 0, 2, 5, 0, 3, 6, 1, 4, 6]

cal = day + some_table[month -1] + last_two_digit + Quarter

print(day,some_table[month -1],last_two_digit,Quarter)

print('cal',cal)

if year >= 2000 and year <= 2099:
    cal -= 1

print('cal',cal)

final_remainder = cal % 7

print('final remainder',final_remainder)

if final_remainder == 1:
    print('Sunday')
elif final_remainder == 2:
    print('Monday')
elif final_remainder == 3:
    print('Tuesday')
elif final_remainder == 4:
    print('Wednesday')
elif final_remainder == 5:
    print('Thursday')
elif final_remainder == 6:
    print('Friday')
elif final_remainder == 0:
    print('Saturday')
else:
    print('Something is wrong')
