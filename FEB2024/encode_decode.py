# This module is to encode and decode a string with key
import sys

class Encode:
    '''This class will encode the given string and returns a key'''
    def __init__(self,message):
        '''This is a class constructor'''
        self.message = message
        self.key()

    def str_to_bin(self):
        '''This method will convert sting to binary value'''
        str_bin = ''
        for x in self.message:
            str_bin += format(ord(x),'b') + ' '
        return str_bin
    
    def bin_to_invert(self):
        '''This method will flip the binary value'''
        bin_inv = ''
        for x in self.str_to_bin():
            if x == '1':
                bin_inv += '0'
            elif x == '0':
                bin_inv += '1'
            else:
                bin_inv += ' '
        return bin_inv
    
    def invert_to_morse(self):
        '''This method will convert a digit to morse code
        to make a mess I used ..... as 0 and _____ as 1'''
        inv_morse = ''
        for x in self.bin_to_invert():
            if x == '0':
                inv_morse += '.....'
            elif x == '1':
                inv_morse += '_____'
            else:
                inv_morse += ' '
        return inv_morse.rstrip()
    
    def key(self):
        '''This method will store the key in separate file'''
        file = open('key.txt','w')
        file.write(self.invert_to_morse())
        file.close()
    
    def __str__(self):
        '''This will print'''
        return self.invert_to_morse()

class Decode:
    '''This class will decode the key and return the actual message'''
    def __init__(self,key):
        '''This is a class constructor'''
        self.key = key.split(' ')

    def morse_to_invert(self):
        '''This method will convert the morse code and return 1st level of binary value'''
        inc = 0
        morse_inv = ''
        for i in range(len(self.key)):
            x = self.key[i]
            for j in range(len(x)//5):
                code = x[inc:inc+5]
                if code == '.....':
                    morse_inv += '1'
                else:
                    morse_inv += '0'
                inc += 5
            morse_inv += ' '
            inc = 0
        morse_inv = morse_inv.rstrip()
        morse_inv_lst = morse_inv.split(' ')
        return morse_inv_lst
    
    def bin_to_str(self):
        '''This method will convert the binary to string'''
        bin_str = ''
        for i in range(len(self.morse_to_invert())):
            bin_str += chr(int(self.morse_to_invert()[i],2))
        return bin_str

    def __str__(self):
        '''This will print'''
        return self.bin_to_str()

encode_decode = input('Do you want to encode or decode? Type E for Encode or D for Decode: ')

if encode_decode == 'E':
    message = input('Enter the message that you want to encode: ')
    key = Encode(message)
    print('Key successfully stored in key.txt file')
elif encode_decode == 'D':
    key = input('Enter the key that you want to decode: ')
    answer = Decode(key)
    print(answer)
else:
    print('Wrong input you should have either type E or D only')
    sys.exit()
