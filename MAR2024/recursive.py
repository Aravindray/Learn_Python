'''Let's learn Recursive'''
import time

# Factorial
def fact(n):
    '''
    fact(n) = if n == 1 return 1
    if n>2 return n * fact(n-1)
    '''
    assert n > 0
    if n == 1:
        return 1
    return n * fact(n-1)

# Fibonacci Sequence
def fibonacci(n):
    '''
    fibonacci(n) = if n == 1 return 0
    if n == 2 return 1
    else return fibonacci(n-1) + fibonacci(n-2)
    '''
    assert n > 0
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Length of String
def length(n):
    '''
    length(n) = if n == '' return 0
    else 1 + length(n[1:])
    '''
    if n == '':
        return 0
    return 1+length(n[1:])

# Reverse a string
def reverse(char):
    '''
    reverse(str) = if n == '' return ''
    else str[-1] + reverse(str[:-1])
    '''
    if char == '':
        return ''
    return char[-1]+reverse(char[:-1])

# Palindrome
def is_palindrome(string):
    '''
    palindrome = if str == '' return True
    else str[0] == str[-1] and palindrome(str[1:-1])
    '''
    if string == '':
        return True
    return string[0] == string[-1] and is_palindrome(string[1:-1])

# Flatten a list
def flatten(lst1, lst2 = []):
    '''
    for every element i in list l
        if i is not a list
            list 2 will append
        else
            flatten(i, lst2)
    '''
    for element in lst1:
        if type(element) is not list:
            lst2.append(element)
        else:
            flatten(element, lst2)
    return lst2

# Copy
def copy(lst1, lst2 = []):
    '''
    if list 1 is empty return empty list 2
    else append every value of the list 1 in list 2 
    '''
    if lst1 == []:
        return lst2
    else:
        lst2.append(lst1[0])
        copy(lst1[1:], lst2)
    return lst2

# Deep copy
def deepcopy(lst1, lst2 = []):
    '''
    if element is the list 1 is not a list append list 2
    else create the list and append the element
    '''
    if lst1 == []:
        pass
    else:
        if type(lst1[0]) != list:
            lst2.append(lst1[0])
        else:
            lst2.append([])
            deepcopy(lst1[0], lst2[-1])
        deepcopy(lst1[1:], lst2)
    return lst2

# Permutation
def permutation(lst1, lst2=[], k = 0, pos = 0):
    pass

def main():
    '''Just main'''
    start = time.perf_counter()
    print()
    # lst = [1, [2, [3, 4, [5, 6, [7, 8], [9, [10]], 11], 12], 13], 14, [[15, 16]], 17]
    new_lst = [1, 3, 78, 13, 54, 1]
    result = copy(new_lst)
    end = time.perf_counter()
    print('result :',result)
    print()
    print(f'Total time to run the function: {start} | {end} = {end-start}')

if __name__ == '__main__':
    main()
