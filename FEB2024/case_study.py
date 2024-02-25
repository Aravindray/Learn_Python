'''
Complete this below 6 steps

1. Invoke the function text_to_object from the module file_object for converting the student information in a text file to a file of student objects. In future, we may use this file of student object instead of the text file. the data in the text file appears in the following format:

1,Amit,36
5,Kriti,50
4,Alok,50
2,Umang,27
3,Shweta,85

2. Create an instance section of the Section class and initialize its list records of student instances from the file created in step 1. This list of records is unsorted as of now.

3. Search for a student in the section using linear search

4. Sort the student objects in the section based on roll_number and write in a file. In future we, may use the sorted file.

5. Read the sorted file created in step 4 to create an instance section of the Section class and use binary search to look for a roll_number

6. Read the sorted file created in step 4 to create a text file for viewing it using a text editor
'''
from file_object import text_to_object, object_to_text
from section import Section


def main():
    print('# Step 1')
    tto_src = 'std_text.txt'
    tto_dst = 'std_object.txt'
    text_to_object(tto_src,tto_dst)

    print('# Step 2')
    std_obj = 'std_object.txt'
    section = Section()
    section.file_import(std_obj)

    print('# Step 3')
    result = section.linear_search('name','Aravind')
    if result >= 0:
        print(f'Name Aravind is in the list at index {result}')
    else:
        print('Name not in the list')

    print('# Step 4')
    section.insertion_sort('roll_number')
    section.lst_export(std_obj)

    print('# Step 5')
    srt_std_obj =  'std_object.txt'
    sec = Section()
    sec.file_import(srt_std_obj)
    result = sec.binary_search('roll_number',5)
    if result >= 0:
        print('Roll Number is in the list')
    else:
        print('No data found!')

    print('# Step 6')
    ott_src = 'std_object.txt'
    ott_dst = 'text_std.txt'
    object_to_text(ott_src, ott_dst)
    
if __name__ == '__main__':
    main()
