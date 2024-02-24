from students_twelve import Student
import pickle

def text_to_object(source, destination):
    '''Objective: To convert the source file which comprise the students data by comma separated and convert into object of students class and store it in destination file'''
    f1 = open(source,'r')
    f2 = open(destination,'wb')
    line = f1.readline()
    while line != '':
        lst = line.split(',')
        student = Student(int(lst[0]),lst[1],float(lst[2]))
        pickle.dump(student, f2)
        line = f1.readline()
    f1.close()
    f2.close()

def object_to_text(source, destination):
    '''Objective: To convert the source file which is students object to txt file as comma separator format'''
    f1 = open(source, 'rb')
    f2 = open(destination, 'w')
    try:
        while True:
            student = pickle.load(f1)
            line = f'{student.roll_number},{student.name},{student.mark}\n'
            f2.write(line)
    except EOFError:
        pass
    f1.close()
    f2.close()
