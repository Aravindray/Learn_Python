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

def main():
    '''Just main'''
    start = time.perf_counter()
    result = fact(5)
    end = time.perf_counter()
    print('result',result)
    print(f'Total time to run the function: {end-start}')

if __name__ == '__main__':
    main()
