n = int(input('Enter no of rows: '))
first_half = n // 2
second_half = n - first_half
inc = 1
dec = n
for i in range(1,first_half+1):
    for j in range(first_half-i,0,-1):
        print(' ',end=' ')
    for k in range(1,inc+1):
        if k == 1 or k == inc:
            print('*',end=' ')
        else:
            print('#',end=' ')
    print()
    inc += 2
for l in range(1,second_half+1):
    for m in range