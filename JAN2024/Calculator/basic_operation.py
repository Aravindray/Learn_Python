import Calculator
def Addition():
    print('You have selected addition operation\nEnter the number as much as you want to add or simply enter E to (E)xit')
    Result = 0
    while True:
        Operands = input('Enter the number: ')
        if Operands == 'E' or Operands == 'e' or Operands == '':
            break
        else:
            Result += float(Operands)
        print('Total:',Result)
def Subtraction():
    print('You have selected subtraction operation\nEnter the number as much as you want to subract or simply enter E to (E)xit')
    while True:
        Operand1 = input('Enter the first number: ')
        if Operand1 == 'E' or Operand1 == 'e' or Operand1 == '':
            break
        else:
            Operand2 = input('Enter the second number: ')
            if Operand2 == 'E' or Operand2 == 'e' or Operand2 == '':
                break
            else:
                Operand1 = float(Operand1)
                Operand2 = float(Operand2)
                Result = Operand1 - Operand2
        print('Total:',Result)
def Multiplication():
    print('You have selected Multiplication operation\nEnter the number as much as you want to multiplie or simply enter E to (E)xit')
    while True:
        Operand1 = input('Enter the first number: ')
        if Operand1 == 'E' or Operand1 == 'e' or Operand1 == '':
            break
        else:
            Operand2 = input('Enter the second number: ')
            if Operand2 == 'E' or Operand2 == 'e' or Operand2 == '':
                break
            else:
                Operand1 = float(Operand1)
                Operand2 = float(Operand2)
                Result = Operand1 * Operand2
        print('Total:',Result)
def Division():
    print('You have selected Division operation\nEnter the number as much as you want to Divide or simply enter E to (E)xit')
    while True:
        Operand1 = input('Enter the first number: ')
        if Operand1 == 'E' or Operand1 == 'e' or Operand1 == '':
            break
        else:
            Operand2 = input('Enter the second number: ')
            if Operand2 == 'E' or Operand2 == 'e' or Operand2 == '':
                break
            else:
                Operand1 = float(Operand1)
                Operand2 = float(Operand2)
                Result = Operand1 / Operand2
        print('Total:',Result)
def Interger_Division():
    print('You have selected Interger Division operation\nEnter the number as much as you want to Divide or simply enter E to (E)xit')
    while True:
        Operand1 = input('Enter the first number: ')
        if Operand1 == 'E' or Operand1 == 'e' or Operand1 == '':
            break
        else:
            Operand2 = input('Enter the second number: ')
            if Operand2 == 'E' or Operand2 == 'e' or Operand2 == '':
                break
            else:
                Operand1 = float(Operand1)
                Operand2 = float(Operand2)
                Result = Operand1 // Operand2
        print('Total:',Result)
def Square_root():
    print('You have selected Square Root operation\nEnter the number as much as you want to find the root or simply enter E to (E)xit')
    while True:
        Operand = input('Enter the number: ')
        if Operand == 'E' or Operand == 'e' or Operand == '':
            break
        else:
            Operand = float(Operand)
            Result = Operand ** (1 / 2)
        print('Total:',Result)
def Cube_root():
    print('You have selected Cube Root operation\nEnter the number as much as you want to find the root or simply enter E to (E)xit')
    while True:
        Operand = input('Enter the number: ')
        if Operand == 'E' or Operand == 'e' or Operand == '':
            break
        else:
            Operand = float(Operand)
            Result = Operand ** (1 / 3)
        print('Total:',Result)
def Remainder():
    print('You have selected Remainder Division operation\nEnter the number as much as you want to Divide or simply enter E to (E)xit')
    while True:
        Operand1 = input('Enter the first number: ')
        if Operand1 == 'E' or Operand1 == 'e' or Operand1 == '':
            break
        else:
            Operand2 = input('Enter the second number: ')
            if Operand2 == 'E' or Operand2 == 'e' or Operand2 == '':
                break
            else:
                Operand1 = float(Operand1)
                Operand2 = float(Operand2)
                Result = Operand1 % Operand2
        print('Total:',Result)
def Exponentitaion():
    print('You have selected Exponentitaion operation\nEnter the number as much as you want to find the power or simply enter E to (E)xit')
    while True:
        Operand1 = input('Enter the base number: ')
        if Operand1 == 'E' or Operand1 == 'e' or Operand1 == '':
            break
        else:
            Operand2 = input('Enter the power number: ')
            if Operand2 == 'E' or Operand2 == 'e' or Operand2 == '':
                break
            else:
                Operand1 = float(Operand1)
                Operand2 = float(Operand2)
                Result = Operand1 ** Operand2
        print('Total:',Result)
def main(NoS):
    if NoS == '1' or NoS == '+':
        Addition()
    elif NoS == '2' or NoS == '-':
        Subtraction()
    elif NoS == '3' or NoS == '*':
        Multiplication()
    elif NoS == '4' or NoS == '/':
        Division()
    elif NoS == '5' or NoS == '//':
        Interger_Division()
    elif NoS == '6' or NoS == '^2':
        Square_root()
    elif NoS == '7' or NoS == '^3':
        Cube_root()
    elif NoS == '8' or NoS == '%':
        Remainder()
    elif NoS == '9' or NoS == '**':
        Exponentitaion()
    else:
        print('Invalid Input')
        doYouWantToContinue = input('Do you want to Continue? Type "Y"(es) to continue or anything to quit: ')
        if doYouWantToContinue == 'Y' or doYouWantToContinue == 'y':
            Calculator.main()
        else:
            print('Thanks for coming these far!')
if __name__ == '__main__':
    main()