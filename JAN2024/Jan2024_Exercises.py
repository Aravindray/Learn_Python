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
