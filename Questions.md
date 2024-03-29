## Table of Content

- [Style block](#style-block)
- [January - 2024](#january---2024)
    - [Mutable and Immutable Objects](#mutable-and-immutable-objects)
    - [Files and Exceptions](#files-and-exceptions)
    - [Calsses I](#calsses-i)
- [February - 2024](#february---2024)
    - [Calsses II](#calsses-ii)
    - [List Manipulation](#list-manipulation)
- [March - 2024](#march---2024)
    - [Data Structures I: Stack and Queues](#data-structures-i-stack-and-queues)
    - [Data Structures II: Linked Lists](#data-structures-ii-linked-lists)
    - [Recursion](#recursion)


<br>

# Style block

<style>
    red {color: Red}
    green {color: Green}
</style>


# January - 2024

### Mutable and Immutable Objects
<hr>

**Exercises**

6. Write a function that takes n as input and creates a list of n lists such that ith list contains first five multiples of i.

7. Write a function that takes a number as an input parameter and returns the correspond text in words. for example, on input 452, the function should return 'Four five Two'. Use a dictionary for mapping digits to their string representation.


### Files and Exceptions
<hr>

**Exercises**

1. Write a function that takes two file names, _file1_ and _file2_ as input. The function should read the content of the _file1_ line by line write them to another file _file2_ after adding a newline at the end of the each line.

2. Write a function that reads a file _file1_ and displays the number of words and the number of vowels in the file.

3. Write a function that takes data to be stored in the file _file2_ as an interactive input from the user until he response with nothing as input. Each line (or paragraph) take as input from the user should be capitalized, and stored in the file _file2_.

4. Write a function that reads the file _file1_ and copies only alternative lines to another file _file2_. Alternative lines copied should be the odd numbered lines. Handle all exceptions that can be raised.

5. Write a function that takes two files of equal size as input from user. The first file contains weights of items and the second file contains corresponding prices. Create another file that should contain price per unit weight for each item.

6. Write a function that read the content of the file _Poem.txt_ and count the number of alphabets, blank spaces, lowercase letters and uppercase letters, the number of words starting with vowels, and no of occurrences of word 'beautiful' in the file.

### Calsses I
<hr>

**Exercises**

1. Define a class Rectangle. The class should contain sides: length and breadth of the rectangle as the data members. It should support the following methods:
    
    (a) \_\_init__ for initializing the data members: length and breadth.
    
    (b) _set_length_ for updating the length of the rectangle.
    
    (c) _set_breadth_ for updating the breadth of the rectangle.
    
    (d) _get_length_ for retrieving the length of the rectangle.
    
    (e) _get_breadth_ for retrieving the breadth of the rectangle.
    
    (f) _area_ to find the area of the rectangle.
    
    (g) _perimeter_ for finding the perimeter of the rectangle.

2. Define the following methods for MyDate class:

    (a) _add_days_ - To add n days to the date

    (b) _add_months_ - To add n months to date

    (c) _add_years_ - To add n years to date

    (d) _weekdays_ - To return weekday of the date

    (e) _diff_dates_ - To find difference between two dates in terms of the years, months, and days.

    (f) _future_date_ - To find a future date after a given number of days, months and years.

    (g) _past_date_ - To find a date in the past before a give number of days, months and years.

3. Define a class _student_ that keep tracks of academic records of students in a school. The class should contain the following data members:

    rollNum - Roll number of student <br>
    name - Name of the student <br>
    markList - List of the mark in five subjects <br>
    stream - A: Arts, C: Commerce, S: Science <br>
    percentage - Percentage computed using marks <br>
    grade - Grade in each subject computed using marks <br>
    division - Division computed on the basis of overall percentage

    The Class should support the following methods:

    (a) _\_\_init___ for initializing the data members. <br>
    (b) _set_marks_ to take marks for five subjects as an input from user. <br>
    (c) _get_stream_ for accessing the stream of the student. <br>
    (d) _percentage_ for computing the overall percentage for the student. <br>
    (e) _grade_gen_ that generates grade for each students in each courses on the basis of the marks obtained. Criteria for computing the grade is as follows:

    | Marks        | Grades |
    |:------------:|:------:|
    | >= 90        |    A   |
    | < 90 & >= 80 |    B   |
    | < 80 & >= 65 |    C   |
    | < 65 & >= 40 |    D   |
    | < 40         |    E   |

    (f) _division_ for computing division on the basis of the following criteria based on overall percentage of marks scored:

    | Percentage        | Division |
    |:-----------------:|:--------:|
    | >= 60             |    I     |
    | <60 and >= 50     |    II    |
    | <50 and >= 35     |    III   |
        
    (g) _\_\_str___ that displays student information.

4. Define a class _Bank_ that keeps track of bank customers. The class should contain the following data members:

    name - Name of the customer <br>
    account_num = Account Number <br>
    type - Account Type (Savings or Current) <br>
    amount - amount deposited in the bank account <br>
    interest - Interest earned by the customer

    The class should support the following methods:

    (a) \_\_init__ for initializing the data members. <br>
    (b) _deposit_ for depositing money in the account. <br>
    (c) _withdrawal_ for withdrawing money from the account. <br>
    (d) _find_interest_ that determines the interest on the basis of amount in the account:

    | Account                   | Interest per annum (%) |
    |:-------------------------:|:----------------------:|
    | >= 5,00,000               |          8             |
    | >= 3,00,000 and <5,00,000 |          7             |
    | >= 1,00,000 and <3,00,000 |          5             |
    | < 1,00,000                |          3             |

    (e) \_\_str__ that displays information about the bank customer.

5. Define a class _Item_ that keeps track of item available in the shop. The class should contain the following data members:

    name - Name of the item <br>
    price - Price of the item <br>
    quantity - Quantity of the item available in the stock

    The class should support the following methods:

    (a) \_\_init__ for initializing the data members. <br>
    (b) _purchase_ for updating the quantity after a purchase made by the customer. The method should take the number of items to be purchased as an input. <br>
    (c) _increaseStock_ for updating the quantity of an items for which new stock has arrived. The method should take the number of items to be added as an input. <br>
    (d) display that display information about an item. <br>

6. Fill in the details to define the method to compute the date on the following day of a given date for the class MyDate.
    
        def next_day(self):
            '''Objective: To display next day's date
            Input parameter: self - Object of the type MyDate
            Return value: string representations of next day's date'''
            '''Approach: Increment day if next day is within same month, else adjust month and year'''
            pass


# February - 2024

### Calsses II
<hr>

**Exercises**

1. Write a class _Point_ having *x* and *y* coordinates as data members. Write another class *LineSegment* that derives the class *Point* Also, list appropriate methods.

2. Define the method \_\_ne__ for the class MyDate.

3. Define the method \_\_sub__ for the class MyDate.

```python        
def __sub__(self,other):
    '''Objective: To subtract two date objects
    Input Parameters:
        self (implicit parameter) - Object of type MyDate
        other - Object of type MyDate
    Return value: string representation of difference of two objects if second object passed as parameter is of MyDate type else message 'Undefined type' is printed and program is terminated'''
    '''Examples:
        yyyy-mm-dd   yyyy-mm-dd   yyyy-mm-dd
        2014-04-04   2012-01-12   2014-06-06
      - 2012-06-06 - 2010-05-13 - 2012-04-04
        ------------ ------------ -----------
        0001-09-28   0001-07-30   0002-02-02 
```

4. Define a class *ComplexNumbers*. Write operations for addition, subtraction, and multiplication, using the notion of operator overloading.

5. Examine the following class *Shape*:
        
```python        
class Shape:
    def __init__(self,shapeType,x,y):
        self.shapeType = shapeType
        self.length = x
        self.width = y
    def compute_area():
        pass
```

The class *Shape* should be inherited by the class *Rectangle* and *Triangle*. Both the derived classes should invoke the method \_\_init__ to initialize data members. Note that *length* and *width* correspond to *height* and *base* for a triangle. The derived classes should override the method *compute_area* fo the superclass Shape.

6. Examine the class *Person* defined in this chapter. Define a class *Student* that derives this class and define *name, roll_number, class, total_marks* and *Year* as the data members. The class should contain the instance method \_\_init__ and the abstract method *percentage*. Define two classes *Grad* and *PostGrad* which inherit from the base class *Student*. Both the classes should define their \_\_init__ method and should override the abstract method *percentage* of the superclass. Note that *total_marks* obtained are out of 600 and 400 for *Grad* and *PostGrad* classes respectively.

7. Define a base class *Vehicle*, having attributes registration number, make, model and color. Also, define classes *PassengerVehicle* and *CommercialVehicle* that derived from the class *Vehicle*. The *PassengerVehicle* class should have additional attribute for maximum passenger capacity. The *CommercialVehicle* class should have an additional attribute for maximum load capacity. Define \_\_init__ method for all these classes. Also, define get and set methods to retrieve and set the value of the data attributes.

8. Define classes *Car*, *Autorickshaw*, and *Bus* which derive from the *PassengerVehicle* class mentioned in the previous question. The *Car* and *Bus* should have attributes for storing information about the number of doors, not shared by *Autorickshaw*. The *Bus* should have Boolean attributes *doubleDecker* not shared by *Car* and *Autorickshaw*. Define \_\_init__ method for all these classes. Also, define get and set methods to determine and set the value of the data attributes.

9. Define a class *Account*, have attributes account holder's name, account number, account type, the amount deposited and minimum deposit amount. Define two classes, namely *Savings* and *Current*. The *Savings* class should have a property interest. Define \_\_init__ method for all these classes. Also, define get and set methods to determine and set the value of the data attributes.

10. Using Python bulit-in functions, write the statements to
    (a) Determine whether A is a subclass of B.
    (b) Determine whether attribute attr exists in the namespace of object ob of class A.
    (c) Assign value 70 to attribute attr of object ob of class A.
    (d) Delete an attribute attr of object ob of class A.


### List Manipulation
<hr>

**Exercises**

[hover]:## "Hold!! Till I learn Recursive"

1. Develop a program to sort the employee data on the basis of pay of the employees using (i) selection sort, (ii) bubble sort, (iii) insertion sort. Consider a list L containing objects of class _Employee_ having _emp\_num_, _name_, and _salary_.

2. [Write the recursive version of linear search and binary search algorithms, discussed in the text.][hover]

3. [Rewrite selection sort, bubble sort and insertion sort functions using recursion.][hover]

4. for the list shown below, show the values of indexes _low_, _high_ and _mid_ at each step of the binary search method discussed in the text when we are searching for the key:

    list = [10, 15, 22, 24, 45, 55]

    (a) 15 <br>
    (b) 25 <br>
    (c) 55 <br>
    (d) 40 <br>
    (e) 22 <br>

5. Write a function _left\_circulate_ that take a list as an input and left circulates the values in the list so that in the final list, each value is left shifted by one position and leftmost value in the original list now appears as the rightmost value. For example, on execution of the function on the list [1, 2, 3, 4, 5] it would be transformed to the list [2, 3, 4, 5, 1]. Modify the function to include a numeric argument to specify the number of position by which left rotation is to carried out.

6. Write a program that define a class *Card* which can be used to instantiate cards with a particular rank and suit. Create another class *DeckOfCards* for maintaining a sorted list of cards using a method *sorted_insert* that takes an object of class *Card* as an input parameter and insert it at the suitable position in the sorted list.

# March - 2024

### Data Structures I: Stack and Queues
<hr>

**Exercises**

1. Imagine that python list does not support methods *append* and *pop*. Examine the [script](https://github.com/Aravindray/Learn_Python/blob/main/FEB2024/own_stack.py)  and define your implementation of push and pop operation of the stack by filling up the code.

2. Imagine the python list does not support methods *append* and *pop*. Examine the [script](https://github.com/Aravindray/Learn_Python/blob/main/FEB2024/own_queue.py) and define your own implementation of enqueue and dequeue operation on a queue by filling up the missing code.

3. The queue implementation defined in question 2 does not utilize the storage space effectively since if front points to index j and rear points to index i >= j, empty space at indexes 0 to i-1 cannot be utilized as shown in book fig 13.13 <green>(But I have implemented the program to overcome this, so no worries!) </green> & rest of the question I didn't type here.

4. Develop a program using a stack to find out whether the given string is a palindrome.

5. Rewrite the code in question 2, so that whenever there is a deletion, all the elements in the queue are shifted towards the front by one position. <green>(I have already overcome this scenario, so no need to worries!)</green>

6. Rewrite the code in exercise 2 so that whenever there is a queue overflow scenario, all the elements in the queue are sifted (if possible so that the front element is at index 0). <red>(I Didn't quit understand this question)</red>

7. Write a program to reverse a string using stack

8. Evaluate the following postfix expression. Show the status of the stack on the execution of each operation.

    (a) 99/52\*9-+ <br>
    (b) 25\*94/5-+ <br>
    (c) 526\*93/-* <br>
    (d) 51+31-* <br>
    (e) 687+\*82/- <br>
    (f) 152-\*25*+ <br>
    (g) 55+93-\*3/ <br>
    (h) 651+21-+\* <br>
    (i) 836+27-9+\*/

9. Convert the following infix expression to its equivalent postfix expression, showing the stack content at each step.

    (a) 8+6/(5-3)\*2 <br>
    (b) (8-3-1)\*6/2+8/4 <br>
    (c) 8+(9-9/3-4*7)-5 <br>
    (d) 7+6-7/2-7\*4-3

### Data Structures II: Linked Lists
<hr>

**Exercises**

1. Write a method *insert_end* for the class *LinkedList* that takes a value as an input and adds a node having the value at the end of the linked list.

2. Write a method *delete_end* for the class *LinkedList* that deletes the last node of the linked list and returns the value of the data attribute of the last node.

3. Write a function that takes two sorted linked list as input parameter and returns the merged, sorted list.

4. Write a method *find_value* for the class *LinkedList* that takes *n* as an input parameter and returns value of the data attribute of the *n*th node starting from the beginning.

5. Write an iterative method *reverse* for the class *LinkedList* that reverses the given linked list.

6. Write a recursive method *reverse_display* for the class *LinkedList* that displays the data values of the linked list from the right end.

7. Write a method *divide_list* for the class *LinkedList*. The method should create and return a tuple comprising two linked lists. one comprising node at even position and another comprising node at odd positions.

8. A variant of the linked list is know as doubly linked list or two-way linked list comprising the following node structure having two links (*next* and *previous*) for traversing in both directions.

```python
Class Node:
    def __init__(self, value):
        '''Objective: To initialize an object of class Node
        Input Parameter:
            self (implicit parameter) - object of type Node
        Return Value: None'''
        self.data = value
        self.next = None
        self.previous = None
```
Define a class *DoublyLinkedList* which supports methods *insert_begin*, *insert_end*, *delete_begin*, *delete_end*, *del_value* and *traverse*.

9. A variant of linked list is known as a circular list for traversing the nodes of the linked list in a circular manner. Define a class *CircularLinkedList* which supports the methods *insert_begin*, *insert_end*, *delete_begin*, *delete_end*, *delete_value* and *traverse*.

### Recursion
<hr>

**Exercises**

1. Write a recursive function that multiplies two positive numbers a and b, and return the result. Multiplication is to be achieved as a + a + a (b times).

2. Write a recursive function that takes number n as an input parameter and prints n-digit strictly increasing numbers.

3. Write a recursive function that generates all binary strings of n-bit length.

4. Write a recursive function that takes two strings as input parameter and prints all interleaving strings of the given two strings preserving their order of occurrence. for example, interleaving of string 'AB' and 'CD' will generate the strings: 'ABCD', 'ACBD', 'ACDB', 'CDAB', 'CADB' and 'CABD'.

5. Write a recursive function that inserts the element x at every kth position in the given list, and returns the modified list. For example, if wew wish to insert element 50 at every 3rd position (counting 0, 1, 2, 3) in the list [1, 2, 3, 4, 5, 6, 7], the output list will be [1, 2, 3, 50, 4, 5, 6, 50, 7].

6. Write a recursive function that deletes every kth element. and returns the modified list. For example, if we wish to delete every 3rd element from the list [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], the output list will be [1, 2, 4, 5, 7, 8, 10, 11].

7. Write a recursive function that recursively removes adjacent duplicates from a given list, and returns the modified list. for example, removing adjacent duplicates recursively from the list [1, 2, 4, 4, 5, 7, 7, 7, 8, 8, 9, 7] will yield list [1, 2, 5, 9, 7].

8. write a recursive function that takes two numbers as input parameters and computes their greatest common divisor.

9. In fig. 8.17 (from the book) after line 25, include following statement, execute the code again and justify the output:
    lst2 = deep_copy(lst1)
