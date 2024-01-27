# January - 2024

## Table of Content

### Mutable and Immutable Objects
<hr>

**Exercises**

Question 6:

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

Question 7:

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


### File and Exceptions
<hr>

**Exercises**

Question 1:

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

Question 2:

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

Question 3:

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

Question 4:

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

Question 5:

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

Question 6:

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

### Calsses I
<hr>

**Exercises**

Question 1: 

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


Question 2: 

Answer file path: [my_date.py](https://github.com/Aravindray/Python/blob/main/JAN2024/my_date.py)

Question 3:

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
