import Calculator

def GCD():
    print('You have selected GCD')
    print('Enter as many digits as you want if you done enter the digits just click "Enter Key" to show the answer')
    initial = 1
    arrayOfDigits = []
    arrayOfDivisor = []
    arrayOfDuplicates = []
    dicOfDuplicate = {}
    while True:
        print('Enter the digit',initial,end=' ')
        val = input(': ')
        if val == '':
            break
        else:
            arrayOfDigits.append(int(val))
        initial += 1
    for digits in arrayOfDigits:
        for i in range(1,digits+1):
            val = digits % i
            if val == 0:
                arrayOfDivisor.append(i)
    for divisor in arrayOfDivisor:
        if arrayOfDivisor.count(divisor) > 1:
            arrayOfDuplicates.append(divisor)
            dicOfDuplicate[divisor] = arrayOfDivisor.count(divisor)
    result = max([k for k, v in dicOfDuplicate.items() if v == max(dicOfDuplicate.values())])
    print('GCD of given numbers is',result)

def LCM():
    print('You have selected LCM')
    print('Enter as many digits as you want if you done enter the digits just click "Enter Key" to show the answer')
    arrayOfDigits = []
    emptyArray = []
    while True:
        UI = input('Enter the number: ')
        if UI == '':
            break
        else:
            arrayOfDigits.append(int(UI))
    for digit in arrayOfDigits:
        for i in range(1,(max(arrayOfDigits)*2)):
            emptyArray.append(i * digit)
    for i in emptyArray:
        if emptyArray.count(i) >= len(arrayOfDigits):
            print('LCM of given numbers is',i)
            break

def main(NoS):
    if NoS == '1':
        GCD()
    elif NoS == '2':
        LCM()
    else:
        print('Invalid Input')
        doYouWantToContinue = input('Do you want to Continue? Type "Y"(es) to continue or anything to quit: ')
        if doYouWantToContinue == 'Y' or doYouWantToContinue == 'y':
            Calculator.main()
        else:
            print('Thanks for coming these far!')

if __name__ == '__main__':
    main()