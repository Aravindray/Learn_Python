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
            str_bin += format(ord(x),'b')
        return str_bin
    
    def bin_to_invert(self):
        '''This method will flip the binary value'''
        bin_inv = ''
        for x in self.str_to_bin():
            if x == '1':
                bin_inv += '0'
            else:
                bin_inv += '1'
        return bin_inv
    
    def invert_to_morse(self):
        '''This method will convert a digit to morse code
        to make a mess I used ..... as 0 and _____ as 1'''
        inv_morse = ''
        for x in self.bin_to_invert():
            if x == '0':
                inv_morse += '.....'
            else:
                inv_morse += '_____'
        return inv_morse
    
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
        self.key = key

    def morse_to_invert(self):
        '''This method will convert the morse code and return 1st level of binary value'''
        inc = 0
        morse_inv = ''
        for x in range(len(self.key)//5):
            code = self.key[inc:inc+5]
            if code == '.....':
                morse_inv += '0'
            else:
                morse_inv += '1'
            inc += 5
        return morse_inv
    
    def invert_to_bin(self):
        '''This method will flip the inverted binary to values to original binary'''
        inv_bin = ''
        for x in self.morse_to_invert():
            if x == '1':
                inv_bin += '0'
            else:
                inv_bin += '1'
        return inv_bin
    
    def bin_to_str(self):
        '''This method will convert the binary to string'''
        inc = 0
        bin_str = ''
        for x in range(len(self.invert_to_bin())//7):
            output = self.invert_to_bin()[inc:inc+7]
            bin_str += chr(int(output,2))
            inc += 7
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
