import re
import datetime

def simple_interest(PA, Y, M, IR):
    SI_Result = 0
    if Y > 0:
        SI_Result += (PA * (Y*12) * IR) / 100
    if M > 0:
        SI_Result += (PA * M * IR) / 100
    return SI_Result

def compound_interest(PA, Y, M, IR):
    Total = PA
    monthsPerYear = 12
    for i in range(1, Y+1):
        CI_Result = (Total * monthsPerYear * IR) / 100
        Total += CI_Result
    if M > 0:
        Total += (Total * M * IR) / 100
    return Total

def pattern(startDate, endDate):
    # return True, New start and end date
    global newStartDate
    global newEndDate
    patternCheck = re.compile('^[0-9]{4}/[0-9]{2}/[0-9]{2}$')
    nSD = []
    nED = []
    if patternCheck.search(startDate) != None and patternCheck.search(endDate) != None:
        startDate = startDate.split('/')
        endDate = endDate.split('/')
        for i in range(0,3):
            nSD.append(int(startDate[i]))
            nED.append(int(endDate[i]))
        if (nSD[0] >= 1 and nSD[0] <= 9999) and (nED[0] >= 1 and nED[0] <= 9999) and (nED[1] >= 1 and nED[1] <= 12) and (nSD[1] >= 1 and nSD[1] <= 12) and (nSD[2] >= 1 and nSD[2] <= 31) and (nED[1] >= 1 and nED[1] <= 31):
            if nED[0] > nSD[0]:
                newStartDate = datetime.date(nSD[0], nSD[1], nSD[2])
                newEndDate = datetime.date(nED[0], nED[1], nED[2])
                return True
            elif nED[1] > nSD[1]:
                newStartDate = datetime.date(nSD[0], nSD[1], nSD[2])
                newEndDate = datetime.date(nED[0], nED[1], nED[2])
                return True
            elif nED[2] > nSD[2]:
                newStartDate = datetime.date(nSD[0], nSD[1], nSD[2])
                newEndDate = datetime.date(nED[0], nED[1], nED[2])
                return True
            else:
                print('end date must be greater then start date')
                return False
        else:
            return False
    else:
        return False


def days_diff(startDate, endDate):
    diff = endDate - startDate
    years = diff.days // 365
    months = (diff.days % 365) // 30
    return years, months


def Year_Month():
    selectType = int(input('Enter 1 for type year and month or \nEnter 2 for type start and end date: '))
    if selectType == 1:
        years = int(input('Enter the Year: '))
        months = int(input('Enter the months (if months are not applicable type 0): '))
        return years, months
    elif selectType == 2:
        startDate = input('Enter the start date as yyyy/mm/dd: ')
        endDate = input('Enter the end date as yyyy/mm/dd: ')
        patternCheck = pattern(startDate, endDate)
        if patternCheck == True:
            diff_year, diff_month = days_diff(newStartDate, newEndDate)
            return diff_year, diff_month
        else:
            print('Entered dates are not valid')
            Year_Month()
    else:
        print('You have to enter 1 or 2 only')
        Year_Month()
    
def interest_rate():
    selectType = int(input('Type 1 to enter the interest rate as amount or\nType 2 to enter the interest rate as percentage: '))
    if selectType == 1:
        interestAmount = float(input('Enter the interest rate as amount: '))
        return interestAmount
    elif selectType == 2:
        interestPercent = float(input('Enter the interest rate as percentage: '))
        return (interestPercent // 12)
    else: 
        print('You have to enter 1 or 2 only')
        interest_rate()

def main():
    newStartDate = ''
    newEndDate = ''
    principalAmount = float(input('Enter the principal amount: '))
    Year, Month = Year_Month()
    interestRate = interest_rate()
    selectInterest = int(input('Enter 1 to perform simple interest or\nEnter 2 to perform compound interest: '))
    if selectInterest == 1:
        SI = simple_interest(principalAmount, Year, Month, interestRate)
        print(f'Given principal amount is {principalAmount} and the simple interest is {SI} at the end of {Year} year you have to pay {principalAmount+SI}')
        print('End of the Program')
    elif selectInterest == 2: 
        CI = compound_interest(principalAmount, Year, Month, interestRate)
        print(f'Given principal amount is {principalAmount} and the compound interest is {CI} at the end of {Year} year you have to pay {principalAmount+CI}')
        print('End of the Program')
    else:
        print("Oops, You didn't enter the valid input!")
        print("End of the program")
    again = input('If you want you may start again enter Y/N: ')
    if again == 'Y':
        main()
    else:
        print('Thanks for using this interest calculator')

if __name__ == '__main__':
    main()
