#Patterns in python

import math

def Simple_Number_Triangle_Pattern(n):
    for i in range(1,n+1):
        for j in range(i):
            print(i,end=' ')
        print()

def Inverted_Pyramid_of_Numbers(n):
    for i in range(1,n+1):
        for j in range((n+1)-i,0,-1):
            print(i,end=' ')
        print()

def Half_Pyramid_Pattern_of_Numbers(n):
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(j,end=' ')
        print()

def Inverted_Pyramid_of_Descending_Numbers(n):
    for i in range(n,0,-1):
        for j in range(1,i+1):
            print(i,end=' ')
        print()

def Reverse_Pyramid_of_Numbers(n):
    for i in range(1,n+1):
        for j in range(i,0,-1):
            print(j,end=' ')
        print()

def Inverted_Half_Pyramid_Number_Pattern(n):
    for i in range(1,n+1):
        for j in range(1,(n+2)-i):
            print(j,end=' ')
        print()

def Pyramid_of_Natural_Numbers(n):
    incNumber = 1
    k = 1
    for i in range(1, n+1):
        for j in range(k):
            print(incNumber,end=' ')
            incNumber += 1
        k += 2
        print()

def Reverse_Pattern_of_Digits(n):
    emptyArray = []
    incNumber = 0
    for i in range(1,n+1):
        for j in range(1,i+1):
            incNumber += 1
            emptyArray.append(incNumber)
        for k in range(1,i+1):
            print(emptyArray[-k],end=' ')
        print()

def Unique_Pyramid_Pattern_of_Digits(n):
    for i in range(1,n+1):
        if i < 2:
            for j in range(1,i+1):
                print(j,end=' ')
        else:
            for j in range(1,i+1):
                print(j,end=' ')
            for k in range(i-1,0,-1):
                print(k,end=' ')
        print()

def Connected_Inverted_Pyramid_Pattern_of_Numbers(n):
    for i in range(1, n+1):
        for j in range(n,i-1,-1):
            print(j,end=' ')
        for k in range(i,n+1):
            print(k,end=' ')
        print()

def Even_Number_Pyramid_Pattern(n):
    emptyArray = []
    for i in range(2,(n*2) + 1, 2):
        emptyArray.append(i)
    for j in range(1,n+1):
        for k in range(1,j+1):
            print(emptyArray[-k],end=' ')
        print()

def Pyramid_of_Horizontal_Tables(n):
    for i in range(n):
        for j in range(i+1):
            print(i * j, end=' ')
        print()

def Pyramid_Pattern_of_Alternate_Numbers(n):
    emptyArray = []
    for i in range(1,(n*2)+1,2):
        emptyArray.append(i)
    for j in range(1,n+1):
        for k in range(1,j+1):
            print(emptyArray[j-1],end=' ')
        print()

def Right_angled_Triangle_Mirrored_Pyramid(n):
    for i in range(1,n+1):
        for j in range(n-i,0,-1):
            print(' ',end=' ')
        for k in range(1, i+1):
            print(k,end=' ')
        print()

def Simple_Inverted_Pyramid_of_a_Digit(n):
    for i in range(1,n+1):
        for j in range(n, i-1, -1):
            print(n,end=' ')
        print()

def Full_Pyramid_of_Numbers(n):
    incNumber = 0
    currentNumber = 0
    for i in range(1,n+1):
        for j in range(n-i,0,-1):
            print(' ', end=' ')
        for k in range(0,i):
            print(i + k, end=' ')
        for l in range(1,i):
            print(currentNumber,end=' ')
            currentNumber -= 1
        incNumber += 2
        currentNumber = incNumber
        print()

def Pascals_Triangle_Pyramid(n):
    '''
    Formula to print pascal's triangle is nCr = n!/((n-r)!*r!)
    where n is no of rows and
    r is the element(position) in that row
    '''
    for i in range(n):
        for j in range(n-i-1,0,-1):
            print(' ',end = '')
        for k in range(i+1):
            result = math.factorial(i) // ((math.factorial(i - k)) * math.factorial(k))
            print(result,end=' ')
        print()

