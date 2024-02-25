'''Binary Search
Pre-request: List must be sorted'''

def binary_search(lst,key):
    start = 0
    end = len(lst)-1
    mid = 0
    while start <= end:
        mid = (start + end) // 2
        if key > lst[mid]:
            start = mid+1
        elif key < lst[mid]:
            end = mid-1
        elif key == lst[mid]:
            return True, mid
    return False, mid

def main():
    pass

if __name__ == '__main__':
    main()
