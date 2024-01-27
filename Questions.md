# January - 2024

## Table of Content

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
