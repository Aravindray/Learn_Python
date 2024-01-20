# Chapter 7 - Mutable and Immutable Objects

'''Exercise 6 -Write a function that takes n as input and creates a list of n lists such that ith list contains first five multiples of i
def e6(n):
    count = 1
    listOflist = [[] for i in range(n)]
    for i in range(len(listOflist)):
        for j in range(1,6):
            listOflist[i].append(count * j)
        count += 1
    print(listOflist)
if __name__ == '__main__':
    e6(5)'''

'''Exercise 7 - Write a function that takes a number as an input parameter and returns the correspond text in words. for example, on input 452, the function should return 'Four five Two'. Use a dictionary for mapping digits to their string representation
def numToStr(n):
    number_nameDictionary = {0:'Zero', 1:'One', 2:'Two', 3:'Three', 4:'Four', 5:'Five', 6:'Six', 7:'Seven', 8:'Eight', 9:'Nine'}
    n = str(n)
    result = []
    for num in n:
        result.append(number_nameDictionary[int(num)])
    for rel in result:
        print(rel,end=' ')
if __name__ == '__main__':
    numToStr(654166468716087467923)'''

# Chapter 9 - Files and Exceptions

'''Exercise 1 - Write a function that takes two file names, file1 and file2 as input. The function should read the content of the file1 line by line write them to another file file2 after adding a newline at the end of the each line

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
    main()'''

'''Exercises - 2 Write a function that reads a file file1 and displays the number of words and the number of vowels in the file
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
    main()'''

'''Exercises - 3 Write a function that takes data to be stored in the file file2 as an interactive input from the user until he response with nothing as input. Each line (or paragraph) take as input from the user should be capitalized, and stored in the file file2
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
    main()'''

'''Exercises - 4 Write a function that reads the file file1 and copies only alternative lines to another file file2. Alternative lines copied should be the odd numbered lines. Handle all exceptions that can be raised
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
    main()'''

'''Exercises - 5 Write a function that takes two files of equal size as input from user. The first file contains weights of items and the second file contains corresponding prices. Create another file that should contain price per unit weight for each item
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
    main()'''

'''Exercises - 6 Write a function that read the content of the file Poem.txt and count the number of alphabets, blank spaces, lowercase letters and uppercase letters, the number of words starting with vowels, and no of occurrences of word 'beautiful' in the file
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
    main()'''