def Reverse_number_pattern(n):
    for i in range(1,n+1):
        for j in range(n+1-i,0,-1):
            print(j,end=' ')
        print()

def Square_pattern_with_numbers(n):
    for i in range(1, n+1):
        if i >= 2:
            for j in range(1,i):
                print(i,end=' ')
        for k in range(i,n+1):
            print(k,end=' ')
        print()

def Double_the_number_pattern(n):
    
    for i in range(1,n+1):
        for j in range(i-1,-1,-1):
            print(2 ** j, end=' ')
        print()

def Random_number_pattern(n):
    
    for i in range(1,n+1):
        for j in range(0,i):
            print(2 ** j, end=' ')
        if i > 1:
            for k in range(i-2,-1,-1):
                print(2 ** k,end=' ')
        print()

def Pant_style_pattern_of_numbers(n):

    for i in range(1,n+1):
        for j in range(n, i-1,-1):
            print(j,end=' ')
        for k in range(i-1):
            print(' '*3,end=' ')
        for l in range(i,n+1):
            print(l,end=' ')
        print()

def Pattern_with_a_combination_of_numbers_and_stars(n):

    for i in range(1, n+1):
        for j in range(1,n+2-i):
            print(j,end=' ')
            if j < n+1-i:
                print('*',end=' ')
        print()

def Inverted_Pyramid(n):
    pass
def Equilateral_Triangle_with_Stars(n):
    pass
def Downward_Triangle_Pattern_of_Stars(n):
    pass
def Right_Triangle(n):
    pass
def Left_Triangle(n):
    pass
def Right_down_mirror_star_Pattern(n):
    pass
def Two_pyramids_of_stars(n):
    pass
def Right_start_pattern_of_star(n):
    pass
def Left_triangle_pascals_pattern(n):
    pass
def Sandglass_pattern_of_star(n):
    pass
def Pant_style_pattern_of_stars(n):
    pass
def Diamond_shaped_pattern_of_stars(n):
    pass
def Hollow_Diamond_shaped_pattern_of_stars(n):
    pass
def Dobule_Hill(n):
    pass
def Butterfly(n):
    pass
def Two_Columns_Hollow_cube(n):
    pass
def Two_Rows_Hollow_cube(n):
    pass
def X_Hollow_Pattern(n):
    pass
def Plus_Hollow_Pattern(n):
    pass
def Hollow_Right_angle_Triangle(n):
    pass
def Invered_Right_Hollow_Triangle(n):
    pass
def Hollow_sand_hour_glass(n):
    pass
def Simple_Alphabet_Pyramid(n):
    pass
def Alphabetic_Triangle_Pattern(n):
    pass
def Right_Alphabet_Triangle(n):
    pass
def Continuous_Character_pattern(n):
    pass
def Right_Angle_Triangle_from_given_String(n):
    pass
