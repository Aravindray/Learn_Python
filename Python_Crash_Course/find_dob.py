from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines:
    pi_string += line.lstrip()

dob = '051699' #mmddyy
if dob in pi_string:
    print('Your birthday appears in the first million digits of the pi!')
else:
    print('Your birthday does not appears in the first million digits of the pi!')
