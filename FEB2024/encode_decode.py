# This module is to encode and decode a string with key
import sys
encode_decode = input('Do you want to encode or decode? Type E for Encode or D for Decode: ')

if encode_decode == 'E':
    message = input('Enter the message that you want to encode: ')
elif encode_decode == 'D':
    key = input('Enter the key that you want to decode: ')
else:
    print('Wrong input you should have either type E or D only')
    sys.exit()


class Encode:
    pass

class Decode:
    pass
