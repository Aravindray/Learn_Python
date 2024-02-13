# string
message = 'Aravind'

# string to binary
str_bin = ''
for x in message:
    str_bin += format(ord(x),'b')
print(str_bin)

# bin to invert bin
inv_bin = ''
for x in str_bin:
    if x == '1':
        inv_bin += '0'
    else:
        inv_bin += '1'
print(inv_bin)

# invert bin to morse
morse = ''
for x in inv_bin:
    if x == '0':
        morse += '.....'
    else:
        morse += '_____'
print(morse)

# morse to binary
inc = 0
mor_bin = ''
for x in range(len(morse)//5):
    code = morse[inc:inc+5]
    if code == '.....':
        mor_bin += '0'
    else:
        mor_bin += '1'
    inc += 5
print(mor_bin)

# inv binary to bin
inv_bin_bin = ''
for x in mor_bin:
    if x == '1':
        inv_bin_bin += '0'
    else:
        inv_bin_bin += '1'
print(inv_bin_bin)

# bin to str
bin_str = ''
inc = 0
for x in range(len(inv_bin_bin)//7):
    output = inv_bin_bin[inc:inc+7]
    bin_str += chr(int(output,2))
    inc += 7
print(bin_str)
