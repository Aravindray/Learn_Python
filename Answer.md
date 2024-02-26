## Table of Content

- [January - 2024](#january---2024)
    - [Mutable and Immutable Objects](#mutable-and-immutable-objects)
    - [File and Exceptions](#file-and-exceptions)
    - [Calsses I](#calsses-i)
    - [Games](#games)
- [February - 2024](#february---2024)
    - [Calsses II](#calsses-ii)
    - [Sorting Methods](#sorting-methods)
    - [List Manipulation](#list-manipulation)

<br>

# January - 2024

### Mutable and Immutable Objects
<hr>

**Exercises**

Question 6:

```python
def e6(n):

    count = 1
    listOflist = [[] for i in range(n)]

    for i in range(len(listOflist)):
        for j in range(1,6):
            listOflist[i].append(count * j)
        count += 1

    print(listOflist)

if __name__ == '__main__':
    e6(5)
```
Question 7:

```python
def numToStr(n):

    number_nameDictionary = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
    n = str(n)
    result = []

    for num in n:
        result.append(number_nameDictionary[int(num)])

    for rel in result:
        print(rel,end=' ')

if __name__ == '__main__':
    numToStr(654166468716087467923)
```

### File and Exceptions
<hr>

**Exercises**

Question 1:

```python
def LetsRead(a,b):

    readA = open(a,'r')
    readB = open(b,'w')
    result = readA.readline()

    while result != '':
        readB.write(result)
        readB.write('\n')
        result = readA.readline()

    readA.close()
        readB.close()
        readB = open(b,'r')
        print(readB.read())
        readB.close()

def main():    
    file1 = input('Enter the file 1 name: ')
    file2 = input('Enter the file 2 name: ')
    LetsRead(file1,file2)

if __name__ == '__main__':
    main()
```

Question 2:

```python
def Words_Vowels(a):

    readFile = open(a,'r')
    readLine = readFile.readline()
    wordCount = 0
    letterList = []
    vowels = list('aeiou')
    vowelsCount = {}

    while readLine != '':
        readList = readLine.split(' ')
        wordCount += len(readList)
        readLine = readFile.readline()

    readFile.close()
    readFile = open(a,'r')
    readLine = readFile.read()

    for st in readLine:
        letterList.append(st)
    readFile.close()

    for vowel in vowels:
        vowelsCount[vowel] = letterList.count(vowel)
    print('No of words present in the',a,'are',wordCount)
    print('No of vowels present in the',a,'are',vowelsCount)

def main():
    Words_Vowels('file1.txt')

if __name__ == '__main__':
    main()
```

Question 3:

```python
def writeLine(a):

    LetsWrite = open(a,'w')
    userInput = input('Type here to store the data: ')

    while userInput != '':
        LetsWrite.writelines(userInput.capitalize() + '\n')
        userInput = input('Type here to store the data: ')

    LetsWrite.close()
    LetsWrite = open(a,'r')
    print(LetsWrite.read())
    LetsWrite.close()
    
def main():
    writeLine('file2.txt')

if __name__ == '__main__':
    main()
```

Question 4:

```python
def OddLines(a,b):

    readFile = open(a,'r')
    writeFile = open(b,'w')
    readLine = readFile.readline()
    oddValue = 1

    while readLine != '':
        if oddValue % 2 != 0:
            writeFile.write(readLine)
        oddValue += 1
        readLine = readFile.readline()

    readFile.close()
    writeFile.close()
    writeFile = open(b,'r')
    print(writeFile.read())
    writeFile.close()

def main():
    OddLines('file1.txt','file2.txt')

if __name__ == '__main__':
    main()
```

Question 5:

```python
def main():

    weightFile = open('file1.txt','r')
    priceFile = open('file2.txt','r')
    unitPriceFile = open('file3.txt','w')
    weightLine = weightFile.readline()

    while weightLine != '':
        weightList = weightLine.split(',')
        priceLine = priceFile.readline()

        while priceLine != '':
            priceList = priceLine.split(',')
            if weightList[0] == priceList[0]:
                result = 'Total weight of ' + weightList[0] + ' is ' + str(int(weightList[1])) + ' total price of '+ priceList[0] + ' is ' + str(int(priceList[1])) +' so the unit price of ' + weightList[0] + ' is '+ str (int(priceList[1]) / int(weightList[1]))
                unitPriceFile.write(result)
                unitPriceFile.write('\n')
            priceLine = priceFile.readline()
        priceFile.seek(0)
        weightLine = weightFile.readline()

    weightFile.close()
    priceFile.close()
    unitPriceFile.close()

    unitPriceFile = open('file3.txt','r')
    print(unitPriceFile.read())
    unitPriceFile.close()

if __name__ == '__main__':
    main()
```

Question 6:

```python
def main():

    noOfLowercases = 0
    noOfUppercases = 0
    noOfSpaces = 0
    poem = open('file1.txt','r')
    result = poem.read()

    for st in result:
        if st.islower():
            noOfLowercases += 1
        elif st.isupper():
            noOfUppercases +=1
        elif st == ' ':
            noOfSpaces += 1

    print('No of occurrences of lower case alphabets are:',noOfLowercases)
    print('No of occurrences of upper case alphabets are:',noOfUppercases)
    print('No of alphabets are:',noOfLowercases + noOfUppercases)
    print('No of occurrences of blank spaces are:',noOfSpaces)
    print('No of occurrences of word "beautiful" are:',result.count('beautiful'))
    poem.close()

    poem = open('file1.txt','r')
    vowelsLine = poem.readline()
    ListOfVowels = []

    while vowelsLine != '':
        vowelsList = vowelsLine.split(' ')
        for i in range(len(vowelsList)):
            if vowelsList[i][0] == 'a' or vowelsList[i][0] == 'e' or vowelsList[i][0] == 'i' or vowelsList[i][0] == 'o' or vowelsList[i][0] == 'u' or vowelsList[i][0] == 'A' or vowelsList[i][0] == 'E' or vowelsList[i][0] == 'I' or vowelsList[i][0] == 'O' or vowelsList[i][0] == 'U':
                ListOfVowels.append(vowelsList[i])                   
        vowelsLine = poem.readline()
    print('No of words starts with vowels are:',len(ListOfVowels))
    poem.close()

if __name__ == '__main__':
    main()
```

### Calsses I
<hr>

**Exercises**

Question 1: 

```python
import sys

class Rectangle:
    '''
    Objective: Class Rectangle is used to find the area and perimeter of the rectangle as per the user input
    Input: Length & Breadth - Float
    Output: Area & Perimeter - Float
    '''

    def __init__(self, length, breadth):
        
    '''Initialization the class and assign length and breadth respectively to the object'''

        if length > 0 and breadth > 0:
            self.length = length
            self.breadth = breadth
        else:
            print('Length or breadth should be greater than zero')
            sys.exit()

    def set_length(self, length):

        '''Update the new length'''

        if length > 0:
            self.length = length
        else:
            print('Length should be greater than zero')
            sys.exit()

    def set_breadth(self, breadth):

        '''Update the new breadth'''

        if breadth > 0:
            self.breadth = breadth
        else:
            print('Breadth should be greater than zero')
            sys.exit()

    def get_length(self):

        '''Return the length'''

        return self.length
    
    def get_breadth(self):

        '''Return the breadth'''

        return self.breadth
    
    def area(self):

        '''Find the area of the rectangle'''

        return self.length * self.breadth

    def perimeter(self):

        '''Find the area of the perimeter'''

        return 2 * (self.length + self.breadth)

    def __str__(self):

        '''You know what __str__ function do'''

        return f'Area of the given length {self.length} and breadth {self.breadth} is {self.area()} and Perimeter of the given length {self.length} and breadth {self.breadth} is {self.perimeter()}'

def main():

    '''This is a main function'''

    length = float(input('Enter the length of the rectangle: '))
    breadth = float(input('Enter the breadth of the rectangle: '))

    result = Rectangle(length, breadth)
    print(result)

if __name__ == '__main__':
    main()
```

Question 2: 

Answer file path: [my_date.py](https://github.com/Aravindray/Python/blob/main/JAN2024/my_date.py)

Question 3:

```python
import sys

class Student:
    '''This class is to store students academic record and give percentage and division of a student'''

    def __init__(self, roll_num, name, stream, mark_list = None):
        '''This is the contractor of the object'''
        self.roll_num = roll_num
        self.name = name
        if stream == 'C':
            self.stream = 'Commerce'
        elif stream == 'A':
            self.stream = 'Arts'
        elif stream == 'S':
            self.stream = 'Science'
        else:
            print('Allowed streams are A: Arts, C: Commerce, S: Science')
            sys.exit()
        self.mark_list = mark_list
        if mark_list == None or mark_list == []:
            self.set_marks()
        self.percentage = self.percent()
        self.grades = self.grade_gen()
        self.division = self.percentage_division()
        
    def set_marks(self):
        '''Get the marks for 5 subject from the user and return it as a list'''
        self.mark_list = []
        no_of_subject = int(input('Enter no of subjects that you want to enter the marks: '))
        assert no_of_subject > 0 and no_of_subject < 100
        for i in range(1,no_of_subject+1):
            enter_marks = float(input(f'Enter the mark of subject {i}: '))
            assert enter_marks > 0 and enter_marks <= 100
            self.mark_list.append(enter_marks)

    def get_stream(self):
        '''Display the student stream'''
        return self.stream

    def percent(self):
        '''Calculated the percentage of entered marks'''
        mrk_lst = self.mark_list
        percentage = ( sum(mrk_lst) / (len(mrk_lst) * 100) ) * 100
        return percentage

    def grade_gen(self):
        '''Generate grades based on the entered marks by user'''
        grades = {}
        mrk_lst = self.mark_list
        for mrk in mrk_lst:
            if mrk >= 90:
                grades[mrk] = 'A'
            elif mrk < 90 and mrk >= 80:
                grades[mrk] = 'B'
            elif mrk < 80 and mrk >= 65:
                grades[mrk] = 'C'
            elif mrk < 65 and mrk >= 40:
                grades[mrk] = 'D'
            else:
                grades[mrk] = 'E'
        return grades

    def percentage_division(self):
        '''Take the percentage and return the division'''
        percentage = self.percentage
        if percentage >= 60:
            return 'I'
        elif percentage < 60 and percentage >= 50:
            return 'II'
        elif percentage < 50 and percentage >= 35:
            return 'III'
        else:
            return 'Fail'

    def __str__(self):
        '''Return string representation of object'''
        return f'Name: {self.name}\nRoll Number: {self.roll_num}\nStream: {self.stream}\nMarks: {self.mark_list}\nAchieved Grades: {self.grades}\nAchieved Percentage: {self.percentage}\nAchieved Division: {self.division}'
```

Question 4:

```python
import sys
class Bank:
    '''Manage customer details'''
    def __init__(self, name, account_num, account_type, amount):
        self.name = name
        self.account_num = account_num
        if account_type == 'S':
            self.account_type = 'Savings'
        elif account_type == 'C':
            self.account_type = 'Current'
        else:
            print('Invalid entry for account_type')
            sys.exit()
        assert amount >= 0
        self.amount = amount

    def deposit(self, amount):
        '''This method to add deposit amount'''
        assert amount > 0
        self.amount += amount
        print(f'Amount successfully deposited your balance is {self.amount}')

    def withdrawal(self, amount):
        '''This method to subtract the withdrawal amount'''
        assert amount > 0
        self.amount -= amount
        print(f'Amount successfully withdrawal your balance is {self.amount}')

    def check_balance(self):
        '''This method will return the current balance'''
        print(f'Your current balance is {self.amount}')

    def find_interest(self):
        '''This method will find the interest and return the amount'''
        if self.amount >= 500000:
            interest_rate = 8 / 100
            after_a_year = self.amount + (self.amount * interest_rate)
            print(f'Your current balance is {self.amount}. Since your deposited amount is more than 5,00,000 you will gain interest rate of 8 %, so after a year your balance will be {after_a_year}')
        elif self.amount < 500000 and self.amount >= 300000:
            interest_rate = 7 / 100
            after_a_year = self.amount + (self.amount * interest_rate)
            print(f'Your current balance is {self.amount}. Since your deposited amount is between less than 5,00,000 and more than or equal to 3,00,00 you will gain interest rate of 7 %, so after a year your balance will be {after_a_year}')
        elif self.amount < 300000 and self.amount >= 100000:
            interest_rate = 5 / 100
            after_a_year = self.amount + (self.amount * interest_rate)
            print(f'Your current balance is {self.amount}. Since your deposited amount is between less than 3,00,000 and more than or equal to 1,00,00 you will gain interest rate of 5 %, so after a year your balance will be {after_a_year}')
        elif self.amount < 100000:
            interest_rate = 3 / 100
            after_a_year = self.amount + (self.amount * interest_rate)
            print(f'Your current balance is {self.amount}. Since your deposited amount is less than 1,00,000 you will gain interest rate of 3 %, so after a year your balance will be {after_a_year}')
        elif self.amount == 0:
            print('You balance is {self.amount}, so your are applicable for annual interest')

    def __str__(self):
        return f'Name: {self.name}\nAccount Number: {self.account_num}\naccount_type: {self.account_type}\nBalance: {self.amount}'
```

Question 5:

```python
class Item:
    '''To track a Item available in a shop'''
    def __init__(self, name, price, quantity):
        '''This is a class initializer'''
        self.name = name
        self.price = price
        self.quantity = quantity
        self.profit = 0
    
    def purchase(self, new_quantity):
        '''This method is track the item available in shop and purchase'''
        assert new_quantity > 0 and isinstance(new_quantity, int)
        if new_quantity > self.quantity:
            print(f'Invalid Input, In shop we have {self.quantity} but you have entered purchased quantity as {new_quantity}')
        else:
            self.quantity -= new_quantity
            self.profit += (new_quantity * self.price)
        
        if self.quantity == 0:
            print('A reminder! We are out of order')

    def increase_stock(self, new_quantity):
        '''This method is track the item available in shop'''
        assert new_quantity > 0 and isinstance(new_quantity, int)
        self.quantity += new_quantity

    def display(self):
        '''This method will display the Item price and quantity'''
        print(f'Price and Quantity of "{self.name}"\n--> Price: {self.price}\n--> Quantity: {self.quantity}')

    def __str__(self):
        '''This method will print'''
        return f'Item Name: {self.name}\nPrice: {self.price}\nQuantity: {self.quantity}\nProfit: {self.profit}'
```
Question 6:

Answer file path: [my_date.py](https://github.com/Aravindray/Python/blob/main/JAN2024/my_date.py) I already created a method name _future_date_ will add the day, month and year.


### Games
<hr>

**Find the Next / Previous Letter**

```python
import random

english_alphabets = {1 : 'a', 2 : 'b', 3 : 'c', 4 : 'd', 5 : 'e', 6 : 'f', 7 : 'g', 8 : 'h', 9 : 'i', 10 : 'j', 11 : 'k', 12 : 'l', 13 : 'm', 14 : 'n', 15 : 'o', 16 : 'p', 17 : 'q', 18 : 'r', 19 : 's', 20 : 't', 21 : 'u', 22 : 'v', 23 : 'w', 24 : 'x', 25 : 'y', 26 : 'z'}
user_input = input("Let's start the game! press 'S' to Start or 'Q' to quit: ")
score = 0
no_of_question = 0
list_choice = ['Next','Previous']

open_file = open('demo_write.txt','w')

if user_input == 'Q' or user_input == 'q':
    print('Okay, we play another time!')
else:
    while user_input != '':
        choice = random.choice(list_choice)
        random_int = random.randint(2,25)
        if choice == 'Next':
            print(f'Find the "{choice}" letter of "{english_alphabets[random_int]}"')
            open_file.write(f'Question: Find the "{choice}" letter of "{english_alphabets[random_int]}"\n')
            no_of_question += 1
            user_input = input('Enter the "next" letter in lowercase: ')
            open_file.write(f'Answer: {user_input}\n')
            if user_input == english_alphabets[random_int + 1]:
                score += 1
                open_file.write(f'Correct Answer! Score is {score}\n')
            elif user_input == '':
                print('Empty String!, Game Ends!!!')
            else:
                # score -= 1
                print(f'Oops! Wrong Answer! The correct answer is "{english_alphabets[random_int + 1]}"')
                open_file.write(f'Oops! Wrong Answer! The correct answer is "{english_alphabets[random_int + 1]}"\n')
        else:
            print(f'Find the "{choice}" letter of "{english_alphabets[random_int]}"')
            open_file.write(f'Question: Find the "{choice}" letter of "{english_alphabets[random_int]}"\n')
            no_of_question += 1
            user_input = input('Enter the "previous" letter in lowercase: ')
            open_file.write(f'Answer: {user_input}\n')
            if user_input == english_alphabets[random_int - 1]:
                score += 1
                open_file.write(f'Correct Answer! Score is {score}\n')
            elif user_input == '':
                print('Empty String!, Game Ends!!!')
            else:
                # score -= 1
                print(f'Oops! Wrong Answer! The correct answer is "{english_alphabets[random_int - 1]}"')
                open_file.write(f'Oops! Wrong Answer! The correct answer is "{english_alphabets[random_int + 1]}"\n')
    print(f'Out of {no_of_question - 1} you scored {score}')
    open_file.write(f'Out of {no_of_question - 1} question you scored {score}')

open_file.close()
```

# February - 2024

### Calsses II
<hr>

**Exercises**

Question 1:

Answer File Path: Base class _[Points](https://github.com/Aravindray/Python/blob/main/FEB2024/points.py)_ and derived class _[Linesegments](https://github.com/Aravindray/Python/blob/main/FEB2024/line_segments.py)_. I just added 2 methods only which are Distance and Midpoint.

Question 2 & 3:

Answer File Path: I have implemented the module in class _[Calendar](https://github.com/Aravindray/Python/blob/main/FEB2024/my_calendar.py)_

Question 4:

Answer File Path: I have implemented the module for class _[ComplexNumber](https://github.com/Aravindray/Python/blob/main/FEB2024/complex_number.py)_

Question 5:

```python
from abc import abstractmethod, ABCMeta

class Shapes:
    '''This is the abstract class with area function'''
    __metaclass__ = ABCMeta
    def __init__(self,shape_type,x,y):
        '''Objective: to initialize the object with shape type and it's dimensions
        shape type - str
        x, y - number type'''
        self.shape_type = shape_type
        self.x = x
        self.y = y

    @abstractmethod
    def compute_area(self):
        '''This is a abstract method'''
        pass

class Rectangle(Shapes):
    '''This is the derived class of shapes'''
    def __init__(self,width,height):
        '''This will initialize the width and height'''
        super().__init__('Rectangle',width,height)
    
    def compute_area(self):
        '''formula to compute area of rectangle is width * height'''
        area = self.x * self.y
        return area

    def __str__(self):
        '''This will print rectangle's width and height'''
        return f'Shape Type: {self.shape_type}\nWidth: {self.x}\nHeight: {self.y}'

class Triangle(Shapes):
    '''This is the derived class of shapes'''
    def __init__(self,base,height):
        '''This will initialize the base and height'''
        super().__init__('Triangle',base,height)

    def compute_area(self):
        '''Formula to compute area of triangle is 1/2 * base * height'''
        area = 0.5 * self.x * self.y
        return area
    
    def __str__(self):
        '''This will print rectangle's width and height'''
        return f'Shape Type: {self.shape_type}\nBase: {self.x}\nHeight: {self.y}'
```
Question 6:

Answer File Path: I have implemented the answer as a separate module class _[Student](https://github.com/Aravindray/Python/blob/main/FEB2024/students.py)_

Question 7 & 8:

Answer File Path: I have also implemented the answers as a separate module classes _[Vehicle, PassengerVehicle, CommercialVehicle](https://github.com/Aravindray/Python/blob/main/FEB2024/vehicle.py)_ & classes _[Car, Bus, Autorickshaw](https://github.com/Aravindray/Python/blob/main/FEB2024/passenger_vehicle.py)_

Question 9:

Answer File Path: I have also implemented the answer as a separate module classes _[Account, Savings, Current](https://github.com/Aravindray/Python/blob/main/FEB2024/account.py)_

Question 10:

```python
class B:
    def __init__(self,attr):
        self.attr = attr

    def __str__(self):
        return f'{self.attr}'

class A(B):
    pass

ob = A(0)
print(issubclass(A,B))
print(hasattr(ob,'attr'))
setattr(ob,'attr',70)
delattr(ob,'attr')
```

### Sorting Methods

**Merge Sort**

```python
def merge(lst1, lst2):
    sorted_list = []
    while len(lst1) != 0 and len(lst2) != 0:
        if lst1[0] < lst2[0]:
            sorted_list.append(lst1[0])
            lst1.remove(lst1[0])
        else:
            sorted_list.append(lst2[0])
            lst2.remove(lst2[0])

    if len(lst2) == 0:
        sorted_list += lst1
    else:
        sorted_list += lst2
    return sorted_list

def merge_sort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        mid = len(lst) // 2
        lst1 = merge_sort(lst[:mid])
        lst2 = merge_sort(lst[mid:])
        return merge(lst1, lst2)

numbers = [15, 12, 14, 17, 13, 11, 12, 16, 14]
print(numbers)
print(merge_sort(numbers))
```

**Quick Sort** No idea how it's working!!!

```python
def partition(lst, start, end):
    pivotElement = lst[end]
    i = start - 1
    for j in range(start, end):
        if lst[j] <= pivotElement:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i+1], lst[end] = lst[end], lst[i+1]
    return i+1


def quick_sort(lst, start = 0, end = None):
    if end == None:
        end = len(lst) - 1
    if start < end:
        splitPoint = partition(lst, start, end)
        quick_sort(lst, start, splitPoint-1)
        quick_sort(lst, splitPoint+1, end)
```

### List Manipulation
<hr>

**Exercises**

Question 1:

```python
'''
Step 1: Fist store the employee object in the list
Step 2: Sort the list using the bubble, insertion and selection sort algorithm
'''
from employee import Employee

object_list = list()
file_name = 'employee_data.txt'

def file_list(file_name):
    '''This function will store the employee object in the list'''
    with open(file_name,'r') as file:
        line = file.readline()
        while line != '':
            name, salary = line.split(',')
            emp = Employee(name,None,None,salary,None)
            object_list.append(emp)
            line = file.readline()

file_list(file_name)
print(object_list)

def bubble_sort(lst,based_on):
    if based_on == 'employee_id':
        length_of_list = len(lst)
        for i in range(length_of_list):
            swap = False
            for j in range(length_of_list-1,i,-1):
                if lst[j].employee_id < lst[j-1].employee_id:
                    swap = True
                    lst[j], lst[j-1] = lst[j-1], lst[j]
            if swap == False:
                break
        print('sorted')
    elif based_on == 'name':
        length_of_list = len(lst)
        for i in range(length_of_list):
            swap = False
            for j in range(length_of_list-1,i,-1):
                if lst[j].name < lst[j-1].name:
                    swap = True
                    lst[j], lst[j-1] = lst[j-1], lst[j]
            if swap == False:
                break
        print('sorted')
    elif based_on == 'basic_salary':
        length_of_list = len(lst)
        for i in range(length_of_list):
            swap = False
            for j in range(length_of_list-1,i,-1):
                if lst[j].basic_salary < lst[j-1].basic_salary:
                    swap = True
                    lst[j], lst[j-1] = lst[j-1], lst[j]
            if swap == False:
                break
        print('sorted')
    else:
        print('wrong argument')


def insertion_sort(lst,based_on):
    '''Already solved in section file'''

def selection_sort(lst,based_on):
    if based_on == 'employee_id':
        length_of_list = len(lst)
        for i in range(length_of_list-1):
            small = i
            for j in range(i,length_of_list-1):
                if lst[j+1].employee_id < lst[small].employee_id:
                    small = j+1
            lst[i], lst[small] = lst[small], lst[i]
    elif based_on == 'name':
        length_of_list = len(lst)
        for i in range(length_of_list-1):
            small = i
            for j in range(i,length_of_list-1):
                if lst[j+1].name < lst[small].name:
                    small = j+1
            lst[i], lst[small] = lst[small], lst[i]
    elif based_on == 'basic_salary':
        length_of_list = len(lst)
        for i in range(length_of_list-1):
            small = i
            for j in range(i,length_of_list-1):
                if lst[j+1].basic_salary < lst[small].basic_salary:
                    small = j+1
            lst[i], lst[small] = lst[small], lst[i]
    else:
        print('Wrong Arguments')
```

Question 4:

```python
def binary_search(lst, key):
    start = 0
    print('start index',start,'value',lst[start])
    end = len(lst) - 1
    print('end index',end,'value',lst[end])
    counter = 0
    while start <= end:
        mid = (start + end) // 2
        print('while loop is',counter,'initial mid',mid,'and value is',lst[mid])
        if key < lst[mid]:
            end = mid - 1
            print('while loop is',counter,'end',end,'and value is',lst[end])
        elif key > lst[mid]:
            start = mid + 1
            print('while loop is',counter,'start',start,'and value is',lst[start])
        elif key == lst[mid]:
            print('while loop is',counter,'conditional mid',mid,'and value is',lst[mid])
            print(f'{key} is found at index {mid}')
            return True
        counter += 1
    return False
```
