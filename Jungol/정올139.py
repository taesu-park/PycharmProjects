a, b = map(int,input().split())

if a >= b:
    for i in range(1, 10):
        for num in range(a, b-1, -1):
            print('{} * {} = {:>2d}'.format(num,i,num*i),end='   ')
        print()
else:
    for i in range(1, 10):
        for num in range(a, b+1):
            print('{} * {} = {:>2d}'.format(num,i,num*i),end='   ')
        print()
