#Calculator
import basic_operation
import geometry
import algebra
import life_mathematics
import convertor
import mensuration
import trigonometry

def main():
    Basic_Operation = ['1: Addition (+)', '2: Subtraction (-)', '3: Multiplication (*)', '4: Division (/)', '5: Floor Division or Integer Division (//)', '6: Square root (^2)', '7: Cube root (^3)', '8: Remainder (%)', '9: Exponentitaion (**)']
    Geometry = [['1 - Theorem:', 'a: Pythagoream Theorem', 'b: Angle Theorems', 'c: Triangle Theorems', 'd: Circle Theorems', 'e: Parallelogram Theorems']]
    Algebra = ['1: GCD', '2: LCM']
    Life_Mathematics = ['1: Percentage', '2: Profit & Loss', '3: Discount', '4: Overhead Expenses and GST', '5: Compound Interest', '6: Time and Work', '7: Attrition', '8: Shrinkage']
    Convertor = [['1 - Length:', 'a: Millimeter', 'b: Centimeter', 'c: Meter', 'd: Kilometer', 'e: Inch', 'f: Feet', 'g: Yards', 'h: Miles'], ['2 - Mass:', 'a: Milligram', 'b: Gram', 'c: Kilogram', 'd: Ounces', 'e: Pounds', 'f: Tons'], ['3 - Temperature:', 'a: Kelvin', 'b: Celsius', 'c: Fahrenheit'], ['4 - Time:', 'a: Seconds', 'b: Minutes', 'c: Hour', 'd: Days', 'e: Weeks', 'f: Months', 'g: Year', 'h: Decades', 'i: Silver jubilee', 'j: Golden jubilee', 'k: Centennial'], ['5 - Capacity / Volume:', 'a: Milliliter', 'b: Centilitre', 'c: Litre', 'd: Kilolitre', 'e: Ounces', 'f: Pint', 'g: Quarts', 'h: Gallons'], ['6 - Current:'], ['7 - Area', 'a: Square Inch', 'b: Square Feet', 'c: Acre', 'd: Square Yard', 'e: Square Mile']]
    Mensuration = [['1 - Find area of regular polygon:', 'a: Triangle', 'b: Square', 'c: Rectangle', 'd: Parallelogram', 'e: Trapezoid', 'f: Rhombus', 'g: Diamond', 'h: Pentagon', 'i: Hexagon', 'j: Heptagon', 'k: Octagon', 'l: Nonagon', 'm: Decagon'],['2 - Find perimeter of:'],['3 - Find the volume of:', 'a: Triangular Prism','b: Sphere', 'c: Rectangular Prism', 'd: Cube', 'e: Cylinder', 'f: Square Pyramid', 'g: Cone', 'h: Hemisphere', 'i: '], ['4 - Find the surface area of:','a: Triangular Prism']]
    Trigonometry = []
    choose = input('Select which operation do you want to perform from the given list:\n1. Basic Operation\n2. Geometry\n3. Algebra\n4. Life Math\n5. Convertors\n6. Mensuration\n7. Trigonometry\nEnter the operation name or number: ')
    if choose == '1' or choose == 'Basic Operation':
        print('You have selected Basic Operations under you can perform',len(Basic_Operation),'operations which are listed below')
        for operation in Basic_Operation:
            print(operation)
        chooseBasicOperation = input('Enter the operation number or symbol to strat the calculation: ')
        basic_operation.main(chooseBasicOperation)
    elif choose == '2' or choose == 'Geometry':
        print('You have selected Geometry Operations under you can perform',len(Geometry),'operations which are listed below')
        for operation in Geometry:
            for op in operation:
                print(op)
        chooseGeometryOperation = int(input('Enter the operation number: '))
        geometry.main(chooseGeometryOperation)
    elif choose == '3' or choose == 'Algebra':
        print('You have selected Algebra Operations under you can perform',len(Algebra),'operations which are listed below')
        for operation in Algebra:
            print(operation)
        chooseAlgebraOperation = input('Enter the operation number: ')
        algebra.main(chooseAlgebraOperation)
    elif choose == '4' or choose == 'Life Math':
        print('You have selected Life Math Operations under you can perform',len(Life_Mathematics),'operations which are listed below')
        for operation in Life_Mathematics:
            print(operation)
        chooseLifeMathematics = int(input('Enter the operation number: '))
        life_mathematics.main(chooseLifeMathematics)
    elif choose == '5' or choose == 'Convertors':
        print('You have selected Convertors Operations under you can perform',len(Convertor),'Operations which are listed below')
        for operation in Convertor:
            for ops in operation:
                print(ops)
        chooseConvertorOperation = int(input('Enter the operation number: '))
        convertor.main(chooseConvertorOperation)
    elif choose == '6' or choose == 'Mensuration':
        print('You have selected Mensuration Operations under you can perform',len(Mensuration),'operation which are listed below')
        for operation in Mensuration:
            for ops in operation:
                print(ops)
        chooseMensurationOperation = int(input('Enter the operation number: '))
        mensuration.main(chooseMensurationOperation)
    elif choose == '7' or choose == 'Trigonometry':
        print('You have selected Trigonometry Operations under you can perform',len(Trigonometry),'operation which are listed below')
        for operation in Trigonometry:
            print(operation)
        chooseTrigonometryOperation = int(input('Enter the operation number: '))
        trigonometry.main(chooseTrigonometryOperation)
    else:
        print('Invalid Input')
        doYouWantAgain = input('Enter "Y"(es) to continue or press anything to quit: ')
        if doYouWantAgain == 'Y' or doYouWantAgain == 'y':
            main()
        else:
            print('Thanks for using the calculator')

if __name__ == '__main__':
    main()