def Acidental_Star_Pattern(n):
    inc = 1
    for i in range(1,(n//2+1)+1):
        for j in range(n-i,0,-1):
            print(' ',end=' ')
        for k in range(1,inc+1):
            print('*',end=' ')
        inc += 2
        print()
    for l in range((n//2+1)+1,0,-1):
        for m in range(n-l,0,-1):
            print(' ',end=' ')
        for x in range(l,0,-1):
            print('*',end=' ')
        print()
def Hollow_Box_Pattern(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            if (i == 1 or j == 1 or i == n or j == n):
                print('$',end=' ')
            else:
                print(' ',end=' ')
    print()

def Hollow_Odd_Diamond_Patter(n):
    n = int(input('Enter no of rows: '))
    first_half = n // 2
    second_half = n - first_half
    inc = 1
    dec = n
    for i in range(1, first_half+1):
        for j in range((first_half+2)-i,0,-1):
            print(' ',end=' ')
        for k in range(1,inc+1):
            if k == 1 or k == inc:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        inc += 2
    for l in range(1,second_half+1):
        for m in range(l):
            print(' ',end=' ')
        for o in range(1,dec+1):
            if o == 1 or o == dec:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()
        dec -= 2

def main():
    patternNames = ['-----Number Pattern (23)-----', "1 : Simple Number Triangle Pattern", "2 : Inverted Pyramid of Numbers", "3 : Half Pyramid Pattern of Numbers", "4 : Inverted Pyramid of Descending Numbers", "5 : Reverse Pyramid of Numbers", "6 : Inverted Half Pyramid Number Pattern", "7 : Pyramid of Natural Numbers", "8 : Reverse Pattern of Digits", "9 : Unique Pyramid Pattern of Digits", "10 : Connected Inverted Pyramid Pattern of Numbers", "11 : Even Number Pyramid Pattern", "12 : Pyramid of Horizontal Tables", "13 : Pyramid Pattern of Alternate Numbers", "14 :Right angled Triangle Mirrored Pyramid", "15 : Simple Inverted Pyramid of a Digit", "16 : Full Pyramid of Numbers", "17 : Pascals Triangle Pyramid", "18 : Reverse number pattern", "19 : Square pattern with numbers", "20 : Double the number pattern", "21 : Random number pattern", "22 : Pant style pattern of numbers", "23 : Pattern with a combination of numbers and stars", '-----Star Pattern (22)-----',"24 : Inverted Pyramid", "25 : Equilateral Triangle with Stars", "26 : Downward Triangle Pattern of Stars", "27 : Right Triangle", "28 : Left Triangle", "29 : Right down mirror star Pattern", "30 : Two pyramids of stars", "31 : Right start pattern of star", "32 : Left triangle pascals pattern", "33 : Sandglass pattern of star", "34 : Pant style pattern of stars", "35 : Diamond shaped pattern of stars", "36 : Hollow Diamond shaped pattern of stars", "37 : Dobule Hill", "38 : Butterfly", "39 : Two Columns Hollow cube", "40 : Two Rows Hollow cube", "41 : X Hollow Pattern", "42 : Plus Hollow Pattern", "43 : Hollow Right angle Triangle", "44 : Invered Right Hollow Triangle", "45 : Hollow sand hour glass",'-----Alphabetic Pattern(4)-----', "46 : Simple Alphabet Pyramid", "47 : Alphabetic Triangle Pattern", "48 : Right Alphabet Triangle", "49 : Continuous Character pattern", "50: Right Angle Triangle from given String",'-----Extra (1)-----','51: Acidental Star Pattern','52: Hollow Box Pattern','53: Hollow Odd Diamond Pattern']
    for pattern in patternNames:
        print(pattern)
    select = input('From the above list select and enter one of the pattern name or number to print: ')
    if select == "Simple Number Triangle Pattern" or select == "1":
        print('''You have select "Simple Number Triangle Pattern" which look like this
        1
        2 2
        3 3 3
        4 4 4 4
        5 5 5 5 5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Simple_Number_Triangle_Pattern(rows)
    elif select == "Inverted Pyramid of Numbers" or select == "2":
        print('''You have selected "Inverted Pyramid of Numbers" which look like this
        1 1 1 1 1
        2 2 2 2
        3 3 3
        4 4
        5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Inverted_Pyramid_of_Numbers(rows)
    elif select == "Half Pyramid Pattern of Numbers" or select == "3":
        print('''You have selected "Half Pyramid Pattern of Numbers" which look like this
        1
        1 2
        1 2 3
        1 2 3 4
        1 2 3 4 5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Half_Pyramid_Pattern_of_Numbers(rows)
    elif select == "Inverted Pyramid of Descending Numbers" or select == "4":
        print('''You have selected "Inverted Pyramid of Descending Numbers" which look like this
        5 5 5 5 5
        4 4 4 4
        3 3 3
        2 2
        1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Inverted_Pyramid_of_Descending_Numbers(rows)
    elif select == "Reverse Pyramid of Numbers" or select == "5":
        print('''You have selected "Reverse Pyramid of Numbers" which look like this
        1
        2 1
        3 2 1
        4 3 2 1
        5 4 3 2 1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Reverse_Pyramid_of_Numbers(rows)
    elif select == "Inverted Half Pyramid Number Pattern" or select == "6":
        print('''You have selected "Inverted Half Pyramid Number Pattern" which look like this
        1 2 3 4 5
        1 2 3 4
        1 2 3
        1 2
        1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Inverted_Half_Pyramid_Number_Pattern(rows)
    elif select == "Pyramid of Natural Numbers" or select == "7":
        print('''You have selected "Pyramid of Natural Numbers" which look like this
        1
        2 3 4
        5 6 7 8 9
        10 11 12 13 14 15 16''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Pyramid_of_Natural_Numbers(rows)
    elif select == "Reverse Pattern of Digits" or select == "8":
        print('''You have selected "Reverse Pattern of Digits" which look like this
        1
        3 2
        6 5 4
        10 9 8 7''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Reverse_Pattern_of_Digits(rows)
    elif select == "Unique Pyramid Pattern of Digits" or select == "9":
        print('''You have selected "Unique Pyramid Pattern of Digits" which look like this
        1
        1 2 1
        1 2 3 2 1
        1 2 3 4 3 2 1
        1 2 3 4 5 4 3 2 1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Unique_Pyramid_Pattern_of_Digits(rows)
    elif select == "Connected Inverted Pyramid Pattern of Numbers" or select == "10":
        print('''You have selected "Connected Inverted Pyramid Pattern of Numbers" which look like this
        5 4 3 2 1 1 2 3 4 5
        5 4 3 2 2 3 4 5
        5 4 3 3 4 5
        5 4 4 5
        5 5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Connected_Inverted_Pyramid_Pattern_of_Numbers(rows)
    elif select == "Even Number Pyramid Pattern" or select == "11":
        print('''You have selected "Even Number Pyramid Pattern" which look like this
        10
        10 8
        10 8 6
        10 8 6 4
        10 8 6 4 2''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Even_Number_Pyramid_Pattern(rows)
    elif select == "Pyramid of Horizontal Tables" or select == "12":
        print('''You have selected "Pyramid of Horizontal Tables" which look like this
        0  
        0 1  
        0 2 4  
        0 3 6 9  
        0 4 8 12 16  
        0 5 10 15 20 25  
        0 6 12 18 24 30 36''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Pyramid_of_Horizontal_Tables(rows)
    elif select == "Pyramid Pattern of Alternate Numbers" or select == "13":
        print('''You have selected "Pyramid Pattern of Alternate Numbers" which look like this
        1
        3 3
        5 5 5
        7 7 7 7
        9 9 9 9 9''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Pyramid_Pattern_of_Alternate_Numbers(rows)
    elif select == "Right angled Triangle Mirrored Pyramid" or select == "14":
        print('''You have selected "Right angled Triangle Mirrored Pyramid" which look like this
                1 
              1 2
            1 2 3
          1 2 3 4
        1 2 3 4 5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Right_angled_Triangle_Mirrored_Pyramid(rows)
    elif select == "Simple Inverted Pyramid of a Digit" or select == "15":
        print('''You have selected "Simple Inverted Pyramid of a Digit" which look like this
        5 5 5 5 5
        5 5 5 5
        5 5 5
        5 5
        5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Simple_Inverted_Pyramid_of_a_Digit(rows)
    elif select == "Full Pyramid of Numbers" or select == "16":
        print('''You have selected "Full Pyramid of Numbers" which look like this
                1
              2 3 2
            3 4 5 4 3
          4 5 6 7 6 5 4
        5 6 7 8 9 8 7 6 5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Full_Pyramid_of_Numbers(rows)
    elif select == "Pascals Triangle Pyramid" or select == "17":
        print('''You have selected "Pascals Triangle Pyramid" which look like this
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Pascals_Triangle_Pyramid(rows)
    elif select == "Reverse number pattern" or select == "18":
        print('''You have selected "Reverse number pattern" which look like this
        5 4 3 2 1 
        4 3 2 1 
        3 2 1 
        2 1 
        1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Reverse_number_pattern(rows)
    elif select == "Square pattern with numbers" or select == "19":
        print('''You have selected "Square pattern with numbers" which look like this
        1 2 3 4 5 
        2 2 3 4 5 
        3 3 3 4 5 
        4 4 4 4 5 
        5 5 5 5 5''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Square_pattern_with_numbers(rows)
    elif select == "Double the number pattern" or select == "20":
        print('''You have selected "Double the number pattern" which look like this
        1 
        2 1 
        4 2 1 
        8 4 2 1 
        16 8 4 2 1 
        32 16 8 4 2 1 
        64 32 16 8 4 2 1 
        128 64 32 16 8 4 2 1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Double_the_number_pattern(rows)
    elif select == "Random number pattern" or select == "21":
        print('''You have selected "Random number pattern" which look like this
        1 
        1 2 1 
        1 2 4 2 1 
        1 2 4 8 4 2 1 
        1 2 4 8 16 8 4 2 1 
        1 2 4 8 16 32 16 8 4 2 1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Random_number_pattern(rows)
    elif select == "Pant style pattern of numbers" or select == "22":
        print('''You have selected "Pant style pattern of numbers" which look like this
        5 4 3 2 1 1 2 3 4 5
        5 4 3 2     2 3 4 5 
        5 4 3         3 4 5
        5 4             4 5 
        5                 5''')
        rows = int(input('Enter no of rows as a positive integer till 10 (well above pattern will work till 10 rows only): '))
        Pant_style_pattern_of_numbers(rows)
    elif select == "Pattern with a combination of numbers and stars" or select == "23":
        print('''You have selected "Pattern with a combination of numbers and starts" which look like this
        1 * 2 * 3 * 4
        1 * 2 * 3
        1 * 2
        1''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Pattern_with_a_combination_of_numbers_and_stars(rows)
    elif select == "Inverted Pyramid" or select == "24":
        print('''You have selected "Inverted Pyramid" which look like this
        * * * * *
        * * * *
        * * *
        * *
        *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Inverted_Pyramid(rows)
    elif select == "Equilateral Triangle with Stars" or select == "25":
        print('''You have selected "Equilateral Triangle with Stars" which look like this
              *   
             * *   
            * * *   
           * * * *   
          * * * * *   
         * * * * * *   
        * * * * * * *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Equilateral_Triangle_with_Stars(rows)
    elif select == "Downward Triangle Pattern of Stars" or select == "26":
        print('''You have selected "Downward Triangle Pattern of Stars" which look like this
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             *''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Right Triangle" or select == "27":
        print('''You have selected "Right Triangle" which look like this
        * 
        * * 
        * * * 
        * * * * 
        * * * * *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Right_Triangle(rows)
    elif select == "Left Triangle" or select == "28":
        print('''You have selected "Left Triangle" which look like this
                * 
              * * 
            * * * 
          * * * * 
        * * * * *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Left_Triangle(rows)
    elif select == "Right down mirror star Pattern" or select == "29":
        print('''You have selected "Right down mirror star Pattern" which look like this
        * * * * *
          * * * *
            * * *
              * *
                *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Right_down_mirror_star_Pattern(rows)
    elif select == "Two pyramids of stars" or select == "30":
        print('''You have selected "Two pyramids of stars" which look like this
        *
        * *  
        * * *  
        * * * *  
        * * * * *  
        * * * * * *
              
        * * * * * *  
        * * * * *  
        * * * *  
        * * *  
        * *  
        *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Two_pyramids_of_stars(rows)
    elif select == "Right start pattern of star" or select == "31":
        print('''You have selected "Right start pattern of star" which look like this
        * 
        * * 
        * * * 
        * * * * 
        * * * * * 
        * * * * 
        * * * 
        * * 
        *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Right_start_pattern_of_star(rows)
    elif select == "Left triangle pascals pattern" or select == "32":
        print('''You have selected "Left triangle pascals pattern" which look like this
                * 
              * * 
            * * * 
          * * * * 
        * * * * * 
          * * * * 
            * * * 
              * * 
                *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Left_triangle_pascals_pattern(rows)
    elif select == "Sandglass pattern of star" or select == "33":
        print('''You have selected "Sandglass pattern of star" which look like this
        * * * * *
         * * * * 
          * * * 
           * * 
            * 
            * 
           * * 
          * * * 
         * * * * 
        * * * * *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Sandglass_pattern_of_star(5)
    elif select == "Pant style pattern of stars" or select == "34":
        print('''You have selected "Pant style pattern of stars" which look like this
        * * * * * * * * * * * * * * * *
        * * * * * * * _ _ * * * * * * *
        * * * * * * _ _ _ _ * * * * * *
        * * * * * _ _ _ _ _ _ * * * * *
        * * * * _ _ _ _ _ _ _ _ * * * *
        * * * _ _ _ _ _ _ _ _ _ _ * * *
        * * _ _ _ _ _ _ _ _ _ _ _ _ * *
        * _ _ _ _ _ _ _ _ _ _ _ _ _ _ *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Pant_style_pattern_of_stars(rows)
    elif select == "Diamond shaped pattern of stars" or select == "35":
        print('''You have selected "Diamond shaped pattern of star" which look like this
             * 
            * * 
           * * * 
          * * * * 
         * * * * * 
        * * * * * * 
         * * * * * 
          * * * * 
           * * * 
            * * 
             *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Diamond_shaped_pattern_of_stars(rows)
    elif select == "Hollow Diamond shaped pattern of stars" or select == "36":
        print('''You have selected "Hollow Diamond shaped pattern" which look like this
            *
           * *
          *   *
         *     *
        *       *
         *     *
          *   *
           * *
            *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Hollow_Diamond_shaped_pattern_of_stars(rows)
    elif select == "Dobule Hill" or select == "37":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Butterfly" or select == "38":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Two Columns Hollow cube" or select == "39":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Two Rows Hollow cube" or select == "40":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "X Hollow Pattern" or select == "41":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Plus Hollow Pattern" or select == "42":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Hollow Right angle Triangle" or select == "43":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Invered Right Hollow Triangle" or select == "44":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Hollow sand hour glass" or select == "45":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Simple Alphabet Pyramid" or select == "46":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Alphabetic Triangle Pattern" or select == "47":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Right Alphabet Triangle" or select == "48":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Continuous Character pattern" or select == "49":
        print('''You have selected " " which look like this
         ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == "Right Angle Triangle from given String" or select == "50":
        print('''You have selected "" which look like this ''')
        rows = int(input('Enter no of rows as a positive integer: '))
    elif select == 'Acidental Star Pattern' or select == '51':
        print('''You have selected "Acidental Star Pattern" which look like this
              * 
            * * * 
          * * * * * 
        * * * * 
          * * * 
            * * 
              *''')
        rows = int(input('Enter no of rows as a postive integer: '))
        Acidental_Star_Pattern(rows)
    elif select == 'Hollow Box Pattern' or select == '52':
        print('''You have selected "Hollow Box Pattern" which look like this
        * * * * *
        *       *
        *       *
        *       *
        * * * * *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Hollow_Box_Pattern(rows)
    elif select == 'Hollow Odd Diamond Pattern' or select == '53':
        print('''You have selected "Hollow Box Pattern" which look like this
            * 
          *   * 
        *       * 
          *   * 
            *''')
        rows = int(input('Enter no of rows as a positive integer: '))
        Hollow_Odd_Diamond_Patter(rows)
    else:
        print('Invalid Input')
        choose = input('If you wish to continue enter Y/N: ')
        if choose == 'Y' or choose == 'y':
            main()
        else:
            print('Thanks!')

if __name__ == '__main__':
    main()
