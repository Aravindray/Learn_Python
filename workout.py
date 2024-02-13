# message = 'Iamopening#PassWords'
# print(message)
# bin_message = ''
# for i in message:
#     bin_message += str(ord(i))
# print(bin_message)
# dic_of_morse = {0 : '_____', 1 : '.____', 2 : '..___', 3 : '...__', 4 : '...._', 5 : '.....', 6 : '_....', 7 : '__...', 8 : '___..', 9 : '____.'}
# key = ''
# for x in bin_message:
#     key += (dic_of_morse[int(x)])

# print(key)


def string_to_binary(string):
    return ' '.join(format(ord(x), 'b') for x in string)
# binary to string
def binary_to_string(binary):
    return ''.join(chr(int(x, 2)) for x in binary.split())
# test
string = 'hello world'
binary = string_to_binary(string)
print(binary)
print(binary_to_string(binary))
