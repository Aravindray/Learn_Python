day = 17
month = 12
year = 2003

addFuture = 500

nday = day
nmonth = month
nyear = year

for i in range(1,addFuture+1):

    month += 1

    if month > 12:
        year += 1
        month = 1

print(day, month, year)
