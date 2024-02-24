from students_twelve import Student

def text_to_object(source, destination):
    '''Objective: To convert the source file which comprise the students data by comma separated and convert into object of students class and store it in destination file'''
    f1 = open(source,'r')
    f2 = open(destination,'w')
    line = f1.readline()
    while line != '':
        lst = line.split(',')
        student = Student(int(lst[0]),lst[1],float(lst[2]))
        f2.write(student)
        line = f1.readline()
    f1.close()
    f2.close()

def object_to_text(source, destination):
    pass


tto_source = 'std_text.txt'
tto_destination = 'std_object.txt'
