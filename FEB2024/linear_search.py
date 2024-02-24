'''Linear Search'''

def linear_search(lst,key):
    length_lst = len(lst)
    for i in range(length_lst):
        if lst[i] == key:
            return i
    return None

def main():
    user_lst = eval(input('Enter the list: '))
    key = input('Enter the key to search in the list: ')
    result = linear_search(user_lst,key)
    if result == None:
        print(f"Entered key '{key}' is not in the list")
    else:
        print(f"Entered key '{key}' is in the list at the index of {result}")

if __name__ == '__main__':
    main()
