import Calculator

def main(NoS):
    if NoS == '1':
        print('You have selected Percentages')
    else:
        print('Invalid Input')
        doYouWantToContinue = input('Do you want to Continue? Type "Y"(es) to continue or anything to quit: ')
        if doYouWantToContinue == 'Y' or doYouWantToContinue == 'y':
            Calculator.main()
        else:
            print('Thanks for coming these far!')
if __name__ == '__main__':
    main()