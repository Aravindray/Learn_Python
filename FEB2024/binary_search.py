'''Binary Search
Pre-request: List must be sorted'''

def binary_search(lst,key):
    start = 0
    end = len(lst)-1
    while start <= end:
        mid = (start + end) // 2
        if key > lst[mid]:
            start = mid+1
        elif key < lst[mid]:
            end = mid-1
        elif key == lst[mid]:
            return True
    return False

def main():
    import random
    lst = random.sample(range(1,1000),99)
    lst.sort()
    print(lst)
    key = int(input('Enter the key to find: '))
    result = binary_search(lst,key)
    print(result)

if __name__ == '__main__':
    main()