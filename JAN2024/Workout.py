sm = open('studentsMarks.txt','r')
mm = open('moderatedMark.txt','w+')

notEmpty = sm.readline()
moderate_Mark = float(input('Enter the moderate mark: '))
while notEmpty != '':
    marks = notEmpty.split(',')
    marks[2] = float(marks[2])
    marks[2] += moderate_Mark
    marks[2] = str(marks[2])+'\n'
    ', '.join(marks)
    print(marks)
    mm.writelines(marks)
    notEmpty = sm.readline()

print(sm.readlines())
print(mm.readlines())
sm.close()
mm.close()
